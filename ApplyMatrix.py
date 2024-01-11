import sys
import math
import J3DFile

class Matrix33:
    def __init__(self):
        self.values = [[1,0,0], [0,1,0], [0,0,1]]

    def set_scale_matrix(self, scale):
        if scale is float:
            self.values = [[scale, 0, 0], [0, scale, 0], [0, 0, scale]]
        elif scale is list:
            self.values = [[scale[0], 0, 0], [scale[1], 0, 0], [scale[2], 0, 0]]
    
    def set_rotate_x_matrix(self, angle):
        self.values[0] = [1, 0, 0]
        self.values[1] = [0, math.cos(angle * math.pi / 180.0), math.sin(angle * math.pi / 180.0)]
        self.values[2] = [0, -math.sin(angle * math.pi / 180.0), math.cos(angle * math.pi / 180.0)]
    
    def set_rotate_y_matrix(self, angle):
        self.values[0] = [math.cos(angle * math.pi / 180.0), 0, -math.sin(angle * math.pi / 180.0)]
        self.values[1] = [0, 1, 0]
        self.values[2] = [math.sin(angle * math.pi / 180.0), 0, math.cos(angle * math.pi / 180.0)]
    
    def set_rotate_z_matrix(self, angle):
        self.values[0] = [math.cos(angle * math.pi / 180.0), math.sin(angle * math.pi / 180.0), 0]
        self.values[1] = [-math.sin(angle * math.pi / 180.0), math.cos(angle * math.pi / 180.0), 0]
        self.values[2] = [0, 0, 1]

    def __rmul__(self, vector):
        result = []
        result.append(vector[0] * self.values[0][0] + vector[1] * self.values[1][0] + vector[2] * self.values[2][0])
        result.append(vector[1] * self.values[0][1] + vector[1] * self.values[1][1] + vector[2] * self.values[2][1])
        result.append(vector[2] * self.values[0][2] + vector[1] * self.values[1][2] + vector[2] * self.values[2][2])
        return result
    
class MatrixApplier:
    def __init__(self, input_path: str, output_path: str, matrix: Matrix33):
        self.input_path = input_path
        self.output_path = output_path
        self.matrix = matrix
    
    def apply(self):
        file = J3DFile.J3DFile()
        file.load_file(self.input_path)
        # Apply to vertices
        for i in range(0, file.vert_num):
            pos = file.verts[i].pos[0:3]
            normal = file.verts[i].normal[0:3]
            applied_pos = pos * self.matrix
            applied_normal = normal * self.matrix
            file.verts[i].set_pos(applied_pos[0], applied_pos[1], applied_pos[2])
            file.verts[i].set_normal(applied_normal[0], applied_normal[1], applied_normal[2])
        # Apply to models' offset vectors
        for i in range(0, file.model_num):
            offset = file.models[i].offset
            applied_offset = offset * self.matrix
            file.models[i].offset = applied_offset

        f = open(self.output_path, 'wb')
        file.serialize(f)
        f.close()



if __name__ == "__main__":
    input_file: str = None
    output_file: str = None
    matrix: Matrix33 = None
    i: int = 1
    while i < len(sys.argv):
        if sys.argv[i].lower() == "-i":
            input_file = sys.argv[i+1]
            i += 1
        elif sys.argv[i].lower() == "-o":
            output_file = sys.argv[i+1]
            i += 1
        elif sys.argv[i].lower() == "-rot":
            matrix = Matrix33()
            if sys.argv[i+1].lower() == "x":
                matrix.set_rotate_x_matrix(float(sys.argv[i+2]))
                i += 2
            elif sys.argv[i+1].lower() == "y":
                matrix.set_rotate_y_matrix(float(sys.argv[i+2]))
                i += 2
            elif sys.argv[i+1].lower() == "z":
                matrix.set_rotate_z_matrix(float(sys.argv[i+2]))
                i += 2
        elif sys.argv[i].lower() == "-scale":
            matrix = Matrix33()
            matrix.set_scale_matrix(float(sys.argv[i+2]), float(sys.argv[i+3]), float(sys.argv[i+4]))
            i += 3
        i+=1
    
    if input_file is not None and matrix is not None:
        if output_file is None:
            matrix_applier: MatrixApplier = MatrixApplier(input_file, input_file, matrix)
            matrix_applier.apply()
        else:
            matrix_applier: MatrixApplier = MatrixApplier(input_file, output_file, matrix)
            matrix_applier.apply()

# Usage:
#   py ApplyMatrix.py -i <input J3D file> [-o <output J3D file>] -rot <axis> <angle>
#   py ApplyMatrix.py -i <input J3D file> [-o <output J3D file>] -scale <scale x> <scale y> <scale z>
#       -o: Optional, the input J3D file will be the output target if it's not specified.
#       -rot: Axis can be x, y or z. Angle is in degrees.
#       -scale: Scale the model (vertices' position & normal, models' offset).
