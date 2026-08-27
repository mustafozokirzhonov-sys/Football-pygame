import pygame
from sys import exit
from ball import Ball
from player import Player

pygame.init()
 
WIDTH = 800
HEIGHT = 600
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("football")
 
stadium_surf = pygame.image.load("./img/soccer-field.jpg")

    
clock = pygame.time.Clock()

blue = (0,0,255)
red = (255,0,0)

ball = Ball(WIDTH//2,HEIGHT//2)

player_keys1 = {"left":pygame.K_a,"up":pygame.K_w,
                "right":pygame.K_d, "down":pygame.K_s}

player_keys2 = {"left":pygame.K_LEFT,"up":pygame.K_UP,
                "right":pygame.K_RIGHT, "down":pygame.K_DOWN}

player1 = Player(x=200, y=300, keys=player_keys1, look=1)
player2 = Player(x=300, y=300, keys=player_keys2, look=-1)

def catch_ball(player, ball):
    if ball.owner is player:
        return
    if ball.catch_cooldown > 0:
        return
    if player.rect.colliderect(ball.rect):
        ball.owner = player
        ball.velocity = pygame.math.Vector2(0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball.kick_ball(player1)

            if event.key == pygame.K_RETURN:
                ball.kick_ball(player2)

    key_pressed = pygame.key.get_pressed()
    player1.move(key_pressed)
    player2.move(key_pressed)
    ball.update()
    catch_ball(player1, ball)
    catch_ball(player2, ball)
 

    """ ОТРИСОВКА """
    screen.blit(stadium_surf,(0,0))


    player1.draw(screen=screen, color=blue)
    player2.draw(screen=screen, color=red )

    ball.draw(screen)

    pygame.display.update()
    clock.tick(60)