import neopixel
import genericFont
from machine import Pin
import time

pinNum = 16

matHeight = 8
matWidth = 32

p = Pin(pinNum, Pin.OUT)
np = neopixel.NeoPixel(p, matHeight * matWidth)

#letterDicts = genericFont()

word = "Hello"

# for (key, value) in letters.items():
#     print(key)
#     print(value)

def renderLetter(letter, index):
    t = genericFont.getSymbol(letter)
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