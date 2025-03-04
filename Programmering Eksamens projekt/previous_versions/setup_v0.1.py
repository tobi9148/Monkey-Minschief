import pygame #Her importerer vi pygame
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

screen = pygame.display.set_mode((1280, 720)) #I den her linje laver vi et vindue med størrelsen 800x600
clock = pygame.time.Clock() #Her laver vi er ur hvor vi kan holde øje med vores frames
pygame.display.set_caption("Monkey Mischief") #I den her linje sætter vi titlen på

fps = 60 #Vi laver er variabel som vil bestemme hvor mange frames vores spil skal køre med

a_font = pygame.font.SysFont("Arial", 26, 255) #Her laver vi en font som vi kan bruge til at skrive tekst

def warrior():
    return {"class": "warrior", "color": (255, 0, 0), "rect": (screen.width/2-50, screen.height/2-50, 60, 60)}

def archer():
    return {"class": "archer", "color": (0, 255, 0), "rect": (screen.width/2-50, screen.height/2-50, 60, 60)}

def mage():
    return {"class": "mage", "color": (0, 0, 255), "rect": (screen.width/2-50, screen.height/2-50, 60, 60)}

player = []

running = True
while running:  #Her begynder loopet som kører spillet
    for event in pygame.event.get():    #I denne linje tjekker vi om der er nogle eventssiden sidst vi tjekkede
        if event.type == pygame.QUIT:   #Hvis der er kommet et event og den er af typet QUIT, sætter 
            running = False             #vi running til False som så stopper spillet

    
    
    screen.fill((0, 0, 0)) #Her sætter vi baggrunden til at være hvid

    if pygame.mouse.get_pressed()[0]:
        screen.fill((25, 25, 25)) #Her gør vi baggrunden mørk
    
    if pygame.key.get_pressed()[pygame.K_1]:
        if player == []:
            player.append(warrior())
        else:
            player[0] = warrior()
        print("Selected warrior")
    elif pygame.key.get_pressed()[pygame.K_2]:
        if player == []:
            player.append(archer())
        else:
            player[0] = archer()
        print("Selected archer")
    elif pygame.key.get_pressed()[pygame.K_3]:
        if player == []:
            player.append(mage())
        else:
            player[0] = mage()
        print("Selected mage")
    
    for plr in player:
        pygame.draw.rect(screen, (plr["color"]), plr["rect"])

    text_surface_fps = a_font.render(f"fps: {pygame.time.Clock.get_fps(clock):.0f}", False, (255, 255, 255)  )
    screen.blit(text_surface_fps, (0, 630))
    text_surface_mouse_pos = a_font.render(f"mouse pos: {pygame.mouse.get_pos()}", False, (255, 255, 255)  )
    screen.blit(text_surface_mouse_pos, (0, 660))
    text_surface_resolution = a_font.render(f"resolution: {screen.get_size()}", False, (255, 255, 255)  )
    screen.blit(text_surface_resolution, (0, 690))

    pygame.display.flip() #Her opdaterer vi skærmen
    clock.tick(fps) #Her sætter vi vores frames til 60

    
