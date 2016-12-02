from PIL import Image

sister = Image.open("cute.jpg")
r, g, b = sister.split()

r.show()
g.show()
b.show()