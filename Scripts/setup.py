import pygame #Her importerer vi pygame
from scenes import menu_scene
from scenes import lobby_scene
from scenes import level0_scene
from scenes import level1_scene
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

screen = pygame.display.set_mode((1280, 720)) #I den her linje laver vi et vindue med størrelsen 800x600
clock = pygame.time.Clock() #Her laver vi er ur hvor vi kan holde øje med vores frames
pygame.display.set_caption("Monkey Mischief") #I den her linje sætter vi titlen på

fps = 120 #Vi laver er variabel som vil bestemme hvor mange frames vores spil skal køre med


def main():
    current_scene = menu_scene()
    running = True
    while running:
        events = pygame.event.get()
        next_scene = current_scene.event_handler(events)
        if next_scene is not None:
            current_scene = next_scene
        current_scene.update()
        current_scene.render(screen)
        pygame.display.flip() #Her opdaterer vi skærmen
        clock.tick(fps) #Her sætter vi vores frames til 60

if __name__ == "__main__":
    main()