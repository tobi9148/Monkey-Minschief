import pygame #Her importerer vi pygame
import math #Her importerer vi math
pygame.init() #Her initialiserer vi pygame og alle modulerne som nu skulle følge med

screen = pygame.display.set_mode((1280, 720)) #I den her linje laver vi et vindue med størrelsen 800x600
clock = pygame.time.Clock() #Her laver vi er ur hvor vi kan holde øje med vores frames
pygame.display.set_caption("Monkey Mischief") #I den her linje sætter vi titlen på

fps = 120 #Vi laver er variabel som vil bestemme hvor mange frames vores spil skal køre med

a_font = pygame.font.Font("fonts\Grand9K Pixel.ttf", 20) #Her laver vi en font som vi kan bruge til at skrive tekst

player_size = 8*3

def warrior():
    return {"class": "warrior", "color": (255, 0, 0), 
            "rect": (screen.get_width()/2-player_size/2, screen.get_height()/2-player_size/2, player_size, player_size)}

def archer():
    return {"class": "archer", "color": (0, 255, 0), 
            "rect": (screen.get_width()/2-player_size/2, screen.get_height()/2-player_size/2, player_size, player_size)}

def mage():
    return {"class": "mage", "color": (0, 0, 255), 
            "rect": (screen.get_width()/2-player_size/2, screen.get_height()/2-player_size/2, player_size, player_size)}

class scene_template:
    def event_handler(self, event):
        pass
    def update(self):
        pass
    def render(self, screen):
        pass

class button():
    def __init__(self, x, y, width, height, color, text, text_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 5)
        text_surface = a_font.render(self.text, False, (self.text_color))
        screen.blit(text_surface, (self.x + self.width/2 - text_surface.get_width()/2, self.y + self.height/2 - text_surface.get_height()/2))

class tile_b():
    def __init__(self, x, y, tile):
        self.x = x
        self.y = y
        self.width = 8*4
        self.height = 8*4
        self.tile = f"sprites/tiles/{tile}.png"
    
    def draw(self, screen):
        sprite = pygame.image.load(self.tile)
        screen.blit(sprite, (self.x, self.y))   

class menu_scene(scene_template):
    def event_handler(self, events):
        pygame.key.set_repeat(1, 1)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            return lobby_scene()
        return self

    def update(self):
        pass
    
    def render(self, screen):
        screen.fill((0, 0, 0))
        text_surface = a_font.render("Press ENTER to start", False, (255, 255, 255)  )
        screen.blit(text_surface, (screen.get_width()/2-text_surface.get_width()/2, screen.get_height()/2-text_surface.get_height()/2))

class lobby_scene(scene_template):
    def __init__(self):
        self.player = []

    def event_handler(self, events):
        global selected_class
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.mouse.get_pos()[0] > screen.get_width()/2-50-300 and pygame.mouse.get_pos()[0] < screen.get_width()/2-50-300+100 and pygame.mouse.get_pos()[1] > screen.get_height()/2+screen.get_height()/4 and pygame.mouse.get_pos()[1] < screen.get_height()/2+screen.get_height()/4+50:
                        if self.player == []:
                            self.player.append(warrior())
                        else:
                            self.player[0] = warrior()
                        selected_class = self.player[0]
                        print("Selected warrior")
                    elif pygame.mouse.get_pos()[0] > screen.get_width()/2-50 and pygame.mouse.get_pos()[0] < screen.get_width()/2-50+100 and pygame.mouse.get_pos()[1] > screen.get_height()/2+screen.get_height()/4 and pygame.mouse.get_pos()[1] < screen.get_height()/2+screen.get_height()/4+50:
                        if self.player == []:
                            self.player.append(archer())
                        else:
                            self.player[0] = archer()
                        selected_class = self.player[0]
                        print("Selected archer")
                    elif pygame.mouse.get_pos()[0] > screen.get_width()/2-50+300 and pygame.mouse.get_pos()[0] < screen.get_width()/2-50+300+100 and pygame.mouse.get_pos()[1] > screen.get_height()/2+screen.get_height()/4 and pygame.mouse.get_pos()[1] < screen.get_height()/2+screen.get_height()/4+50:
                        if self.player == []:
                            self.player.append(mage())
                        else:
                            self.player[0] = mage()
                        selected_class = self.player[0]
                        print("Selected mage")
                    elif pygame.mouse.get_pos()[0] > screen.get_width()/2-50 and pygame.mouse.get_pos()[0] < screen.get_width()/2-50+100 and pygame.mouse.get_pos()[1] > screen.get_height()/2+screen.get_height()/4+100 and pygame.mouse.get_pos()[1] < screen.get_height()/2+screen.get_height()/4+150:
                        print("Starting game")
                        return level0_scene()

        if pygame.key.get_pressed()[pygame.K_x]:
            return death_scene()
        return self
    

    def update(self):
        screen.fill((0, 0, 0))

        warrior_button = button(screen.get_width()/2-50-300, screen.get_height()/2+screen.get_height()/4, 100, 50, (255, 0, 0), "Warrior", (255, 0, 0)).draw(screen)
        archer_button = button(screen.get_width()/2-50, screen.get_height()/2+screen.get_height()/4, 100, 50, (0, 255, 0), "Archer", (0, 255, 0)).draw(screen)
        mage_button = button(screen.get_width()/2-50+300, screen.get_height()/2+screen.get_height()/4, 100, 50, (0, 0, 255), "Mage", (0, 0, 255)).draw(screen)
        if self.player != []:
            start_button = button(screen.get_width()/2-50, screen.get_height()/2+screen.get_height()/4+100, 100, 50, (255, 255, 255), "Start", (255, 255, 255)).draw(screen)
        
    def render(self, screen):
        for plr in self.player:
            pygame.draw.rect(screen, (plr["color"]), plr["rect"])

        text_surface_fps = a_font.render(f"fps: {pygame.time.Clock.get_fps(clock):.0f}", False, (255, 255, 255))
        screen.blit(text_surface_fps, (0, 630))
        text_surface_mouse_pos = a_font.render(f"mouse pos: {pygame.mouse.get_pos()}", False, (255, 255, 255))
        screen.blit(text_surface_mouse_pos, (0, 660))
        text_surface_resolution = a_font.render(f"resolution: {screen.get_size()}", False, (255, 255, 255))
        screen.blit(text_surface_resolution, (0, 690))

class level0_scene(scene_template):
    def __init__(self):
        self.player = []
        self.player.append(selected_class)
        print(self.player)

    def event_handler(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if pygame.key.get_pressed()[pygame.K_x]:
            return death_scene()
        return self
    
    def update(self):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))

        tile_left = [tile_b(50, 0, "green_brick_l")]

        edge = pygame.draw.rect(screen, (255, 255, 255), (screen.get_width()/2-(720/2), screen.get_height()/2-(480/2), 720, 480), 1)
        side_increments = int(edge.height/24)
        top_bottom_increments = edge.width/24

        for i in range(24):
            print(i+1)

        for tile in tile_left:
            tile.draw(screen)

        for plr in self.player:
            pygame.draw.rect(screen, (plr["color"]), plr["rect"])
        
        text_surface_fps = a_font.render(f"fps: {pygame.time.Clock.get_fps(clock):.0f}", False, (255, 255, 255))
        screen.blit(text_surface_fps, (0, 630))
        text_surface_mouse_pos = a_font.render(f"mouse pos: {pygame.mouse.get_pos()}", False, (255, 255, 255))
        screen.blit(text_surface_mouse_pos, (0, 660))
        text_surface_resolution = a_font.render(f"resolution: {screen.get_size()}", False, (255, 255, 255))
        screen.blit(text_surface_resolution, (0, 690))


class death_scene(scene_template):
    def event_handler(self, events):
        pygame.key.set_repeat(1, 1)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    return menu_scene()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_e:
                    print(selected_class)

    def update(self):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))
        text_surface = a_font.render("Death is inevitable! Press ENTER to restart", False, (255, 0, 0))
        screen.blit(text_surface, (screen.get_width() // 2 - text_surface.get_width() // 2, screen.get_height() // 2))

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