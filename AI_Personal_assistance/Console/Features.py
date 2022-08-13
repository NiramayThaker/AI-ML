import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia  # pip install wikipedia
import webbrowser as wb
import os
import smtplib
import psutil  # pip install psutil
import pyjokes
import pyautogui  # pip install pyautogui
from time import sleep
import random
import pywhatkit as kit  # as kit = we can use pywhatkit by just writing kit
import keyboard
import requests
import json

# TODO:
# Create projects
# Send message
# Trace location
# Gathering data (from APIs)
# Contact
# Get view from satellite
# Gathers latest news to know
# mark the way/route
# Search for people
# Identifies location (where am i)
# Trace Time
# Identify physical objects
# Recording video/audio
# Show time between 2 process
# Youtube video downloader
# URL Shortner


# Done:
# google, youtube search
# Date, time
# Wikipedia
# Send mail, msg
# Tells jokes
# Takes screenshot
# CPU details
# Find place
# Open any pc softwares
# Date, time, joke
# Self reboot
# Search number in truecaller


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)


def speak(audio):
	print(f": {audio}")
	engine.say(audio)
	engine.runAndWait()


def about_yourself():
	"""
	telling about his creator
	(you can add more to it if you want)
	"""

	speak('dear sir, my name is SIREN;'
		  'one type of personal assistance ,;'
		  'i can help you in as many way you allow me to do;'
		  'i am created by one genius person names niramay thakar;'
		  'it can be also said that niramay thakar is my creator')


def spelling_name():
	"""
	it will print the spelling on console and also speak the spelling
	of his name whenever you will ask for
	"""

	speak("Spelling of my name is ... ")
	print("Spelling of my name is\n")
	print("       ||       ")
	print("       \/         ")
	print("\n :-- SIREN --: \n")
	speak("S,; I,; R,; E,; N")
	speak("SIREN")
	speak("Meaning of my name is a beautiful but dangerous woman")


def date():
	"""
	tell me the date whenever i will ask for
	"""

	year = int(datetime.datetime.now().year)
	month = int(datetime.datetime.now().month)
	current_date = int(datetime.datetime.now().day)
	speak("dear sir, the current date is")
	speak(current_date)
	speak(month)
	speak(year)


def time():
	"""
	tell me the time whenever i will ask for
	"""

	current_time = datetime.datetime.now().strftime("%I:%M:%S")
	speak("dear sir, the current time is")
	speak(current_time)


def wishme():
	"""
	it will wish me as we start it
	"""

	speak("Welcome back sir!")
	speak("i am SIREN, your personal assistance ... ")

	"""speak("how are you sir ... ")
	Iam = takeCommand().lower
	if 'i am fine' in Iam:
		speak("That's great i am happy to know that you are fine..")
	elif 'how are you' in Iam:
		speak("i am also fine because you are fine")

	elif 'i am not fine' in Iam:
		speak("why what happened sir, can i help you ?")
		if 'no nothing' or "no you can't" in Iam:
			speak("as you wish sir")
			if 'how are you' in Iam:
				speak("i am also not fine because you are not fine")
	time()
	date()"""

	hour = datetime.datetime.now().hour
	if 6 <= hour < 12:
		speak("Good morning sir!")
	elif 12 <= hour < 18:
		speak("Good afternoon sir")
	elif 18 <= hour < 24:
		speak("Good Evening sir")
	else:
		speak("Good night sir")

	# speak("I am ALEXIS, your personal assistance ...")
	speak("Please tell me how can i help you ..?")


def take_command():
	"""
	It takes microphone input from user
	"""

	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listing ... ")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing ... ")
		taking_audio = r.recognize_google(audio, language='en-in')
		print(f"User said ->>  {taking_audio}\n")

	except Exception as E:
		print(E)

		print("plz repeat")
		speak("Can you please say it again ... ")
		return "None"
	return taking_audio


def wait():
	"""
	will make ALEXIS sleep till doesn't called or quit
	"""

	speak("Type on your console as per given option to tell me what i should do ")
	print("TYPE :-\n awake -: to continue")
	print(" \n         'OR'          \n")
	print("TYPE :-\n offline -: to leave")

	i = input("\nType when you want to call me back ->> ").lower()

	if i == 'come back' or 'awake':
		speak("I am back for your service sir")
	elif i == 'offline' or i == 'goodbye':
		speak('good bye sir')
		quit()
	else:
		speak("can't recognize type it again")
		wait()


def send_email(send_to, contact):
	"""
	will help you to send email
	"""

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login('youremail@gamil.com', '123')
	server.sendmail('youremail@gmail.com', send_to, contact)
	server.close()


def cpu():
	"""
	will show system detail
	"""

	cpu_usage = str(psutil.cpu_percent())
	speak('CPU is at' + cpu_usage)
	_battery = psutil.sensors_battery()
	speak("Battery is at")
	speak(_battery.percent)


def jokes():
	"""
	will find and tell the jocks
	"""

	speak(pyjokes.get_joke())


def screenshot():
	"""
	will take a screenshot
	"""

	img = pyautogui.screenshot()
	img.save("C:\\Users\\Admin\\Pictures\\Camera Roll")


def start_project():
	"""Will help opening our IDE"""

	speak("which IDE you want to work")
	open_softs = take_command()

	if "pycharm" in open_softs:
		os.startfile("F:\\Pycharm\\PyCharm Community Edition 2022.2\\bin\\pycharm64.exe")
	if "vs code" in open_softs:
		os.startfile("D:\Microsoft VS Code\Code.exe")


def youtube_automate():
	"""Control youtube"""

	speak("What's your command")
	comm = take_command()

	if "pause" or "play" in comm:
		keyboard.press("space bar")

	if "next" in comm:
		keyboard.press("shift + n")

	if "press" in comm:
		keyboard.press(comm)


def alarm(query):
	with open(".\\data.txt", 'w') as data_file:
		data_file.write(query)
		data_file.close()
		os.startfile("D:\\Code,Software\\python\\PycharmProjects\\Alexis\\practice\\DataBase\\alarm.py")


def open_softs():
	"""open any installed software"""

	speak("What do you want to open")
	comm = take_command()
	keyboard.press_and_release('windows + S', '\n')
	speak(f"Opening {comm}")

	keyboard.write(comm)
	keyboard.press("space bar")
	# keyboard.press_and_release('enter')
	pyautogui.keyDown("enter")
	pyautogui.keyUp("enter")


def restart_yourself():
	"""Restart itslef"""

	pyautogui.keyDown("shift")
	pyautogui.keyDown("f10")
	pyautogui.keyUp("shift")
	pyautogui.keyUp("f10")
	keyboard.press("enter")


def my_location():
	ip_addr = requests.get(url='https://api.ipify.org').text

	# url = "https://get.geojs.io/v1/ip/geo" + ip_addr + ".json"

	url = "http://api.ipstack.com/check?access_key=" + ip_addr + ".json"
	geo_q = requests.get(url)
	geo_json = json.loads(geo_q.text)
	print(url)
	state, country = geo_json['state'], geo_json['country']
	speak(f"sir your are currently at {state} {country}")


def google_maps(place):
	place_url = "https://www.google.com/maps/place/" + str(place)
	wb.open(url=place_url)


def search_caller():
	"""Search caller ID on truecaller"""

	speak("Tell me his number sir")
	number = take_command()

	number_url = "https://www.truecaller.com/search/in/" + str(number)
	wb.open(url=number_url)


def press_keys(keys, n):
	for i in range(n):
		if keys[i + 1] == "+":
			pyautogui.keyDown(keys[i])
			pyautogui.keyDown(keys[i + 1])
			pyautogui.keyUp(keys[i])
			pyautogui.keyUp(keys[i + 1])
		else:
			keyboard.press_and_release(keys[i])
			if i == n - 1:
				keyboard.press_and_release(keys[i + 1])
