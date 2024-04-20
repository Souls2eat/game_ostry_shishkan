from pygame import * 
from random import randint

clock = time.Clock()
screen = display.set_mode((1600, 900))
display.set_caption("Супер-мега игра")
screen.fill((255, 255, 255))
img = image.load("images/map2.png").convert_alpha()


class Tower(sprite.Sprite):  # башня, она же "растение"
    def __init__(self, unit, pos):
        super().__init__(towers_group, all_sprites_group)
        self.image = image.load(f"images/{unit}.png").convert_alpha()
        self.is_dead = False

        self.name = unit
        self.rect = self.image.get_rect(topleft=(pos))

        # СТАТЫ начало
            
        if self.name == 'strelyatel':  # циферки поменять
            self.hp = 200
            self.atk = 20
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = 75
            self.damage_type = ''

        if self.name == 'kopitel':
            self.hp = 200
            self.atk = 25
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.attack_cooldown = 100
            self.damage_type = ''
            self.nakopleno = 0
            self.max_nakopit = 9

        if self.name == 'thunder':
            self.hp = 100
            self.atk = 30
            self.bullet_speed_x = 7
            self.bullet_speed_y = 3
            self.attack_cooldown = 200
            self.damage_type = ''

        if self.name == 'zeus':
            self.hp = 100
            self.atk = 40
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.attack_cooldown = 150
            self.damage_type = ''


        if self.name == 'terpila':  # циферки поменять
            self.hp = 5000
            self.atk = 0
            self.bullet_speed = 0
            self.attack_cooldown = 0
            self.damage_type = ''

        # СТАТЫ конец


    def delat_chtoto(self): # тут надо будет написать условие при котором башня стреляет
        if self.is_dead != True:
            if self.name == 'strelyatel' or self.name == 'zeus':
                for enemy in enemies_group:
                    if enemy.rect.y == self.rect.y:
                        self.is_shooting()

            if self.name == 'kopitel':
                    self.is_shooting()

            if self.name == 'thunder':
                for enemy in enemies_group:
                    if enemy.rect.y == self.rect.y or enemy.rect.y == self.rect.y + 128 or enemy.rect.y == self.rect.y - 128:
                        self.is_shooting()

            if self.hp <= 0:
                self.is_dead = True
                self.kill()


    def is_shooting(self):
        #keys = key.get_pressed() если нужно будет затестить по нажатию
            
        if self.name == 'strelyatel':
            if self.attack_cooldown <= 0:
                self.attack_cooldown = 75
                self.bullet = Bullet("blue_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'default', self)


        if self.name == 'kopitel':
            if self.attack_cooldown <= 0:
                self.attack_cooldown = 100
                if self.nakopleno < self.max_nakopit:
                    self.joska_schitayu_x = 64*(1 + (self.nakopleno//3))
                    self.joska_schitayu_y = 32*(self.nakopleno%3)+20
                    self.spear_or_sword = randint(0, 1)
                    if self.spear_or_sword == 0:
                        self.bullet = Bullet("light_spear", self.rect.centerx-self.joska_schitayu_x, self.rect.y+self.joska_schitayu_y, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'kopilka', self)
                    if self.spear_or_sword == 1:
                        self.bullet = Bullet("light_sword", self.rect.centerx-self.joska_schitayu_x, self.rect.y+self.joska_schitayu_y, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'kopilka', self)
                    
                    self.nakopleno += 1

        if self.name == 'thunder':
            if self.attack_cooldown <= 0:
                self.attack_cooldown = 200
                self.bullet = Bullet("Frigl_bul", self.rect.centerx - 8, self.rect.centery - 8,
                                     self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'hrom',
                                     self)


                self.bullet = Bullet("Frigl_bul", self.rect.centerx - 8, self.rect.centery - 8,
                                     self.damage_type, self.atk, self.bullet_speed_x, 0, 'hrom',
                                     self)


                self.bullet = Bullet("Frigl_bul", self.rect.centerx - 8, self.rect.centery - 8,
                                     self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y * -1, 'hrom',
                                     self)


        if self.name == 'zeus':
            if self.attack_cooldown <= 0:
                self.attack_cooldown = 225
                self.bullet = Bullet("Laser", self.rect.centerx + 640, self.rect.centery,
                                    self.damage_type, self.atk * 10, self.bullet_speed_x, 0,
                                    'ls', self)


            
    def update(self):
        self.delat_chtoto()
        

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1


class Bullet(sprite.Sprite):
    def __init__(self, bullet_sprite, x, y, damage_type, damage, speed_x, speed_y, name, parent):
        super().__init__(all_sprites_group, bullets_group)
        self.image = image.load(f"images/{bullet_sprite}.png").convert_alpha()
        self.rect = self.rect = self.image.get_rect(center=(x, y))
        self.is_dead = False
        self.damage_type = damage_type
        self.damage = damage
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.name = name
        self.parent = parent

        if self.name == 'ls':
            self.off = 75

    def bullet_movement(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.name == 'hrom':
            if (self.parent.rect.centery - self.rect.centery) >= 128 or (self.rect.centery - self.parent.rect.centery) >= 128:
                self.speed_y = 0
        
        if self.name == 'ls':
            if self.off <= 0:
                self.off = 75
                self.kill()

        if self.name == 'kopilka':
            for enemy in enemies_group:
                if enemy.rect.y == self.parent.rect.y:
                    self.speed_x = 7
                    self.parent.nakopleno = 0
                    self.parent.attack_cooldown = 100
        
        if self.rect.x >= 1700:
            self.kill()

    def update(self):
        self.bullet_movement()

        if self.name == 'ls':
            if self.off > 0:
                self.off -= 1

class Enemy(sprite.Sprite):  # враг, он же "зомби"
    def __init__(self, name, x, y):
        super().__init__(all_sprites_group, enemies_group)
        self.image = image.load(f"images/{name}.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
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

            if self.hp <= 0:
                self.is_dead = True
                self.kill()
        
    def update(self):
        self.delat_chtoto()



class Slot(sprite.Sprite):
    def __init__(self, pos, unit_inside):
        super().__init__(slots_group)
        self.image = image.load(f"images_inside/{unit_inside}_inside.png").convert_alpha()
        self.pos = pos
        self.default_pos = pos
        self.rect = self.image.get_rect(topleft=(self.pos))
        self.is_move = False
        self.unit_inside = unit_inside

    def move(self):
        self.image = image.load(f"images/{self.unit_inside}.png").convert_alpha()
        self.pos = mouse.get_pos()
        self.rect = self.image.get_rect(center=(self.pos))

    def back_to_default(self):
        self.image = image.load(f"images_inside/{self.unit_inside}_inside.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.default_pos))

    def update(self):
        if self.is_move == True:
            self.move()
        if self.is_move == False:
            self.back_to_default()


class GameMapUnits(sprite.Sprite):
    def __init__(self, pos, unit_inside):
        super().__init__(game_map_group)
        self.image = image.load(f"images_inside/{unit_inside}_inside.png").convert_alpha()
        self.pos = pos
        self.rect = self.image.get_rect()


all_sprites_group = sprite.Group()
bullets_group = sprite.Group()
enemies_group = sprite.Group()
towers_group = sprite.Group()


unit = Tower("zeus", (384, 704))
unit = Tower("kopitel", (384, 192))

enemy = Enemy("popusk", 1408, 320),\
        Enemy("sigma", 1408, 192),\
        Enemy("josky", 1408, 576),\
        Enemy("popusk", 1208, 576),\
        Enemy("popusk", 1508, 576)




game_map_group = sprite.Group()
slots_group = sprite.Group()
slot = Slot((94, 160), "t"),\
       Slot((94, 256), "thunder"),\
       Slot((94, 352), "terpila"),\
       Slot((94, 448), "kopitel")
       # Slot((34, 640)),\
       # Slot((34, 736))


all_sprites_group.add(enemies_group, slots_group, game_map_group, towers_group)


running = True

while running:

    screen.blit(img, (0, 0))

    all_sprites_group.update()
    all_sprites_group.draw(screen)
    

    for bullet in bullets_group:

        if bullet.name == 'ls':
            for enemy in enemies_group:
                if sprite.collide_rect(enemy, bullet) and enemy.hp > 0:
                    enemy.hp -= bullet.damage
            bullet.remove(bullets_group)

        for enemy in enemies_group:
            if sprite.collide_rect(enemy, bullet) and enemy.hp > 0:
                if bullet.name == 'default' or bullet.name == 'hrom' or bullet.name == 'kopilka':
                    enemy.hp -= bullet.damage
                    bullet.kill()



    clock.tick(75)
    display.update()

    for e in event.get():
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            running = False
        if keys[K_SPACE]:
            enemy6 = Enemy("popusk", 1508, 704)
            all_sprites_group.add(enemy6)
            enemies_group.add(enemy6)
        if e.type == QUIT:
            running = False
        # misha
        if e.type == MOUSEBUTTONDOWN:
            mouse_pos = mouse.get_pos()
            for slot in slots_group:
                if slot.rect.collidepoint(mouse_pos):
                    slot.is_move = True
        if e.type == MOUSEBUTTONUP:
            mouse_pos = mouse.get_pos()
            for slot in slots_group:
                if slot.rect.collidepoint(mouse_pos):
                    slot.is_move = False

                    unit_pos = (384 + ((mouse_pos[0] - 384) // 128) * 128), (192 + ((mouse_pos[1] - 192) // 128) * 128)
                    if 1536 >= unit_pos[0] >= 384 and 832 >= unit_pos[1] >= 192:

                        print(slot.unit_inside, unit_pos)
                        unit = Tower(slot.unit_inside, unit_pos)
