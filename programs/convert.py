import cv2
import matplotlib.pyplot as plt
import numpy as np
import pyautogui
import scipy.spatial as sp
import win32api
from PIL import Image

fileName = "FINAL.png"

main_colors = {(21, 21, 21): "ink sac",
(17, 17, 17): "ink sac + 1x coal",
(13, 13, 13): "ink sac + 2x coal",
(25, 25, 25): "ink sac + feather",
(255, 0, 0): "poppy",
(230, 0, 0): "poppy + 1x coal",
(173, 0, 0): "poppy + 2x coal",
(85, 114, 23): "green dye",
(70, 93, 19): "green dye + 1x coal",
(52, 70, 14): "green dye + 2x coal",
(98, 133, 27): "green dye + feather",
(95, 63, 34): "cocoa beans",
(78, 51, 28): "cocoa beans + 1x coal",
(58, 39, 21): "cocoa beans + 2x coal",
(110, 74, 39): "cocoa beans + feather",
(34, 64, 187): "lapis lazuli",
(28, 52, 153): "lapis lazuli + 1x coal",
(21, 39, 115): "lapis lazuli + 2x coal",
(40, 75, 217): "lapis lazuli + feather",
(120, 43, 182): "purple dye",
(98, 35, 148): "purple dye + 1x coal",
(74, 26, 112): "purple dye + 2x coal",
(140, 50, 211): "purple dye + feather",
(52, 113, 145): "cyan dye",
(42, 92, 119): "cyan dye + 1x coal",
(32, 70, 89): "cyan dye + 2x coal",
(61, 132, 168): "cyan dye + feather",
(144, 144, 144): "light gray dye",
(117, 117, 117): "light gray dye + 1x coal",
(88, 88, 88): "light gray dye + 2x coal",
(167, 167, 167): "light gray due + feather",
(140, 144, 163): "gray dye",
(114, 118, 133): "gray dye + 1x coal",
(85, 88, 100): "gray dye + 2x coal",
(162, 168, 190): "gray dye + feather",
(234, 96, 142): "pink dye",
(191, 78, 116): "pink dye + 1x coal",
(144, 59, 87): "pink dye + 2x coal",
(255, 112, 165): "pink dye + feather",
(97, 191, 0): "lime dye",
(79, 156, 0): "lime dye + 1x coal",
(60, 117, 0): "lime dye + 2x coal",
(113, 221, 0): "lime dye + feather",
(204, 204, 0): "dandelion",
(166, 166, 0): "dandelion + 1x coal",
(125, 125, 0): "dandelion + 2x coal",
(237, 237, 0): "dandelion + feather",
(73, 135, 211): "light blue dye",
(73, 135, 211): "light blue dye + 1x coal",
(60, 110, 172): "light blue dye + 2x coal",
(85, 156, 245): "light blue dye + feather",
(172, 49, 219): "magenta dye",
(141, 40, 179): "magenta dye + 1x coal",
(141, 40, 179): "magenta dye + 2x coal",
(200, 58, 254): "magenta dye + feather",
(210, 103, 12): "orange dye",
(172, 84, 10): "orange dye + 1x coal",
(129, 63, 7): "orange dye + 2x coal",
(244, 120, 13): "orange dye + feather",
(221, 217, 209): "bone meal",
(181, 177, 170): "bone meal + 1x coal",
(136, 133, 127): "bone meal + 2x coal",
(255, 252, 242): "bone meal + feather",
(219, 202, 117): "pimpin seeds",
(179, 165, 96): "pumpkin seeds + 1x coal",
(134, 124, 72): "pumpkin seeds + 2x coal",
(254, 234, 136): "pumpkin seeds + feather",
(141, 91, 52): "melon seeds",
(115, 73, 43): "melon seeds + 1x coal",
(86, 55, 31): "melon seeds + 2x coal",
(164, 105, 61): "melon seeds + feather",
(65, 65, 65): "flint",
(53, 53, 53): "flint + 1x coal",
(40, 40, 40): "flint + 2x coal",
(76, 76, 76): "flint + feather",
(132, 132, 132): "gunpowder",
(108, 108, 108): "gunpowder + 1x coal",
(81, 81, 81): "gunpowder + 2x coal",
(153, 153, 153): "gunpowder + feather",
(123, 0, 0): "netherwart",
(101, 0, 0): "netherwart + 1x coal",
(75, 0, 0): "netherwart + 2x coal",
(143, 0, 0): "netherwart + feather",
(49, 201, 194): "prismarine crystals",
(39, 165, 159): "prismarine crystals + 1x coal",
(29, 123, 119): "prismarine crystals + 2x coal",
(57, 235, 226): "prismarine crystals + feather",
(101, 163, 16): "grass",
(83, 133, 13): "grass + 1x coal",
(62, 100, 9): "grass + 2x coal",
(118, 189, 19): "grass + feather",
(224, 210, 15): "golden nugget",
(183, 172, 12): "golden nugget + 1x coal",
(137, 129, 9): "golden nugget + 2x coal",
(224, 210, 15): "golden nugget + feather",
(171, 171, 171): "cobweb",
(140, 140, 140): "cobweb + 1x coal",
(105, 105, 105): "cobweb + 2x coal",
(199, 199, 199): "cobweb + feather",
(134, 134, 249): "ice",
(109, 109, 204): "ice + 1x coal",
(82, 82, 153): "ice + 2x coal",
(156, 156, 255): "ice + feather",
(0, 123, 0): "oak leaves",
(0, 101, 0): "oak leaves + 1x coal",
(0, 76, 0): "oak leaves + 2x coal",
(0, 144, 0): "oak leaves + feather",
(221, 217, 209): "snow",
(180, 180, 180): "snow + 1x coal",
(135, 135, 135): "snow + 2x coal",
(255, 255, 255): "snow + feather",
(96, 96, 96): "ghast tear",
(79, 79, 79): "ghast tear + 1x coal",
(59, 59, 59): "ghast tear + 2x coal",
(112, 112, 112): "ghast tear + feather",
(48, 48, 255): "lapis block",
(39, 39, 228): "lapis block + 1x coal",
(29, 29, 171): "lapis block  + 2x coal",
(56, 56, 255): "lapis block + feather",
(131, 101, 45): "oak wood",
(106, 84, 36): "oak wood + 1x coal",
(79, 63, 28): "oak wood + 2x coal",
(152, 118, 52): "oak wood + feather",
(157, 33, 33): "brick",
(128, 27, 27): "brick + 1x coal",
(96, 21, 21): "brick + 2x coal",
(182, 39, 39): "brick + feather",
(45, 111, 255): "lapis ore",
(37, 91, 217): "lapis ore + 1x coal",
(28, 67, 163): "lapis ore + 2x coal",
(53, 129, 255): "lapis ore + feather",
(0, 215, 24): "emerald",
(0, 176, 18): "emerald + 1x coal",
(0, 131, 14): "emeral + 2x coal",
(0, 250, 27): "emeral + feather",
(123, 71, 26): "birch wood",
(101, 57, 21): "birch wood + 1x coal",
(75, 43, 15): "birch wood + 2x coal",
(143, 82, 31): "birch wood + feather",
(188, 149, 130): "egg",
(154, 122, 106): "egg + 1x coal",
(115, 91, 80): "egg + 2x coal",
(219, 174, 151): "egg + feather",
(157, 64, 9): "magma cream",
(129, 52, 7): "magma cream + 1x coal",
(97, 39, 6): "magma cream + 2x coal",
(183, 75, 10): "magma cream + feather",
(142, 68, 93): "beetroot",
(117, 55, 76): "beetroot + 1x coal",
(86, 42, 57): "beetroot + 2x coal",
(165, 79, 108): "beetroot + feather",
(96, 91, 128): "mycelium",
(79, 75, 104): "mycelium + 1x coal",
(59, 56, 78): "mycelium + 2x coal",
(112, 106, 148): "mycelium + feather",
(177, 112, 0): "glowstone dust",
(145, 91, 0): "glowstone dust + 1x coal",
(108, 69, 0): "glowstone dust + 2x coal",
(205, 131, 0): "glowstone dust + feather",
(87, 104, 27): "slime ball",
(71, 85, 22): "slime ball + 1x coal",
(53, 63, 17): "slime ball + 2x coal",
(102, 121, 32): "slime ball + feather",
(158, 57, 59): "spider eye",
(128, 47, 48): "spider eye + 1x coal",
(96, 35, 36): "spider eye + 2x coal",
(183, 67, 68): "spider eye + feather",
(53, 34, 27): "soul sand",
(44, 27, 21): "soul sand + 1x coal",
(33, 20, 16): "soul sand + 2x coal",
(62, 39, 31): "soul sand + feather",
(123, 89, 78): "brown mushroom",
(101, 73, 64): "brown mushroom + 1x coal",
(75, 54, 47): "brown mushroom + 2x coal",
(143, 104, 91): "brown mushroom + feather",
(74, 79, 79): "iron nugget",
(60, 64, 64): "iron nugget + 1x coal",
(45, 48, 48): "iron nugget + 2x coal",
(86, 93, 93): "iron nugget + feather",
(116, 56, 74): "chorus fruit",
(95, 46, 62): "chorus fruit + 1x coal",
(71, 35, 46): "chorus fruit + 2x coal",
(135, 66, 87): "chorus fruit + feather",
(224, 210, 15): "purpur block",
(55, 41, 70): "purpur block + 1x coal",
(42, 30, 53): "purpur block + 2x coal",
(79, 59, 101): "purpur block + feather",
(72, 41, 23): "coarse dirt",
(59, 33, 18): "coarse dirt + 1x coal",
(44, 25, 13): "coarse dirt + 2x coal",
(84, 48, 27): "coarse dirt + feather",
(65, 72, 24): "potato",
(53, 59, 20): "potato + 1x coal",
(40, 44, 15): "potato + 2x coal",
(76, 84, 28): "potato + feather",
(142, 43, 26): "apple",
(117, 35, 21): "apple + 1x coal",
(88, 26, 16): "apple + 2x coal",
(166, 51, 31): "apple + feather",
(35, 17, 10): "charcoal",
(29, 14, 8): "charcoal + 1x coal",
(21, 10, 6): "charcoal + 2x coal",
(41, 20, 12): "charcoal + feather"}

rgb, color = zip(*main_colors.items())
file = input("Path to file: ")
image = cv2.imread(file)
# convert BGR to RGB image
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

h, w, bpp = np.shape(image)

KDTree = sp.KDTree

for y in range(0, h):
    for x in range(0, w):
        print("\r" + "                                                                        ", end="")
        print("\r" + f"reading pixel ({x + 1}, {y + 1})", end="")
        ########################
        # Used this part to find nearest color
        # reference : https://stackoverflow.com/a/22478139/9799700
        input_color = (image[y][x][0], image[y][x][1], image[y][x][2])
        tree = KDTree(rgb)
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


