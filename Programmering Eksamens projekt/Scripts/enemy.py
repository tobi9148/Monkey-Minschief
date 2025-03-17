import pygame #Her importerer vi pygame
import math
from config import screen, a_font
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

#git config pull.rebase false

enemy_size = 30
enemy_cooldown = 200

class Enemy(object):

    def __init__(self, health, max_health, skills, damage, expget, pos, speed): #Giver enemien forskellige attributtes som den skal have i spillet
        self.health = health
        self.max_health = max_health
        self.skills = skills
        self.damage = damage
        self.expget = expget
        self.pos = pygame.Vector2(pos)
        self.speed = speed
        self.direction = pygame.Vector2(0, 0)
        self.rect = pygame.rect.Rect(screen.get_width()/2-enemy_size/2, screen.get_height()/2-enemy_size, enemy_size * 2, enemy_size * 2)
        self.last_dmg_cooldown = 0
        
    def draw(self, screen): #Tegner hereftter enemien på vinduet (som en cirkel)
        pygame.draw.circle(screen, (255, 0, 0), (int(self.pos.x), int(self.pos.y)), 15)
        health_text = a_font.render(f"{self.health} / {self.max_health}", False, (255, 0, 0))
        screen.blit(health_text, (self.pos.x - health_text.get_width() / 2, self.pos.y+15))

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
            if room_rect.contains(pygame.Rect(new_pos.x, new_pos.y, enemy_size, enemy_size)):
                self.pos = new_pos
            else:
                if enemy_rect.left < room_rect.left:
                    self.rect.left = room_rect.left
                elif enemy_rect.right > room_rect.right:
                    self.rect.right = room_rect.right    
                else:
                    self.rect.x += move_vector.x

                if enemy_rect.top < room_rect.top:
                    self.rect.top = room_rect.top
                elif enemy_rect.bottom > room_rect.bottom:
                    self.rect.bottom = room_rect.bottom
                else:
                    self.rect.y += move_vector.y

        self.check_collision_and_damage(target)
        
    def check_collision_and_damage(self, player):
        # Calculate the distance between the centers of the player and enemy circles
        distance = self.pos.distance_to(player.pos)
        # Check if the distance is less than the sum of their radii
        if distance < 15 + player.rect.width / 2:  # Assuming player.rect.width / 2 is the player's radius
            player.damage_player(self.damage)

    def damage_player(self, damage):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_dmg_cooldown >= enemy_cooldown:
            self.health -= damage
            self.last_dmg_cooldown = current_time