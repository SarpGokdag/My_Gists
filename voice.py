'''
Speech Recognition using Google Speech API
SARP GOKDAG
'''

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	while True:
		audio = r.listen(source)
		output_result = r.recognize_google(audio)
		try:
			print(output_result)
		except:
			print(" sorry , I couldnt understand what you've said")
