import pygame

num_font = 'fonts/KL.ttf'
num_color = (255, 255, 255) # white
num_size = 72

class numberpad():
	def __init__(self, screen, pos):
		self.font = pygame.font.Font(num_font, num_size)
		self.screen = screen
		self.numbers = []
		self.input_number = ""
		self.input_number_display = self.font.render(self.input_number, True, num_color)
		self.pos = pos

		horizontal_spacing = 100
		vertical_spacing = 100
		initial_pos = self.pos
		num = 1
		for y in range(3):
			for x in range(3):
				self.numbers.append(number(screen, 
					(initial_pos[0] + x*horizontal_spacing, initial_pos[1] + y*vertical_spacing),
					num, self.font))
				num += 1
		self.numbers.append(number(screen, (self.pos[0] + 200, self.pos[1] + 265), "<-", self.font))

	def draw(self):
		rect = self.input_number_display.get_rect()
		self.screen.blit(self.input_number_display, (self.pos[0] + 221 - rect.width, self.pos[1] - 120))
		for num in self.numbers:
			num.draw()

	def click_event(self, number):
		if number == "<-":
			self.input_number = self.input_number[:len(self.input_number) - 1]
		elif len(self.input_number) < 2:
			self.input_number = self.input_number + str(number)
		self.input_number_display = self.font.render(self.input_number, True, num_color)

class number():
	def __init__(self, screen, pos, content, font):
		self.screen = screen
		self.pos = pos
		self.content = str(content)

		self.obj = font.render(self.content, True, num_color)

		self.rect = self.obj.get_rect()
		self.rect.x = self.pos[0] - self.rect.width/2
		self.rect.y = self.pos[1] - self.rect.height/2

		self.screen.blit(self.obj, (self.pos[0] - self.rect.width/2, self.pos[1] - self.rect.height/2))

	def draw(self):
		self.screen.blit(self.obj, (self.pos[0] - self.rect.width/2, self.pos[1] - self.rect.height/2))