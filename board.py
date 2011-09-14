#!/usr/bin/env python
# -*- coding: utf-8 -*-

def printBoard(w, h, line):
	#print line
	for i in range(h):
		print line[i * w: (i + 1) * w]
	print '\n'

def getAnswer(w, h, line):
	aline = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	num = line.count('=')
	pos = -1
	for i in range(num):
		pos = line.index('=', pos+1)
		aline = aline[0:pos] + '=' + aline[pos+1:]
	return aline[0:w * h - 1] + '0'

def goLeft(w, h, line):
	bp = line.index('0')
	if bp % w == 0 or line[bp-1] == '=':
		return False
	return line[0:bp-1] + '0' + line[bp-1] + line[bp+1:]

def goRight(w, h, line):
	bp = line.index('0')
	if bp % w == w - 1 or line[bp+1] == '=':
		return False
	return line[0:bp] + line[bp+1] + '0' + line[bp+2:]

def goUp(w, h, line):
	bp = line.index('0')
	if bp - w < 0 or line[bp-w] == '=':
		return False
	return line[0:bp-w] + '0' + line[bp-w+1:bp] + line[bp-w] + line[bp+1:]

def goDown(w, h, line):
	bp = line.index('0')
	if w * (h - 1) - 1 < bp or line[bp+w] == '=':
		return False
	return line[0:bp] + line[bp+w] + line[bp+1:bp+w] + '0' + line[bp+w+1:]

def getPos(w, h, line, sub):
	p = line.index(sub)
	return  p % w, p / w
	
	