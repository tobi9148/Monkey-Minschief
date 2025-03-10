import pygame #Her importerer vi pygame
import math
from config import screen
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

player_size = 8*3
player_speed = 2
player_cooldown = 500

class player_class(object):
    def __init__(self, player_class, max_health, health, damage, color):
        self.player_class = player_class
        self.max_health = max_health
        self.health = health
        self.damage = damage
        self.color = color
        self.rect = pygame.rect.Rect(screen.get_width()/2-player_size/2, screen.get_height()/2-player_size/2, player_size, player_size)
        self.speed = player_speed
        self.last_dmg_cooldown = 0
    
    @classmethod
    def warrior(cls):
        return cls("warrior", 20, 20, 5, (255, 0, 0))

    @classmethod
    def archer(cls):
        return cls("archer", 15, 15, 10, (0, 255, 0))
    
    @classmethod
    def mage(cls):
        return cls("mage", 10, 10, 15, (0, 0, 255))
    
    def player_movement(self, room_rect):
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
        
        player_rect = self.rect.move(self.total_velocity.x, self.total_velocity.y)

        if room_rect.contains(player_rect):
            self.rect = player_rect
        else:
            if player_rect.left < room_rect.left:
                self.rect.left = room_rect.left
            elif player_rect.right > room_rect.right:
                self.rect.right = room_rect.right
            else:
                self.rect.x += self.total_velocity.x

            if player_rect.top < room_rect.top:
                self.rect.top = room_rect.top
            elif player_rect.bottom > room_rect.bottom:
                self.rect.bottom = room_rect.bottom
            else:
                self.rect.y += self.total_velocity.y
    
    def player_draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def get_size(self):
        return self.rect.size
    
    def heal_player(self, heal):
        self.health += heal
    
    def damage_player(self, damage):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_dmg_cooldown >= player_cooldown:
            self.health -= damage
            self.last_dmg_cooldown = current_time
    
    def update_dmg_cooldown(self):
        if self.dmg_cooldown > 0:
            self.dmg_cooldown -= 1
            print(self.dmg_cooldown)
    
    def reset_position(self):
        self.rect = pygame.rect.Rect(screen.get_width() / 2 - player_size / 2, screen.get_height() / 2 - player_size / 2, player_size, player_size)