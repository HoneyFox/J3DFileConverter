// This is only pseudo-code to represent the J3D file structure.
// Feature like variable-length array declaration is not allowed by C++.

struct Vertex
{
	float pos[4];
	float normal[3];
	float uv[3];
};

struct Triangle
{
	unsigned short indices[3];
};

struct TextureName
{
	char textureName[32];
};

struct Model
{
	char modelName[32];
	float offset[3];
	float rotation[4]; // Perhaps it's rotation? Looks like it's always [0,0,0,0] in many J3D files.
	int nextSiblingModelIndex;
	int prevSiblingModelIndex;
	int parentModelIndex; // If multiple children exist, all children will have same parentModelIndex value.
	int childModelIndex; // If multiple children exist, it will point to the first child.
	unsigned short face_num;
	unsigned short face_offset;
	unsigned short vert_num;
	unsigned short vert_offset;
	unsigned short use_tex; // 1 - this model uses texture, 0 - this model doesn't use texture.
	unsigned short mat_index;
	unsigned short unknown[4]; // Looks like it's always [1,0,0,0].
};

struct Material
{
	float ambient[4];
	float diffuse[4];
	float specular[4];
	float emissive[4];
	float shininess;
};

public struct J3DFile
{
	unsigned int vert_num;
	unsigned int face_num;
	unsigned int tex_num;
	unsigned int model_num;
	unsigned int mat_num;

	Vertex verts[vert_num];
	Triangle tris[face_num];
	TextureName tex_names[tex_num];
	Model models[model_num];
	char triTexIndex[face_num]; // Each triangle's texture index.
	Material mats[mat_num];
};
