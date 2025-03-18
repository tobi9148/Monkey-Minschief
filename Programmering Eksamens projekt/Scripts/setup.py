import pygame #Her importerer vi pygame
from config import a_font, screen, clock #Her importerer vi vores screen og clock
from scenes import menu_scene, lobby_scene, level0_scene #Her importerer vi alle vores scener
import math
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

pygame.display.set_caption("Monkey Mischief") #I den her linje sætter vi titlen på

fps = 120 #Vi laver er variabel som vil bestemme hvor mange frames vores spil skal køre med
volume = 0.4


pygame.mixer.init()

pygame.mixer.music.set_volume(volume)  # 0.0 to 1.0
pygame.mixer.music.load("Programmering Eksamens projekt\music\doom_Music.mp3")  # Replace with the path to your music file
pygame.mixer.music.play(-1)  # -1 means that the music will loop indefinitely

def main():
    global volume
    current_scene = menu_scene()
    running = True
    show_text = False
    hide_text_time = 0
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    if volume < 1:
                        volume = round(volume + 0.1, 1)
                        pygame.mixer.music.set_volume(volume)
                        show_text = True
                        hide_text_time = pygame.time.get_ticks() + 1000
                if event.key == pygame.K_2:
                    if volume > 0:
                        volume = round(volume - 0.1, 1)
                        pygame.mixer.music.set_volume(volume)
                        show_text = True
                        hide_text_time = pygame.time.get_ticks() + 1000
        next_scene = current_scene.event_handler(events)
        if next_scene is not None:
            current_scene = next_scene
        current_scene.update()
        current_scene.render(screen)

        if show_text and pygame.time.get_ticks() < hide_text_time:
            text_surface = a_font.render(f"Volume: {volume * 100:.0f}", True, (255, 255, 255))
            print(volume)
            screen.blit(text_surface, (screen.get_width() // 2 - text_surface.get_width() // 2, screen.get_height() // 2 + 150))
        else:
            show_text = False

        pygame.display.flip() #Her opdaterer vi skærmen
        clock.tick(fps) #Her sætter vi vores frames til 60

if __name__ == "__main__":
    main()