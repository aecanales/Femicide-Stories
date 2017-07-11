import pygame

class image_object():

	def __init__(self, screen, img, highlight_img, pos, this_id):
		self.screen = screen
		self.obj = pygame.image.load(img)
		#I'm assuming both images have the same size (so there isn't problems with the rect)
		self.img = img
		self.highlight_img = highlight_img 
		self.pos = pos
		self.rect = self.obj.get_rect()
		self.rect.x = self.pos[0] - self.rect.width/2
		self.rect.y = self.pos[1] - self.rect.height/2
		self.id = this_id

		self.highlighted = False

	def draw(self):
		if not self.highlighted:
			self.obj = pygame.image.load(self.img)
		else:
			self.obj = pygame.image.load(self.highlight_img)
		self.screen.blit(self.obj, (self.pos[0] - self.rect.width/2, self.pos[1] - self.rect.height/2))


