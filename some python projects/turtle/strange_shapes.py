from turtle import *
from random import randint



def func(seq):
	nseq = ""
	for i in seq:
		nseq += str(i % 2)
	return nseq


speed(300)
color('black')


for a in range(2, 5):
	for b in range(1, 50):
		seq = []
		for x in range(70):
			seq.append(x**a // b + a*b)

		for i in func(seq):
			forward(20)
			if int(i):
				right(90)
			else:
			    left(90)
		clear()
		setpos((0,0))
		clear()


done()