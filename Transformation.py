from PIL import Image

baby = Image.open("cute.jpg")
source = baby.resize(250, 250)
flip = baby.transpose(Image.FLIP_LEFT_RIGHT)
spin = baby.transpose(Image.ROTATE_90)

baby.show()
source.show()
flip.show()
spin.show()