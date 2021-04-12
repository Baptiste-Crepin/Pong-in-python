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

delay = 10
ball_color = WHITE
speed = 5
automatic = False
x_sens = y_sens = speed

pygame.draw.circle(screen, ball_color, (x, y), RADIUS)

screen.fill(BLACK)
pygame.display.update()


end = False
while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
            
    screen.fill(BLACK)
    key = pygame.key.get_pressed()
    if key[pygame.K_m] == 1:
        automatic = False
    if key[pygame.K_o] == 1:
        automatic = True
    if automatic == False:
        if key[pygame.K_UP] and y - RADIUS > 0:
            y -= speed
        if key[pygame.K_DOWN] and y + RADIUS < HEIGHT:
            y += speed
        if key[pygame.K_RIGHT] and x + RADIUS < WIDTH:
            x += speed
        if key[pygame.K_LEFT] and x - RADIUS > 0:
            x -= speed
    if automatic == True:
        if x + RADIUS > WIDTH or x - RADIUS < 0:
            x_sens = - x_sens
        if y + RADIUS > HEIGHT or y - RADIUS < 0:
            y_sens = - y_sens
        x = x + x_sens
        y = y + y_sens
    
    if key[pygame.K_ESCAPE] == 1:
        end = True
    
    pygame.draw.circle(screen, ball_color, (x, y), RADIUS)
    pygame.display.update()
    pygame.time.delay(delay)
            

pygame.quit()
