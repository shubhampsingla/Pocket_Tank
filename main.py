import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Pocket Tank")


## Icon Part is not working
# icon = pygame.image.load('icons8-tank-48.png'
# pygame.display.set_icon(icon)

# Image of tank 
image = pygame.image.load('icons8-tank-48.png')
playerX = 400
playerY = 300 
playerX_change = 0

def show_image(playerX, playerY):

	# Drawing of image on screen (blit means to draw)
	screen.blit(image, (playerX, playerY))

# Game loop
running = True

while running:

	#RGB - Red, Green, Blue
	screen.fill((50, 100, 50))

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False

		# If Keystroke is pressed check whether it is left or right
		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_LEFT:
				playerX_change = -0.1

			if event.key == pygame.K_RIGHT:
				playerX_change = 0.1
					
		if event.type == pygame.KEYUP:

			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0

	playerX += playerX_change

	# Tank image
	show_image(playerX, playerY)

	# To update the display
	pygame.display.update()