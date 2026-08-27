import pygame
class Ball:
    def __init__(self, x, y):
        self.pos = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0) 
        self.surf = pygame.image.load("./img/ball.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf,(285//8,272//8))
        self.rect = self.surf.get_rect(center=(x,y))
        self.owner = None
        self.friction = 0.98
        self.catch_cooldown = 0

    def update(self):
        if self.owner is None:
            self.pos += self.velocity
            self.velocity *= self.friction
            if self.velocity.length() < 0.1:
                self.velocity = pygame.math.Vector2(0, 0)
        else:
            offset = self.owner.facing * 30
            self.pos = pygame.math.Vector2(self.owner.rect.center) + offset
        if self.catch_cooldown > 0:
            self.catch_cooldown -= 1

        self.rect.center=(self.pos.x,self.pos.y)

        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.velocity *= -0.7

        if self.rect.right >= 800 or self.rect.left <= 0:
            self.velocity *= -0.7


    def kick_ball(self,player, power=12):
        if self.owner is player:
            self.owner = None
            self.velocity = player.facing * power
            self.catch_cooldown = 15

    def draw(self,screen):
        screen.blit(self.surf,self.rect)