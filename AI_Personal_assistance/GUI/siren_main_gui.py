# import sys
#
# from siren_gui import Ui_AI_UX
# from PyQt5 import QtCore, QtGui, QtWidgets
# # from PyQt5.QtCore import Qt, Qtimer, QDate
# # from PyQt5.uic import loadUiType
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# import main
#
#
# class MainThread(QThread):
# 	def __init__(self):
# 		super(MainThread, self).__init__()
#
# 	def run(self):
# 		main.Main()
#
# start_exe = MainThread()
#
#
# class GUIStart(MainThread):
# 	def __init__(self):
# 		super().__init__()
# 		self.ux = Ui_AI_UX()
# 		self.ux.setupUi(self)
# 		self.ux.start_btn.clicked.connect(self.start_task)
# 		self.ux.exit_btn.clicked.connect(self.exit())
#
# 	def start_task(self):
# 		self.ux.label1 = QtGui.QMovie("ExtraGui//Earth_Template.gif")
# 		self.ux.earth.setMovie(self.ux.label1)
# 		self.ux.label1.start()
#
# 		self.ux.label2 = QtGui.QMovie("ExtraGui//initial.gif")
# 		self.ux.initiate_sys.setMovie(self.ux.label2)
# 		self.ux.label2.start()
#
# 		self.ux.label3 = QtGui.QMovie("VoiceReg//Aqua.gif")
# 		self.ux.arc_rec.setMovie(self.ux.label3)
# 		self.ux.label3.start()
# 		start_exe.start()
#
#
# GuiApp = QApplication(sys.argv)
# siren = GUIStart()
# exit(GuiApp.exec_())

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from JarvisUi import Ui_MainWindow
import sys
import main


class MainThread(QThread):

	def __init__(self):
		super(MainThread, self).__init__()

	def run(self):
		self.Task_Gui()

	def Task_Gui(self):
		main.Main()


startFunctions = MainThread()


class Gui_Start(QMainWindow):

	def __init__(self):
		super().__init__()

		self.jarvis_ui = Ui_MainWindow()

		self.jarvis_ui.setupUi(self)

		self.jarvis_ui.pushButton.clicked.connect(self.startFunc)

		self.jarvis_ui.pushButton_2.clicked.connect(self.close)

	def startFunc(self):
		self.jarvis_ui.movies = QtGui.QMovie("VoiceReg//Aqua.gif")
		self.jarvis_ui.Gif.setMovie(self.jarvis_ui.movies)
		self.jarvis_ui.movies.start()

		self.jarvis_ui.movies_2 = QtGui.QMovie("B.G//Iron_Template_1.gif")

		self.jarvis_ui.Gif_2.setMovie(self.jarvis_ui.movies_2)

		self.jarvis_ui.movies_2.start()

		self.jarvis_ui.movies_3 = QtGui.QMovie("ExtraGui//Earth_Template.gif")

		self.jarvis_ui.Gif_3.setMovie(self.jarvis_ui.movies_3)

		self.jarvis_ui.movies_3.start()

		timer = QTimer(self)

		timer.timeout.connect(self.showtime)

		timer.start(1000)

		startFunctions.start()

	def showtime(self):
		current_time = QTime.currentTime()
		label_time = current_time.toString("hh:mm:ss")
		labbel = label_time
		self.jarvis_ui.textBrowser.setText(labbel)


Gui_App = QApplication(sys.argv)
Gui_Jarvis = Gui_Start()
Gui_Jarvis.show()
exit(Gui_App.exec_())
