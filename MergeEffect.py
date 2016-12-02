from PIL import Image

sister = Image.open("cute.jpg")
bucky = Image.open("bb.jpg")
r1, g1, b1 = sister.split()
r2, g2, b2 = bucky.split()

new_img = Image.merge("RGB", (r2, g1, b2))
new_img.show()