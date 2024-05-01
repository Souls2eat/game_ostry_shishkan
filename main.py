from pygame import *
from random import randint, choice

init()

clock = time.Clock()
screen = display.set_mode((1600, 900))
display.set_caption("game_ostry_shishkan")
screen.fill((255, 255, 255))

bg = image.load(f"images/maps/map1.png").convert_alpha()
menu = image.load("images/menu/pause_menu.png").convert_alpha()
main_menu = image.load("images/menu/main_menu.png").convert_alpha()
level_select_menu = image.load("images/menu/level_select_menu.png").convert_alpha()
level_box = image.load("images/menu/level_box.png").convert_alpha()
tower_select_menu = image.load("images/menu/tower_select_menu.png").convert_alpha()

font20 = font.Font("fonts/ofont.ru_Nunito.ttf", 20)
font30 = font.Font("fonts/ofont.ru_Nunito.ttf", 30)
font40 = font.Font("fonts/ofont.ru_Nunito.ttf", 40)
font60 = font.Font("fonts/ofont.ru_Nunito.ttf", 60)

game_name = font60.render("GAME_OSTRY_SHISHIKAN", True, (255, 255, 255))  # GAME_OSTRY_SHISHIKAN
game_state = "main_menu"
last_game_state = game_state
selected_towers = []
buttons_group = []


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
        for sprite in self.sprites():
            if hasattr(sprite, "image2"):
                sprite.draw2(surf)


class Level:
    def __init__(self, level_number, level_time, time_to_spawn, start_money):
        self.image = image.load(f"images/maps/map{level_number}.png").convert_alpha()
        self.current_level = level_number
        self.money = self.start_money = start_money
        self.state = "not_run"
        self.level_time = self.start_level_time = level_time
        self.start_time_to_spawn = self.time_to_spawn = time_to_spawn

    @staticmethod
    def random_spawn_enemies():
        line_cords = [192, 320, 448, 576, 704]
        enemy_sprites = ["josky", "popusk", "sigma"]
        enemy_y_cord = choice(line_cords)
        enemy_name = choice(enemy_sprites)
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
        self.money = self.start_money
        self.time_to_spawn = self.start_time_to_spawn

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
        if self.time_to_spawn > 0:
            self.time_to_spawn -= 1
        else:
            self.time_to_spawn = self.start_time_to_spawn
            self.random_spawn_enemies()

        if self.state == "not_run":
            self.state = self.spawn()

        if self.level_time > 0:
            self.level_time -= 1
            return "run"
        else:
            return "level_complited"


class Tower(sprite.Sprite):
    def __init__(self, unit, pos):
        super().__init__(towers_group, all_sprites_group)
        self.image = image.load(f"images/towers/{unit}.png").convert_alpha()
        self.is_dead = False

        self.name = unit
        self.rect = self.image.get_rect(topleft=(pos))
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
            self.cost = 10

        if self.name == 'boomchick':  
            self.hp = 200
            self.atk = 20  # типа по кому попадёт получит 40 а остальные по 20
            self.bullet_speed_x = 4
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = 85
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''
            self.cost = 20

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
            self.cost = 20

        if self.name == 'thunder':
            self.hp = 100
            self.atk = 30
            self.bullet_speed_x = 7
            self.bullet_speed_y = 3
            self.basic_attack_cooldown = 200
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''
            self.cost = 15

        if self.name == 'zeus':
            self.hp = 100
            self.atk = 100
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = 225
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''
            self.cost = 20

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
            self.cost = 10

        if self.name == 'parasitelniy':
            self.hp = 2200
            self.max_hp = 2200
            self.atk = 10
            self.basic_attack_cooldown = 150
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''
            self.have_parasite = sprite.Group()
            self.cost = 20

        if self.name == 'spike':  
            self.hp = 1
            self.atk = 20
            self.basic_attack_cooldown = 75
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''
            self.remove(towers_group)
            self.add(nekusaemie_group)
            self.cost = 10

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
            self.cost = 25

        if self.name == 'terpila':  # циферки поменять
            self.hp = 6000
            self.cost = 30

        if self.name == 'oh_shit_i_am_sorry__barrier_mag':
            self.hp = 1500
            self.barrier_hp = 3000
            self.basic_barrier_cooldown = 750 #3375
            self.barrier_cooldown = 0
            self.cost = 20

        if self.name == 'davalka':
            self.hp = 200
            self.skolko_deneg_dast = 30
            self.basic_davanie_cooldown = 900
            self.davanie_cooldown = self.basic_davanie_cooldown
            self.cost = 20
            self.time_on_screen = 0  # это для плюс денег

        if self.name == 'matricayshon':
            self.hp = 500
            for i in range(9):
                self.buff_x = 1+(i%3)*128-128
                self.buff_y = 1+(i//3)*128-128
                self.buff = Buff("mat", self.rect.x + self.buff_x, self.rect.y + self.buff_y)
            self.cost = 30

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

            if self.name == 'thunder':
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

            if self.name == 'davalka' or self.name == 'oh_shit_i_am_sorry__barrier_mag':
                self.dayot()
            

            if self.hp <= 0:
                self.is_dead = True
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

    def dayot(self):
        if self.name == 'davalka':
            if self.davanie_cooldown <= 0:
                self.davanie_cooldown = self.basic_davanie_cooldown
                level.money += self.skolko_deneg_dast
                self.plus_dengi = font20.render('+30', True, (0, 70, 200))
                self.time_on_screen = 50

        if self.name == 'oh_shit_i_am_sorry__barrier_mag': 
            if self.barrier_cooldown <= 0:
                self.barrier_cooldown = self.basic_barrier_cooldown
                self.best_x = self
                for tower in towers_group: # решил не добавлять некусаемых тк врядли кто то будет ставить барьер на шипы, но я чувствую что с пукишем я задолбаюсь
                    if tower.rect.y == self.rect.y and tower.rect.x > self.best_x.rect.x:
                        self.best_x = tower
                self.best_x.have_barrier = True
                self.barrier = Parasite('oh_shit_i_am_sorry__barrier_mag__sobstvenno_govorya_barrier', self.best_x.rect.centerx, self.best_x.rect.centery, '', 0, self.best_x, self)


    def update(self):
        self.delat_chtoto()

        if self.name == 'fire_mag' or self.name == 'kopitel' or self.name == 'thunder' or self.name == 'zeus' or self.name == 'boomchick' or self.name == 'parasitelniy' or self.name == 'spike' or self.name == 'pukish':
            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1

        if self.name == 'pukish':
            if self.attack_cooldown2 > 0:
                self.attack_cooldown2 -= 1

        if self.name == 'oh_shit_i_am_sorry__barrier_mag' and self.barrier not in all_sprites_group:
            if self.barrier_cooldown > 0:
                self.barrier_cooldown -= 1

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
            self.parent.attack_cooldownwn = 375

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


    def prisasivanie(self):
        if self.parent not in all_sprites_group or self.owner not in all_sprites_group:
            self.kill()
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

            
    def update(self):
        self.prisasivanie()
        
        if self.name == 'sosun':
            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1


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
                    if tower.name == 'fire_mag' or tower.name == 'kopitel' or tower.name == 'thunder' or tower.name == 'yascerica' or tower.name == 'zeus' or tower.name == 'boomchick' or tower.name == 'parasitelniy':
                        tower.basic_attack_cooldown //= 2
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
                if tower.rect.collidepoint(self.rect.centerx, self.rect.centery):
                    self.attack_cooldown -= 1
                    self.stop = True
                    if self.attack_cooldown <= 0:
                        self.attack_cooldown = 75
                        if tower.have_barrier == True:
                            for barrier in parasites_group:
                                if barrier.name == 'oh_shit_i_am_sorry__barrier_mag__sobstvenno_govorya_barrier' and barrier.owner == tower:
                                    barrier.hp -= self.atk
                        else:
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
        self.rect = self.image.get_rect(topleft=self.pos)
        self.path = path
        self.unit_inside = unit_inside
        self.is_move = False

        if self.path == "towers":
            unit = Tower(self.unit_inside, (0, 0))
            if hasattr(unit, "cost"):
                self.cost = unit.cost
                self.image2 = font30.render(str(self.cost), True, (255, 255, 255))
                self.rect2 = self.image2.get_rect(topleft=(self.default_pos[0] - 49, self.default_pos[1] + 4))
            if hasattr(unit, "bullet"):
                unit.bullet.kill()
            unit.kill()
            for buff in buffs_group:
                buff.kill()

    def move(self):
        self.image = image.load(f"images/{self.path}/{self.unit_inside}.png").convert_alpha()
        self.pos = mouse.get_pos()
        self.rect = self.image.get_rect(center=self.pos)

    def back_to_default(self):
        self.image = image.load(f"images/{self.path}/images_inside/{self.unit_inside}_inside.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=self.default_pos)
        self.pos = self.default_pos

    def draw2(self, surface):
        surface.blit(self.image2, self.rect2)

    def update(self):
        if self.is_move:
            self.move()
        if self.is_move is not True:
            self.back_to_default()

        if hasattr(self, "text"):
            screen.blit(self.text, (self.default_pos[0] - 49, self.default_pos[1] + 4))


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

    def click(self, surf, mouse_pos, pos, col=(255, 255, 255)):
        if self.data_type == "text":
            self.image = self.font.render(self.text, font, col)   # По дефолту цвет текста белый. Я ебал по 50 раз писать одно и тоже
        self.pos = pos
        self.rect = self.image.get_rect(topleft=self.pos)
        self.rect = self.image.get_rect(topleft=pos)
        if not self.rect.collidepoint(mouse_pos):
            self.pushed = False
        if self.rect.collidepoint(mouse_pos):
            if mouse.get_pressed()[0] == 1 and not self.pushed:
                self.pushed = True
        if mouse.get_pressed()[0] == 0 and self.pushed:
            self.pushed = False
            return True

        surf.blit(self.image, self.rect)
        if self.ok is True:
            surf.blit(image.load("images/other/ok.png").convert_alpha(), self.rect)


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
    def __init__(self, text, pos, alert_time, font=font60, col=(255, 0, 0)):
        super().__init__(alert_group)
        self.image = font.render(text, True, col)
        self.rect = self.image.get_rect(topleft=pos)
        self.alert_time = alert_time

    def update(self):
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


def add_to_slots_slots(i, *blocked_slots):
    if tower_select_buttons[i].ok:
        tower_select_buttons[i].ok = False
        selected_towers.remove(tower_select_buttons[i].unit_inside)
        for ui in ui_group:
            if ui.unit_inside == tower_select_buttons[i].unit_inside:
                ui.kill()

    elif len(selected_towers) <= 6 - len(blocked_slots):
        tower_select_buttons[i].ok = True
        if blocked_slots:
            UI((94, first_empty_slot(*blocked_slots)), "towers", tower_select_buttons[i].unit_inside)
        else:
            UI((94, first_empty_slot()), "towers", tower_select_buttons[i].unit_inside)
        selected_towers.append(tower_select_buttons[i].unit_inside)
    else:
        Alert("Закончились пустые слоты", (404, 580), 75)


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
            level

    mouse_pos = mouse.get_pos()

    if game_state == "main_menu":

        screen.blit(main_menu, (0, 0))
        screen.blit(game_name, (501, 10))

        if new_game_button.click(screen, mouse_pos, (30, 460)):                         # 1 кнопка
            last_game_state = game_state
            game_state = "tower_select"  # новая игра
            new_game = False
            level = levels[0]
            level.clear()
            level.state = "not_run"
        if new_game:
            if resume_button.click(screen, mouse_pos, (30, 540), col=(130, 130, 130)):  # 2 кнопка серая
                Alert("<- Тыкай новую игру", (500, 460), 75)
        else:
            if resume_button.click(screen, mouse_pos, (30, 540)):                       # 2 кнопка белая
                last_game_state = game_state
                game_state = "run"
        if level_select_button.click(screen, mouse_pos, (30, 620)):                     # 3 кнопка
            game_state = "level_select"
        if settings_button.click(screen, mouse_pos, (30, 700)):                         # 4 кнопка
            last_game_state = game_state
            game_state = "settings_menu"   # Экран под землю
        if quit_button.click(screen, mouse_pos, (30, 780)):                             # 5 кнопка
            running = False

    if game_state == "level_select":
        screen.blit(main_menu, (0, 0))
        screen.blit(level_select_menu, (320, 150))

        for i in range(len(level_box_buttons)):
            if i <= 3:
                if level_box_buttons[i].click(screen, mouse_pos, (48 + 320 + 208 * i, 198)):     # +320, 150   (368, 198)
                    if not level_box_buttons[i].closed:
                        new_game = False
                        level = levels[i]
                        level.clear()
                        game_state = "tower_select"
                        level.current_level = i+1
                if not level_box_buttons[i].closed:
                    screen.blit(font60.render(str(i+1), True, (255, 255, 255)), (108 + 320 + 208 * i, 228))  # + 380, 40

            elif i <= 7:
                if level_box_buttons[i].click(screen, mouse_pos, (48 + 320 + 208 * (i-4), 406)):
                    if not level_box_buttons[i].closed:
                        new_game = False
                        level = levels[i]
                        level.clear()
                        game_state = "tower_select"
                        level.current_level = i+1
                if not level_box_buttons[i].closed:
                    screen.blit(font60.render(str(i+1), True, (255, 255, 255)), (108 + 320 + 208 * (i-4), 438))
        # draw.line(level_select_menu, (255, 255, 255), (900, 48), (900, 552), 15)
        if back_button.click(screen, mouse_pos, (709, 620)):
            game_state = last_game_state

    if game_state != "main_menu" and game_state != "main_settings_menu" and game_state != "level_select":
        screen.blit(bg, (0, 0))     # level.image
        screen.blit(font40.render(str(level.current_level) + " уровень", True, (255, 255, 255)), (893, 30))
        screen.blit(font40.render(str(level.money), True, (0, 0, 0)), (88, 53))
        all_sprites_group.draw(screen)
        all_sprites_group.draw2(screen)

    if game_state == "run":
        game_state = level.update()
        # ---- ok
        if pause_button.click(screen, mouse_pos, (1550, 30)):
            last_game_state = game_state
            if game_state == "paused":
                game_state = "run"
            elif game_state == "run":
                game_state = "paused"

    if game_state == "paused":
        screen.blit(menu, (480, 250))
        screen.blit(font60.render("Пауза", True, (193, 8, 42)), (700, 280))
        if resume_button.click(screen, mouse_pos, (614, 360)):
            last_game_state = game_state
            game_state = "run"
        if settings_button.click(screen, mouse_pos, (642, 440)):
            last_game_state = game_state
            game_state = "settings_menu"
        if main_menu_button.click(screen, mouse_pos, (567, 520)):
            last_game_state = game_state
            game_state = "main_menu"
        if pause_button.click(screen, mouse_pos, (1550, 30)):
            last_game_state = game_state
            if game_state == "paused":
                game_state = "run"
            elif game_state == "run":
                game_state = "paused"

    if game_state == "tower_select":
        screen.blit(tower_select_menu, (320, 150))
        blocked_slots = []  # если надо, чтобы не во все слоты можно было пихать башни

        if level.current_level == 1:            # |
            blocked_slots = []               # | > Жестки пример
        if level.current_level == 2:            # |
            blocked_slots = [160, 352]          # |

        for i in range(len(tower_select_buttons)):
            if i < 6:
                if tower_select_buttons[i].click(screen, mouse_pos, (350 + i * 158, 180)):
                    add_to_slots_slots(i, *blocked_slots)
            elif i < 12:
                if tower_select_buttons[i].click(screen, mouse_pos, (350 + (i-6) * 158, 334)):
                    add_to_slots_slots(i, *blocked_slots)
            elif i < 18:
                if tower_select_buttons[i].click(screen, mouse_pos, (350 + (i-12) * 158, 488)):
                    add_to_slots_slots(i, *blocked_slots)
        if start_level_button.click(screen, mouse_pos, (567, 650)):
            game_state = "run"
            level.clear("ui_group")
            game_state = "run"
        ui_group.draw(screen)

    if game_state == "settings_menu":
        if last_game_state == "main_menu":
            screen.blit(main_menu, (0, 0))
            screen.blit(game_name, (501, 10))
        screen.blit(menu, (480, 250))
        if back_button.click(screen, mouse_pos, (709, 520)):
            game_state = last_game_state

    if game_state == "death":
        screen.blit(menu, (480, 250))
        screen.blit(font60.render("Вы проиграли", True, (193, 8, 42)), (590, 280))
        if settings_button.click(screen, mouse_pos, (642, 360)):
            last_game_state = game_state
            game_state = "settings_menu"
        if restart_button.click(screen, mouse_pos, (582, 440)):
            last_game_state = game_state
            game_state = "run"
            level.state = "not_run"
            level.money = level.start_money
            level.clear("ui_group")
        if main_menu_button.click(screen, mouse_pos, (567, 520)):
            last_game_state = game_state
            game_state = "main_menu"
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
            tower_select_button13]

levels = [Level(1, 100000, 375, 300), Level(2, 750, 150, 300)]
level = levels[0]


running = True
while running:

    mouse_pos = mouse.get_pos()

    menu_positioning()
    alert_group.update()
    alert_group.draw(screen)

    for bullet in bullets_group:
        if bullet.name == 'ls' or bullet.name == 'explosion':
            for enemy in enemies_group:
                if sprite.collide_rect(enemy, bullet) and enemy.hp > 0:
                    enemy.hp -= bullet.damage
            bullet.remove(bullets_group)

    for enemy in enemies_group:
        if enemy.rect.x <= 150:
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
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE and game_state == "run" or game_state == "paused" or game_state == "settings_menu":
                if game_state == "run":
                    game_state = "paused"
                else:
                    game_state = "run"
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
                                if level.money - unit.cost < 0:  # Это пиздец, но оно работает. Придумаете лучше -- переделаете
                                    unit.kill()
                                    if hasattr(unit, "bullet"):
                                        unit.bullet.kill()
                                else:
                                    level.money -= unit.cost
                        if el.path == "shovel":
                            for tower in towers_group:
                                if tower.rect.collidepoint(el.rect.centerx, el.rect.centery):
                                    level.money += tower.cost // 2
                                    if hasattr(tower, "bullet"):
                                        tower.bullet.kill()
                                    tower.kill()
                            for nekusaemiy in nekusaemie_group:
                                if nekusaemiy.rect.collidepoint(el.rect.centerx, el.rect.centery):
                                    level.money += nekusaemiy.cost // 2
                                    nekusaemiy.kill()


with open("save.txt", "w", encoding="utf-8") as file:
    new_game = True
    file.write(just_text + "\n")
    file.write("new_game = " + str(new_game) + "\n")
    file.write("unlocked_levels = " + str(unlocked_levels))
