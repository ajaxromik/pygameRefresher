import pygame

pygame.init()
# pygame.font.init()
pygame.display.set_caption("Matrix RREF")

screen = pygame.display.set_mode((600,400))
# main_font = pygame.font.SysFont('Arial',28)

BACKGROUND = (0,63,191)

on = True
while on:

	for e in pygame.event.get():
        if e.type == pygame.QUIT:
            on = False

	pygame.display.flip()

	pygame.time.Clock().tick(10) # 10fps because we don't need much

pygame.quit()