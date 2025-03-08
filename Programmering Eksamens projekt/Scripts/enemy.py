import pygame #Her importerer vi pygame
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med


class Enemy(object):

    def __init__(self, HP, skills, attack, expget):
        self.HP = HP
        self.skills = skills
        self.attack = attack
        self.expget = expget
    def move(self):
        pass