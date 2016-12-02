from PIL import Image

sister = Image.open("bb.jpg")
girl = Image.open("cute.jpg")

area = (100,100,300,300)
sister.paste(girl, area)

sister.show()