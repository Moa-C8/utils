from PIL import Image
import glob

pathin = input("path in:")
pathout = input("path out:")
i= 1

for jpegfile in glob.glob(f"{pathin}/*.JPEG"):
    print(jpegfile)
    im = Image.open(jpegfile)
    im.save(f'{pathout}/{i}.png')
    i += 1
