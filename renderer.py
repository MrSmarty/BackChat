import neopixel
import genericFont
from machine import Pin
import time

pinNum = 14

matHeight = 8
matWidth = 32

initialDelay = 5
endDelay = 3
moveDelay = 0.15

p = Pin(pinNum, Pin.OUT)
np = neopixel.NeoPixel(p, matHeight * matWidth)

defaultColor = (1, 1, 1)
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


def renderText(text, index):
    for letter in list(text):
        index += renderLetter(letter, index)
        index += renderLetter("spacing", index)
        
    np.write()
    
            
def render(word):
    totalLen = 0
    for letter in list(word):
        totalLen += genericFont.getPixelLen(letter) + 1
    
    
    if totalLen > matWidth:
        renderText(word, 0)
        time.sleep(initialDelay)
        for x in range(totalLen - matWidth):
            renderText(word, 0-x)
            time.sleep(moveDelay)
        time.sleep(endDelay)
        clear()

clear()
render("I LIKE BIG BUTTS AND I CANNOT LIE")

