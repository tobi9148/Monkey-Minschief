import pygame #Her importerer vi pygame
import math
from config import screen
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

player_size = 8*3
player_speed = 2

class player_class(object):
    def __init__(self, player_class, max_health, health, damage, color):
        self.player_class = player_class
        self.max_health = max_health
        self.health = health
        self.damage = damage
        self.color = color
        self.rect = pygame.rect.Rect(screen.get_width()/2-player_size/2, screen.get_height()/2-player_size/2, player_size, player_size)
        self.speed = player_speed
    
    @classmethod
    def warrior(cls):
        return cls("warrior", 20, 20, 5, (255, 0, 0))

    @classmethod
    def archer(cls):
        return cls("archer", 15, 15, 10, (0, 255, 0))
    
    @classmethod
    def mage(cls):
        return cls("mage", 10, 10, 15, (0, 0, 255))
    
    def player_movement(self):
        self.velocity_x = 0
        self.velocity_y = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.velocity_y = -self.speed
        if keys[pygame.K_s]:
            self.velocity_y = self.speed
        if keys[pygame.K_a]:
            self.velocity_x = -self.speed
        if keys[pygame.K_d]:
            self.velocity_x = self.speed
    
        self.total_velocity = pygame.math.Vector2(self.velocity_x, self.velocity_y)
        if self.total_velocity.length() > 0:
            self.total_velocity.x = self.velocity_x / player_speed * 2
            self.total_velocity.y = self.velocity_y / player_speed * 2
        
        self.rect.move_ip(self.total_velocity.x, self.total_velocity.y)
    
    def player_draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def heal_player(self, heal):
        self.health += heal
    
    def damage_player(self, damage):
        self.health -= damage
    
    def reset_position(self):
        self.rect = pygame.rect.Rect(screen.get_width() / 2 - player_size / 2, screen.get_height() / 2 - player_size / 2, player_size, player_size)