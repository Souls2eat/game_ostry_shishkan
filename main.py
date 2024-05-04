from pygame import *
from math import *
from random import randint, choice
from config import *

init()

clock = time.Clock()
screen = display.set_mode((1600, 900))
display.set_caption("game_ostry_shishkan")
mouse.set_visible(False)
screen.fill((255, 255, 255))

bg = image.load(f"images/maps/map1.png").convert_alpha()
menu = image.load("images/menu/pause_menu.png").convert_alpha()
main_menu = image.load("images/menu/main_menu.png").convert_alpha()
select_menu = image.load("images/menu/level_select_menu.png").convert_alpha()
select_menu_copy = select_menu.__copy__()
level_box = image.load("images/menu/level_box.png").convert_alpha()
# tower_select_menu = image.load("images/menu/tower_select_menu.png").convert_alpha()
# tower_select_menu_copy = tower_select_menu.__copy__()
amogus = image.load("images/other/amogus!!!.png").convert_alpha()
cursor = image.load("images/other/cursor.png").convert_alpha()

font20 = font.Font("fonts/ofont.ru_Nunito.ttf", 20)
font30 = font.Font("fonts/ofont.ru_Nunito.ttf", 30)
font40 = font.Font("fonts/ofont.ru_Nunito.ttf", 40)
font60 = font.Font("fonts/ofont.ru_Nunito.ttf", 60)

game_name = font60.render("GAME_OSTRY_SHISHIKAN", True, (255, 255, 255))  # GAME_OSTRY_SHISHIKAN
game_state = "main_menu"
last_game_state = game_state
selected_towers = []
buttons_group = []
blocked_slots = []
scroll_offset = 0
current_scroll_offset_state = game_state


with open("save.txt", "r", encoding="utf-8") as file:
    just_text = file.readline().strip()
    new_game = file.readline().strip().split()[2]               # получить значение переменной
    unlocked_levels = int(file.readline().strip().split()[2])
    if new_game.lower() == "true":
        new_game = True
    else:
        new_game = False


class ModGroup(sprite.Group):
    def __init__(self):
        super().__init__()

    def draw2(self, surf):
        for obj in self.sprites():
            if hasattr(obj, "image2"):
                obj.draw2(surf)


class Level:
    def __init__(self, level_number, level_time, time_to_spawn, start_money, waves: dict, allowed_enemies: dict, allowed_cords=(192, 320, 448, 576, 704)):
        self.image = image.load(f"images/maps/map{level_number}.png").convert_alpha()
        self.current_level = level_number
        self.money = self.start_money = start_money
        self.state = "not_run"
        self.level_time = self.start_level_time = level_time
        self.start_time_to_spawn = self.time_to_spawn = time_to_spawn
        self.cheat = False
        self.waves = waves
        self.allowed_enemies = allowed_enemies
        self.allowed_cords = allowed_cords

        self.x = 384     # для полоски уровня
        self.y = 110
        self.w = 1151
        self.h = 40

    def draw_level_time(self):      # надо бы написать по-понятней
        ratio = self.level_time / self.start_level_time
        draw.rect(screen, (233, 126, 72), (self.x, self.y, self.w, self.h))
        draw.rect(screen, (55, 127, 236), (self.x, self.y, self.w * ratio, self.h))
        draw.rect(screen, (0, 0, 0), (self.x, self.y, self.w, self.h), 4)
        for wave_time in self.waves:
            mark_ratio = wave_time / self.start_level_time
            screen.blit(amogus, (self.x + int(mark_ratio * self.w), self.y - 30))

    def wave_spawn_enemies(self, wave_time):
        waves_points = self.waves[wave_time]
        enemy_x_cord = 1600
        while waves_points > 0:
            enemy_name = choice([*self.allowed_enemies])
            enemy_y_cord = choice(self.allowed_cords)
            Enemy(enemy_name, (enemy_x_cord, enemy_y_cord))
            waves_points -= self.allowed_enemies[enemy_name]
            enemy_x_cord += randint(10, 30)

    def random_spawn_enemies(self):
        enemy_y_cord = choice(self.allowed_cords)
        enemy_name = choice([*self.allowed_enemies])
        Enemy(enemy_name, (1600, enemy_y_cord))

    @staticmethod
    def clear(*without):
        if without:
            if "enemies_group" not in without:
                for enemy in enemies_group:
                    enemy.kill()
            if "towers_group" not in without:
                for tower in towers_group:
                    tower.kill()
                    if hasattr(tower, "bullet"):
                        tower.bullet.kill()
            if "nekusaemie_group" not in without:
                for nekusaemiy in nekusaemie_group:
                    nekusaemiy.kill()
            if "bullets_group" not in without:
                for bullet in bullets_group:
                    bullet.kill()
            if "ui_group" not in without:
                for ui in ui_group:
                    ui.kill()
            if "clouds_group" not in without:
                for cloud in clouds_group:
                    cloud.kill()
            if "buttons_group" not in without:
                for button in buttons_group:
                    button.ok = False
        else:
            for enemy in enemies_group:
                enemy.kill()
            for tower in towers_group:
                tower.kill()
                if hasattr(tower, "bullet"):
                    tower.bullet.kill()
            for nekusaemiy in nekusaemie_group:
                nekusaemiy.kill()
            for bullet in bullets_group:
                bullet.kill()
            # for el in ui_group:
            #     el.is_move = False
            for cloud in clouds_group:
                cloud.kill()
            for ui in ui_group:
                ui.kill()
            for button in buttons_group:
                button.ok = False

    def spawn(self):
        UI((1500, 800), "shovel", "lopata")
        selected_towers.clear()

        if self.current_level == 1:
            Enemy("popusk", (1408, 320))
            Enemy("sigma", (1408, 192))
            Enemy("josky", (1408, 576))
            Enemy("popusk", (1208, 576))
            Enemy("popusk", (1508, 576))

        elif self.current_level == 2:
            Enemy("josky", (1408, 320))
            Enemy("popusk", (1208, 576))

        Cloud((1000, 100))
        Cloud((600, 60))
        Cloud((300, 70))
        Cloud((720, 20))
        Cloud((1400, 50))
        Cloud((1200, 30))
        Cloud((1800, 90))

        return "run"

    def refresh(self):
        self.money = self.start_money
        self.level_time = self.start_level_time
        self.time_to_spawn = self.start_time_to_spawn
        self.clear()

    def update(self):
        all_sprites_group.update()
        for wave_time in self.waves:
            if self.level_time == wave_time:
                self.wave_spawn_enemies(wave_time)
        if self.state == "not_run":
            self.state = self.spawn()
        if not self.cheat:
            if self.time_to_spawn > 0:
                self.time_to_spawn -= 1
            else:
                self.time_to_spawn = self.start_time_to_spawn
                self.random_spawn_enemies()
            if self.level_time > 0:
                self.level_time -= 1
                return "run"
            else:
                return "level_complited"
        else:
            return "run"


class Tower(sprite.Sprite):
    def __init__(self, unit, pos):
        super().__init__(towers_group, all_sprites_group)
        self.image = image.load(f"images/towers/{unit}.png").convert_alpha()
        self.is_dead = False
        self.pos = pos
        self.kd = 150

        self.name = unit
        self.rect = self.image.get_rect(topleft=pos)
        self.have_barrier = False

        # СТАТЫ начало

        if self.name == 'fire_mag':  # циферки поменять
            self.hp = 200
            self.atk = 20
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = 55
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''

        if self.name == 'boomchick':  
            self.hp = 200
            self.atk = 20  # типа по кому попадёт получит 40 а остальные по 20
            self.bullet_speed_x = 4
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = 85
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''

        if self.name == 'kopitel':
            self.hp = 200
            self.atk = 30
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = 80
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''
            self.nakopleno = 0
            self.max_nakopit = 7

        if self.name == 'thunder':
            self.hp = 100
            self.atk = 30
            self.bullet_speed_x = 7
            self.bullet_speed_y = 3
            self.basic_attack_cooldown = 200
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''

        if self.name == 'zeus':
            self.hp = 100
            self.atk = 100
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = 225
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''

        if self.name == 'yascerica':
            self.hp = 250
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = 150
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''
            self.bullet = Bullet("blackik", self.rect.centerx - 26, self.rect.centery,
                                 self.damage_type, 0, self.bullet_speed_x, self.bullet_speed_y, 'yas',
                                 self)
            self.bullet.remove(bullets_group)

        if self.name == 'parasitelniy':
            self.hp = 2200
            self.max_hp = 2200
            self.atk = 10
            self.basic_attack_cooldown = 150
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''
            self.have_parasite = sprite.Group()

        if self.name == 'spike':  
            self.hp = 1
            self.atk = 20
            self.basic_attack_cooldown = 75
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''
            self.remove(towers_group)
            self.add(nekusaemie_group)

        if self.name == 'pukish':
            self.hp = 1
            self.atk = 50
            self.atk2 = 5
            self.bullet_speed_x = 2
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = 150
            self.attack_cooldown = self.basic_attack_cooldown
            self.basic_attack_cooldown2 = 15
            self.attack_cooldown2 = self.basic_attack_cooldown2
            self.damage_type = ''

        if self.name == 'urag_anus':
            self.hp = 100
            self.atk = 3
            self.uragan_duration = 375
            self.basic_uragan_cooldown = 1875  
            self.uragan_cooldown = 375
            self.uragan = None

        if self.name == 'drachun':
            self.hp = 400
            self.atk = 25
            self.kulak_time = 15
            self.basic_attack_cooldown = 55
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''

        if self.name == 'nuka_kusni':
            self.hpchela = 500
            self.hpkonya = 500
            self.speed_x = 0
            self.atk = 30
            self.taran_atk = 500
            self.kulak_time = 15
            self.basic_attack_cooldown = 55
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''
            self.toptop_group = sprite.Group()
            self.konb_sushestvuet = True

        if self.name == 'tolkan':
            self.hp = 2000
            self.atk = 50
            self.ottalkivanie_solo = 384
            self.ottalkivanie_ne_solo = 128
            self.za_towerom = False
            self.kulak_time = 15
            self.basic_attack_cooldown = 750
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''

        if self.name == 'big_mechman':
            self.hp = 600
            self.atk = 75
            self.kulak_time = 15
            self.basic_attack_cooldown = 250
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''

        if self.name == 'terpila':  # циферки поменять
            self.hp = 6000

        if self.name == 'oh_shit_i_am_sorry__barrier_mag':
            self.hp = 1500
            self.barrier_hp = 3000
            self.basic_barrier_cooldown = 750  # 3375
            self.barrier_cooldown = 0

        if self.name == 'davalka':
            self.hp = 200
            self.skolko_deneg_dast = 30
            self.basic_davanie_cooldown = 900
            self.davanie_cooldown = self.basic_davanie_cooldown

        if self.name == 'matricayshon':
            self.hp = 500
            for i in range(9):
                self.buff_x = 1+(i%3)*128-128
                self.buff_y = 1+(i//3)*128-128
                self.buff = Buff("mat", self.rect.x + self.buff_x, self.rect.y + self.buff_y)

        # СТАТЫ конец


    def delat_chtoto(self):  # тут надо будет написать условие при котором башня стреляет
        if self.is_dead != True:
            if self.name == 'zeus' or self.name == "fire_mag" or self.name == 'boomchick':
                for enemy in enemies_group:
                    if enemy.rect.y == self.rect.y and enemy.rect.x >= self.rect.x:
                        self.is_shooting()

            if self.name == 'pukish':
                if self in towers_group:
                    for enemy in enemies_group:
                        if enemy.rect.y == self.rect.y and enemy.rect.x >= self.rect.x:
                            self.is_shooting()

            if self.name == 'kopitel':
                    self.is_shooting()

            if self.name == 'thunder' or self.name == 'urag_anus':
                for enemy in enemies_group:
                    if (enemy.rect.y == self.rect.y or enemy.rect.y == self.rect.y + 128 or enemy.rect.y == self.rect.y - 128) and enemy.rect.x >= self.rect.x:
                        self.is_shooting()

            if self.name == 'parasitelniy':
                for enemy in enemies_group:
                    if enemy not in self.have_parasite:
                        self.is_shooting()

            if self.name == 'spike':
                if self.attack_cooldown <= 0:
                    for enemy in enemies_group:
                        if sprite.collide_rect(self, enemy) and enemy.hp > 0:
                            enemy.hp -= self.atk
                    self.attack_cooldown = self.basic_attack_cooldown

            if self.name == 'pukish':
                self.remove(nekusaemie_group)
                self.add(towers_group)
                for enemy in enemies_group:
                    if sprite.collide_rect(self, enemy):
                        self.remove(towers_group)
                        self.add(nekusaemie_group)
                if self in towers_group:
                    self.image = image.load(f"images/towers/{self.name}.png").convert_alpha()
                    for enemy in enemies_group:
                        if enemy.rect.y == self.rect.y and enemy.rect.x >= self.rect.x:
                            self.is_shooting()
                if self in nekusaemie_group:
                    self.image = image.load(f"images/towers/{self.name}2.png").convert_alpha()
                    if self.attack_cooldown2 <= 0:
                        for enemy in enemies_group:
                            if sprite.collide_rect(self, enemy) and enemy.hp > 0:
                                enemy.hp -= self.atk2
                        self.attack_cooldown2 = self.basic_attack_cooldown2

            if self.name == 'drachun' or self.name == 'tolkan' or self.name == 'big_mechman'  or self.name == 'nuka_kusni':
                if self.kulak_time > 0:
                    self.kulak_time -= 1
                if self.kulak_time <= 0:
                    self.kulak_time = 15
                    if hasattr(self, 'konb_sushestvuet'):
                        if self.konb_sushestvuet:
                            self.image = image.load(f"images/towers/{self.name}.png").convert_alpha()
                        if not self.konb_sushestvuet:
                            self.image = image.load("images/towers/nuka_kusni_no_net_konya.png").convert_alpha()
                    else:
                        self.image = image.load(f"images/towers/{self.name}.png").convert_alpha()
                for enemy in enemies_group:
                    if self.name == 'drachun' or self.name == 'tolkan' or self.name == 'nuka_kusni':
                        if enemy.rect.y == self.rect.y and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x <= 256:
                            self.is_shooting()
                    if self.name == 'big_mechman':
                        if (enemy.rect.y - self.rect.y <= 128 or self.rect.y - enemy.rect.y <= 128) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x <= 256:
                            self.is_shooting()

            if self.name == 'davalka' or self.name == 'oh_shit_i_am_sorry__barrier_mag':
                self.dayot()
            
            if self.name == 'nuka_kusni':
                if self.hpkonya <= 0 and self.konb_sushestvuet:
                    self.konb_sushestvuet = False
                    self.image = image.load("images/towers/nuka_kusni_no_net_konya.png").convert_alpha()

                if self.hpchela <= 0:
                    if self.konb_sushestvuet == True:
                        self.konb = Bullet("kusni_ne_probuy", self.rect.centerx, self.rect.centery, '', self.taran_atk, 7, 0, 'gas', self)
                    self.kill()

            if self.name != 'nuka_kusni':
                if self.hp <= 0:
                    self.is_dead = True
                    if self.name == 'boomchick':
                        self.explosion = Bullet("explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.atk*5, 0, 0, 'explosion', self)
                    self.kill()


    def is_shooting(self):

        if self.name == "fire_mag":  # пока привет
            if self.attack_cooldown <= 0:
                self.attack_cooldown = self.basic_attack_cooldown
                Bullet("blue_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'default', self)

        if self.name == 'boomchick':  
            if self.attack_cooldown <= 0:
                self.attack_cooldown = self.basic_attack_cooldown
                Bullet("yellow_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'boom', self)

        if self.name == 'kopitel':
            if self.attack_cooldown <= 0:
                self.attack_cooldown = self.basic_attack_cooldown
                if self.nakopleno < self.max_nakopit:
                    self.joska_schitayu_y = 16 * (self.nakopleno) + 16
                    self.spear_or_sword = randint(0, 1)
                    if self.spear_or_sword == 0:
                        self.pulya = Bullet("light_spear", self.rect.centerx-28, self.rect.y+self.joska_schitayu_y, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'kopilka', self)
                    if self.spear_or_sword == 1:
                        self.pulya = Bullet("light_sword", self.rect.centerx-28, self.rect.y+self.joska_schitayu_y, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'kopilka', self)
                    self.pulya.remove(bullets_group)
                    self.nakopleno += 1

        if self.name == 'thunder':
            if self.attack_cooldown <= 0:
                self.attack_cooldown = self.basic_attack_cooldown
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
                self.attack_cooldown = self.basic_attack_cooldown
                self.bullet = Bullet("Laser", self.rect.centerx + 640, self.rect.centery,
                                    self.damage_type, self.atk, self.bullet_speed_x, 0,
                                    'ls', self)

        if self.name == 'parasitelniy':
            if self.attack_cooldown <= 0:
                self.attack_cooldown = self.basic_attack_cooldown
                for enemy in enemies_group:
                    if enemy not in self.have_parasite:
                        self.parasix = randint(0, 32)
                        self.parasiy = randint(-32, 32)
                        self.parasite = Parasite('sosun', enemy.rect.centerx+self.parasix, enemy.rect.centery+self.parasiy, '', self.atk, enemy, self)
                        enemy.add(self.have_parasite)
                        break

        if self.name == "pukish":
            if self.attack_cooldown <= 0:
                self.attack_cooldown = self.basic_attack_cooldown
                Bullet("gas", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'gas', self)

        if self.name == 'urag_anus':
            if self.uragan_cooldown <= 0:
                self.uragan_cooldown = self.basic_uragan_cooldown
                self.nearest_enemy = 0
                for enemy in enemies_group:
                        if (enemy.rect.y == self.rect.y or enemy.rect.y == self.rect.y + 128 or enemy.rect.y == self.rect.y - 128) and enemy.rect.x >= self.rect.x:
                            if self.nearest_enemy == 0:
                                self.nearest_enemy = enemy
                            if self.nearest_enemy.rect.x > enemy.rect.x:
                                self.nearest_enemy = enemy 
                if self.nearest_enemy.rect.centerx+128 < 1500:
                    self.uragan = Parasite('uragan', self.nearest_enemy.rect.centerx+128, self.rect.centery, '', self.atk, self, self)
                else:
                    self.uragan = Parasite('uragan', 1472, self.rect.centery, '', self.atk, self, self)

        if self.name == 'drachun':
            if self.attack_cooldown <= 0:
                self.attack_cooldown = self.basic_attack_cooldown
                self.image = image.load(f"images/towers/{self.name}2.png").convert_alpha()
                for enemy in enemies_group:
                    if enemy.rect.y == self.rect.y and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x <= 256:
                        enemy.hp -= self.atk
                self.kulak_time = 15

        if self.name == 'nuka_kusni':
            if self.attack_cooldown <= 0:
                self.attack_cooldown = self.basic_attack_cooldown
                if self.konb_sushestvuet:
                    self.image = image.load(f"images/towers/{self.name}2.png").convert_alpha()
                if not self.konb_sushestvuet:
                    self.image = image.load("images/towers/nuka_kusni_no_net_konya2.png").convert_alpha()
                for enemy in enemies_group:
                    if enemy.rect.y == self.rect.y and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x <= 256:
                        enemy.hp -= self.atk
                self.kulak_time = 15

        if self.name == 'tolkan':
            if self.attack_cooldown <= 0:
                self.attack_cooldown = self.basic_attack_cooldown
                self.image = image.load(f"images/towers/{self.name}2.png").convert_alpha()
                self.za_towerom = False
                for tower in towers_group:
                    if tower.rect.y == self.rect.y and tower.rect.x > self.rect.x and tower.rect.x - self.rect.x <= 128 and tower.name != 'pukish' and tower != self:
                        self.za_towerom = True
                for enemy in enemies_group:
                    if enemy.rect.y == self.rect.y and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x <= 256:
                        enemy.hp -= self.atk
                        if self.za_towerom == True:
                            enemy.rect.x += self.ottalkivanie_ne_solo
                        else:
                            enemy.rect.x += self.ottalkivanie_solo
                self.kulak_time = 15

        if self.name == 'big_mechman':
            if self.attack_cooldown <= 0:
                self.attack_cooldown = self.basic_attack_cooldown
                self.explosion = Bullet("big_mechman2", self.rect.right, self.rect.centery, self.damage_type, self.atk, 0, 0, 'explosion', self)
                


    def dayot(self):
        if self.name == 'davalka':
            if self.davanie_cooldown <= 0:
                self.davanie_cooldown = self.basic_davanie_cooldown
                level.money += self.skolko_deneg_dast
                Alert("+30", (self.rect.centerx-15, self.rect.centery-55), 50, font30, (0, 70, 200))  # мне было больно смотреть на time_on_screen, когда есть алерты

        if self.name == 'oh_shit_i_am_sorry__barrier_mag': 
            if self.barrier_cooldown <= 0:
                self.barrier_cooldown = self.basic_barrier_cooldown
                self.best_x = self
                for tower in towers_group:
                    if tower.rect.y == self.rect.y and tower.rect.x > self.best_x.rect.x and tower.name != 'pukish' and tower.have_barrier == False:
                        self.best_x = tower
                self.best_x.have_barrier = True
                self.barrier = Parasite('oh_shit_i_am_sorry__barrier_mag__sobstvenno_govorya_barrier', self.best_x.rect.centerx, self.best_x.rect.centery, '', 0, self.best_x, self)


    def update(self):
        self.delat_chtoto()

        if self.name == 'fire_mag'\
                or self.name == 'kopitel'\
                or self.name == 'thunder'\
                or self.name == 'zeus'\
                or self.name == 'boomchick'\
                or self.name == 'parasitelniy'\
                or self.name == 'spike'\
                or self.name == 'pukish'\
                or self.name == 'drachun'\
                or self.name == 'tolkan'\
                or self.name == 'big_mechman'\
                or self.name == 'nuka_kusni':

            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1

        if self.name == 'pukish':
            if self.attack_cooldown2 > 0:
                self.attack_cooldown2 -= 1

        if self.name == 'oh_shit_i_am_sorry__barrier_mag' and self.barrier not in all_sprites_group:
            if self.barrier_cooldown > 0:
                self.barrier_cooldown -= 1

        if self.name == 'urag_anus' and self.uragan not in all_sprites_group:
            if self.uragan_cooldown > 0:
                self.uragan_cooldown -= 1

        if self.name == 'davalka':
            if self.davanie_cooldown > 0:
                self.davanie_cooldown -= 1


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
            self.parent.attack_cooldownwn = 375

        if self.name == 'gas':
            self.gazirovannie_group = sprite.Group()

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
            if self.parent not in all_sprites_group and self.speed_x == 0:
                self.kill()

            for enemy in enemies_group:
                if enemy.rect.y == self.parent.rect.y and enemy.rect.x >= self.parent.rect.x:
                    self.speed_x = 7
                    self.add(bullets_group)
                    self.parent.nakopleno = 0
                    self.parent.attack_cooldown = self.parent.basic_attack_cooldown


        if self.name == 'yas':
            for enemy in enemies_group:

                if enemy.rect.y == self.parent.rect.y and enemy.rect.x >= self.parent.rect.x and self.sumon == 'ready':
                    self.speed_x = 2
                    self.sumon = 'go'
                    self.parent.bullet.add(bullets_group)

                if enemy.rect.colliderect(self.rect) and self.sumon == 'go':
                    self.speed_x *= -1
                    self.sumon = 'back'

            if self.rect.centerx >= 1500 and self.sumon == 'go':
                self.speed_x *= -1
                self.sumon = 'back'

            if self.rect.centerx == self.parent.rect.centerx - 26 and self.sumon == 'back':
                self.speed_x = 0
                self.sumon = 'wait'

            if self.parent.attack_cooldown <= 0 and self.sumon == 'wait':
                self.parent.attack_cooldown = self.parent.basic_attack_cooldown
                self.sumon = 'ready'

            if self.parent.is_dead == True:
                self.kill()

        if self.name == 'gas':
            for enemy in enemies_group:
                if sprite.collide_rect(enemy, self) and enemy.hp > 0:
                    if enemy not in self.gazirovannie_group:
                        enemy.hp -= self.damage
                        enemy.add(self.gazirovannie_group)

        if self.rect.x >= 1700:
            self.kill()

    def update(self):
        self.bullet_movement()

        if self.name == 'yas' and self.sumon == 'wait':
            if self.parent.attack_cooldown > 0:
                self.parent.attack_cooldown -= 1


class Parasite(sprite.Sprite):
    def __init__(self, name, x, y, damage_type, damage, owner, parent):
        super().__init__(all_sprites_group, parasites_group)
        self.image = image.load(f"images/buffs/{name}.png").convert_alpha() # не думаю что их будет много так что пусть в папке пуль будут(если хотите можете поменять)
        self.rect = self.image.get_rect(center=(x, y))
        self.is_dead = False
        self.damage_type = damage_type
        self.damage = damage
        self.name = name
        self.owner = owner # это враг к которому привязан паразит
        self.parent = parent


        if self.name == 'sosun':
            self.parasix = self.parent.parasix
            self.parasiy = self.parent.parasiy
            self.attack_cooldown = 75
        
        if self.name == 'oh_shit_i_am_sorry__barrier_mag__sobstvenno_govorya_barrier':
            self.hp = self.parent.barrier_hp

        if self.name == 'uragan':
            self.duration = self.parent.uragan_duration
            self.attack_cooldown = 15


    def prisasivanie(self):
        if self.parent not in all_sprites_group or self.owner not in all_sprites_group:
            self.kill()
            if self.name == 'uragan':
                for enemy in enemies_group:
                    enemy.back_to_line()
            if self.name == 'sosun':        
                self.parent.have_parasite.remove(self.owner)
            if self.name == 'oh_shit_i_am_sorry__barrier_mag__sobstvenno_govorya_barrier':
                self.owner.have_barrier = False

        if self.name == 'oh_shit_i_am_sorry__barrier_mag__sobstvenno_govorya_barrier' and self.hp <= 0:
            self.kill()
            self.owner.have_barrier = False
                
        if self.name == 'sosun':
            self.rect.centerx = self.owner.rect.centerx+self.parasix
            self.rect.centery = self.owner.rect.centery+self.parasiy
            if self.attack_cooldown <= 0:
                self.attack_cooldown = 75
                self.owner.hp -= self.damage
                if self.parent.hp < self.parent.max_hp - (self.damage//2):
                    self.parent.hp += self.damage//2

        if self.name == 'uragan':
            for enemy in enemies_group:
                if self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                    enemy.angle = atan2(self.rect.centery - enemy.rect.centery, self.rect.centerx - enemy.rect.centerx)
                    enemy.x_vel = cos(enemy.angle) * enemy.speed * 6
                    enemy.y_vel = sin(enemy.angle) * enemy.speed * 6
                    enemy.rect.x += enemy.x_vel
                    enemy.rect.y += enemy.y_vel

                    if self.attack_cooldown <= 0:
                        self.attack_cooldown = 15
                        enemy.hp -= self.damage
                        

                
    def update(self):
        self.prisasivanie()
        
        if self.name == 'sosun' or self.name == 'uragan':
            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1

        if self.name == 'uragan':
            if self.duration > 0:
                self.duration -= 1
            else:
                self.kill()
                for enemy in enemies_group:
                    enemy.back_to_line()


class Buff(sprite.Sprite):
    def __init__(self, name, x, y):
        super().__init__(all_sprites_group, buffs_group)
        self.image = image.load(f"images/buffs/{name}.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.rect.x = x
        self.rect.y = y
        self.rect2 = Rect(self.rect.x-128, self.rect.y-128, 384, 384) 
        self.name = name
        self.buffed_towers = sprite.Group()
        if self.name == 'mat':
            self.mozhet_zhit = False
        for buff in buffs_group:
            if self.rect.collidepoint(buff.rect.centerx, buff.rect.centery) and self != buff:
                self.kill()

    def delat_buff(self):
        for tower in towers_group:
            if tower not in self.buffed_towers:
                if self.rect.collidepoint(tower.rect.centerx, tower.rect.centery):
                    if tower.name == 'fire_mag'\
                            or tower.name == 'kopitel'\
                            or tower.name == 'thunder'\
                            or tower.name == 'yascerica'\
                            or tower.name == 'zeus'\
                            or tower.name == 'boomchick'\
                            or tower.name == 'parasitelniy'\
                            or tower.name == 'pukish'\
                            or tower.name == 'drachun'\
                            or tower.name == 'tolkan'\
                            or tower.name == 'big_mechman'\
                            or tower.name == 'nuka_kusni':

                        tower.basic_attack_cooldown //= 2
                        tower.add(self.buffed_towers)
                    if tower.name == 'urag_anus':
                        tower.basic_uragan_cooldown //= 2
                        tower.add(self.buffed_towers)

        for nekusaemiy in nekusaemie_group:
            if nekusaemiy not in self.buffed_towers:
                if self.rect.collidepoint(nekusaemiy.rect.centerx, nekusaemiy.rect.centery):
                    if nekusaemiy.name == 'spike':
                        nekusaemiy.basic_attack_cooldown //= 2
                        nekusaemiy.add(self.buffed_towers)

    def check_tower(self):
        for tower in towers_group:
            if tower.name == 'matricayshon':
                if self.rect2.collidepoint(tower.rect.centerx, tower.rect.centery):
                    self.mozhet_zhit = True
        if self.mozhet_zhit == False:
            self.kill()
            for tower in self.buffed_towers:
                if tower.name == 'fire_mag'\
                        or tower.name == 'kopitel'\
                        or tower.name == 'thunder'\
                        or tower.name == 'yascerica'\
                        or tower.name == 'zeus'\
                        or tower.name == 'boomchick'\
                        or tower.name == 'parasitelniy'\
                        or tower.name == 'pukish'\
                        or tower.name == 'drachun'\
                        or tower.name == 'tolkan'\
                        or tower.name == 'big_mechman'\
                        or tower.name == 'nuka_kusni':
                    tower.basic_attack_cooldown *= 2
                if tower.name == 'urag_anus':
                    tower.basic_uragan_cooldown *= 2
        self.mozhet_zhit = False

    def update(self):
        self.delat_buff()
        self.check_tower()


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
            self.atk_type = 'earth'
            self.speed = 1
            self.attack_cooldown = 75

        if self.name == 'josky':
            self.hp = 600
            self.atk = 100
            self.atk_type = 'earth'
            self.speed = 1
            self.attack_cooldown = 75

        if self.name == 'sigma':
            self.hp = 1200
            self.atk = 100
            self.atk_type = 'air'
            self.speed = 1
            self.attack_cooldown = 75

        # СТАТЫ конец

    def delat_chtoto(self):
        if self.is_dead != True:
            if self.stop != True:
                self.rect.x -= self.speed

            self.stop = False  # нужно чтобы в случае колизии останавливался, а если колизии не будет то шёл дальше. ОБЯЗАТЕЛЬНО ПОСЛЕ ПРОВЕРКИ СТОПА НО ПЕРЕД ПРОВЕРКОЙ КОЛИЗИИ
            for tower in towers_group:
                if tower.rect.collidepoint(self.rect.centerx, self.rect.centery):
                    self.attack_cooldown -= 1
                    self.stop = True
                    if self.attack_cooldown <= 0:
                        self.attack_cooldown = 75
                        if tower.have_barrier == True:
                            for barrier in parasites_group:
                                if barrier.name == 'oh_shit_i_am_sorry__barrier_mag__sobstvenno_govorya_barrier' and barrier.owner == tower:
                                    barrier.hp -= self.atk
                                    break
                        else:
                            if tower.name == 'nuka_kusni':
                                if self.atk_type == 'earth':
                                    if tower.konb_sushestvuet == True:
                                        tower.hpkonya -= self.atk
                                    else:
                                        tower.hpchela -= self.atk
                                if self.atk_type == 'air':
                                    tower.hpchela -= self.atk
                            else:
                                tower.hp -= self.atk

            if self.hp <= 0 or self.rect.x <= -256:
                self.is_dead = True
                self.kill()
        
    def back_to_line(self):
        if (self.rect.y-192) % 128 < 64:
            self.rect.y -= (self.rect.y-192) % 128
        else:
            self.rect.y += 128 - ((self.rect.y-192) % 128)

    def update(self):
        self.delat_chtoto()


class UI(sprite.Sprite):
    def __init__(self, pos, path, unit_inside, kd_time=0):
        super().__init__(ui_group, all_sprites_group)
        self.image = image.load(f"images/{path}/images_inside/{unit_inside}_inside.png").convert_alpha()
        self.pos = pos
        self.default_pos = pos
        self.rect = self.image.get_rect(topleft=self.pos)
        self.path = path
        self.unit_inside = unit_inside
        self.is_move = False
        self.kd_time = 0
        self.default_kd_time = kd_time
        self.loaded_p = False

        if self.path == "towers":
            self.cost = tower_costs[unit_inside]                                # Аналог без ебанины :)
            self.image2 = font30.render(str(self.cost), True, (255, 255, 255))
            self.rect2 = self.image2.get_rect(topleft=(self.default_pos[0] - 49, self.default_pos[1] + 4))

    def move(self):
        self.pos = mouse.get_pos()
        self.rect = self.image.get_rect(center=self.pos)

    def back_to_default(self):
        self.image = image.load(f"images/{self.path}/images_inside/{self.unit_inside}_inside.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=self.default_pos)
        self.pos = self.default_pos

    def draw2(self, surf):
        surf.blit(self.image2, self.rect2)

    def update(self):
        if level.cheat:
            self.kd_time = -1

        if self.is_move and self.kd_time == -1:                         # если нажал кнопку и кд откатилось
            self.image = image.load(f"images/{self.path}/{self.unit_inside}.png").convert_alpha()
            self.move()
        if self.is_move and self.kd_time != -1:                         # если нажал кнопку и кд не откатилось
            self.is_move = False
        if self.is_move is not True and self.pos != self.default_pos:   # если отжал кнопку и не на дефолтной позиции.
            self.back_to_default()                                      # тут короче баг был, что функция постоянно вызывалась и подгружала изображение :)

        if self.kd_time == self.default_kd_time:                        # когда  обновилось кд, загрузить картинку закрытого слота
            self.image = image.load("images/other/kd_slota.png").convert_alpha()
        if self.kd_time == 0:                                           # когда кд дошло до нуля, загрузить картину юнита
            self.image = image.load(f"images/{self.path}/images_inside/{self.unit_inside}_inside.png").convert_alpha()
            self.kd_time = -1                                           # чтобы картинка загрузилась только 1 раз, а потом проверка не пройдёт

        if self.kd_time > 0:                                            # уменьшает кд с каждым циклом
            self.kd_time -= 1

        screen.blit(font30.render(str(self.kd_time), True, (255, 255, 255)), (self.default_pos[0] - 49, self.default_pos[1] + 50))  # потом будет графически так что пох что пропадает


class Button:  # Переделать на спрайты кнопок
    def __init__(self, data_type, font_or_path, text_or_img, closed=False):
        if data_type == "img":
            self.image = image.load(f"images/{font_or_path}/{text_or_img}.png").convert_alpha()
            self.unit_inside = text_or_img
        if data_type == "text":
            self.font = font_or_path
            self.text = text_or_img

        self.data_type = data_type
        self.clicked = False
        self.pushed = False
        self.ok = False
        self.closed = closed
        buttons_group.append(self)

    def click(self, surf, mouse_pos, pos, col=(255, 255, 255), offset_pos=(0, 0)):  # offset_pos нужно только где есть скрол
        if self.data_type == "text":
            self.image = self.font.render(self.text, font, col)   # По дефолту цвет текста белый. Я ебал по 50 раз писать одно и тоже
        self.rect = self.image.get_rect(topleft=(pos[0] + offset_pos[0], pos[1] + offset_pos[1]))

        surf.blit(self.image, (self.rect.x - offset_pos[0], self.rect.y - offset_pos[1]))
        if self.ok is True:
            surf.blit(image.load("images/other/ok.png").convert_alpha(), (self.rect.x - offset_pos[0], self.rect.y - offset_pos[1]))

        if not self.rect.collidepoint(mouse_pos):
            self.pushed = False
        if self.rect.collidepoint(mouse_pos):
            if mouse.get_pressed()[0] == 1 and not self.pushed:
                self.pushed = True
        if mouse.get_pressed()[0] == 0 and self.pushed:
            self.pushed = False
            return True


class Cloud(sprite.Sprite):
    def __init__(self, *pos):
        super().__init__(all_sprites_group, clouds_group)
        r = randint(1, 5)
        self.image = image.load(f"images/clouds/cloud{r}.png").convert_alpha()
        if pos:
            self.x = pos[0][0]
            self.y = pos[0][1]
        else:
            self.x = 1600
            self.y = randint(0, 100)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self):
        self.x -= 1
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        if self.x < - 200:
            self.kill()
            Cloud()


class Alert(sprite.Sprite):
    def __init__(self, text, pos, alert_time, font=font60, col=(255, 0, 0), after_sec=0):
        super().__init__(alert_group)
        self.standard_image = font.render(text, True, col)
        self.rect = self.standard_image.get_rect(topleft=pos)
        self.alert_time = alert_time
        self.trigger = after_sec * 75
        self.already_triggered = False
        self.text = text

    def update(self):
        if self.trigger > 0 and not self.already_triggered:
            self.trigger -= 1
            self.image = image.load("images/other/nothing.png").convert_alpha()
        else:
            self.already_triggered = True
            self.image = self.standard_image

            if self.alert_time < 0:
                self.kill()
            else:
                self.alert_time -= 1


def is_free(obj):
    is_free_list = []  # Проверка свободна ли клетка
    for tower in towers_group:
        is_free_list.append(tower.rect.collidepoint(obj.rect.centerx, obj.rect.centery) is False)
    for nekusaemiy in nekusaemie_group:
        is_free_list.append(nekusaemiy.rect.collidepoint(obj.rect.centerx, obj.rect.centery) is False)
    if all(is_free_list):
        is_free_list.clear()
        return True
    is_free_list.clear()


def add_to_slots_slots(i, *blocked_slots):              # instant_select будет потом
    if tower_select_buttons[i].ok:
        tower_select_buttons[i].ok = False
        selected_towers.remove(tower_select_buttons[i].unit_inside)
        for ui in ui_group:
            if ui.unit_inside == tower_select_buttons[i].unit_inside:
                ui.kill()

    elif len(selected_towers) <= 6 - len(blocked_slots):
        tower_select_buttons[i].ok = True
        if blocked_slots:
            UI((94, first_empty_slot(*blocked_slots)), "towers", tower_select_buttons[i].unit_inside, towers_kd[tower_select_buttons[i].unit_inside])
        else:
            UI((94, first_empty_slot()), "towers", tower_select_buttons[i].unit_inside, towers_kd[tower_select_buttons[i].unit_inside])
        selected_towers.append(tower_select_buttons[i].unit_inside)
    else:
        Alert("Закончились свободные слоты", (345, 580), 75)


def first_empty_slot(*blocked_slots):
    if blocked_slots:
        ui_pos_list = {160, 256, 352, 448, 544, 640, 736} - set(blocked_slots)
    else:
        ui_pos_list = {160, 256, 352, 448, 544, 640, 736}
    fill_pos = set()
    for ui in ui_group:
        if ui.rect.y in ui_pos_list:
            fill_pos.add(ui.rect.y)

    return min(ui_pos_list - fill_pos)


def level_box_button_create(button_number):
    if button_number <= unlocked_levels:
        return Button("img", "menu", "level_box")
    else:
        return Button("img", "menu", "level_box_closed", True)


def scroll_offset_min_max(min_offset, max_offset):
    global scroll_offset, current_scroll_offset_state

    if scroll_offset < min_offset:
        scroll_offset = min_offset
    if scroll_offset > max_offset:
        scroll_offset = max_offset

    if current_scroll_offset_state != game_state:
        scroll_offset = 0
        current_scroll_offset_state = game_state


def menu_positioning():
    global game_state,\
            new_game,\
            running,\
            last_game_state,\
            selected_towers,\
            tower_select_buttons,\
            level_box_buttons,\
            unlocked_levels, \
            levels, \
            level,\
            blocked_slots,\
            scroll_offset

    mouse_pos = mouse.get_pos()

    if game_state == "main_menu":

        screen.blit(main_menu, (0, 0))
        screen.blit(game_name, (416, 10))

        if new_game_button.click(screen, mouse_pos, (30, 460)):                         # 1 кнопка
            last_game_state = game_state
            game_state = "tower_select"  # новая игра
            new_game = False
            level = levels[0]
            level.refresh()
            level.state = "not_run"
        if new_game:
            if resume_button.click(screen, mouse_pos, (30, 540), col=(130, 130, 130)):  # 2 кнопка серая
                Alert("<- Тыкай новую игру", (500, 460), 75)
        else:
            if resume_button.click(screen, mouse_pos, (30, 540)):                       # 2 кнопка белая
                last_game_state = game_state
                if level.state == "run":
                    game_state = "run"
                else:
                    selected_towers.clear()
                    game_state = "level_select"
        if level_select_button.click(screen, mouse_pos, (30, 620)):                     # 3 кнопка
            last_game_state = game_state
            game_state = "level_select"
        if settings_button.click(screen, mouse_pos, (30, 700)):                         # 4 кнопка
            last_game_state = game_state
            game_state = "settings_menu"
        if quit_button.click(screen, mouse_pos, (30, 780)):                             # 5 кнопка
            running = False

    if game_state == "level_select":
        screen.blit(main_menu, (0, 0))
        screen.blit(select_menu, (320, 150))      # (320, 150) и будет offset_pos
        select_menu.blit(select_menu_copy, (0, 0))
        scroll_offset_min_max(-1000, 0)

        for i in range(1, len(level_box_buttons) + 1):
            column = i
            line = i
            if i <= 3:
                column = 0
            elif i <= 7:
                column = 1
            elif i <= 11:
                column = 2
            # column = (i % 5)

            line = int((i - 1) / 4)
            column = (i - 1) % 4

            if level_box_buttons[i-1].click(select_menu, mouse_pos, (48 + 208 * column, 48 + (line * 208) + scroll_offset), offset_pos=(320, 150)):     # +320, 150   (368, 198)
                print(line, column)
                if not level_box_buttons[i-1].closed:
                    scroll_offset = 0
                    new_game = False
                    level.refresh()
                    level = levels[i-1]
                    last_game_state = game_state
                    game_state = "tower_select"
                    level.state = "not_run"
            if not level_box_buttons[i-1].closed:
                select_menu.blit(font60.render(str(i), True, (255, 255, 255)), (108 + 208 * column, 68 + (line * 370) + scroll_offset))  # + 380, 40
        # draw.line(level_select_menu, (255, 255, 255), (900, 48), (900, 552), 15)
        if back_button.click(screen, mouse_pos, (709, 620)):
            game_state = last_game_state

    if game_state != "main_menu" and game_state != "main_settings_menu" and game_state != "level_select":
        screen.blit(level.image, (0, 0))
        if level.cheat:
            screen.blit(font40.render("CHEAT MODE", True, (255, 0, 0)), (853, 110))
        else:
            level.draw_level_time()
            # screen.blit(font40.render(str(level.level_time) + " осталось", True, (255, 255, 255)), (853, 110))    # циферки
        screen.blit(font40.render(str(level.current_level) + " уровень", True, (255, 255, 255)), (893, 30))
        screen.blit(font40.render(str(level.money), True, (0, 0, 0)), (88, 53))

        all_sprites_group.draw(screen)
        all_sprites_group.draw2(screen)

    if game_state == "run":
        game_state = level.update()
        if pause_button.click(screen, mouse_pos, (1550, 30)):
            last_game_state = game_state
            Alert("Пауза", (700, 200), 75)
            game_state = "paused"

    if game_state == "paused":
        screen.blit(menu, (480, 250))
        # screen.blit(font60.render("Пауза", True, (193, 8, 42)), (700, 280))
        if resume_button.click(screen, mouse_pos, (614, 280)):
            last_game_state = game_state
            if level.state == "run":            # len(selected_towers) == 7 - len(blocked_slots)
                game_state = "run"
            else:
                game_state = "tower_select"
        if settings_button.click(screen, mouse_pos, (642, 360)):
            last_game_state = game_state
            game_state = "settings_menu"
        if level.state == "run":           # белая кнопка
            if restart_button.click(screen, mouse_pos, (582, 440)):
                last_game_state = game_state
                level.refresh()
                game_state = "tower_select"
                level.state = "not_run"
        else:
            if restart_button.click(screen, mouse_pos, (582, 440), col=(130, 130, 130)):  # 2 кнопка серая
                pass
        if main_menu_button.click(screen, mouse_pos, (567, 520)):
            last_game_state = game_state
            game_state = "main_menu"
        if pause_button.click(screen, mouse_pos, (1550, 30)):
            Alert("Пауза", (700, 200), 75)
            if level.state == "run":
                last_game_state = game_state
                game_state = "run"
            else:
                game_state, last_game_state = last_game_state, game_state

    if game_state == "level_complited":
        screen.blit(menu, (480, 250))
        screen.blit(font60.render("Уровень пройден", True, (193, 8, 42)), (544, 280))
        if next_level_button.click(screen, mouse_pos, (496, 360)):
            level.refresh()
            level = levels[level.current_level]
            game_state = "tower_select"
        if restart_button.click(screen, mouse_pos, (582, 440)):
            last_game_state = game_state
            level.refresh()
            game_state = "tower_select"
            level.state = "not_run"
        if main_menu_button.click(screen, mouse_pos, (567, 520)):
            last_game_state = game_state
            game_state = "main_menu"
            level.state = "not_run"

    if game_state == "tower_select":
        screen.blit(select_menu, (320, 150))
        select_menu.blit(select_menu_copy, (0, 0))
        scroll_offset_min_max(-1000, 0)
        blocked_slots = []  # если надо, чтобы не во все слоты можно было пихать башни

        if level.current_level == 1:
            blocked_slots = []               # 160, 256, 352, 448, 544, 640, 736
        if level.current_level == 2:
            blocked_slots = []

        for i in range(1, len(tower_select_buttons) + 1):

            line = int((i - 1) / 6)
            column = (i - 1) % 6
            if tower_select_buttons[i-1].click(select_menu, mouse_pos, (column * 158, 30 + line * 154 + scroll_offset), offset_pos=(320, 150)):
                add_to_slots_slots(i-1, *blocked_slots)
        if start_level_button.click(screen, mouse_pos, (567, 650)):
            if len(selected_towers) == 7 - len(blocked_slots):
                scroll_offset = 0
                game_state = "run"
                level.clear("ui_group")
                level.state = "not_run"
            else:
                Alert("Остались свободные слоты", (400, 580), 75)
        if pause_button.click(screen, mouse_pos, (1550, 30)):
            last_game_state = game_state
            Alert("Пауза", (700, 200), 75)
            game_state = "paused"
        ui_group.draw(screen)

    if game_state == "settings_menu":
        if last_game_state == "main_menu" or last_game_state == "level_select":
            screen.blit(main_menu, (0, 0))
            screen.blit(game_name, (416, 10))
        screen.blit(menu, (480, 250))
        if back_button.click(screen, mouse_pos, (709, 520)):
            game_state = last_game_state

        Alert("Возможна проблема с галочкой", (300, 700), 25)
        if cheat_button.click(screen, mouse_pos, (736, 280)):
            if cheat_button.ok:
                cheat_button.ok = False
                level.cheat = False
                # ----
                alert_list = [alert.text for alert in alert_group]
                if "Спавн врагов выключен" in alert_list:
                    Alert("Читы отключены", (562, 30), 150, after_sec=2)
                else:
                    Alert("Читы отключены", (562, 30), 150)
                alert_list.clear()
                # ----
            else:
                Alert("Спавн врагов выключен", (442, 30), 150)
                Alert("Время уровня бесконечно", (417, 110), 150)
                Alert("Проиграть невозможно", (452, 190), 150)
                Alert("Бесконечные деньги", (470, 270), 150)

                cheat_button.ok = True
                level.cheat = True

    if game_state == "death":
        screen.blit(menu, (480, 250))
        screen.blit(font60.render("Вы проиграли", True, (193, 8, 42)), (590, 280))
        if settings_button.click(screen, mouse_pos, (642, 360)):
            last_game_state = game_state
            game_state = "settings_menu"
        if restart_button.click(screen, mouse_pos, (582, 440)):
            last_game_state = game_state
            level.refresh()
            game_state = "tower_select"
            level.state = "not_run"
        if main_menu_button.click(screen, mouse_pos, (567, 520)):
            last_game_state = game_state
            game_state = "main_menu"
            level.state = "not_run"
    # -------


bullets_group = sprite.Group()
parasites_group = sprite.Group()
buffs_group = sprite.Group()
enemies_group = sprite.Group()
towers_group = sprite.Group()
nekusaemie_group = sprite.Group()
ui_group = sprite.Group()
all_sprites_group = ModGroup()
clouds_group = sprite.Group()
alert_group = sprite.Group()
level_group = sprite.Group()    # заебись, левел груп в которой 1 значение


pause_button = Button("text", font40, "||",)
restart_button = Button("text", font60, "Перезапустить")
resume_button = Button("text", font60, "Продолжить")
settings_button = Button("text", font60, "Настройки")
main_menu_button = Button("text", font60, "В главное меню")
back_button = Button("text", font60, "Назад")
quit_button = Button("text", font60, "Выход")
new_game_button = Button("text", font60, "Новая игра",)
level_select_button = Button("text", font60, "Выбрать уровень")
next_level_button = Button("text", font60, "Следующий уровень")
cheat_button = Button("img", "menu", "cheat")


level_box_button1 = level_box_button_create(1)
level_box_button2 = level_box_button_create(2)
level_box_button3 = level_box_button_create(3)
level_box_button4 = level_box_button_create(4)
level_box_button5 = level_box_button_create(5)
level_box_button6 = level_box_button_create(6)
level_box_button7 = level_box_button_create(7)
level_box_button8 = level_box_button_create(8)

level_box_buttons = [
    level_box_button1,
    level_box_button2,
    level_box_button3,
    level_box_button4,
    level_box_button5,
    level_box_button6,
    level_box_button7,
    level_box_button8
]

start_level_button = Button("text", font60, "Начать уровень")

tower_select_button1 = Button("img", "towers", "fire_mag")
tower_select_button2 = Button("img", "towers", "davalka")
tower_select_button3 = Button("img", "towers", "boomchick")
tower_select_button4 = Button("img", "towers", "kopitel")
tower_select_button5 = Button("img", "towers", "matricayshon")
tower_select_button6 = Button("img", "towers", "parasitelniy")
tower_select_button7 = Button("img", "towers", "pukish")
tower_select_button8 = Button("img", "towers", "spike")
tower_select_button9 = Button("img", "towers", "terpila")
tower_select_button10 = Button("img", "towers", "thunder")
tower_select_button11 = Button("img", "towers", "yascerica")
tower_select_button12 = Button("img", "towers", "zeus")
tower_select_button13 = Button("img", "towers", "oh_shit_i_am_sorry__barrier_mag")
tower_select_button14 = Button("img", "towers", "urag_anus")
tower_select_button15 = Button("img", "towers", "drachun")
tower_select_button16 = Button("img", "towers", "tolkan")
tower_select_button17 = Button("img", "towers", "big_mechman")
tower_select_button18 = Button("img", "towers", "nuka_kusni")

tower_select_buttons = [
            tower_select_button1,
            tower_select_button2,
            tower_select_button3,
            tower_select_button4,
            tower_select_button5,
            tower_select_button6,
            tower_select_button7,
            tower_select_button8,
            tower_select_button9,
            tower_select_button10,
            tower_select_button11,
            tower_select_button12,
            tower_select_button13,
            tower_select_button14,
            tower_select_button15,
            tower_select_button16,
            tower_select_button17,
            tower_select_button18
]

levels = [Level(1, 7500, 375, 300, level_1_waves, enemy_costs),         # enemy_costs -- туда закидывается враг и его стоимость
          Level(2, 3000, 150, 300, level_2_waves, enemy_costs),         # типо можно выбрать, каких врагов спавнить можно, а каких нет
          Level(3, 6000, 225, 300, level_3_waves, enemy_costs)]         # это из конфига

level = levels[0]


running = True
while running:

    mouse_pos = mouse.get_pos()

    menu_positioning()
    # scroll_offset_back_to_default("level_select", "tower_select")
    alert_group.update()
    alert_group.draw(screen)

    screen.blit(cursor, mouse_pos)
    # print(f"now: {game_state}, last: {last_game_state}")      # не убирать!!!
    # print(level.state)

    for bullet in bullets_group:
        if bullet.name == 'ls' or bullet.name == 'explosion':
            for enemy in enemies_group:
                if sprite.collide_rect(enemy, bullet) and enemy.hp > 0:
                    enemy.hp -= bullet.damage
            bullet.remove(bullets_group)

    for enemy in enemies_group:
        if enemy.rect.x <= 150:
            if not level.cheat:
                game_state = "death"
            enemy.kill()
        for bullet in bullets_group:
            if enemy.rect.collidepoint(bullet.rect.right, bullet.rect.centery):
                if bullet.name == 'kopilka':
                    enemy.hp -= bullet.damage
                    bullet.kill()
            if sprite.collide_rect(enemy, bullet) and enemy.hp > 0:
                if bullet.name == 'default' or bullet.name == 'hrom':
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
        if e.type == MOUSEWHEEL and (game_state == "level_select" or game_state == "tower_select"):
            scroll_offset += e.y * 50
            print(e.y, scroll_offset)
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE and game_state == "run" \
                                or game_state == "paused"\
                                or game_state == "settings_menu"\
                                or game_state == "tower_select":
                if game_state == "run":
                    last_game_state = game_state
                    Alert("Пауза", (700, 200), 75)
                    game_state = "paused"
                elif game_state == "tower_select":
                    last_game_state = game_state
                    Alert("Пауза", (700, 200), 75)
                    game_state = "paused"
                elif game_state == "settings_menu" and last_game_state != "main_menu":
                    game_state = "paused"
                elif game_state == "settings_menu" and last_game_state == "main_menu":
                    game_state = "main_menu"
                elif last_game_state == "tower_select":
                    last_game_state = game_state
                    game_state = "tower_select"
                # else:
                #     if level.state == "run":
                #         last_game_state = game_state
                #         game_state = "run"
                #     else:
                #         last_game_state = game_state
                #         game_state = "tower_select"

            if e.key == K_z:
                Enemy("popusk", (1508, 192))
            if e.key == K_x:
                Enemy("josky", (1508, 320))
            if e.key == K_c:
                Enemy("sigma", (1508, 448))
            if e.key == K_v:
                Enemy("josky", (1508, 576))
            if e.key == K_b:
                Enemy("sigma", (1508, 704))
            if e.key == K_r:
                game_state = "main_menu"
            if e.key == K_q:         
                running = False
        if e.type == QUIT:           # низя!!!
             running = False
        if e.type == MOUSEBUTTONDOWN:  # При нажатии кнопки мыши
            mouse_pos = mouse.get_pos()
            for el in ui_group:
                if el.rect.collidepoint(mouse_pos):
                    el.is_move = True
        if e.type == MOUSEBUTTONUP:  # При отжатии кнопки мыши
            mouse_pos = mouse.get_pos()
            unit_pos = (384 + ((mouse_pos[0] - 384) // 128) * 128), (192 + ((mouse_pos[1] - 192) // 128) * 128)

            for el in ui_group:
                if el.rect.collidepoint(mouse_pos):  # если элемент отпущен
                    el.is_move = False

                    if 1536 > unit_pos[0] >= 384 and 832 > unit_pos[1] >= 192:
                        if el.path == "towers":
                            if is_free(el):
                                if level.money - tower_costs[el.unit_inside] >= 0:  # Это пиздец, но оно работает. Придумаете лучше -- переделаете
                                    Tower(el.unit_inside, unit_pos)
                                    if not level.cheat:
                                        level.money -= tower_costs[el.unit_inside]
                                    el.kd_time = el.default_kd_time

                        if el.path == "shovel":
                            for obj in [*towers_group, *nekusaemie_group]:           # Сразу по 2 группам
                                if obj.rect.collidepoint(el.rect.centerx, el.rect.centery):
                                    if not level.cheat:
                                        level.money += tower_costs[obj.name] // 2
                                    if hasattr(obj, "bullet"):
                                        obj.bullet.kill()
                                    obj.kill()

with open("save.txt", "w", encoding="utf-8") as file:
    new_game = True
    file.write(just_text + "\n")
    file.write("new_game = " + str(new_game) + "\n")
    file.write("unlocked_levels = " + str(unlocked_levels))
