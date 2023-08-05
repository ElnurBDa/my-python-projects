n = int(input())
answers=[]
for i in range(n):
	l = int(input())
	arr = list(map(int, input().split()))
	if l%2==0: answers+=[0]
	else:
		x=0
		for j in range(0,l,2):
			x=x^arr[j]
		answers+=[x]
for x in answers:print(x)
