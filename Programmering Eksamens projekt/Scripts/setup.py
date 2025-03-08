import pygame #Her importerer vi pygame
from config import screen, clock #Her importerer vi vores screen og clockd
from scenes import menu_scene, lobby_scene, level0_scene, level1_scene #Her importerer vi alle vores scener
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

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