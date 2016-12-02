from urllib import request

goog_url = ""

def stockData(url):
    response = request.urlopen(url)
    csv = response.read(url)
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog_url'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line+"\n")
        fx.close()