import pyttsx3
import speech_recognition as sr
from bs4 import BeautifulSoup
import requests
import random


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)


def speak(audio):
	"""
	Speak whatever you pass to it as parameter
	"""

	print(f": {audio}")
	engine.say(audio)
	engine.runAndWait()


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
	recursive function
	which will make it sleep till doesn't called or quit
	"""

	wake_word = ["wake up", "listen", "hey darling", "daddys home"]
	i = take_command()
	if i in wake_word:
		return
	else:
		wait()


def live_info():
	"""
	Will scrape live information from BRAVE Search engine and speak it
	"""

	while True:
		speak("yes sir?")
		search_data = take_command()
		if search_data != "quit":
			search_data = search_data.split()
			search_data = [f"{i}+" for i in search_data]

			print("".join(search_data))

			response = requests.get(f"https://search.brave.com/search?q={search_data}&source=desktop")
			soup = BeautifulSoup(response.text, "html.parser")

			data = soup.find_all("p", class_="snippet-description")
			reply_data = []

			i = 0
			while i <= 5:
				reply_data.append(data[i].getText())
				i += 1

			speak(reply_data[random.randint(0, 5)])
		else:
			break
	return
