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
inputBox.rect.center = tuple(x // 2 for x in screen_res)

matrix = []
i, j, rows, columns = -2, 0, 0, 0

on = True
finishedMatrix = False
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
				if not inputBox.isEmpty() and not finishedMatrix:
					val = int(inputBox.text)

					if i == -2 and val > 0:
						rows = val
						i = -1
						print("i-2")
					elif i == -1 and val > 0:
						columns = val
						matrix = [[] for _ in range(rows)]
						i = 0
						print("i-1")
					elif i < rows:
						# i < rows, j < columns
						print("in range")
						matrix[i].append(val)
						j += 1

						if j >= columns:
							j = 0
							i += 1
							print("j too big")
					else:
						finishedMatrix = True

				print(f'number: {inputBox.text}\nmatrix: {matrix}')
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
