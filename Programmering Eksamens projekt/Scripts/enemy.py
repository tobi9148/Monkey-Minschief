import pygame #Her importerer vi pygame
import math
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

#git config pull.rebase false


class Enemy(object):

    def __init__(self, HP, skills, attack, expget):
        self.HP = HP
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
    