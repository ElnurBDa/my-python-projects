
from useble_py_files import txtblimg as t
from time import sleep
import asyncio
import keyboard

sym_pen = t.syms[0] * 2
sym_bg = t.syms[2] * 2
main_sym_pen = sym_pen
width, height = 10, 10
time = 1
x, y = 2, 2

my_field = t.Field(width, height, sym_bg)


async def move():
    while True:
        p = t.Point(x, y, my_field, main_sym_pen)
        p.draw()
        await asyncio.sleep(time * .1)


def change_pen():
    global sym_pen, sym_bg, main_sym_pen
    if main_sym_pen == sym_pen:
        main_sym_pen = sym_bg
        return main_sym_pen
    if main_sym_pen == sym_bg:
        main_sym_pen = sym_pen
        return main_sym_pen


async def butt():
    global x, y, my_field, main_sym_pen
    while True:
        try:
            if keyboard.is_pressed('d'):
                x += 1
                sleep(.3)
            elif keyboard.is_pressed('a'):
                x -= 1
                sleep(.3)
            elif keyboard.is_pressed('w'):
                y -= 1
                sleep(.3)
            elif keyboard.is_pressed('s'):
                y += 1
                sleep(.3)

            elif keyboard.is_pressed('e'):
                my_field = t.Field(width, height, sym_bg)
            elif keyboard.is_pressed('q'):
                main_sym_pen = change_pen()
                input()
            if y >= height:
                y = 0
            elif y < 0:
                y = height - 1
            if x >= width:
                x = 0
            elif x < 0:
                x = width - 1


        except:
            pass
        await asyncio.sleep(0.1)


async def run():
    while True:
        print()
        my_field.draw()
        print(x, y)
        await asyncio.sleep(time * .5)


loop = asyncio.get_event_loop()
asyncio.ensure_future(run())
asyncio.ensure_future(move())
asyncio.ensure_future(butt())

loop.run_forever()
