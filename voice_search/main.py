from browsing_AI import *


if __name__ == "__main__":
	speak("at your service sir")
	while True:
		wake_up_AI = take_command()
		if "search" in wake_up_AI:
			speak("what to search sir ?")
			live_info()

		if "good bye" in wake_up_AI:
			speak("Good bye sir")
			exit()

		if "go to sleep" in wake_up_AI:
			wait()
