import pygame
import player
from config import a_font, screen, clock
war = player.player_class.warrior()
arc = player.player_class.archer()
mag = player.player_class.mage()
pygame.init()

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
        self.tile = f"Programmering Eksamens projekt/sprites/tiles/{tile}.png"
    
    def draw(self, screen):
        sprite = pygame.image.load(self.tile)
        screen.blit(sprite, (self.x, self.y))   

class menu_scene(scene_template):
    def event_handler(self, events):
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
                            self.player.append(war)
                        else:
                            self.player[0] = war
                        selected_class = self.player[0]
                        print("Selected warrior")
                        print(self.player[0].player_class)
                    elif pygame.mouse.get_pos()[0] > screen.get_width()/2-50 and pygame.mouse.get_pos()[0] < screen.get_width()/2-50+100 and pygame.mouse.get_pos()[1] > screen.get_height()/2+screen.get_height()/4 and pygame.mouse.get_pos()[1] < screen.get_height()/2+screen.get_height()/4+50:
                        if self.player == []:
                            self.player.append(arc)
                        else:
                            self.player[0] = arc
                        selected_class = self.player[0]
                        print("Selected archer")
                        print(self.player[0].player_class)
                    elif pygame.mouse.get_pos()[0] > screen.get_width()/2-50+300 and pygame.mouse.get_pos()[0] < screen.get_width()/2-50+300+100 and pygame.mouse.get_pos()[1] > screen.get_height()/2+screen.get_height()/4 and pygame.mouse.get_pos()[1] < screen.get_height()/2+screen.get_height()/4+50:
                        if self.player == []:
                            self.player.append(mag)
                        else:
                            self.player[0] = mag
                        selected_class = self.player[0]
                        print("Selected mage")
                        print(self.player[0].player_class)
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
            plr.player_draw()

        text_surface_fps = a_font.render(f"fps: {clock.get_fps():.0f}", False, (255, 255, 255))
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
        self.edge = None

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

        for tile in tile_left:
            tile.draw(screen)

        for plr in self.player:
            plr.player_draw()
            plr.player_movement()
        
        text_surface_fps = a_font.render(f"fps: {clock.get_fps():.0f}", False, (255, 255, 255))
        screen.blit(text_surface_fps, (0, 600))
        text_surface_fps = a_font.render(f"pos: ({plr.rect.x}, {plr.rect.y})", False, (255, 255, 255))
        screen.blit(text_surface_fps, (0, 630))
        text_surface_mouse_pos = a_font.render(f"mouse pos: {pygame.mouse.get_pos()}", False, (255, 255, 255))
        screen.blit(text_surface_mouse_pos, (0, 660))
        text_surface_resolution = a_font.render(f"resolution: {screen.get_size()}", False, (255, 255, 255))
        screen.blit(text_surface_resolution, (0, 690))

class level1_scene(scene_template):
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

        for tile in tile_left:
            tile.draw(screen)

        for plr in self.player: #Her tegnes playeren på banen
            pygame.draw.rect(screen, (plr["color"]), plr["rect"])
        
        text_surface_fps = a_font.render(f"fps: {clock.get_fps():.0f}", False, (255, 255, 255))
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

    def update(self):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))
        text_surface = a_font.render("Death is inevitable! Press ENTER to restart", False, (255, 0, 0))
        screen.blit(text_surface, (screen.get_width() // 2 - text_surface.get_width() // 2, screen.get_height() // 2))
