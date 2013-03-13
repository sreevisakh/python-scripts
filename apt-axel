#!/usr/bin/python

import sys
import subprocess as sp
import re
import os
if len(sys.argv)>1:
	packagename = sys.argv[1]
else:
	print "Usage: ./apt-web packagename"
	exit(0)
deps = []
apt = sp.Popen(['apt-get','-y','--print-uris','install',packagename],stdout = sp.PIPE)
output = apt.stdout.read()
sp.Popen.kill(apt)
if output.find('Unable to locate package')>0:
	print 'Unable to locate package'
elif output.find('is already the newest version')>0:
	print packagename+ 'is already the newest version'
elif output.find("E: Unmet dependencies. Try 'apt-get -f install'")>0:
	print "Error: Try 'apt-get -f install'"

else:
	apt = sp.Popen(['apt-get','-y','--print-uris','install',packagename],stdout = sp.PIPE)
	for line in apt.stdout:
		if line.startswith("'http"):
			one = (url,name,size,md5) = line.split(" ")
			deps.append(one)
	sp.Popen.kill(apt)

	for x in deps:
		if not os.path.exists('/tmp/'+x[1]):
			print "Downloading "+str(len(deps))+" Packages"
			if os.system('axel -a -n 10 -o /tmp '+ x[0]): 
				print 'Downloaded'
		os.system('sudo chmod 755 /tmp/*.deb')
		if os.system('sudo cp -vu --preserve /tmp/*.deb /var/cache/apt/archives/'):
			print 'Copied'
	os.system('sudo rm -f /var/cache/apt/archives/lock')
	if os.system('sudo apt-get -y install '+ packagename):
		print 'Successfull'

	

