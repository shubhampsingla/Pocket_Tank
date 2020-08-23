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
image_1 = pygame.image.load('icons8-tank-48.png')
playerX_1 = 200
playerY_1 = 300 
playerX_change_1 = 0

image_2 = pygame.image.load('icons8-tank-48.png')
playerX_2 = 600
playerY_2 = 300
playerX_change_2 = 0

def show_image_1(playerX_1, playerY_1):

	# Drawing of image on screen (blit means to draw)
	screen.blit(image_1, (playerX_1, playerY_1))

def show_image_2(playerX_2, playerY_2):

	screen.blit(image_2, (playerX_2, playerY_2))

# Game loop
running = True

flag = 0

while running:

	#RGB - Red, Green, Blue
	screen.fill((50, 100, 50))

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False

		# If Keystroke is pressed check whether it is left or right
		if event.type == pygame.KEYDOWN:

			if flag == 0:

				if event.key == pygame.K_LEFT:
					playerX_change_1 = -0.1

				if event.key == pygame.K_RIGHT:
					playerX_change_1 = 0.1

			else:
				if event.key == pygame.K_LEFT:
					playerX_change_2 = -0.1

				if event.key == pygame.K_RIGHT:
					playerX_change_2 = 0.1

			if event.key == pygame.K_RETURN:
				if flag==0:
					flag=1
				else:
					flag=0
					
		if event.type == pygame.KEYUP:

			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change_1 = 0
				playerX_change_2 = 0

	playerX_1 += playerX_change_1

	playerX_2 += playerX_change_2

	# Tank image
	show_image_1(playerX_1, playerY_1)

	show_image_2(playerX_2, playerY_2)

	# To update the display
	pygame.display.update()