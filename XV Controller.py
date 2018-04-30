X = 1
Execute = True

import sys
import os
import time
import subprocess
import pygame
pygame.init()

class MainApp:

	def Path():
		return os.path.dirname(os.path.realpath(__file__))

	def Exit():
		Screen.Stop()
		pygame.quit()
		time.sleep(1)
		sys.exit()

class Display:

	def New(Name, DisplayWidth, DisplayHeight, Caption):
		Name = pygame.display.set_mode((DisplayWidth, DisplayHeight))
		pygame.display.set_caption(Caption)

class Screen:

	def Start():
		os.system("screen -S XVControl")

	def Stop():
		os.system("")

class Control: #Set parameter "Velocity" to 0 to stop movement

	DefaultVelocity = 50

	def Forward(Velocity):
		os.system("")

		if Velocity == 0:
			print("Stopping Forward Movement...")

		else:
			print("Moving Forward...")

	def Backward(Velocity):
		os.system("")

		if Velocity == 0:
			print("Stopping Backward Movement...")

		else:
			print("Moving Backward...")

	def Left(Velocity):
		os.system("")

		if Velocity == 0:
			print("Stopping Left Movement...")

		else:
			print("Moving Left...")

	def Right(Velocity):
		os.system("")

		if Velocity == 0:
			print("Stopping Right Movement...")

		else:
			print("Moving Right...")

	def Vacuum(Velocity):
		os.system("")

		if Velocity == 0:
			print("Stopping Vacuum...")

		else:
			print("Starting Vacuum...")

	def Brush(Velocity):
		os.system("")

		if Velocity == 0:
			print("Stopping Brush...")

		else:
			print("Starting Brush...")

class MainEventLoop:

	pygame.camera.list_cameras()

	while Execute == True:
		time.sleep(0.5)

		for event in pygame.event.get():
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LSHIFT:
					break


print("Goodbye...")
MainApp.Quit()
