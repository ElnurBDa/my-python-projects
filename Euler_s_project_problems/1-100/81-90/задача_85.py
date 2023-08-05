def pols_in_pols(w, h):
    # polygons in polygons
    count = 0
    for x in range(1, w + 1):
        for y in range(1, h + 1):
            _w_ = w - x + 1
            _h_ = h - y + 1
            count += _h_ * _w_
    return count

perfect=2000000
max=1000
best=[0,0]
for x in range(1, 1000):
    for y in range(1, 1000):
        m=abs(perfect-pols_in_pols(x,y))
        if m<max:
            best=(x,y)
            max=m
            print(best,m)
print(max,best)
'''
(3, 816) 16
(36, 77) 2
'''