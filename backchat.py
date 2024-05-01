from vosk import Model, KaldiRecognizer
import pyaudio
import RPi.GPIO as GPIO
import time
import renderer
import censor

GPIO.setmode(GPIO.BCM)

modelPath = "vosk-model-small-en-us-0.15"
#modelPath = "vosk-model-en-us-0.22-lgraph"
modelPath = "vosk-model-en-us-0.22"

rate = 44100
chunk = 1024 * 12

buttonPin = 23
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

model = Model(modelPath)



mic = pyaudio.PyAudio()


while True:
	time.sleep(0.2)
	
	if GPIO.input(buttonPin) == 1:
		print("recording")
		while True:
			try:
				frames=[]
				stream = mic.open(format=pyaudio.paInt16, channels=1, rate=rate, input=True, frames_per_buffer=chunk)
				while GPIO.input(buttonPin) == 1:
					data = stream.read(chunk)
					frames.append(data)
					
				
				print("done recording")
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
				renderer.render(text)
				break
			except Exception as e:
				print("error")
				print(e)
# ~ print("go")


# ~ data = stream.read(chunk)
# ~ #print(data)
	
# ~ if recognizer.AcceptWaveform(data):
	# ~ text = recognizer.Result()
	# ~ print(f"{text[14:-3]}")
# ~ else:
	# ~ print("nada")
