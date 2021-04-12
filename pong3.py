import pygame

pygame.init()

WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Single Player Pong')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)
RADIUS = 25
x = WIDTH//2
y = HEIGHT//2

pygame.draw.circle(screen, WHITE, (x, y), RADIUS)

screen.fill(BLACK)
pygame.display.update()


end = False
while not end:
    screen.fill(BLACK)
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == 1:
        y -= 1
    if key[pygame.K_DOWN] == 1:
        y += 1
    if key[pygame.K_RIGHT] == 1:
        x += 1
    if key[pygame.K_LEFT] == 1:
        x -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            end = True
    pygame.draw.circle(screen, WHITE, (x, y), RADIUS)
    pygame.display.update()
    pygame.time.delay(10)
            

pygame.quit()
