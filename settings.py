#!/bin/python3
import os


def use():
	print("Volume = 1")
	print("Customize = 2")
	print("Brightness = 3")
	print("(Laptops) Display battery = 4")
	print("Background = 5")
	print("Change Wifi connection = 6 (requires root privellages)")
	print("Go Back = 0")
	command = int(input(": "))

	if command == 1:
		os.system("alsamixer")

	if command == 2:
		os.system("lxappearance")

	if command == 3:
		print("25 Brightness = 1")
		print("50 Brightness = 2")
		print("75 Brightness = 3")
		print("100 Brightness = 4")
		brightness = int(input(": "))
		if brightness == 1:
			os.system("xbacklight -set 25")
		if brightness == 2:
			os.system("xbacklight -set 50")
		if brightness == 3:
			os.system("xbacklight -set 75")
		if brightness == 4:
			os.system("xbacklight -set 100")

	if command == 4:
		os.system("acpi -b | lolcat")

	if command == 5:
		os.system("nitrogen")

	if command == 6:
		os.system("sudo wifi-menu")
	if command == 0:
		main_menu()
def download():
	print("Arch = 1")
	print("Debian/Ubuntu = 2")
	mod_slct = int(input(": "))
	if mod_slct == 1:		
		print("Install alsa-utils(Alsamixer) = 1")
		print("Install lxappearance = 2")
		print("Install xbacklight = 3")
		print("Install nitrogen = 4")
		print("Install netctl (Wifi-menu) = 5")
		print("Install all of the above = 6")
		print("Go Back = 0")
		install_slct = int(input(": "))
		if install_slct == 1:
			os.system("sudo pacman -S alsa-utils")
		if install_slct == 2:
			os.system("sudo pacman -S lxappearance")
		if install_slct == 3:
			os.system("sudo pacman -S xorg-xbacklight")
		if install_slct == 4:
			os.system("sudo pacman -S nitrogen")
		if install_slct == 5:
			os.system("sudo pacman -S netctl")
		if install_slct == 6:
			os.system("sudo pacman -S alsa-utils && sudo pacman -S lxappearance && sudo pacman -S xorg-xbacklight && sudo pacman -S nitrogen && sudo pacman -S netctl")
		if install_slct == 0:
			main_menu()
	if mod_slct == 2:
		print("Install alsa-utils = 1")
		print("Install lxappearance = 2")
		print("Install xbacklight = 3")
		print("Install nitrogen = 4")
		print("Install netctl (Wifi-menu) = 5")
		print("Install all of the above = 6")
		print("Go back = 0")
		install_slct = int(input(": "))
		if install_slct == 1:
			os.system("sudo apt install alsa-utils")
		if install_slct == 2:
			os.system("sudo apt install lxappearance")
		if install_slct == 3:
			os.system("sudo apt install xorg-xbacklight")
		if install_slct == 4:
			os.system("sudo apt install nitrogen")
		if install_slct == 5:
			os.system("sudo apt install netctl")
		if install_slct == 6:
			os.system("sudo apt install alsa-utils && sudo apt install lxappearance && sudo apt install xorg-xbacklight && sudo apt install nitrogen && sudo apt install netctl")
		if install_slct == 0:
			main_menu()
def main_menu():			
	print("Use = 1")
	print("Download = 2")
	while True:
		mode = int(input(": "))
		if mode == 1:
			use()
			print("1 = Use")
			print("2 = Download")
		if mode == 2:
			download()
			print("1 = Use")
			print("2 = Download")

main_menu()

