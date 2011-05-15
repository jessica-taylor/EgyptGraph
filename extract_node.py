#! /usr/bin/env python

import fileinput



for line in fileinput.input("nodes.txt"):
	tokens = line.split('"')
	print tokens[1]



