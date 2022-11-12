import matplotlib.pyplot as plt
from PIL import Image
import cv2
import pyautogui
import win32api

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

file = input("Path to file: ")

if file == "":
    file = fileName

image = cv2.imread(file)
# convert BGR to RGB image
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

rgb, color = zip(*main_colors.items())

plt.ion()
plt.figure()
plt.axis("off")
plt.imshow(image)
im = Image.open(file)
pix = im.load()
text = plt.figtext(0.03, 0.03, s="COLOR HERE", fontsize=20)

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