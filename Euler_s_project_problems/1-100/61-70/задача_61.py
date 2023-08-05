
def func(n,k):
	if k==3: return int(n*(n+1)/2)
	elif k==4: return n*n
	elif k==5: return int((3*n-1)*n/2)
	elif k==6: return n*(2*n-1)
	elif k==7: return int(n*(5*n-3)/2)
	elif k==8: return n*(3*n-2)

l=[]
for i in range(6):
	l.append([])
	for x in range(150):
		s=func(x,i+3)
		if s>=10000: break
		if s>=1000:
			l[i].append(str(s))






def recfunc(r,k,a):
	global l
	y=[]
	for x in a:y.append(x[1])
	for x in k: 
		if x not in y:
			k.remove(x)
			break
	if a[0][0][:2]==a[-1][0][2:]:
		print(a,k)

	for i in range(6):
		if i not in k:
			for x in l[i]:
				if r==x[:2]:
					a.append((x,i))
					k.append(i)
					recfunc(x[2:],k,a)
					a.pop(-1)	


k=4
for x in l[k]:
	recfunc(x[2:],[k],[(x,k)])

'''
[('2512', 4), ('1281', 5), ('8128', 3), ('2882', 2), ('8256', 0), ('5625', 1)] [4, 5, 3, 2, 0, 1]
'''

print(2512+1281+8128+2882+8256+5625)