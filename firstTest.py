import pygame
import sys


# print(f"""
# Arguments: {sys.argv} 
# Platform: {sys.platform}
# Version: {sys.version}""")

print("Otto is my favorite media character")

pygame.init()
pygame.font.init()

pygame.display.set_caption("circles are attracted to your mouse..")
screen = pygame.display.set_mode((600,400))
main_font = pygame.font.SysFont('Arial',28)

BACKGROUND, BOX_COLOR = (0,63,191),(0,191,0)
box_len, box_wid = 50, 50
window_leave, window_enter = 32784, 32783 #events show as numbers

on = True
onScreen = True
text_surface = main_font.render("Otto", False, (0,255,0)) #picks text to display
text = text_surface.get_rect(center=(300,200)) # makes a rect centered at center of screen
while on:
    for e in pygame.event.get():
        # print(e.type)
        if e.type == pygame.QUIT:
            on = False
        elif e.type == window_leave:
            onScreen = False
        elif e.type == window_enter:
            onScreen = True

    screen.fill(BACKGROUND) # makes the screen some color

    m_x,m_y = pygame.mouse.get_pos()

    if onScreen and m_x in range(0,601) and m_y in range(0,401):
        pygame.draw.circle(screen, BOX_COLOR, (m_x, m_y), box_len/2)
        #pygame.draw.rect(screen, BOX_COLOR, (m_x-box_len/2,m_y-box_wid/2,box_len,box_wid))

    screen.blit(text_surface, text)

    pygame.display.flip() # updates display

    pygame.time.Clock().tick(30) # maintains frame rate of 30fps

    
pygame.quit()
sys.exit(0)
