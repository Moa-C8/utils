import os
import shutil

path = input("path:")
name = input("str a delete :")

liste = os.listdir(path)
i = 0
for folder in liste:
    if name in folder:
        i += 1
        NewName = folder.replace(name,"")
        oldFile = os.path.join(path,folder)
        newFile = os.path.join(path,NewName)
        os.rename(oldFile,newFile)

print(i)
