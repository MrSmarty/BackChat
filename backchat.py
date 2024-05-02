from vosk import Model, KaldiRecognizer
import pyaudio
import RPi.GPIO as GPIO
import time
import renderer
import censor

from tkinter import *
from tkinter import ttk

GPIO.setmode(GPIO.BCM)

modelPath = "vosk-model-small-en-us-0.15"
#modelPath = "vosk-model-en-us-0.22-lgraph"
modelPath = "vosk-model-en-us-0.22"

rate = 44100
chunk = 1024 * 12

buttonPin = 26
sendPin = 6
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sendPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

toRender = ""

model = Model(modelPath)



mic = pyaudio.PyAudio()


root = Tk()
root.attributes("-fullscreen", True)
#root.overrideredirect(True)
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Backchat", font=("Times New Roman", 20)).grid(column=0, row=0)

message = StringVar()
message.set("Waiting...")
output = StringVar()
output.set("Output: ")
ttk.Label(frm, textvariable = message, font=("Times New Roman", 15)).grid(column=0, row=1)
ttk.Label(frm, textvariable = output, font=("Times New Roman", 15)).grid(column=0, row=2)
#root.mainloop()
root.update_idletasks()

while True:
	time.sleep(0.2)
	
	if GPIO.input(buttonPin) == 1:
		print("recording")
		message.set("Recording")
		output.set("Output: ")
		root.update_idletasks()
		while True:
			try:
				frames=[]
				stream = mic.open(format=pyaudio.paInt16, channels=1, rate=rate, input=True, frames_per_buffer=chunk)
				while GPIO.input(buttonPin) == 1:
					data = stream.read(chunk)
					frames.append(data)
					
				
				print("Done Recording")
				message.set("Done Recording")
				root.update_idletasks()
				stream.stop_stream()
				stream.close()
				
				print(len(b''.join(frames)))
				recognizer = KaldiRecognizer(model, rate)
				text=""
				if recognizer.AcceptWaveform(b''.join(frames)):
					text = recognizer.Result()[14:-3]
					print("full: " + text)
				
				text += recognizer.PartialResult()[17:-3]
				print("partial: " + text)
				text = censor.Censor(text)
				#renderer.render(text)
				toRender=text
				output.set("Output: " + text)
				root.update_idletasks()
				break
			except Exception as e:
				print("error")
				print(e)

	if GPIO.input(sendPin) == 1:
		print("sending " + toRender + " to renderer")
		renderer.render(toRender)

# ~ print("go")


# ~ data = stream.read(chunk)
# ~ #print(data)
	
# ~ if recognizer.AcceptWaveform(data):
	# ~ text = recognizer.Result()
	# ~ print(f"{text[14:-3]}")
# ~ else:
	# ~ print("nada")
