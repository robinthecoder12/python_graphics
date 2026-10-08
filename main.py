import pygame
import sys

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame Graphics")

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Fill background with black (RGB)
    screen.fill((0, 0, 0)) 
    
    # Draw a green circle: (surface, color, center_coordinates, radius)
    pygame.draw.circle(screen, (0, 255, 0), (300, 200), 50)
    
    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()
