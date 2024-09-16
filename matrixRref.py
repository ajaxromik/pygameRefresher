import pygame
from tkinter import Tk

def clip_text(text: str = "this was copied"):
	clipper = Tk()
	clipper.withdraw()
	clipper.clipboard_clear()
	clipper.clipboard_append(text)
	clipper.update() # now it stays on the clipboard after the window is closed
	clipper.destroy()

clip_text()

pygame.init()
# pygame.font.init()
pygame.display.set_caption("Matrix RREF")

screen_res = (600,400)
screen = pygame.display.set_mode(screen_res)
# main_font = pygame.font.SysFont('Arial',28)

BACKGROUND = (0,63,191)
on = True
while on:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			on = False


	screen.fill(BACKGROUND)
	pygame.display.flip()

	pygame.time.Clock().tick(10) # 10fps because we don't need much

pygame.quit()