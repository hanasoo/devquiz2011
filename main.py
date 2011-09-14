#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from datetime import datetime
#from solver1 import * #0:00:19.648231
from solver2 import * #0:00:12.842348

FILE_NAME = 'data'
IN_FILE = FILE_NAME + '.in'
OUT_FILE = FILE_NAME + '.out'

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

#TODO
# pattern再利用
# 端から評価
# wayの再評価

lx, rx, ux, dx = map(lambda x: int(x), src.pop(0).strip().split(' '))
s = Solver(lx, rx, ux, dx)

case_num = int(src.pop(0))

result = ""
solved = 0
count = 0
all = 0
print('############ start #################')
for case_count in range(case_num):
	w, h, q = src.pop(0).strip().split(',')
	#if int(w) + int(h) < 8:
	size = int(w) + int(h)
	if size < 11:
		if size < 8:
			limit = 30000
		else:
			limit = 1000
		#start = datetime.now()
		#w = 3
		#h = 4
		#q = '2BA684307159'
		
		print('############ start %d ###################' % all)
		s.setup(int(w), int(h), q, limit)
		a = s.search()
		result = result + a + '\n'
		if not a == '':
			solved = solved + 1
		count = count + 1
		
		#print datetime.now() - start
		#break
	else:
		print('############ pass %d ###################' % all)
		result = result + '\n'
	all = all + 1

print('############ end ###################')

print 'all:    %5d' % all
print 'scope:  %5d' % count
print 'solved: %5d' % solved
print 'U:%d D:%d R:%d L:%d' % (s.ux, s.dx, s.rx, s.lx)

f = open(OUT_FILE, 'w')
f.write(result)
f.close()


