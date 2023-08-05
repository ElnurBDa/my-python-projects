n = int(input())
answers=[]
for i in range(n):
	l = int(input())
	arr = list(map(int, input().split()))
	if l == 1: answers.append("YES")
	else:
		for j in range(l):
			if arr[j]!=0:break
		if 0 in arr[j:]: 
			answers.append("NO")
			continue
		arr = arr[j:]
		for j in range(l):
			if arr[j]!=1:break
		if 1 in arr[j:]: 
			answers.append("NO")
			continue
		
		answers.append("YES")
for x in answers:print(x)
