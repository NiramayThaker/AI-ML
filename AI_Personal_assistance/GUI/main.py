from Features import *
import keyboard


# if __name__ == "__main__":
def Main():
	wishme()
	print("----------------- SIREN Turned ON -----------------")
	while True:
		query = take_command().lower()
		if "listen" or "wake up" in query:
			# all Logic starts here
			speak("At your service sir")
			query = take_command().lower()

			# device status
			if 'cpu status' in query:
				usage = str(psutil.cpu_percent())
				# usage = str(psutil.cpu_percent())
				speak('CPU is at' + usage)

			elif 'restart yourself' in query:
				restart_yourself()

			elif 'battery status' in query:
				battery = psutil.sensors_battery()
				speak("Battery is at")
				speak(battery.percent)

			# logic to open
			elif 'open software' in query:
				open_softs()
				keyboard.press_and_release("enter")

			elif 'start project' in query:
				# codePath = "D:\\VS CODE NIRAMAY"
				# codePath = "C:\\Users\\91830\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio " \
				#            "Code "
				# os.startfile(codePath)
				start_project()

			elif 'control youtube' in query:
				youtube_automate()

			elif 'press' in query:
				speak("ok sir")
				query = query.replace("press", "")
				str_q = "".join(query)
				print(str_q)
				q_list = list(str_q)
				print(q_list)
				n = len(q_list)
				press_keys(q_list, n)

			# for searching (on google, wikipedia)
			elif 'search' in query:
				speak('yes, why not. what do you want me to search for ..??')
				cm = take_command().lower()
				if "break" in cm:
					pass
				else:
					wb.Chrome()
					wb.open(f"{cm}")

				speak("done sir ... ")
			# wait()

			elif 'wikipedia' in query:
				speak("Searching Wikipedia .... ")
				query = query.replace("wikipedia", "")
				results = wikipedia.summary(query, sentences=3)
				speak("According to wikipedia :- \n")
				print(results)
				speak(results)

			# logic to play music
			elif 'play songs on youtube' in query:
				speak("which one ?")
				# str1 = input("Song Name -> ")
				str1 = take_command()
				kit.playonyt(str1)

			elif 'search on youtube' in query:
				speak("what we are looking for ?")
				# str1 = input("Song Name -> ")
				str1 = take_command()
				kit.playonyt(str1)

			elif "go to sleep" in query:
				speak("as you wish sir")
				wait()

			# Location
			elif 'find place' in query:
				speak("Which place you want to find ?")
				find_place = take_command()
				google_maps(find_place)

			elif 'find caller' in query:
				search_caller()

			# information (asking)
			elif 'about yourself' in query:
				speak("Yes, offcouse")
				# sleep(1)
				about_yourself()

			elif "your spelling" in query:
				spelling_name()
				speak("you can also see it on your console, if you want to see spelling of my name")

			elif 'the time' in query:
				time()

			elif 'the date' in query:
				date()

			elif 'send email' in query:
				try:
					speak("tell me the gmail address of person you want to send the mail")
					send_to = take_command()
					speak("what do you want to say ..??")
					content = take_command()

					to = send_to + "@gmail.com"

					send_email(to, content)
					speak("Email has been sent")

				except Exception as e:
					print(e)
					speak("Sorry can't send email")

			# logic for polite reply
			elif 'thank' in query:
				speak("it's my pleasure sir ")

			elif 'joke' in query:
				speak(pyjokes.get_joke())

			elif 'goodbye' or 'good bye' in query:
				speak("Good Bye dear sir ")
				print("----------------- ALEXIS turned OFF -----------------")
				quit()

			else:
				speak("can you please say it again")
