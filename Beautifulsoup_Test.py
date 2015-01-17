import bs4 #BeautifulSoup 4.3.2 
import urllib2
 
try:
    webpage = urllib2.urlopen('http://en.wikipedia.org/wiki/Main_Page')
    soup = bs4.BeautifulSoup(webpage.read().decode('utf8'))
except:
    print("Error")
else:
    for anchor in soup.find_all('a'):
        print(anchor.get('href', '/'))
