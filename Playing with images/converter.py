import imageio

b = [0, 0, 0]
w = [255, 255, 255]
g = [145, 255, 255]

img = imageio.imread('image_karandash.png')
new_img = []
"""
[
[[piksel],[piksel]...[piksel],[piksel]],
[[piksel],[piksel]...[piksel],[piksel]],
[[piksel],[piksel]...[piksel],[piksel]]
]"""

i = 0

for x in img:
    new_img.append([])
    for y in x:
        y = str(y)[1:-1].split()
        for a in y:
            y[0] = int(y[0])
            y[1] = int(y[1])
            y[2] = int(y[2])
        if y == w:
            new_img[i].append(w)
        else:
            new_img[i].append([y[1], y[2], y[0]])
    i += 1
print(new_img)
imageio.imwrite('new_image.png', new_img)
