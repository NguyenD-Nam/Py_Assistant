import speech_recognition
import pyttsx3
from datetime import date, datetime
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
import pyowm
from pyowm import OWM
import subprocess
import win32gui, win32con

robot_ear = speech_recognition.Recognizer() 



#										~~~~~ STARTING THE ASSISTANT ~~~~~


while True:
	#										~~~~~ LISTENNING ~~~~~
	with speech_recognition.Microphone() as mic:
		print("Robot: *I'm listening\n")
		audio = robot_ear.adjust_for_ambient_noise(mic)
		audio = robot_ear.listen(mic)


	#									 ~~~~~ VOICE RECOGNITION ~~~~~
	print("Robot: ...\n")

	try:
		you=robot_ear.recognize_google(audio)
	except:
		you=""
	#you=input('You: ')
	print(f'You: {you}\n')


	#									 ~~~~~ ANALYZING COMMANDS ~~~~~
	#							 ==============================================
	#					 ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
	#							 ==============================================


	#										~~~~~ EMPTY COMMAND ~~~~~
	if you=="":
		robot_brain="Please say something clearly"
		robot_print=robot_brain+"\n"


	#										  ~~~~~ GREETING ~~~~~
	elif "hello" in you or "hi" in you or "hey" in you:
		robot_brain="Hello, what can I help you"
		robot_print="Hello, what can I help you\n"


	#										 ~~~~~ DATE TODAY ~~~~~
	elif "today" in you or "date" in you:
		today=date.today()
		d=today.strftime("%B %d, %Y")
		robot_brain=f'Today is {d}'
		robot_print=f"{d}\n"


	#											~~~~~ TIME ~~~~~
	elif "time" in you or "tam" in you or "what time is it" in you:
		time=datetime.now()
		t=time.strftime("%H hours %M minutes %S seconds")
		robot_brain=f"It's {t}"
		robot_print=F"{t}\n"


	#											~~~~~ FROM ~~~~~
	elif "where are you from" in you:
		robot_brain="I'm from Vietnam"
		robot_print=robot_brain+"\n"



	#											~~~~~ THANKS ~~~~~
	elif "thank" in you or "thank you" in you or "thanks" in you:
		robot_brain="You're welcome"
		robot_print=robot_brain+"\n"


	#									~~~~~ CAPITAL CITY OF VIETNAM ~~~~~
	elif "capital" in you or "city" in you and "Vietnam" in you:
		robot_brain="The capital city of Vietnam is Hanoi"
		robot_print=robot_brain+"\n"


	#											~~~~~ MCK RAP ~~~~~
	# elif ("play a song" in you or "rap" in you) and "mck" in you:
	# 	mixer.init()
	# 	mixer.music.load("giau-vi-ban-sang-vi-vo.mp3")
	# 	mixer.music.set_volume(0.05)
	# 	mixer.music.play()
	# 	while True:
	# 		print("Press 'p' to pause,\n      'r' to resume")
	# 		print("      'e' to stop playing song")
	# 		print("Command:",end="")
	# 		query = input("  ")
	# 		if query == 'p':
	# 			mixer.music.pause()
	# 		elif query == 'r':
	# 			mixer.music.unpause()
	# 		elif query == 'e':
	# 			mixer.music.stop()
	# 			break
	# 	continue


	#											~~~~~ WEATHER ~~~~~
	elif "weather" in you or "weather status" in you or "temperature" in you:
		ahi="Please tell me the name of the city"
		print(f'Robot: {ahi}')
		engine1=pyttsx3.init()
		engine1.say(ahi)
		engine1.runAndWait()

		with speech_recognition.Microphone() as mi:
			print("Name?")
			audio1 = robot_ear.adjust_for_ambient_noise(mi)
			audio1 = robot_ear.listen(mi)
		try:
			you3=robot_ear.recognize_google(audio1)
		except:
			you3="Ho Chi Minh"
		#you3=input()
		city = you3
		APIKEY='d3bcd430a04cb83bc5bd73e385a9030f'  
		owm=OWM(APIKEY)
		mgr=owm.weather_manager()        
		obs=mgr.weather_at_place(city)  
		Data=obs.weather
		a=Data.temperature(unit='celsius')['temp']
		robot_brain=f'City: {city}: Status: {Data.detailed_status}'+', '+f'Temperature: {a} degree Celsius'
		robot_print=robot_brain


	#											~~~~~ CHROME ~~~~~
	elif "chrome" in you or "Google Chrome" in you or "Chrome" in you:
		robot_brain="Opening Google Chrome"
		robot_print=robot_brain+"\n"
		subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])


	#										 ~~~~~ CLOSE WINDOW ~~~~~
	elif "close" in you and "window" in you:
		robot_brain="Closing foreground window"
		robot_print=robot_brain+"\n"
		Minimize = win32gui.GetForegroundWindow()
		win32gui.PostMessage(Minimize,win32con.WM_CLOSE,0,0)#CloseWindow(Minimize, win32con.SW_MINIMIZE)


	#										~~~~~ PROGRAM SLEEP ~~~~~
	elif "wait" in you or "temporarily stop" in you or "pause" in you:
		ahii="Please tell me the time interval in seconds"
		print(f'Robot: {ahii}')
		engine1=pyttsx3.init()
		engine1.say(ahii)
		engine1.runAndWait()

		while True:
			with speech_recognition.Microphone() as mii:
				print("Time?")
				audiohihi = robot_ear.adjust_for_ambient_noise(mii)
				audiohihi = robot_ear.listen(mii)
				you4=''
			try:
				you4=robot_ear.recognize_google(audiohihi)
			except:
				you="10"
			if you4.isdigit():
				break
			else:
				print("Cannot understand, please repeat the time interval in seconds")
				numb="Cannot understand, please repeat the time interval in seconds"
				engine1=pyttsx3.init()
				engine1.say(numb)
				engine1.runAndWait()
		#you4=input()
		tiime = you4
		robot_brain=f'Stopping program for {tiime} seconds'
		robot_print=robot_brain+"\n"
		print(f"Robot: {robot_print}")

		engine=pyttsx3.init()
		engine.say(robot_brain)
		engine.runAndWait()
		nam=int(tiime)
		time.sleep(nam)

		robot_brain=f'Waiting session ends, resuming program'
		robot_print=robot_brain+"\n"
		print(f"Robot: {robot_print}")

		engine=pyttsx3.init()
		engine.say(robot_brain)
		engine.runAndWait()

		continue


	#											~~~~~ BYE ~~~~~
	elif "bye" in you or "goodbye" in you or "goodnight" in you or "good bye" in you: 
		robot_brain = "Goodbye, see you later"
		robot_print = "Goodbye, see you later"
		print(robot_print)

		engine=pyttsx3.init()
		engine.say(robot_brain)
		engine.runAndWait()
		break


	#									  ~~~~~ DON'T UNDERSTAND ~~~~~
	else:
		robot_brain="I cannot understand"
		robot_print="I cannot understand\n"


	#									  ~~~~~ PRINTING REPLIES ~~~~~
	print(f"Robot: {robot_print}")

	engine=pyttsx3.init()
	engine.say(robot_brain)
	engine.runAndWait()