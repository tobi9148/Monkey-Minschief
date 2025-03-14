import pygame #Her importerer vi pygame
import math
from config import screen
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

#git config pull.rebase false

enemy_size = 8.3

class Enemy(object):

    def __init__(self, health, skills, attack, expget, pos, speed): #Giver enemien forskellige attributtes som den skal have i spillet
        self.health = health
        self.skills = skills
        self.attack = attack
        self.expget = expget
        self.pos = pygame.Vector2(pos)
        self.speed = speed
        self.direction = pygame.Vector2(0, 0)
        self.rect = pygame.rect.Rect(screen.get_width()/2-enemy_size/2, screen.get_height()/2-enemy_size, enemy_size * 2, enemy_size * 2)

    def draw(self, screen): #Tegner hereftter enemien på vinduet (som en cirkel)
        pygame.draw.circle(screen, (255, 0, 0), (int(self.pos.x), int(self.pos.y)), 8*3)

    def enemy_movement(self, target, room_rect):
        # Calculate the direction vector towards the target (player)
        direction_vector = target.pos - self.pos
        length = direction_vector.length()
        if length > 0:
            direction_vector.x /= length
            direction_vector.y /= length

        # Move the enemy towards the target at a constant speed
        move_vector = direction_vector * self.speed
        new_pos = self.pos + move_vector

        enemy_rect = self.rect.move(move_vector.x, move_vector.y)
        # Ensure the enemy stays within the room_rect
        if room_rect != None:
            if room_rect.contains(pygame.Rect(new_pos.x, new_pos.y, 8*3, 8*3)):
                self.pos = new_pos
            else:
                self.rect.x += move_vector.x

            if enemy_rect.top < room_rect.top:
                self.rect.top = room_rect.top
            elif enemy_rect.bottom > room_rect.bottom:
                self.rect.bottom = room_rect.bottom
            else:
                self.rect.y += move_vector.y

def draw(screen, enemy):
    pygame.draw.circle(screen, (255, 0, 0), (int(enemy.pos.x), int(enemy.pos.y)), enemy_size)