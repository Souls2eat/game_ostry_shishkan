from pygame import *
from random import randint, choice

init()

clock = time.Clock()
screen = display.set_mode((1600, 900))
display.set_caption("Супер-мега игра")
screen.fill((255, 255, 255))

bg = image.load("images/maps/map2.png").convert_alpha()
pause_menu = image.load("images/menu/pause_menu.png").convert_alpha()
settings_menu = image.load("images/menu/settings_menu.png").convert_alpha()
main_menu = image.load("images/menu/main_menu.png").convert_alpha()

font20 = font.Font("fonts/ofont.ru_Nunito.ttf", 20)
font40 = font.Font("fonts/ofont.ru_Nunito.ttf", 40)
font60 = font.Font("fonts/ofont.ru_Nunito.ttf", 60)

current_level = 1
level_state = "not_run"
money = 1200
time_to_spawn = 0
game_state = "run"


class Tower(sprite.Sprite):
    def __init__(self, unit, pos):
        super().__init__(towers_group, all_sprites_group)
        self.image = image.load(f"images/towers/{unit}.png").convert_alpha()
        self.is_dead = False

        self.name = unit
        self.rect = self.image.get_rect(topleft=(pos))

        # СТАТЫ начало

        if self.name == 'fire_mag':  # циферки поменять
            self.hp = 200
            self.atk = 20
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = 55
            self.damage_type = ''
            self.cost = 10

        if self.name == 'boomchick':  
            self.hp = 200
            self.atk = 20 #типа по кому попадёт получит 40 а остальные по 20
            self.bullet_speed_x = 4
            self.bullet_speed_y = 0
            self.attack_cooldown = 85
            self.damage_type = ''
            self.cost = 20

        if self.name == 'kopitel':
            self.hp = 200
            self.atk = 30
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.attack_cooldown = 80
            self.damage_type = ''
            self.nakopleno = 0
            self.max_nakopit = 9
            self.cost = 20

        if self.name == 'thunder':
            self.hp = 100
            self.atk = 30
            self.bullet_speed_x = 7
            self.bullet_speed_y = 3
            self.attack_cooldown = 200
            self.damage_type = ''
            self.cost = 15

        if self.name == 'zeus':
            self.hp = 100
            self.atk = 100
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.attack_cooldown = 150
            self.damage_type = ''
            self.cost = 20

        if self.name == 'yascerica':
            self.hp = 250
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.attack_cooldown = 0
            self.damage_type = ''
            self.bullet = Bullet("blackik", self.rect.centerx - 26, self.rect.centery,
                                 self.damage_type, 0, self.bullet_speed_x, self.bullet_speed_y, 'yas',
                                 self)
            self.bullet.remove(bullets_group)
            self.cost = 10

        if self.name == 'terpila':  # циферки поменять
            self.hp = 5000
            self.cost = 30

        if self.name == 'davalka':
            self.hp = 200
            self.skolko_deneg_dast = 30
            self.davanie_cooldown = 900
            self.cost = 20
            self.time_on_screen = 0 #это для плюс денег

        # СТАТЫ конец


    def delat_chtoto(self):  # тут надо будет написать условие при котором башня стреляет
        if self.is_dead != True:
            if self.name == 'zeus' or self.name == "fire_mag" or self.name == 'boomchick':
                for enemy in enemies_group:
                    if enemy.rect.y == self.rect.y and enemy.rect.x >= self.rect.x:
                        self.is_shooting()

            if self.name == 'kopitel':
                    self.is_shooting()

            if self.name == 'thunder':
                for enemy in enemies_group:
                    if (enemy.rect.y == self.rect.y or enemy.rect.y == self.rect.y + 128 or enemy.rect.y == self.rect.y - 128) and enemy.rect.x >= self.rect.x:
                        self.is_shooting()

            if self.name == 'davalka':
                self.dayot()

            if self.hp <= 0:
                self.is_dead = True
                self.kill()


    def is_shooting(self):
        #keys = key.get_pressed() если нужно будет затестить по нажатию
            
        if self.name == "fire_mag":  # пока привет
            if self.attack_cooldown <= 0:
                self.attack_cooldown = 55
                Bullet("blue_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'default', self)

        if self.name == 'boomchick':  
            if self.attack_cooldown <= 0:
                self.attack_cooldown = 85
                Bullet("yellow_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'boom', self)

        if self.name == 'kopitel':
            if self.attack_cooldown <= 0:
                self.attack_cooldown = 100
                if self.nakopleno < self.max_nakopit:
                    self.joska_schitayu_x = 64 * (1 + (self.nakopleno // 3))
                    self.joska_schitayu_y = 32 * (self.nakopleno % 3) + 20
                    self.spear_or_sword = randint(0, 1)
                    if self.spear_or_sword == 0:
                        Bullet("light_spear", self.rect.centerx-self.joska_schitayu_x, self.rect.y+self.joska_schitayu_y, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'kopilka', self)
                    if self.spear_or_sword == 1:
                        Bullet("light_sword", self.rect.centerx-self.joska_schitayu_x, self.rect.y+self.joska_schitayu_y, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'kopilka', self)

                    self.nakopleno += 1

        if self.name == 'thunder':
            if self.attack_cooldown <= 0:
                self.attack_cooldown = 200
                Bullet("Frigl_bul", self.rect.centerx - 8, self.rect.centery - 8,
                                     self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'hrom',
                                     self)

                Bullet("Frigl_bul", self.rect.centerx - 8, self.rect.centery - 8,
                                     self.damage_type, self.atk, self.bullet_speed_x, 0, 'hrom',
                                     self)

                Bullet("Frigl_bul", self.rect.centerx - 8, self.rect.centery - 8,
                                     self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y * -1, 'hrom',
                                     self)

        if self.name == 'zeus':
            if self.attack_cooldown <= 0:
                self.attack_cooldown = 225
                self.bullet = Bullet("Laser", self.rect.centerx + 640, self.rect.centery,
                                    self.damage_type, self.atk, self.bullet_speed_x, 0,
                                    'ls', self)


    def dayot(self):
        if self.name == 'davalka':
            if self.davanie_cooldown <= 0:
                self.davanie_cooldown = 900
                global money
                money += self.skolko_deneg_dast
                self.plus_dengi = font20.render('+30', True, (0, 70, 200))
                self.time_on_screen = 50

        

    def update(self):
        self.delat_chtoto()

        if self.name == 'fire_mag' or self.name == 'kopitel' or self.name == 'thunder' or self.name == 'yascerica' or self.name == 'zeus' or self.name == 'boomchick':
            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1

        if self.name == 'davalka':
            if self.davanie_cooldown > 0:
                self.davanie_cooldown -= 1
            if self.time_on_screen > 0:
                screen.blit(self.plus_dengi, (self.rect.centerx-15, self.rect.centery-55))
                self.time_on_screen -= 1


class Bullet(sprite.Sprite):
    def __init__(self, bullet_sprite, x, y, damage_type, damage, speed_x, speed_y, name, parent):
        super().__init__(all_sprites_group, bullets_group)
        self.image = image.load(f"images/bullets/{bullet_sprite}.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.is_dead = False
        self.damage_type = damage_type
        self.damage = damage
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.name = name
        self.parent = parent

        if self.name == 'ls':
            self.off = 75
        if self.name == 'explosion':
            self.off = 20

        if self.name == 'yas':
            self.sumon = 'ready'
            self.cooldown = 375

    def bullet_movement(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.name == 'hrom':
            if (self.parent.rect.centery - self.rect.centery) >= 128 or (self.rect.centery - self.parent.rect.centery) >= 128:
                self.speed_y = 0
        
        if self.name == 'ls':
            if self.off <= 0:
                self.off = 75  # так потом же kill(), зачем возврашать 75? хпхпхппхпххп
                self.kill()
            else:
                self.off -= 1

        if self.name == 'explosion':
            if self.off <= 0:
                self.off = 20  # так потом же kill(), зачем возврашать 20? хпхпхппхпххп
                self.kill()
            else:
                self.off -= 1

        if self.name == 'kopilka':
            for enemy in enemies_group:
                if enemy.rect.y == self.parent.rect.y and enemy.rect.x >= self.parent.rect.x:
                    self.speed_x = 7
                    self.parent.nakopleno = 0
                    self.parent.attack_cooldown = 100

            if self.parent not in all_sprites_group and self.speed_x == 0:
                self.kill()

        if self.name == 'yas':
            for enemy in enemies_group:

                if enemy.rect.y == self.parent.rect.y and enemy.rect.x >= self.parent.rect.x and self.sumon == 'ready':
                    self.speed_x = 2
                    self.sumon = 'go'
                    self.parent.bullet.add(bullets_group)

                if (enemy.rect.colliderect(self.rect) or self.rect.centerx >= 1500) and self.sumon == 'go':
                    self.speed_x *= -1
                    self.sumon = 'back'

            if self.rect.centerx == self.parent.rect.centerx - 26 and self.sumon == 'back':
                self.speed_x = 0
                self.sumon = 'wait'

            if self.cooldown <= 0 and self.sumon == 'wait':
                self.cooldown = 375
                self.sumon = 'ready'

            if self.parent.is_dead == True:
                self.kill()

        if self.rect.x >= 1700:
            self.kill()

    def update(self):
        self.bullet_movement()

        if self.name == 'yas' and self.sumon == 'wait':
            if self.cooldown > 0:
                self.cooldown -= 1


class Enemy(sprite.Sprite):  # враг, он же "зомби"
    def __init__(self, name, pos):
        super().__init__(all_sprites_group, enemies_group)
        self.image = image.load(f"images/enemies/{name}.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(pos))
        self.is_dead = False
        self.name = name
        self.stop = False

        # СТАТЫ начало

        if self.name == 'popusk':  # циферки поменять
            self.hp = 300
            self.atk = 100
            self.speed = 1
            self.attack_cooldown = 75

        if self.name == 'josky':
            self.hp = 600
            self.atk = 100
            self.speed = 1
            self.attack_cooldown = 75

        if self.name == 'sigma':
           self.hp = 1200
           self.atk = 100
           self.speed = 1
           self.attack_cooldown = 75

        # СТАТЫ конец

    def delat_chtoto(self):
        if self.is_dead != True:
            if self.stop != True:
                self.rect.x -= self.speed

            self.stop = False  # нужно чтобы в случае колизии останавливался, а если колизии не будет то шёл дальше. ОБЯЗАТЕЛЬНО ПОСЛЕ ПРОВЕРКИ СТОПА НО ПЕРЕД ПРОВЕРКОЙ КОЛИЗИИ
            for tower in towers_group:
                if sprite.collide_rect(self, tower):
                    self.attack_cooldown -= 1
                    self.stop = True
                    if self.attack_cooldown <= 0:
                        self.attack_cooldown = 75
                        tower.hp -= self.atk

            if self.hp <= 0 or self.rect.x <= -256:
                self.is_dead = True
                self.kill()
        
    def update(self):
        self.delat_chtoto()


class UI(sprite.Sprite):
    def __init__(self, pos, path, unit_inside):
        super().__init__(ui_group, all_sprites_group)
        self.image = image.load(f"images/{path}/images_inside/{unit_inside}_inside.png").convert_alpha()
        self.pos = pos
        self.default_pos = pos
        self.rect = self.image.get_rect(topleft=(self.pos))
        self.is_move = False
        self.unit_inside = unit_inside
        self.path = path

    def move(self):
        self.image = image.load(f"images/{self.path}/{self.unit_inside}.png").convert_alpha()
        self.pos = mouse.get_pos()
        self.rect = self.image.get_rect(center=(self.pos))

    def back_to_default(self):
        self.image = image.load(f"images/{self.path}/images_inside/{self.unit_inside}_inside.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.default_pos))

    def update(self):
        if self.is_move == True:
            self.move()
        if self.is_move == False:
            self.back_to_default()


class Button:
    def __init__(self, text, font, pos, col=(255, 255, 255)):  # Можно добавить scale
        self.image = font.render(text, font, col)   # По дефолту цвет текста белый. Я ебал по 50 раз писать одно и тоже
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        # self.image = transform.scale(self.image, (int(self.w * scale), int(self.h * scale))) # для скейла
        self.rect = self.image.get_rect(topleft=(pos))
        self.clicked = False
        self.pushed = False

    def click(self, surf, mouse_pos):
        if not self.rect.collidepoint(mouse_pos):
            self.pushed = False
        if self.rect.collidepoint(mouse_pos):
            if mouse.get_pressed()[0] == 1 and not self.pushed:
                self.pushed = True
        if mouse.get_pressed()[0] == 0 and self.pushed:
            self.pushed = False
            return True

        surf.blit(self.image, self.rect)


def random_spawn_enemies():
    line_cords = [192, 320, 448, 576, 704]
    enemy_sprites = ["josky", "popusk", "sigma"]
    y_cord = choice(line_cords)
    name = choice(enemy_sprites)
    Enemy(name, (1600, y_cord))


def is_free(object):
    global money
    is_free_list = []  # Проверка свободна ли клетка
    for tower in towers_group:
        is_free_list.append(tower.rect.collidepoint(object.rect.centerx, object.rect.centery) is False)
    if all(is_free_list):
        is_free_list.clear()
        return True
    is_free_list.clear()


def spawn_level(current_level):
    print(current_level)
    if current_level == 1:
        pass
        # Enemy("popusk", (1408, 320))
        # Enemy("sigma", (1408, 192))
        # Enemy("josky", (1408, 576))
        # Enemy("popusk", (1208, 576))
        # Enemy("popusk", (1508, 576))

    elif current_level == 2:
        Enemy("josky", (1408, 320))
        Enemy("popusk", (1208, 576))

    return "run", current_level + 1


def clear_level():
    for enemy in enemies_group:
        enemy.kill()
    for tower in towers_group:
        tower.kill()
        if hasattr(tower, "bullet"):
            tower.bullet.kill()
    for bullet in bullets_group:
        bullet.kill()


bullets_group = sprite.Group()
enemies_group = sprite.Group()
towers_group = sprite.Group()
ui_group = sprite.Group()
all_sprites_group = sprite.Group()
buttons_group = sprite.Group()

# Tower("zeus", (384, 704))
Tower("kopitel", (384, 192))
Tower("yascerica", (512, 704))





UI((1500, 800), "shovel", "lopata")

UI((94, 160), "towers", "davalka", )
UI((94, 256), "towers", "boomchick")
UI((94, 352), "towers", "terpila")
UI((94, 448), "towers", "kopitel")
UI((94, 544), "towers", "zeus")
UI((94, 640), "towers", "yascerica")
UI((94, 736), "towers", "fire_mag")  # +0, +96


pause_button = Button("||", font40, (1550, 30))
death_button = Button("Вы проиграли", font60, (591, 280))
resume_button = Button("Продолжить", font60, (614, 360))
settings_button = Button("Настройки", font60, (642, 440))
maim_menu_button = Button("В главное меню", font60, (567, 520))
back_button = Button("Назад", font60, (709, 520))


running = True

while running:

    screen.blit(bg, (0, 0))
    screen.blit(font40.render(str(money), True, (0, 0, 0)), (88, 53))
    all_sprites_group.draw(screen)
    mouse_pos = mouse.get_pos()

    if level_state == "not_run":
        level_state, current_level = spawn_level(current_level)

    # -------
    if game_state == "run":
        all_sprites_group.update()
        time_to_spawn += 1
        if time_to_spawn == 375:
            random_spawn_enemies()
            time_to_spawn = 0

    if game_state == "paused":
        screen.blit(pause_menu, (480, 250))
        screen.blit(font60.render("Пауза", True, (193, 8, 42)), (700, 280))
        if resume_button.click(screen, mouse_pos):
            game_state = "run"
        if settings_button.click(screen, mouse_pos):
            game_state = "settings_menu"
        if maim_menu_button.click(screen, mouse_pos):
            game_state = "main_menu"

    if game_state == "settings_menu":
        screen.blit(settings_menu, (480, 250))
        if back_button.click(screen, mouse_pos):
            time.wait(100)
            game_state = "paused"

    if game_state == "main_menu":
        screen.blit(main_menu, (0, 0))

    if game_state == "death":
        screen.blit(pause_menu, (480, 250))
        if death_button.click(screen, mouse_pos):
            game_state = "run"
            level_state = "not_run"
            clear_level()
    # -------

    if pause_button.click(screen, mouse_pos):
        if game_state == "paused":
            game_state = "run"
        elif game_state == "run":
            game_state = "paused"

    for bullet in bullets_group:
        if bullet.name == 'ls' or bullet.name == 'explosion':
            for enemy in enemies_group:
                if sprite.collide_rect(enemy, bullet) and enemy.hp > 0:
                    enemy.hp -= bullet.damage
            bullet.remove(bullets_group)

    for enemy in enemies_group:
        if enemy.rect.x <= 100:
            game_state = "death"
            enemy.kill()
        for bullet in bullets_group:
            if sprite.collide_rect(enemy, bullet) and enemy.hp > 0:
                if bullet.name == 'default' or bullet.name == 'hrom' or bullet.name == 'kopilka':
                    enemy.hp -= bullet.damage
                    bullet.kill()
                if bullet.name == 'yas':
                    enemy.hp -= enemy.hp
                    bullet.parent.bullet.remove(bullets_group)
                if bullet.name == 'boom':
                    enemy.hp -= bullet.damage
                    bullet.explosion = Bullet("explosion", bullet.rect.centerx, bullet.rect.centery, bullet.damage_type, bullet.damage, 0, 0, 'explosion', bullet.parent)
                    bullet.kill()

    clock.tick(75)
    display.update()

    for e in event.get():
        # keys = key.get_pressed()
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE and game_state != "death":
                if game_state == "run":
                    game_state = "paused"
                else:
                    game_state = "run"
            if e.key == K_SPACE:
                Enemy("sigma", (1508, 704))
            if e.key == K_q:
                running = False
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:  # При нажатии кнопки мыши
            mouse_pos = mouse.get_pos()
            for el in ui_group:
                if el.rect.collidepoint(mouse_pos):
                    el.is_move = True
                    el.last_clicked = True

        if e.type == MOUSEBUTTONUP:  # При отжатии кнопки мыши
            mouse_pos = mouse.get_pos()
            unit_pos = (384 + ((mouse_pos[0] - 384) // 128) * 128), (192 + ((mouse_pos[1] - 192) // 128) * 128)


            for el in ui_group:

                if el.rect.collidepoint(mouse_pos):  # если элемент отпущен
                    el.is_move = False

                    if 1536 > unit_pos[0] >= 384 and 832 > unit_pos[1] >= 192:

                        if el.path == "towers":
                            if is_free(el):
                                unit = Tower(el.unit_inside, unit_pos)
                                if money - unit.cost < 0:  # Это пиздец, но оно работает. Придумаете лучше -- переделаете
                                    unit.kill()
                                    if hasattr(unit, "bullet"):
                                        unit.bullet.kill()
                                else:
                                    money -= unit.cost

                        if el.path == "shovel":
                            for tower in towers_group:
                                if tower.rect.collidepoint(el.rect.centerx, el.rect.centery):
                                    money += tower.cost // 2
                                    if hasattr(tower, "bullet"):
                                        tower.bullet.kill()
                                    tower.kill()
            # for button in buttons_group:
            #     if button.rect.collidepoint(mouse_pos):
            #         button.clicked = True
