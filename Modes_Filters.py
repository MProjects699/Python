from PIL import Image
from PIL import ImageFilter

sister = Image.open("cute.jpg")
blur = sister.filter(ImageFilter.BLUR)
detail = sister.filter(ImageFilter.DETAIL)
edges = sister.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()