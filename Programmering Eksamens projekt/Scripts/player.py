import pygame #Her importerer vi pygame
from config import screen
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

player_size = 8*3
player_speed = 1

class player_class(object):
    def __init__(self, player_class, health, damage, color):
        self.player_class = player_class
        self.health = health
        self.damage = damage
        self.color = color
        self.rect = pygame.rect.Rect(screen.get_width()/2-player_size/2, screen.get_height()/2-player_size/2, player_size, player_size)
        self.speed = player_speed
    
    @classmethod
    def warrior(cls):
        return cls("warrior", 20, 5, (255, 0, 0))

    @classmethod
    def archer(cls):
        return cls("archer", 15, 10, (0, 255, 0))
    
    @classmethod
    def mage(cls):
        return cls("mage", 10, 15, (0, 0, 255))
    
    def player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
    
    def player_draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def heal_player(self, heal):
        self.health += heal
    
    def damage_player(self, damage):
        self.health -= damage

    
    
    

def warrior():
    return {"class": "warrior", 
            "health" : 20,
            "color": (255, 0, 0), 
            "rect": (screen.get_width()/2-player_size/2, screen.get_height()/2-player_size/2, player_size, player_size)}

def archer():
    return {"class": "archer", 
            "health" : 20,
            "color": (0, 255, 0), 
            "rect": (screen.get_width()/2-player_size/2, screen.get_height()/2-player_size/2, player_size, player_size)}

def mage():
    return {"class": "mage", 
            "health" : 20,
            "color": (0, 0, 255), 
            "rect": (screen.get_width()/2-player_size/2, screen.get_height()/2-player_size/2, player_size, player_size)}