# By Elnur The Great
count = 0
n,m = 3,3
marr = [[0]*(n+1) for _ in range(m+1)]
marr[0][0] = 1

def print_arr(arr,text="__"):
	global m,n
	for j in range(m+1):
		print(*arr[j])
	print(text*(n+1))

def func(arr,x,y):# x,y coordinates of the point => arr[y][x]
	global n,m
	if x==n:
		return 1
	r = 0
	d = 0
	u = 0
	ru = 0
	#to_right
	arr[y][x+1] = 1
	r = func(arr,x+1,y)
	arr[y][x+1] = 0
	#to_down
	if y<m and arr[y+1][x] == 0:
		arr[y+1][x] = 1
		d = func(arr,x,y+1)
		arr[y+1][x] = 0
	#to_up
	if arr[y-1][x] == 0 and y>0:
		arr[y-1][x] = 1
		u = func(arr,x,y-1)
		arr[y-1][x] = 0
	#to_rigth_up
	if arr[y-1][x+1] == 0 and y>0:
		arr[y-1][x+1] = 1
		ru = func(arr,x+1,y-1)
		arr[y-1][x+1] = 0
	return r+d+u+ru

print(func(marr, 0, 0))
	 

