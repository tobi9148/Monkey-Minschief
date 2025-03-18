import pygame #Her importerer vi pygame
import math #Her importerer vi math
from config import screen, a_font #her importerer vi screen og a_font fra config.py
pygame.init() 

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
        self.rect = pygame.rect.Rect(screen.get_width()/2-enemy_size/2, screen.get_height()/2-enemy_size, enemy_size * 2, enemy_size * 2) #Her laver vi en rektangel som vi bruger til at tjekke om enemien er i rummet
        self.last_dmg_cooldown = 0
        
    def draw(self, screen): #Tegner hereftter enemien på vinduet (som en cirkel)
        pygame.draw.circle(screen, (255, 0, 0), (int(self.pos.x), int(self.pos.y)), 15)
        health_text = a_font.render(f"{self.health} / {self.max_health}", False, (255, 0, 0))
        screen.blit(health_text, (self.pos.x - health_text.get_width() / 2, self.pos.y+15))

    def enemy_movement(self, target, room_rect): #Her laver vi en funktion som gør at enemien bevæger 
        #udregner en vektor som peger mod playeren
        direction_vector = target.pos - self.pos
        length = direction_vector.length()
        if length > 0:
            direction_vector.x /= length
            direction_vector.y /= length

        # Bevæger enemien mod playeren med en konstant hastighed1
        move_vector = direction_vector * self.speed 
        new_pos = self.pos + move_vector

        enemy_rect = self.rect.move(move_vector.x, move_vector.y)
        #sikre at enemien forbliver inden for rummet
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
        # calculere afstanden mellem player center og enemy cirklen
        distance = self.pos.distance_to(player.pos)
        #tjekker om afstanden er mindre end summen af deres radian
        if distance < 15 + player.rect.width / 2: #Der antages at player.rect.width / 2 er playerens radius
            player.damage_player(self.damage)  # Hvis de overlapper, tager vi skade

    def damage_player(self, damage):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_dmg_cooldown >= enemy_cooldown:
            self.health -= damage
            self.last_dmg_cooldown = current_time

    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True #Hvis enemien har 0 eller mindre liv, ville det betyde at den er død
        return False #hvis enemien dør, bliver den fjernet fra listen over enemier i spillet