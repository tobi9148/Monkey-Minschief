import pygame #Her importerer vi pygame
import math
from config import screen
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

#git config pull.rebase false

enemy_size = 8*3

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

        enemy_radius = enemy_size / 2
        enemy_rect = self.rect.move(move_vector.x, move_vector.y)
        # Ensure the enemy stays within the room_rect
        if room_rect != None:
            if room_rect.contains(pygame.Rect(new_pos.x - enemy_radius, new_pos.y - enemy_radius, enemy_size, enemy_size)):
                self.pos = new_pos
            else:
                if enemy_rect.left < room_rect.left:
                    self.pos.x = room_rect.left + enemy_radius
                elif enemy_rect.right > room_rect.right:
                    self.pos.x = room_rect.right - enemy_radius
                else:
                    self.pos.x += move_vector.x

                if enemy_rect.top < room_rect.top:
                    self.pos.y = room_rect.top + enemy_radius
                elif enemy_rect.bottom > room_rect.bottom:
                    self.pos.y = room_rect.bottom - enemy_radius
                else:
                    self.pos.y += move_vector.y

def draw(screen, enemy):
    pygame.draw.circle(screen, (255, 0, 0), (int(enemy.pos.x), int(enemy.pos.y)), enemy_size)