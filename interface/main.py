# GENERAL INITIALIZATION
import pygame
from pygame.locals import * # Fullscreen support

pygame.init()
pygame.mixer.init()

import text_handler, image_handler, numpad, layouts, audio_selector

import time

import serial
arduino = serial.Serial('COM3', 9600, timeout=.1)

# SCREEN INITIALIZATION
width=1280
height=720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Femicidio en Chile')

# FONTS
font_kl = 'fonts/KL.ttf'

# COLORS
color_white = (255, 255, 255)
color_highlight = (234, 119, 166)

# LAYOUT INITIALIZATION
this_numpad = numpad.numberpad(screen, (540, 420))

# First element of a layout is text group, second is image group
layout_list = []
current_layout = 0
layout_list.append([text_handler.create_text_group(layouts.l0_text_data, screen, font_kl, color_white),
	[image_handler.image_object(screen, 'images\male.png', 'images\male_highlight.png', (446,460), 1),
	image_handler.image_object(screen, 'images\woman.png', 'images\woman_highlight.png', (801,460), 2)]
	])
layout_list.append([text_handler.create_text_group(layouts.l1_text_data, screen, font_kl, color_white),
	[]
	])
layout_list.append([text_handler.create_text_group(layouts.l2_text_data, screen, font_kl, color_white),
	[]
	])
layout_list.append([text_handler.create_text_group(layouts.l3_text_data, screen, font_kl, color_white),
	[]
	])
layout_list.append([text_handler.create_text_group(layouts.l4_text_data, screen, font_kl, color_white),
	[]
	])
layout_list.append([text_handler.create_text_group(layouts.l5_text_data, screen, font_kl, color_white),
	[]
	])
layout_list.append([text_handler.create_text_group(layouts.l6_text_data, screen, font_kl, color_white),
	[]
	])

#DATA
female_age = 0
female_region = ""

#EVENTS (there has to be a better way to do this...)
# 0 is no event on click
def click_event(this_id, layout):
	if this_id == 0:
		return current_layout
	elif this_id == 1:
		print("clicked on male!")
		return 4 #closest female
	elif this_id == 2:
		print("clicked on female!")
		return 1 # age
	elif this_id == 3:
		print("female age: " + str(female_age))
		return 2 # region
	elif this_id == 4:
		print("female region: " + female_region)
		arduino.write("w".encode()) #Waiting for door to close
		print("Waiting...")
		return 3 # end
	elif this_id == 5:
		print("Chose: " + clicked_content)
		return 5 #age
	elif this_id == 6:
		print("female age: " + str(female_age))
		return 6 #region
	elif this_id == 7:
		print("female region: " + female_region)
		arduino.write("w".encode()) #Waiting for door to close
		print("Waiting...")
		return 3 #end

clicked_content = ""

#AUDIO
#Wanted to have this in a module but then I didn't now how to handle the arduino... 
#Encoding (if there is any better way to do this, I'm open ears):
# "f": female on "o": female off
# "m": message on "n": message off
# "d": data on "s": data off

def test():
	arduino.write("f".encode())
	print(arduino.readline().strip())
	time.sleep(1)
	arduino.write("o".encode())
	print(arduino.readline().strip())
	arduino.write("m".encode())
	print(arduino.readline().strip())
	time.sleep(1)
	arduino.write("n".encode())
	print(arduino.readline().strip())
	arduino.write("d".encode())
	print(arduino.readline().strip())
	time.sleep(1)
	arduino.write("s".encode())
	print(arduino.readline().strip())

def control_lights(lightshow):
	for action in lightshow:
		if str(action).isalpha():
			arduino.write(action.encode())
		else:
			time.sleep(action)

def get_lightshow(audio_name):
	if "norte_joven.m4a": return ["f", 1, "o", 1, "m", 1, "n", "d", 1, "s"]
	elif "norte_medio.m4a": return ["f", 1, "o", 1, "m", 1, "n", "d", 1, "s"]
	elif "norte_mayor.m4a": return ["f", 1, "o", 1, "m", 1, "n", "d", 1, "s"]
	elif "centro_joven.m4a": return ["f", 1, "o", 1, "m", 1, "n", "d", 1, "s"]
	elif "centro_medio.m4a": return ["f", 1, "o", 1, "m", 1, "n", "d", 1, "s"]
	elif "centro_mayor.m4a": return ["f", 1, "o", 1, "m", 1, "n", "d", 1, "s"]
	elif "sur_joven.m4a": return ["f", 1, "o", 1, "m", 1, "n", "d", 1, "s"]
	elif "sur_medio.m4a": return ["f", 1, "o", 1, "m", 1, "n", "d", 1, "s"]
	elif "sur_mayor.m4a": return ["f", 1, "o", 1, "m", 1, "n", "d", 1, "s"]

# MAIN LOOP
while True:
	screen.fill((0,0,0))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			arduino.close()
			running = pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #1 -> left click
			mpos = pygame.mouse.get_pos()
			for text in layout_list[current_layout][0]:
				if text.rect.collidepoint(mpos):
					clicked_content = text.content
					if current_layout == 1 or current_layout == 5:
						female_age = int(this_numpad.input_number)
					if current_layout == 2 or current_layout == 6:
						female_region = text.content
					current_layout = click_event(text.id, current_layout)
			for image in layout_list[current_layout][1]:
				if image.rect.collidepoint(mpos):
					current_layout = click_event(image.id, current_layout)
			for num in this_numpad.numbers:
				if num.rect.collidepoint(mpos):
					this_numpad.click_event(num.content)

	#'text' is a text object
	for text in layout_list[current_layout][0]:
		if text.highlightable:
			if text.rect.collidepoint(pygame.mouse.get_pos()):
				text.color = color_highlight
			else:
				text.color = color_white
		text.draw()

	#'image' is an image object
	for image in layout_list[current_layout][1]:
		if image.rect.collidepoint(pygame.mouse.get_pos()):
			image.highlighted = True
		else:
			image.highlighted = False
		image.draw()

	if current_layout == 1 or current_layout == 5:
		this_numpad.draw()

	pygame.display.flip()

	#ARDUINO CODE

	# Waiting for person to enter cabin 
	if current_layout == 3:
		data = arduino.readline().strip()
		if data == b'r': # 'r' for ready
			print ("Ready!")
			current_layout = 7

	# Playing audio
	if current_layout == 7:
		audio = "audio\\" + audio_selector.return_audio_name(female_region, female_age)
		print("selected audio: " + audio)
		pygame.mixer.music.load(audio)
		pygame.mixer.music.play()
		control_lights(get_lightshow(audio))
		current_layout = 0


