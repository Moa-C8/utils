import os
import shutil
savesFolder = "./saves/"
liste = os.listdir(savesFolder)
i = 0
for folder in liste:
    if "Random Speedrun #" in folder:
        i += 1
        shutil.rmtree(savesFolder+folder)

print(i)

#put in .minecraft
