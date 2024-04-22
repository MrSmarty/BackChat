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
           "D": "#### \n#   #\n#   #\n#   #\n#   #\n#   #\n#   #\n#### \n", "E": "#####\n#    \n#    \n#### \n#    \n#    \n#    \n#####\n", "F": "#####\n#    \n#    \n#### \n#    \n#    \n#    \n#    \n",
           "G": " ### \n#   #\n#    \n# ###\n#   #\n#   #\n#   #\n ### \n", "H": "#   #\n#   #\n#   #\n#####\n#   #\n#   #\n#   #\n#   #\n", "I": "###\n # \n # \n # \n # \n # \n # \n###\n", "J": " ###\n   #\n   #\n   #\n   #\n   #\n#  #\n ## \n",
           "K": "#   #\n#  # \n# #  \n##   \n# #  \n#  # \n#   #\n#   #\n", "L": "#   \n#   \n#   \n#   \n#   \n#   \n#   \n####\n", "M": "#     #\n##   ##\n# # # #\n#  #  #\n#     #\n#     #\n#     #\n#     #\n"}


# for (key, value) in letters.items():
#     print(key)
#     print(value)

def renderLetter(letter, index):
    t = letters[letter]
    t = t.split("\n")
    maxWidth = 0
    for x in range(len(t)):
        for y in range(len(t[x])):

            if len(t[x]) > maxWidth:
                maxWidth = len(t[x])

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
    return maxWidth


def renderWord(word):
    index = 0
    for letter in list(word):
        index += renderLetter(letter, index) + 1
    np.write()


renderWord("MALL")


