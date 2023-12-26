@echo off

C:
cd "C:\Games\Fleet Command\Graphics"

for %%a in (%*) do (
  copy "%%a" "C:\Games\Fleet Command\Graphics"
  "cmpUtil.exe" 3d "%%~nxa"
)

pause