import cv2
import matplotlib.pyplot as plt
import numpy as np
import pyautogui
import scipy.spatial as sp
import win32api
from PIL import Image
from pynput.mouse import Listener

fileName = "FINAL.png"

main_colors = {(0, 0, 0): "black",
               (255, 255, 255): "white",
               (255, 0, 0): "red",
               (0, 255, 0): "green",
               (0, 0, 255): "blue",
               (255, 255, 0): "yellow",
               (0, 255, 255): "cyan",
               (255, 0, 255): "magenta",
}

rgb, color = zip(*main_colors.items())
file = input("Path to file: ")
image = cv2.imread(file)
# convert BGR to RGB image
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

h, w, bpp = np.shape(image)


for y in range(0, h):
    for x in range(0, w):
        print("\r" + "                                                                        ", end="")
        print("\r" + f"reading pixel ({x + 1}, {y + 1})", end="")
        ########################
        # Used this part to find nearest color
        # reference : https://stackoverflow.com/a/22478139/9799700
        input_color = (image[y][x][0], image[y][x][1], image[y][x][2])
        tree = sp.KDTree(rgb)
        ditsance, result = tree.query(input_color)
        nearest_color = rgb[result]
        ###################

        image[y][x][0] = nearest_color[0]
        image[y][x][1] = nearest_color[1]
        image[y][x][2] = nearest_color[2]

print("\nimage saved as: " + fileName)

# show image
plt.ion()
plt.figure()
plt.axis("off")
plt.imshow(image)
plt.imsave(fileName, image)
im = Image.open(fileName)
pix = im.load()
text = plt.figtext(0, 0, s="COLOR HERE")

while True:
    plt.show()
    plt.pause(0.05)
    x, y = pyautogui.position()
    if win32api.GetKeyState(0x01)<0:
        try:
            rgbval = pyautogui.pixel(x, y)
            name = color[rgb.index(rgbval)]
            print("\r" + "                                             ", end="")
            print("\r" + str(pyautogui.pixel(x, y)) + " " + name, end="")
            text.set_text(name)
        except:
            pass


