#!/usr/bin/env python
import sys, math
def add(a,b):
	return a + b
def minus(a,b):
	return a - b 
def multiply(a,b):
	return a * b
def divide(a,b):
	return a/b
def remainder(a,b):
	return a%b
def power(a,b):
	return a**b

binary_opt = {
	"+": add,
	"-": minus,
	"*": multiply,
	"/": divide,
	"%": remainder,
	"**": power,
}

def negate(a):
	return -(a)
def square(a):
	return a**2
def square_root(a):
	return math.sqrt(a)
def logarithm(a):
	return math.log(a)





unary_opt = {
	"n": negate,
	"s": square,
	"r": square_root,
	"l": logarithm,
}

def check(token):
	return token.isdigit() or (token[0] == "-" and token[1:].isdigit())

def check_float(a):
	x = a.split(".")
	return len(x) == 2 and check(x[0]) and x[1].isdigit()


stack = []
s = sys.stdin.readline()
while 0 < len(s):
	tokens = s.split(" ")
	i = 0
	while i < len(tokens):
		token = tokens[i].rstrip()
		if check_float(token):
			stack.append(float(token))	
		elif check(token):
			stack.append(int(token))
		elif token in binary_opt:
			b = stack.pop()
			a = stack.pop()
			c = binary_opt[token](a,b)
			stack.append(c)
		elif token in unary_opt:
			a = stack.pop()
			c = unary_opt[token](a)
			stack.append(c)
		elif token == "p":
			print stack[-1]
		else:
			None
		i += 1
	s = sys.stdin.readline()









