from useble_py_files import txtblimg as t

my_field = t.Field(9, 55, t.syms[3] * 2)
# Смайлик
'''r1 = t.Rect(1, 2, 8, 8, my_field)
r1.draw()
r2 = t.Rect(2, 1, 7, 9, my_field)
r2.draw()

l1 = t.HorizontalLine(3, 6, 7, my_field, sym=t.syms[2] * 2)
l1.draw()

p1 = t.Point(2, 6, my_field, sym=t.syms[2] * 2)
p1.draw()
p2 = t.Point(7, 6, my_field, sym=t.syms[2] * 2)
p2.draw()

r3 = t.Rect(2, 3, 3, 4, my_field, sym=t.syms[2] * 2)
r3.draw()
r3 = t.Rect(6, 3, 7, 4, my_field, sym=t.syms[2] * 2)
r3.draw()

p3 = t.Point(3, 4, my_field, sym=t.syms[3] * 2)
p3.draw()
p4 = t.Point(7, 4, my_field, sym=t.syms[3] * 2)
p4.draw()
p5 = t.Point(3, 3, my_field, sym=t.syms[3] * 2)
p5.draw()
p6 = t.Point(7, 3, my_field, sym=t.syms[3] * 2)
p6.draw()'''

# Привет
'''s='ПРИВЕТ'
for x in range(0,6):
    y_start = 1+x*8
    y_end = 7+x*8
    lit1 = t.Literals(1, y_start, 7, y_end, s[x], my_field)
    lit1.draw()'''




my_field.draw()
