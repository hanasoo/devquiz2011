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
	
	def setup(self, w, h, q, limit):
		self.w = w
		self.h = h
		self.first = q
		self.goal = getAnswer(w, h, q)
		self.limit = limit
		
		self.go = 0
		self.pat = [[self.first], [self.goal]]
		self.way = [[''], ['G']]
		self.ind = [0,0]
		self.answer = False
		
		fx, fy = getPos(w, h, self.first, '0')
		gx, gy = getPos(w, h, self.goal, '0')
		if not (fx + fy) % 2 == (gx + gy) % 2:
			self.pat[0] = []
			self.way[0] = []
			self.action('', self.first, 1)
		
		printBoard(w, h, self.first)
		
	def search(self):
		while (True):
			i = self.ind[self.go]
			self.action(self.way[self.go][i], self.pat[self.go][i], 2)
			if not self.answer == 0:
				break
			self.ind[self.go] = self.ind[self.go] + 1
			self.go = self.go ^ 1
			
			if i % 1000 == 0:
				print "pat[%d][%d]" % (len(self.pat[0]), len(self.pat[1]))
			if self.limit < i:
				return ''
		
		self.lx = self.lx - self.answer.count('L')
		self.rx = self.rx - self.answer.count('R')
		self.ux = self.ux - self.answer.count('U')
		self.dx = self.dx - self.answer.count('D')
		print self.answer
		return self.answer
	
	def action(self, way, src, depth):
		if depth == 0 and src:
			self.add(way, src)
		else:
			res = goUp(self.w, self.h, src)
			if res:
				self.action(way + 'U', res, depth - 1)
			res = goDown(self.w, self.h, src)
			if res:
				self.action(way + 'D', res, depth - 1)
			res = goRight(self.w, self.h, src)
			if res:
				self.action(way + 'R', res, depth - 1)
			res = goLeft(self.w, self.h, src)
			if res:
				self.action(way + 'L', res, depth - 1)
		
	def add(self, way, src):
		r = self.go ^ 1
		if src in self.pat[r]:
			ri = self.pat[r].index(src)
			w1 = way if self.go == 0 else self.way[r][ri]
			w2 = self.way[r][ri] if self.go == 0 else way
			self.finish(w1, w2)
		elif src not in self.pat[self.go]:
			self.pat[self.go].append(src)
			self.way[self.go].append(way)

	def finish(self, way1, way2):
		ans = way1 + self.reverseWay(way2)
		if not self.answer or len(ans) < len(self.answer):
			self.answer = ans
		
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
		

