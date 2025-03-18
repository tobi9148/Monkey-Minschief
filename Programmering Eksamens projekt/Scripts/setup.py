import pygame #Her importerer vi pygame
from config import screen, clock #Her importerer vi vores screen og clock
from scenes import menu_scene, lobby_scene, level0_scene #Her importerer vi alle vores scener
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

pygame.display.set_caption("Monkey Mischief") #I den her linje sætter vi titlen på

fps = 120 #Vi laver er variabel som vil bestemme hvor mange frames vores spil skal køre med


pygame.mixer.init()

pygame.mixer.music.set_volume(0.4)  # 0.0 to 1.0
pygame.mixer.music.load("Programmering Eksamens projekt\music\doom_Music.mp3")  # Replace with the path to your music file
pygame.mixer.music.play(-1)  # -1 means that the music will loop indefinitely

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