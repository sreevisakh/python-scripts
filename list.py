#!/usr/bin/python

import os
import sys
import babynames

def List(dir):
	filenames = os.listdir(dir)
	for filename in filenames:
		if filename[4:]=='baby' and filename[-4:]=='html':
			names=babynames.extract_names(filename)
			text = '\n'.join(names)
			f = open(filename+'.summary','w')
			f.write(text)
			f.close()	



List(sys.argv[1])
