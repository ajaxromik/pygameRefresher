import pygame
from tkinter import Tk
import TextInput as ti

def clip_text(text: str = "this was copied"):
	clipper = Tk()
	clipper.withdraw()
	clipper.clipboard_clear()
	clipper.clipboard_append(text)
	clipper.update() # now it stays on the clipboard after the window is closed
	clipper.destroy()

pygame.init()
pygame.font.init()
pygame.display.set_caption("Matrix RREF")

screen_res = (600,400)
screen = pygame.display.set_mode(screen_res)
# main_font = pygame.font.SysFont('Arial',28)

BACKGROUND = (0,63,191)

inputBox = ti.TextInput()

on = True
while on:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			on = False
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_BACKSPACE:
				inputBox.backspace()
			elif e.unicode == " ":
				inputBox.negate()
			elif e.key == pygame.K_RETURN or e.key == pygame.K_KP_ENTER:
				if not inputBox.isEmpty():
					print(f'number: {inputBox.text}')
					inputBox.clear()
			else:
				# print(f"\nkey: {e.unicode}")
				inputBox.charAdd(e.unicode)

	screen.fill(BACKGROUND)
	inputBox.update()
	screen.blit(inputBox.image, inputBox.rect)

	pygame.display.flip()
	pygame.time.Clock().tick(10) # 10fps because we don't need much

pygame.quit()
