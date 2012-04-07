import sys
import re

file = sys.argv[1]
match = re.search('\w+\.(\w+)',file)
ext = match.group(1)
f = open(file,'r')
g = open(str(file[:len(file)-len(ext)-1])+'-stripped.'+ext,'w')
for line in f:
    if str(line)[:1]!='#':
        g.write(line)
        
g.close()
f.close()
    
