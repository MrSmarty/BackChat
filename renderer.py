import neopixel
import genericFont
#from machine import Pin
import board
import time

pinNum = 14

matHeight = 8
matWidth = 32

initialDelay = 1
endDelay = 3
moveDelay = 0.1

#p = Pin(pinNum, Pin.OUT)
np = neopixel.NeoPixel(board.D18, matHeight * matWidth, auto_write=False)

defaultColor = (250, 1, 1)
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
     np.fill(blankColor)
     np.show()
#    for x in range(matWidth * matHeight):
#        np[x] = (0, 0, 0)
#    np.write()


def renderText(text, index):
    for letter in list(text):
        index += renderLetter(letter, index)
        index += renderLetter("spacing", index)
        
    np.show()
    
            
def render(word):
    np.fill(blankColor)
    totalLen = 0
    for letter in list(word):
        totalLen += genericFont.getPixelLen(letter) + 1
    
    renderText(word,0)
    if totalLen > matWidth:
        #renderText(word, 0)
        time.sleep(initialDelay)
        for x in range(totalLen - matWidth + 1):
            renderText(word, 0-x)
            time.sleep(moveDelay)
   # time.sleep(endDelay)
   # clear()

clear()
# render("WEE")
# time.sleep(1)
# while True:
	# defaultColor=(250,1,1)
	# render("WOO")
	# time.sleep(0.5)
	# clear()
	# defaultColor = (1,1,250)
	# render("WEE")
	# time.sleep(0.5)
