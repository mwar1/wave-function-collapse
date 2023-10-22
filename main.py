import pygame
pygame.init()

SCREENWIDTH = 750
SCREENHEIGHT = 750
size = (SCREENWIDTH, SCREENHEIGHT)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wave Function Collapse")
clock = pygame.time.Clock()

carryOn = True
while carryOn:
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
			carryOn=False

	pygame.display.flip()
	clock.tick(60)

pygame.quit()