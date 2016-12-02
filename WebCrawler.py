from urllib import request
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page < max_pages:
        url = "http://php.net/manual/en/function.file.php"+str(page)
        source_code = request.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {"class":"item.name"}):
            href = "http://php.net" +link.get('hrf')
            title = link.string
            print(href)
            print(title)
            page+=1

            trade_spider(1)

            def get_single_item_data(item_url):
                source_code = request.get(item_url)
                plain_text = source_code.text
                soup = BeautifulSoup(plain_text)
                for item_name in soup.findAll('div', {'class': 'i.name'}):
                    print(item_name.string)
                    for link in soup.findAll('a'):
                        href =  "http://php.net" +link.get('href')
                        print(href)

                        trade_spider(3)