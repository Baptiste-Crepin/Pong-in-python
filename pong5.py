import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Single Player Pong')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

ball = {"RADIUS" : 10,
        "x" : WIDTH//2,
        "color" : WHITE,
        "speed" : 5
        }
ball["y"] = ball["RADIUS"]
ball["x_sens"] = 0
ball["y_sens"] = ball["speed"]

paddle = {"color": BLUE,
            "width" : WIDTH // 4,
            "height" : HEIGHT // 30,
            "speed" : 5
            }
paddle["x"] = WIDTH//2 - paddle["width"]//2
paddle["y"] = HEIGHT - paddle["height"]

pause = game_over = False
delay = 10

end = False
while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
            
    screen.fill(BLACK)
    key = pygame.key.get_pressed()

    if pause == False and game_over == False:
        if key[pygame.K_SPACE]:
            pause = True
        if key[pygame.K_RIGHT] and paddle["x"] + paddle["width"] < WIDTH:
            paddle["x"] += paddle["speed"]
        if key[pygame.K_LEFT] and paddle["x"] > 0:
            paddle["x"] -= paddle["speed"]
        if (ball["x"] + ball["RADIUS"] > WIDTH or
         ball["x"] - ball["RADIUS"] < 0):
            ball["x_sens"] = -ball["x_sens"]
        if ball["y"] - ball["RADIUS"] < paddle["y"]:
            if ((ball["y"] + ball["RADIUS"] > paddle["y"] and
             (ball["x"] > paddle["x"] and
             ball["x"] < paddle["x"] + paddle["width"])) or
             ball["y"] - ball["RADIUS"] < 0):
                ball["y_sens"] = - ball["y_sens"]
            if ball["y"] + ball["RADIUS"] == HEIGHT - ball["RADIUS"]:
                game_over = True
                print("GAME OVER")
            ball["x"] += ball["x_sens"]
            ball["y"] += ball["y_sens"]
    if key[pygame.K_RETURN]:
        pause = False
    
    
    if key[pygame.K_ESCAPE]:
        end = True
    
    pygame.draw.rect(screen,
                    paddle["color"],
                    ((paddle["x"],
                    paddle["y"]),
                    (paddle["width"],
                    paddle["height"]))
                    )
    pygame.draw.circle(screen,
                        ball["color"],
                        (ball["x"],
                        ball["y"]),
                        ball["RADIUS"]
                        )
    pygame.display.update()
    pygame.time.delay(delay)

pygame.quit()
