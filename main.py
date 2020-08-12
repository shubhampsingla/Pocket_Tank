import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Pocket Tank")

icon = pygame.image.load('icons8-tank-48.png')

pygame.display.set_icon(icon)


# Game loop 
running = True

while running:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False