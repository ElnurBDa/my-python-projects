import os
from skimage import io
import matplotlib.pyplot as plt
from skimage.color import rgb2hsv
filename = os.path.join('Flowers_cut.jpg')
file = io.imread(filename)
rgb_img = file
hsv_img = rgb2hsv(rgb_img)
value_img = hsv_img[:, :, 2]

fig, (ax0, ax2) = plt.subplots(ncols=2, figsize=(6, 4))

ax0.imshow(rgb_img)
ax0.set_title("RGB image")
ax0.axis('off')
ax2.imshow(value_img)
ax2.set_title("Value channel")
ax2.axis('off')

fig.tight_layout()
plt.show()
