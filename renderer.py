import neopixel
from machine import Pin
import time

pinNum = 16

matHeight = 8
matWidth = 32

P = Pin(pinNum, Pin.OUT)
np = neopixel.NeoPixel(P, matHeight * matWidth)

word = "Hello"

test = """
 ### 
#   #
#   #
#   #
#####
#   #
#   #
#   #
"""

letters = {"A": " ### \n#   #\n#   #\n#   #\n#####\n#   #\n#   #\n#   #\n", "B": "#### \n#   #\n#   #\n#### \n#   #\n#   #\n#   #\n#### \n", "C": " ### \n#   #\n#    \n#    \n#    \n#    \n#   #\n ### \n",
           "D": "#### \n#   #\n#   #\n#   #\n#   #\n#   #\n#   #\n#### \n", "E": "#####\n#    \n#    \n#### \n#    \n#    \n#    \n#####\n", "F": "#####\n#     \n#    \n#### \n#    \n#    \n#    \n#    \n", "G": " ### \n#   #\n#    \n# ###\n#   #\n#   #\n#   #\n ### \n"}


# for (key, value) in letters.items():
#     print(key)
#     print(value)

def renderLetter(letter, index):
    for elem in letter:
        t = letters[elem]
        t = t.split("\n")
        for x in range(len(t)):
            for y in range(len(t[x])):
                if (y+index) % 2 == 0:
                    if t[x][y] == "#":
                        np[x + (y+index) * matHeight] = (255, 0, 0)
                    else:
                        np[x + (y+index) * matHeight] = (0, 0, 0)
                else:
                    if t[x][y] == "#":
                        np[(y+1+index) * matHeight - x-1] = (255, 0, 0)
                    else:
                        np[(y+1+index) * matHeight-x-1] = (0, 0, 0)
    np.write()


def renderWord(word):
    index = 0
    for letter in list(word):
        renderLetter(letter, index)
        index += 6


renderWord("FAD")
