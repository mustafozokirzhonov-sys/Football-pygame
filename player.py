import pygame
class Player:
    def __init__(self, x, y, keys, look):
        self.speed =3
        self.rect = pygame.Rect(x,y,40,60)
        self.keys = keys

        self.facing = pygame.math.Vector2(look,0)

    def move(self, keys_pressed):
        direction = pygame.math.Vector2(0, 0)
        if keys_pressed[self.keys["right"]]:
            direction.x += 1
        if keys_pressed[self.keys["left"]]:
            direction.x -= 1
        if keys_pressed[self.keys["up"]]:
            direction.y -= 1
        if keys_pressed[self.keys["down"]]:
            direction.y += 1
 
        if direction.length() > 0:
            direction = direction.normalize()
            self.facing = direction   # <-- запоминаем направление
 
        self.rect.x += direction.x * self.speed
        self.rect.y += direction.y * self.speed
    
    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)       