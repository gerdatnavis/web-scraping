from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.knmi.nl/nederland-nu/luchtvaart/weerbulletin-kleine-luchtvaart")
bsObj = BeautifulSoup(html.read())
print(bsObj.pre)
