import pygame #Her importerer vi pygame
import math
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

#git config pull.rebase false


class Enemy(object):

    def __init__(self, health, skills, attack, expget):
        self.health = health
        self.skills = skills
        self.attack = attack
        self.expget = expget

class EnemyController:

    def __init__(self, target):
        self.direction = pygame.math.Vector2(1, 0)
        self.target = target

    def update(self, sprite, events, dt):
        k = self.target.vel.magnitude() / sprite.speed

        distance_to_target = (sprite.pos - self.target.pos).magnitude()

        b_hat = self.target.vel
        c_hat = sprite.pos - self.target.pos

        CAB = b_hat.angle_to(c_hat)
        ABC = math.asin(math.sin(CAB) * k)
        ACB = math.pi - (CAB + ABC)

        j = distance_to_target / math.sin(ACB)
        a = j * math.sin(CAB)
        b = j * math.sin(ABC)

        time_to_collision = b / self.target.vel.magnitude() if self.target.vel.magnitude() > 0 else 1
        collision_pos = self.target.pos + (self.target.vel * time_to_collision)

        v = sprite.pos - collision_pos
        if v.length() > 0:
            sprite.direction = -v.normalize()

        if v.length() <= 10:
            sprite.pos = pygame.Vector2(400, 100)
    




import pygame #Her importerer vi pygame
import math
import random
from config import screen
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

#git config pull.rebase false

enemy_size = 8*3
enemy_cooldown = 500
enemy_speed = 0.9

class Enemy(object):

    def __init__(self, enemy_type, damage, max_health, health, color, edge_rect):
        self.enemy_type = enemy_type
        self.damage = damage
        self.max_health = max_health
        self.health = health
        self.color = color

        self.target = None

        exclusion_zone_size = 200
        exclusion_zone_x = edge_rect.left + (edge_rect.width - exclusion_zone_size) // 2
        exclusion_zone_y = edge_rect.top + (edge_rect.height - exclusion_zone_size) // 2

        while True:
            x = random.randint(edge_rect.left, edge_rect.right - enemy_size)
            y = random.randint(edge_rect.top, edge_rect.bottom - enemy_size)
            if not (exclusion_zone_x <= x <= exclusion_zone_x + exclusion_zone_size and exclusion_zone_y <= y <= exclusion_zone_y + exclusion_zone_size):
                break
        
        self.rect = pygame.Rect(x, y, enemy_size, enemy_size)
    
    @classmethod
    def slime(cls, edge_rect):
        return cls("Slime", 5, 10, 10, (166, 206, 74), edge_rect)
    
    def enemy_draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def enemy_move(self, room_rect, player_rect):
        to_player = pygame.math.Vector2(player_rect.x-self.rect.x, player_rect.y-self.rect.y)
        to_player.scale_to_length(enemy_speed)
        enemy_rect = self.rect.move(to_player)

        if room_rect.contains(enemy_rect):
            self.rect = enemy_rect
        else:
            if enemy_rect.left < room_rect.left:
                self.rect.left = room_rect.left
            elif enemy_rect.right > room_rect.right:
                self.rect.right = room_rect.right
            else:
                self.rect.x += self.total_velocity.x

            if enemy_rect.top < room_rect.top:
                self.rect.top = room_rect.top
            elif enemy_rect.bottom > room_rect.bottom:
                self.rect.bottom = room_rect.bottom
            else:
                self.rect.y += self.total_velocity.y



        self.enemies = []


def update(self):
        for emy in self.enemies:
            emy.enemy_move(self.edge_rect, self.player[0].rect)

        if len(self.enemies) < 5:
            for _ in range(5):
                self.enemies.append(enemy.Enemy.slime(self.edge_rect))


        for emy in self.enemies:
            emy.enemy_move(self.edge_rect, self.player[0].rect)
            emy.enemy_draw()
            print(emy.rect)