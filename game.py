
import pygame
from sys import exit
from ball import Ball
from player import Player
 
pygame.init()
 
WIDTH = 1100
HEIGHT = 600
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("football")
 
soccer_field_surf = pygame.image.load("./img/soccer-field.jpg")

goal1_surf = pygame.image.load("./img/goal.png").convert_alpha()
goal1_rect = goal1_surf.get_rect(center=(50,275))

goal2_surf = pygame.image.load("./img/goal.png").convert_alpha()
goal2_surf = pygame.transform.flip(goal2_surf,True,False).convert_alpha()
goal2_rect = goal2_surf.get_rect(center=(1050,275))

score = 0
score2 = 0
 
GOAL_WIDTH = 40
GOAL_HEIGHT = 120

clock = pygame.time.Clock()
 
blue = (0,0,255)
red = (255,0,0)
black = (0,0,0)
ball = Ball(WIDTH//2,HEIGHT//2)
 
player_keys1 = {"left":pygame.K_a,"up":pygame.K_w,
                "right":pygame.K_d, "down":pygame.K_s}
 
player_keys2 = {"left":pygame.K_LEFT,"up":pygame.K_UP,
                "right":pygame.K_RIGHT, "down":pygame.K_DOWN}
 
player1 = Player(x=200, y=300, keys=player_keys1, look=1)
player2 = Player(x=300, y=300, keys=player_keys2, look=-1)
 
TACKLE_COOLDOWN_FRAMES = 40  
 
def catch_ball(player, ball):
    if ball.owner is not None:
        return
    if ball.catch_cooldown > 0:
        return
    if player.rect.colliderect(ball.rect):
        ball.owner = player
        ball.velocity = pygame.math.Vector2(0, 0)
        ball.catch_cooldown = TACKLE_COOLDOWN_FRAMES 



font = pygame.font.Font(None, 36)
text_surf_1 = font.render("1-ый Игрок: 0",True,(0,0,0))
text_surf_2 = font.render("2-ый Игрок: 0",True,(0,0,0))
 
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

    if ball.rect.colliderect(goal1_rect):
        score += 1
 
        print(score)
        text_surf_2 = font.render(f"2-ый Игрок:{score}",True,(0,0,0))
        ball.pos = pygame.math.Vector2(WIDTH//2,HEIGHT//2)
        ball.velocity = pygame.math.Vector2(0,0)
        ball.owner = None
 
    if ball.rect.colliderect(goal2_rect):
        score2 += 1
 
        print(score2)
        text_surf_1 = font.render(f"1-ый Игрок: {score2}",True,(0,0,0))
        ball.pos = pygame.math.Vector2(WIDTH//2,HEIGHT//2)
        ball.velocity = pygame.math.Vector2(0,0)
        ball.owner = None
 
    """ ОТРИСОВКА """
    screen.blit(soccer_field_surf,(0,0))

    screen.blit(goal1_surf,goal1_rect)    
    screen.blit(goal2_surf,goal2_rect)
    
    player1.draw(screen=screen, color=blue)
 
    player2.draw(screen=screen, color=red )
 
    screen.blit(text_surf_1,(200,100))
 
    screen.blit(text_surf_2,(400,100))
 
    ball.draw(screen)
 
    pygame.display.update()
    clock.tick(60)