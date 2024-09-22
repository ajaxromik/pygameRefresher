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

"""
stringify takes in a matrix(2d array of ints), and returns a string for wolfram alpha
"""
def stringify(matrix): 
	return ("rref " + str(matrix)).replace("[", "{").replace("]", "}")

pygame.init()
pygame.font.init()
pygame.display.set_caption("Matrix RREF")

screen_res = (600,400)
screen = pygame.display.set_mode(screen_res)
# main_font = pygame.font.SysFont('Arial',28)

BACKGROUND = (0,63,191)

inputBox = ti.TextInput(placeholder = "Enter in number of rows")
inputBox.rect.center = tuple(x // 2 for x in screen_res)

matrix = []
i, j, rows, columns = -2, 0, 0, 0

on = True
finishedMatrix = False
while on:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			on = False
		if not finishedMatrix and e.type == pygame.KEYDOWN:
			if e.key == pygame.K_BACKSPACE:
				inputBox.backspace()
			elif e.unicode == " ":
				inputBox.negate()
			elif e.key == pygame.K_RETURN or e.key == pygame.K_KP_ENTER:
				print(f'number: {inputBox.text}\nmatrix: {matrix}')
				if not inputBox.isEmpty() and not finishedMatrix:
					val = int(inputBox.text)

					if i == -2:
						inputBox.text = "Enter in number of rows"
						if val > 0: # split up so that program doesnt move on until columns and rows have positive values
							rows = val
							i = -1
							print("i-2")
							inputBox.text = "Enter in number of columns"
					elif i == -1:
						inputBox.text = "Enter in number of columns"
						if val > 0:
							columns = val
							matrix = [[] for _ in range(rows)]
							i = 0
							print("i-1")
							inputBox.text = f"Enter value for row {i+1}, column {j+1}"
					elif i < rows and i >= 0:
						# i < rows, j < columns
						print("in range")
						matrix[i].append(val)
						j += 1

						if j >= columns:
							j = 0
							i += 1
							print("j too big")

						if i >= rows:
							finishedMatrix = True
							inputBox.text = ''
							string = stringify(matrix)
							print(string)
							clip_text(string)
						else:
							inputBox.text = f"Enter value for row {i+1}, column {j+1}"

				inputBox.update()
				inputBox.clear()
				inputBox.modified = False
			else:
				# print(f"\nkey: {e.unicode}")
				inputBox.charAdd(e.unicode)

	screen.fill(BACKGROUND)
	inputBox.update()
	screen.blit(inputBox.image, inputBox.rect)

	pygame.display.flip()
	pygame.time.Clock().tick(10) # 10fps because we don't need much

pygame.quit()
