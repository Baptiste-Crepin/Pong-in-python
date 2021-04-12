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

ball = {"RADIUS": 10,
        "x": WIDTH//2,
        "color": WHITE,
        "starting_speed": 3
        }
ball["y"] = ball["RADIUS"]
ball["x_sens"] = ball["y_sens"] = ball["starting_speed"]

paddle = {"color": BLUE,
          "width": WIDTH // 4,
          "height": HEIGHT // 30,
          "speed": 5
          }
paddle["x"] = WIDTH//2 - paddle["width"]//2
paddle["y"] = HEIGHT - paddle["height"]


myfont = pygame.font.SysFont('monospace', 50)

print("pong6")
screen.fill(BLACK)

title = myfont.render("Single Player Pong :", False, GREEN)
for i in range(3, -1, -1):
    countdown = myfont.render(str(i), False, GREEN)
    screen.blit(title,
                (WIDTH//2-title.get_width()//2,
                 HEIGHT//2-title.get_height()*2)
                )
    screen.blit(countdown, (WIDTH//2, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(1000)
    screen.fill(BLACK)

while True:
    try:
        fichier = open('highest_score.txt')
        break
    except FileNotFoundError:
        fichier = open('highest_score.txt',"w")
        fichier.write(str(0))

high_score = fichier.readline()
fichier.close()
high_score = high_score.rstrip()
high_score_txt = myfont.render(str(high_score), False, GREEN)
screen.blit(high_score_txt, (WIDTH-high_score_txt.get_width(), 0))
pygame.display.update()

pause = game_over = False
delay = 10
score = 0

end = False
while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    screen.fill(BLACK)
    key = pygame.key.get_pressed()

    if not pause and not game_over:
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
            if ((ball["y"] + ball["RADIUS"] > paddle["y"] and
                (ball["x"] > paddle["x"] and
                 ball["x"] < paddle["x"] + paddle["width"]))):
                score += 1
                if score % 10 == 0:
                    if paddle["width"] > 40:
                        paddle["width"] -= 20
                        paddle["x"] += 10
                elif score % 5 == 0:
                    if ball["y_sens"] > -10:
                        ball["y_sens"] -= 1
            if ball["y"] + ball["RADIUS"] > HEIGHT - ball["RADIUS"]:
                game_over = True
                pygame.display.update()
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

    score_txt = myfont.render(str(score), False, GREEN)
    screen.blit(score_txt, (10, 0))
    screen.blit(high_score_txt, (WIDTH-high_score_txt.get_width(), 0))

    pygame.time.delay(delay)
    pygame.display.update()

    if game_over:
        game_over_txt = myfont.render("GAME OVER", False, GREEN)
        replay_txt = myfont.render("Press 'R' to Retry", False, GREEN)
        quit_txt = myfont.render("Press 'esc' to Quit", False, GREEN)
        screen.blit(game_over_txt,
                    (WIDTH//2-game_over_txt.get_width()//2,
                     HEIGHT//2-game_over_txt.get_height()*4)
                    )
        screen.blit(replay_txt,
                    (WIDTH//2-replay_txt.get_width()//2,
                     HEIGHT//2-replay_txt.get_height())
                    )
        screen.blit(quit_txt,
                    (WIDTH//2-quit_txt.get_width()//2,
                     HEIGHT//2-quit_txt.get_height()*-1)
                    )
        pygame.display.update()
        pygame.time.delay(delay + 50)
        
        if score > int(high_score):
            fichier = open('highest_score.txt', "w")
            high_score = score
            fichier.write(str(high_score))
        if key[pygame.K_r]:
            ball["y"] = ball["RADIUS"]
            ball["x"] = WIDTH//2
            ball["x_sens"] = ball["y_sens"] = ball["starting_speed"]
            paddle["x"] = WIDTH//2 - paddle["width"]//2
            paddle["width"] = WIDTH // 4
            high_score_txt = myfont.render(str(high_score), False, GREEN)
            score = 0
            game_over = False


pygame.quit()
