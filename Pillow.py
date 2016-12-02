from PIL import Image

img = Image.open("cute.jpg")
print(img.size)
print(img.format)

img.show()