import pygame
import random
import player
import enemy
from config import a_font, screen, clock

selected_class = None

war = player.player_class.warrior()
arc = player.player_class.archer()
mag = player.player_class.mage()
pygame.init()

death_messages = [
    "Death is inevitable!",
    "You play like an infant...",
    "HE NEED SOME MILK!",
    "My dead grandma could've done better!",
    "Have you tried actually playing the game?",
    "Death is temporary. Victory is permanent!",
    "Tis but a scratch!",
    "I had bigger plans for you...",
    "Try not to do that again next time...",
    "Yikes...",
    "Unlock God Mode for $49.99.",
    "Skill issue?",
    "I swear it didn't hit me!",
    "WTF?!",
    "Horrible hitboxes!",
    "Devs fix the game please...",
    "I guess you weren't ready to rumble..."
]

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

class room_size():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = None
    
    def draw(self):
        self.rect = pygame.draw.rect(screen, (255, 255, 255), (screen.get_width()/2-(self.x/2), screen.get_height()/2-(self.y/2), self.x, self.y), 1)

    def get_rect(self):
        return self.rect

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
                            self.player[0].reset_position()
                        selected_class = self.player[0]
                        print("Selected warrior")
                        print(self.player[0].player_class)
                    elif pygame.mouse.get_pos()[0] > screen.get_width()/2-50 and pygame.mouse.get_pos()[0] < screen.get_width()/2-50+100 and pygame.mouse.get_pos()[1] > screen.get_height()/2+screen.get_height()/4 and pygame.mouse.get_pos()[1] < screen.get_height()/2+screen.get_height()/4+50:
                        if self.player == []:
                            self.player.append(arc)
                        else:
                            self.player[0] = arc
                            self.player[0].reset_position()
                        selected_class = self.player[0]
                        print("Selected archer")
                        print(self.player[0].player_class)
                    elif pygame.mouse.get_pos()[0] > screen.get_width()/2-50+300 and pygame.mouse.get_pos()[0] < screen.get_width()/2-50+300+100 and pygame.mouse.get_pos()[1] > screen.get_height()/2+screen.get_height()/4 and pygame.mouse.get_pos()[1] < screen.get_height()/2+screen.get_height()/4+50:
                        if self.player == []:
                            self.player.append(mag)
                        else:
                            self.player[0] = mag
                            self.player[0].reset_position()
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
        
        if self.player != []:
                text_surface_damage_display = button(screen.get_width()/2-70-100, screen.get_height()/2+50, 140, 50, (255, 255, 255), f"Damage: {self.player[0].damage}", (255, 255, 255)).draw(screen)
                text_surface_health_display = button(screen.get_width()/2-70+100, screen.get_height()/2+50, 140, 50, (255, 255, 255), f"Health: {self.player[0].health}", (255, 255, 255)).draw(screen)
        
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
        self.edge = room_size(720, 480)
        self.edge_rect = self.edge.get_rect()

        self.enemies = [enemy.Enemy(100, [], 10, 50, (400, 400), 1)]

    def event_handler(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    self.player[0].damage_player(5)
                    print({self.player[0].health})
        if self.player[0].health <= 0:
            return death_scene()
        if pygame.key.get_pressed()[pygame.K_x]:
            return death_scene()
        return self
    
    def update(self):
        for emy in self.enemies:
            emy.enemy_movement(self.player[0], self.edge_rect)

    def render(self, screen):
        screen.fill((0, 0, 0))

        tile_left = [tile_b(50, 0, "green_brick_l")]

        self.edge.draw()
        self.edge_rect = self.edge.get_rect()

        for tile in tile_left:
            tile.draw(screen)

        for plr in self.player:
            plr.player_draw()
            player_width, player_height = plr.get_size()
            health_text = a_font.render(f"{plr.max_health} / {plr.health}", False, (255, 0, 0))
            screen.blit(health_text, (plr.rect.x-health_text.get_width()/2+player_width/2,plr.rect.y+player_height+2))
            plr.player_movement(self.edge_rect)
        
        for emy in self.enemies:
            emy.draw(screen)
        
        text_surface_fps = a_font.render(f"fps: {clock.get_fps():.0f}", False, (255, 255, 255))
        screen.blit(text_surface_fps, (0, 600))
        text_surface_fps = a_font.render(f"player_pos: ({plr.rect.x+player_width/2:.0f}, {plr.rect.y+player_height/2:.0f})", False, (255, 255, 255))
        screen.blit(text_surface_fps, (0, 630))
        text_surface_mouse_pos = a_font.render(f"mouse pos: {pygame.mouse.get_pos()}", False, (255, 255, 255))
        screen.blit(text_surface_mouse_pos, (0, 660))
        text_surface_resolution = a_font.render(f"resolution: {screen.get_size()}", False, (255, 255, 255))
        screen.blit(text_surface_resolution, (0, 690))

class levelnext_scene(scene_template):
    pass

class death_scene(scene_template):
    def __init__(self):
        self.player = []
        if selected_class != None:
            self.player.append(selected_class)

        self.text_surface = a_font.render(f"{random.choice(death_messages)} Press ENTER to restart", False, (255, 0, 0))

    def event_handler(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    return menu_scene()

    def update(self):
        if self.player != []:
            self.player[0].reset_position()
            if self.player[0].health != self.player[0].max_health:
                self.player[0].heal_player(self.player[0].max_health-self.player[0].health)
            print(f"Health: {self.player[0].health} / {self.player[0].max_health}")

    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.text_surface, (screen.get_width() // 2 - self.text_surface.get_width() // 2, screen.get_height() // 2))
