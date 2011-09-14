#!/usr/bin/env python
# -*- coding: utf-8 -*-

from board import *

class Solver:
	def __init__(self, lx, rx, ux, dx):
		self.lx = lx
		self.rx = rx
		self.ux = ux
		self.dx = dx
		
	def __str__(self):
		return "L:%d R:%d U:%d D:%d" % (self.lx, self.rx, self.ux, self.dx)
	
	def setup(self, w, h, q):
		self.w = w
		self.h = h
		self.first = q
		self.goal = getAnswer(w, h, q)
		
		self.go = 0
		self.pat = [[self.first], [self.goal]]
		self.way = [[''], ['G']]
		self.ind = [0,0]
		self.answer = False
		
		printBoard(w, h, q)
	
	def search(self):
		while (True):
			i = self.ind[self.go]
			src = self.pat[self.go][i]
			way = self.way[self.go][i]
			self.add(way + 'U', goUp(self.w, self.h, src))
			self.add(way + 'D', goDown(self.w, self.h, src))
			self.add(way + 'R', goRight(self.w, self.h, src))
			self.add(way + 'L', goLeft(self.w, self.h, src))
			if not self.answer == 0:
				break
			self.ind[self.go] = i + 1
			self.go = self.go ^ 1
			
			if i % 1000 == 0:
				print "pat[%d][%d]" % (len(self.pat[0]), len(self.pat[1]))
		return self.answer
	
	def add(self, way, src):
		if not src:
			return
		r = self.go ^ 1
		if src in self.pat[r]:
			ri = self.pat[r].index(src)
			if not self.go == 0:
				w1 = way if self.go == 0 else self.way[r][ri]
				w2 = self.way[r][ri] if self.go == 0 else way
				self.finish(w1, w2)
		elif src not in self.pat[self.go]:
			self.pat[self.go].append(src)
			self.way[self.go].append(way)

	def finish(self, way1, way2):
		print way1
		print way2
		self.answer = way1 + self.reverseWay(way2)
		
		self.lx = self.lx - self.answer.count('L')
		self.rx = self.rx - self.answer.count('R')
		self.ux = self.ux - self.answer.count('U')
		self.dx = self.dx - self.answer.count('D')

		print self.answer
	
	def reverseWay(self, way):
		ans = way[::-1]
		result = ""
		for s in ans:
			if s == 'U':
				result = result + 'D'
			elif s == 'D':
				result = result + 'U'
			elif s == 'R':
				result = result + 'L'
			elif s == 'L':
				result = result + 'R'
		return result
		
	def checkAnswer(self):
		print "### check ###"
		printBoard(self.w, self.h, self.goal)
		src = self.goal
		for s in self.answer:
			print s
			if s == 'U':
				src = goUp(self.w, self.h, src)
			elif s == 'D':
				src = goDown(self.w, self.h, src)
			elif s == 'R':
				src = goRight(self.w, self.h, src)
			elif s == 'L':
				src = goLeft(self.w, self.h, src)
			printBoard(self.w, self.h, src)
			raw_input()
		

