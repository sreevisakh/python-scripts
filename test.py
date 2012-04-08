#! /usr/bin/env python
from bs4 import BeautifulSoup
import urllib
from xml.dom.minidom import Document

# Get a file-like object for the Python Web site's home page.
print 'Downloading Page...'
f = urllib.urlopen("http://moviesmobile.net/hollywood-mobile-movies/index.php")
# Read from the object, storing the page's contents in 's'.
print 'Reading Page...'
html_doc = f.read()
f.close()
print 'Processing Page...'
soup = BeautifulSoup(html_doc)
#print(soup.prettify())
print 'Parsing result'
b=[]
for link in soup.find_all('a'):
    b.append(link.get('href'))

f = open("hello.xml",'w')


# Create the minidom document
doc = Document()
# Create the <wml> base element
wml = doc.createElement("wml")
doc.appendChild(wml)

# Create the main <card> element
maincard = doc.createElement("links")
maincard.setAttribute("id", "main")
wml.appendChild(maincard)

for s in b:
	if str(s)[-1:] =='/':
		
		linkNode = doc.createElement("link")
		linkNode.setAttribute("status", '0')
		maincard.appendChild(linkNode)
		
		
		linkurl = doc.createTextNode("http://moviesmobile.net/hollywood-mobile-movies/"+str(s)+"index.php")
		linkNode.appendChild(linkurl)


	
doc.writexml(f)
f.close()