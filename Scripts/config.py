import pygame #Her importerer vi pygame
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

screen = pygame.display.set_mode((1280, 720)) #I den her linje laver vi et vindue med størrelsen 800x600
clock = pygame.time.Clock() #Her laver vi er ur hvor vi kan holde øje med vores frames
pygame.display.set_caption("Monkey Mischief") #I den her linje sætter vi titlen på

fps = 120 #Vi laver er variabel som vil bestemme hvor mange frames vores spil skal køre med

a_font = pygame.font.Font("Programmering Eksamens projekt/fonts/Grand9K Pixel.ttf", 20) #Her laver vi en font som vi kan bruge til at skrive tekst
