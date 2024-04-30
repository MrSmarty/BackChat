from vosk import Model, KaldiRecognizer
import pyaudio
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

modelPath = "vosk-model-small-en-us-0.15"

rate = 44100
chunk = 1024 * 16

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
				if recognizer.AcceptWaveform(b''.join(frames)):
					text = recognizer.Result()
					print(text[14:-3])
				else:
					print(recognizer.PartialResult())
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
