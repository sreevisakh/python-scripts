import urllib
import re
import sys

url = sys.argv[1]
#g = open('input.txt','w')

#f = urllib.urlopen(url)
f = open('file.txt','r')
content = f.read()
match = re.search(r'\/watch\?v=(\w+)&amp;',content)
for item in match.group():
    print item,
f.close()
