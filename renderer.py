import neopixel
import genericFont
from machine import Pin
import time

pinNum = 16

matHeight = 8
matWidth = 32

p = Pin(pinNum, Pin.OUT)
np = neopixel.NeoPixel(p, matHeight * matWidth)

defaultColor = (50, 1, 1)
blankColor = (0, 0, 0)

# letterDicts = genericFont()

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
            if y + index < matWidth and y + index >= 0:

                if (y+index) % 2 == 0:
                    if t[x][y] == "#":
                        np[x + (y+index) * matHeight] = defaultColor
                    else:
                        np[x + (y+index) * matHeight] = blankColor
                else:
                    if t[x][y] == "#":
                        np[(y+1+index) * matHeight - x-1] = defaultColor
                    else:
                        np[(y+1+index) * matHeight-x-1] = blankColor
    return maxWidth


def clear():
    for x in range(matWidth * matHeight):
        np[x] = (0, 0, 0)
    np.write()


def renderWord(word, index):
    for letter in list(word):
        index += renderLetter(letter, index) + 1
    np.write()


i = 0
# while i < 1000:
#     clear()
#     renderWord(".000001001", 0 - i)
#     time.sleep(0.5)
#     i += 1

renderWord("STOP", 0)
