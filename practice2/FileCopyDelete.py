import shutil
import os

# Returns True if path or directory does exists.

print(os.path.exists("E:\\CodeWorkspace\\PythonWorkspace\\PythonMarch2020\\practice1"))

# Copy File
shutil.copy("abc.txt", "E:\\CodeWorkspace\\PythonWorkspace\\PythonMarch2020\\practice1")

# Returns True if path is File.

print(os.path.isfile("E:\\CodeWorkspace\\PythonWorkspace\\PythonMarch2020\\practice1\\abc.txt"))

# Returns True if path is Directory.

print(os.path.isdir("E:\\CodeWorkspace\\PythonWorkspace\\PythonMarch2020\\practice1"))

# Delete File
os.remove("E:\\CodeWorkspace\\PythonWorkspace\\PythonMarch2020\\practice1\\abc.txt")

