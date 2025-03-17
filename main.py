import pygame
import sys
from datetime import datetime

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((0,0),pygame.RESIZABLE)
width,height = screen.get_width(),screen.get_height()
pygame.display.set_caption("Cute Digital Clock")

# Define colors
background_color = (255, 223, 186)  # Peach
text_color = (255, 105, 180)  # Pink
shadow_color = (255, 182, 193)  # Light Pink
skyblue = (135,206,235)

# Load a custom font
font = pygame.font.Font(None, 100)  # You can replace `None` with a path to a custom font file
rect = (width//4-100,height//2-100,500,300)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # Render the text
    text = font.render(current_time, True, text_color)
    shadow = font.render(current_time, True, shadow_color)

    # Clear the screen
    screen.fill(background_color)
    pygame.draw.rect(screen,skyblue,rect,border_radius = 15)
    pygame.draw.rect(screen,text_color,rect,5,border_radius = 15)

    # Draw the shadow
    screen.blit(shadow, (width // 4+4,height//2+8))

    # Draw the text
    screen.blit(text, (width//4,height//2))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
