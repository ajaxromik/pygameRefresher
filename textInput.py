import pygame
pygame.init()
# pygame.font.init()
GREY = (200,200,200)

class textInput(pygame.sprite.Sprite):
	allowedChars = " 1234567890" # for now just numbers and space
	DEFAULT_COLOR = WHITE = (0,0,0)
	
	def __init__(self, color = DEFAULT_COLOR):
		pygame.sprite.Sprite.__init__(self) # for some reason sprites cant be initialized with just the super().__init__()
		self.text = ""
		self.font = pygame.font.SysFont('Arial', 34)
		self.image = self.font.render("Type numbers, press space for negative", True, self.DEFAULT_COLOR)
		self.rect = self.image.get_rect()

	def output(self):
		print(f"\ncurrent output: {self.text}")

	def update(self):
		center = self.rect.center
		self.image = self.font.render(self.text, True, self.DEFAULT_COLOR)
		self.rect = self.image.get_rect()
		self.rect.center = center

	def charAdd(self, char): # placeholder text disappears after first call
		self.output()
		if char in self.allowedChars:
			self.text += char
			self.update()

	def backspace(self):
		if(len(self.text) != 0):
			self.text = self.text[:-1]

	def clear(self):
		self.text = ""

	def negate(self): # puts a negative sign at the front if there's one there already
		if(self.text[:1] == "-"):
			self.text = self.text[1:]
		elif(len(self.text) > 0):
			self.text = "-" + self.text


a = textInput()
print(a)

screen = pygame.display.set_mode((600,400))
a.rect.center = (300,200)
on = True
while on:
	screen.fill(GREY)
	screen.blit(a.image, a.rect)

	for e in pygame.event.get():
		match e.type:
			case pygame.QUIT:
				on = False
			case pygame.KEYDOWN:
				if e.key == pygame.K_BACKSPACE:
					a.backspace()
					print("\nerased")
				elif e.unicode == " ":
					a.negate()
				elif e.key == pygame.K_RETURN or e.key == pygame.K_KP_ENTER:
					print(f'number: {a.text}')
					a.clear()
				else:
					# print(f"\nkey: {e.unicode}")
					a.charAdd(e.unicode)

	a.update()
	pygame.display.flip()
	pygame.time.Clock().tick(20)


pygame.quit()