import pygame

class text_object():
	#bleah that's one ugly init...
	def __init__(self, screen, content, font_type, font_size, color, pos, highlightable, this_id):
		self.screen = screen
		self.pos = pos
		self.content = str(content)
		self.font = pygame.font.Font(font_type, font_size)
		self.color = color
		self.obj = self.font.render(self.content, True, self.color)
		self.rect = self.obj.get_rect()
		self.rect.x = self.pos[0] - self.rect.width/2
		self.rect.y = self.pos[1] - self.rect.height/2
		self.highlightable = highlightable
		self.id = this_id

	def draw(self):
		self.obj = self.font.render(self.content, True, self.color)
		self.screen.blit(self.obj, (self.pos[0] - self.rect.width/2, self.pos[1] - self.rect.height/2))

# Each entry of this_list ('text'):
#  0- content (string)
#  1- size (int)
#  2- pos (tuple)
#  3- highlightable (bool)
# Returns a list of text objetcts.
def create_text_group(this_list, screen, font, color):
	return_list = []
	for text in this_list:
		return_list.append(text_object(screen, text[0], font, text[1], color, text[2], text[3], text[4]))
	return return_list