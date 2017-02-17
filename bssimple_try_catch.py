from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as http_err:
		print(http_err)
		#{TODO} in case this errors: return null for now, break, or do some other "Plan B" 
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.body.h1
	except AttributeError as attr_err:
		print(attr_err)
		#{TODO} in case this errors: return null for now, break, or do some other "Plan B" 
		return None
	return title

title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
	print("Title (h1) could not be found")
else:
	print (title)

print(bsObj)
#prints to whole thing 
#{TODO} should probably go into a file.
#then you can dissect what you really want from that Request
#if not using browser tools to have an idea already


#https://www.knmi.nl/nederland-nu/luchtvaart/weerbulletin-kleine-luchtvaart
#print(bsObj.pre) gives the Bulletin text 
#{TODO} needs more clean up

