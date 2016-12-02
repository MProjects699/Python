import random
import urllib.request

def downloadImage(url):
    name = random.randrange(1, 1000)
    full_name = str(name)+ ".jpg"
    urllib.request.urlretrieve(url, full_name)

    downloadImage("http://1.bp.blogspot.com/-6nVT-rxNxSA/VMZjzr6u6TI/AAAAAAAAMK8/s4-Pae2m4bI/s1600/Disney%2BCartoon%2BLittle%2BKrishna%2BHD%2BWallpapers2.jpg")