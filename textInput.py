import pygame
pygame.init()

class textInput:
	chars = " 1234567890" # for now just numbers and space

	def __init__(self):
		self.text = ""
		self.font = pygame.font.Font('Arial', 28)

pygame.quit()