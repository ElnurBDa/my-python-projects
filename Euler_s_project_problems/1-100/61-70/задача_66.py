from math import floor, sqrt
squares=[]
maxX=1

for x in range(1,40):
	squares.append(x**2) 
for D in range(500,1001):
	if D not in squares:
		notfound=True
		y=1
		while notfound:
			x=(1+D*(y**2))**.5
			if x==floor(x) :
				if x> maxX  :
					print(D," |",x )
					maxX=x
				notfound=False
			y+=1 

input("VSO!!!")
#661

