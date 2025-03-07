import pygame #Her importerer vi pygame
import math #Her importerer vi math
import setup
from setup import screen
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

player_size = 8*3
player_speed = 0.5

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