import pygame
import random
import player
import enemy
from config import a_font, b_font, screen, clock

selected_class = None
last_door_right = False
rooms = []

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

class next_level_door():
    def __init__(self, x, y, color, right_door):
        self.x = x
        self.y = y
        self.width = 8*4
        self.height = 8*4
        self.color = color
        self.right_door = right_door
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        self.rect = pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        return self

class room_size():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = None
    
    def draw(self):
        self.rect = pygame.draw.rect(screen, (255, 255, 255), (screen.get_width()/2-(self.x/2), screen.get_height()/2-(self.y/2), self.x, self.y), 1)
    
    def get_rect(self):
        return self.rect

def generate_random_room_size():
    x = random.randint(600, 800)
    y = random.randint(300, 600)
    return room_size(x, y)

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
        text_surface = b_font.render("Press ENTER to start", False, (255, 255, 255))
        screen.blit(text_surface, (screen.get_width()/2-text_surface.get_width()/2, screen.get_height()/2-text_surface.get_height()/2))
        text_surface_volume = a_font.render("Volume up/down : [1] [2]", False, (255, 255, 255))
        screen.blit(text_surface_volume, (screen.get_width()/2-text_surface_volume.get_width()/2, screen.get_height()/2-text_surface_volume.get_height()/2+text_surface_volume.get_height()+20))
        text_surface_music = a_font.render("Music : Mick Gordon - Doom Eternal OST - The Only Thing They Fear Is You", False, (255, 255, 255))
        screen.blit(text_surface_music, (screen.get_width()/2-text_surface_music.get_width()/2, screen.get_height()-text_surface_music.get_height()))

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

        warrior_button = button(screen.get_width()/2-50-300, screen.get_height()/2+screen.get_height()/4, 100, 50, (255, 155, 0), "Warrior", (255, 155, 0)).draw(screen)
        archer_button = button(screen.get_width()/2-50, screen.get_height()/2+screen.get_height()/4, 100, 50, (0, 255, 0), "Archer", (0, 255, 0)).draw(screen)
        mage_button = button(screen.get_width()/2-50+300, screen.get_height()/2+screen.get_height()/4, 100, 50, (0, 0, 255), "Mage", (0, 0, 255)).draw(screen)
        if self.player != []:
            start_button = button(screen.get_width()/2-50, screen.get_height()/2+screen.get_height()/4+100, 100, 50, (255, 255, 255), "Start", (255, 255, 255)).draw(screen)
        
        if self.player != []:
                text_surface_damage_display = button(screen.get_width()/2-70-100, screen.get_height()/2+50, 140, 50, (255, 255, 255), f"Damage: {self.player[0].damage:.0f}", (255, 255, 255)).draw(screen)
                text_surface_health_display = button(screen.get_width()/2-70+100, screen.get_height()/2+50, 140, 50, (255, 255, 255), f"Health: {self.player[0].health:.0f}", (255, 255, 255)).draw(screen)
        
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
        global last_door_right
        self.player = []
        self.player.append(selected_class)
        print(self.player)
        self.edge = room_size(720, 480)
        self.edge.draw()
        self.edge_rect = self.edge.get_rect()

        self.right_door = None
        self.left_door = None

        self.enemies = [enemy.Enemy(20, 20, [], 1, 50, (screen.get_width()/2-self.edge_rect.width/4, screen.get_height()/2), 1),
                        enemy.Enemy(20, 20, [], 1, 50, (screen.get_width()/2+self.edge_rect.width/4, screen.get_height()/2), 1)]

    def event_handler(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    self.player[0].damage_player(5)
                    print({self.player[0].health})
                if event.key == pygame.K_k:
                    self.player[0].heal_player(5)
                    print({self.player[0].health})
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    for emy in self.enemies:
                        distance = pygame.Vector2(mouse_pos).distance_to(emy.pos)
                        if distance <= 30:  # Assuming the radius of the enemy's circle is 15
                            emy.take_damage(self.player[0].damage)  # Adjust damage value as needed
                            break
        if self.player[0].health <= 0:
            return death_scene()
        if pygame.key.get_pressed()[pygame.K_x]:
            return death_scene()
        if pygame.key.get_pressed()[pygame.K_t]:
            self.enemies = []
        
        if self.left_door and self.right_door:
            if self.player[0].rect.colliderect(self.left_door.rect) or self.player[0].rect.colliderect(self.right_door.rect):
                rooms.append(levelnext_scene)
                return rooms[len(rooms)-1]()
        
        return self
    
    def update(self):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))

        tile_left = [tile_b(50, 0, "green_brick_l")]

        self.edge.draw()
        self.edge_rect = self.edge.get_rect()

        for tile in tile_left:
            tile.draw(screen)

        text_surface_tutorial = b_font.render(f"Tutorial", False, (255/2, 255/2, 255/2))
        text_surface_move = a_font.render(f"Move player:", False, (255/2, 255/2, 255/2))
        text_surface_wasd = a_font.render(f"[W] [A] [S] [D]", False, (255/2, 255/2, 255/2))
        text_surface_arrow = a_font.render(f"[UP] [DOWN] [LEFT] [RIGHT]", False, (255/2, 255/2, 255/2))
        text_surface_attack = a_font.render(f"Click on the enemy to attack", False, (255/2, 255/2, 255/2))
        text_surface_next = a_font.render(f"Walk to one of the brown doors to continue", False, (255/2, 255/2, 255/2))
        screen.blit(text_surface_tutorial, (screen.get_width()/2-text_surface_tutorial.get_width()/2, screen.get_height()/3-text_surface_tutorial.get_height()/2))
        if self.enemies != []:
            screen.blit(text_surface_move, (screen.get_width()/2-text_surface_move.get_width()/2, 400))
            screen.blit(text_surface_wasd, (screen.get_width()/2-text_surface_wasd.get_width()/2, 430))
            screen.blit(text_surface_arrow, (screen.get_width()/2-text_surface_arrow.get_width()/2, 460))
            screen.blit(text_surface_attack, (screen.get_width()/2-text_surface_attack.get_width()/2, 520))
        elif self.enemies == []:
            screen.blit(text_surface_next, (screen.get_width()/2-text_surface_next.get_width()/2, 520))


        for plr in self.player:
            plr.player_draw()
            player_width, player_height = plr.get_size()
            health_text = a_font.render(f"{plr.health} / {plr.max_health}", False, (255, 0, 0))
            screen.blit(health_text, (plr.rect.x-health_text.get_width()/2+player_width/2,plr.rect.y+player_height+2))
            plr.player_movement(self.edge_rect)
        
        for emy in self.enemies:
            emy.draw(screen)
            if emy.health <= 0:
                self.enemies.remove(emy)

        text_surface_cntl = a_font.render(f"Controls:", False, (255, 255, 255))
        text_surface_suicide = a_font.render(f"Suicide [x]", False, (255, 255, 255))
        text_surface_plr_dmg = a_font.render(f"Damage Player [z]", False, (255, 255, 255))
        text_surface_plr_heal = a_font.render(f"Heal Player [k]", False, (255, 255, 255))
        text_surface_dlt_emy = a_font.render(f"Remove all enemies [t]", False, (255, 255, 255))
        screen.blit(text_surface_cntl, (0, 400))
        screen.blit(text_surface_suicide, (0, 430))
        screen.blit(text_surface_plr_heal, (0, 460))
        text_surface_floors = a_font.render(f"floor: {len(rooms)}", False, (255, 255, 255))
        screen.blit(text_surface_floors, (0, 570))
        text_surface_fps = a_font.render(f"fps: {clock.get_fps():.0f}", False, (255, 255, 255))
        screen.blit(text_surface_fps, (0, 600))
        text_surface_fps = a_font.render(f"player_pos: ({plr.rect.x+player_width/2:.0f}, {plr.rect.y+player_height/2:.0f})", False, (255, 255, 255))
        screen.blit(text_surface_fps, (0, 630))
        text_surface_mouse_pos = a_font.render(f"mouse pos: {pygame.mouse.get_pos()}", False, (255, 255, 255))
        screen.blit(text_surface_mouse_pos, (0, 660))
        text_surface_resolution = a_font.render(f"resolution: {screen.get_size()}", False, (255, 255, 255))
        screen.blit(text_surface_resolution, (0, 690))

        if self.enemies == []:
            left_door_x = self.edge_rect.x + self.edge_rect.width // 4 - 8 * 2
            right_door_x = self.edge_rect.x + self.edge_rect.width // 4 * 3 - 8 * 2
            self.left_door = next_level_door(left_door_x, self.edge_rect.y, ((91, 60, 17)), False).draw(screen)
            self.right_door = next_level_door(right_door_x, self.edge_rect.y, ((91, 60, 17)), True).draw(screen)

class levelnext_scene(scene_template):
    def __init__(self):
        self.player = []
        self.player.append(selected_class)
        print(self.player)
        self.edge = generate_random_room_size()
        self.edge.draw()
        self.edge_rect = self.edge.get_rect()

        self.player[0].rect.x = screen.get_width() / 2 - self.player[0].rect.width / 2
        self.player[0].rect.y = screen.get_height() / 2 + self.edge.y / 2 - self.player[0].rect.height

        self.right_door = None
        self.left_door = None

        margin = 20
        enemy_amount = random.randint(1, 5)
        self.enemies = []
        for i in range(enemy_amount):
            while True:
                enemy_x = random.randint(self.edge_rect.left + margin, self.edge_rect.right - margin)
                enemy_y = random.randint(self.edge_rect.top + margin, self.edge_rect.bottom - margin)
                player_pos = pygame.Vector2(self.player[0].rect.center)
                enemy_pos = pygame.Vector2(enemy_x, enemy_y)
                if player_pos.distance_to(enemy_pos) >= 200:
                    break
            self.enemies.append(enemy.Enemy(10 * (len(rooms)/3), 10 * (len(rooms)/3), [], (len(rooms)/2), 50, (enemy_x, enemy_y), 1 + (len(rooms)/10)))

    def event_handler(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    self.player[0].damage_player(5)
                    print({self.player[0].health})
                if event.key == pygame.K_k:
                    if self.enemies == []:
                        self.player[0].heal_player(self.player[0].max_health-self.player[0].health)
                        print({self.player[0].health})
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    for emy in self.enemies:
                        distance = pygame.Vector2(mouse_pos).distance_to(emy.pos)
                        if distance <= 30:  # Assuming the radius of the enemy's circle is 15
                            emy.take_damage(self.player[0].damage)  # Adjust damage value as needed
                            break
        if self.player[0].health <= 0:
            return death_scene()
        if pygame.key.get_pressed()[pygame.K_x]:
            return death_scene()
        if pygame.key.get_pressed()[pygame.K_t]:
            self.enemies = []
        
        if self.left_door and self.right_door:
            if self.player[0].rect.colliderect(self.left_door.rect) or self.player[0].rect.colliderect(self.right_door.rect):
                rooms.append(levelnext_scene)
                return rooms[len(rooms)-1]()

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
            health_text = a_font.render(f"{plr.health:.0f} / {plr.max_health:.0f}", False, (255, 0, 0))
            screen.blit(health_text, (plr.rect.x-health_text.get_width()/2+player_width/2,plr.rect.y+player_height+2))
            plr.player_movement(self.edge_rect)
        
        for emy in self.enemies:
            emy.draw(screen)
            if emy.health <= 0:
                self.enemies.remove(emy)

        text_surface_cntl = a_font.render(f"Controls:", False, (255, 255, 255))
        text_surface_suicide = a_font.render(f"Suicide [x]", False, (255, 255, 255))
        text_surface_plr_dmg = a_font.render(f"Damage Player [z]", False, (255, 255, 255))
        text_surface_plr_heal = a_font.render(f"Heal Player [k]", False, (255, 255, 255))
        text_surface_dlt_emy = a_font.render(f"Remove all enemies [t]", False, (255, 255, 255))
        screen.blit(text_surface_cntl, (0, 400))
        screen.blit(text_surface_suicide, (0, 430))
        screen.blit(text_surface_plr_heal, (0, 460))
        text_surface_floors = a_font.render(f"floor: {len(rooms)}", False, (255, 255, 255))
        screen.blit(text_surface_floors, (0, 570))
        text_surface_fps = a_font.render(f"fps: {clock.get_fps():.0f}", False, (255, 255, 255))
        screen.blit(text_surface_fps, (0, 600))
        text_surface_fps = a_font.render(f"player_pos: ({plr.rect.x+player_width/2:.0f}, {plr.rect.y+player_height/2:.0f})", False, (255, 255, 255))
        screen.blit(text_surface_fps, (0, 630))
        text_surface_mouse_pos = a_font.render(f"mouse pos: {pygame.mouse.get_pos()}", False, (255, 255, 255))
        screen.blit(text_surface_mouse_pos, (0, 660))
        text_surface_resolution = a_font.render(f"resolution: {screen.get_size()}", False, (255, 255, 255))
        screen.blit(text_surface_resolution, (0, 690))

        if self.enemies == []:
            left_door_x = self.edge_rect.x + self.edge_rect.width // 4 - 8 * 2
            right_door_x = self.edge_rect.x + self.edge_rect.width // 4 * 3 - 8 * 2
            self.left_door = next_level_door(left_door_x, self.edge_rect.y, ((91, 60, 17)), False).draw(screen)
            self.right_door = next_level_door(right_door_x, self.edge_rect.y, ((91, 60, 17)), True).draw(screen)

class death_scene(scene_template):
    def __init__(self):
        self.player = []
        if selected_class != None:
            self.player.append(selected_class)

        self.text_surface = a_font.render(f"{random.choice(death_messages)} Press ENTER to restart", False, (255, 0, 0))

        if rooms != []:
            rooms.clear()

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
