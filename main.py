from pygame import *  # мне не прикольно каждый раз писать pygame. и не говорите мне что так легче, это полный кал

clock = time.Clock()
screen = display.set_mode((1600, 900))
display.set_caption("Супер-мега игра")
screen.fill((255, 255, 255))
img = image.load("images/map2.png").convert_alpha()


class SpriteGame(sprite.Sprite):
    def __init__(self, player_image, x, y):
        super().__init__()
        self.image = image.load(player_image)
        self.player_image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Tower(SpriteGame): # башня, она же "растение"
    def __init__(self, player_image, x, y, group, name):
        super().__init__(player_image, x, y)
        self.is_dead = False
        self.group = group
        self.name = name



        # СТАТЫ начало
        if self.group == 'attack':  # пример из пвз: горохострел
            
            if self.name == 'strelyatel':  # циферки поменять
                self.hp = 200
                self.atk = 20
                self.bullet_speed_x = 5
                self.bullet_speed_y = 0
                self.attack_cooldown = 75
                self.damage_type = ''

            if self.name == 'thunder':
                self.hp = 100
                self.atk = 30
                self.bullet_speed_x = 7
                self.bullet_speed_y = 3
                self.attack_cooldown = 200
                self.damage_type = ''

            if self.name == 'zeus':
                self.hp = 100
                self.atk = 10
                self.bullet_speed_x = 0
                self.bullet_speed_y = 0
                self.attack_cooldown = 150
                self.damage_type = ''

        elif self.group == 'defend':  # пример из пвз: стеноорех
            if self.name == 'terpila':  # циферки поменять
                self.hp = 5000
                self.atk = 0
                self.bullet_speed = 0
                self.attack_cooldown = 0
                self.damage_type = ''

        elif self.group == 'dengi_davatel':  # пример из пвз: подсолнух
            pass

        elif self.group == 'instant':  # пример из пвз: вишня бомба 
            pass
        # СТАТЫ конец


    def delat_chtoto(self): # тут надо будет написать условие при котором башня стреляет
        if self.is_dead != True:
            if self.name == 'strelyatel':
                for enemy in enemies_group:
                    if enemy.rect.y == self.rect.y:
                        self.is_shooting()
            if self.name == 'thunder':
                for enemy in enemies_group:
                    if enemy.rect.y == self.rect.y or enemy.rect.y == self.rect.y + 128 or enemy.rect.y == self.rect.y - 128:
                        self.is_shooting()
            if self.name == 'zeus':
                for enemy in enemies_group:
                    if enemy.rect.y == self.rect.y:
                        self.is_shooting()

            if self.hp <= 0:
                self.is_dead = True
                self.kill()

    
    def is_shooting(self):
        #keys = key.get_pressed() если нужно будет затестить по нажатию
        if self.group == 'attack':  
            
            if self.name == 'strelyatel':
                if self.attack_cooldown <= 0:
                    self.attack_cooldown = 75
                    self.bullet = Bullet("images/blue_bullet.png", self.rect.centerx-8, self.rect.centery-8, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'default',  self)
                    all_sprites_group.add(self.bullet)
                    bullets_group.add(self.bullet)

            if self.name == 'thunder':
                if self.attack_cooldown <= 0:
                    self.attack_cooldown = 200
                    self.bullet = Bullet("images/Frigl_bul.png", self.rect.centerx - 8, self.rect.centery - 8,
                                         self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'hrom',
                                         self)
                    all_sprites_group.add(self.bullet)
                    bullets_group.add(self.bullet)

                    self.bullet = Bullet("images/Frigl_bul.png", self.rect.centerx - 8, self.rect.centery - 8,
                                         self.damage_type, self.atk, self.bullet_speed_x, 0, 'hrom',
                                         self)
                    all_sprites_group.add(self.bullet)
                    bullets_group.add(self.bullet)

                    self.bullet = Bullet("images/Frigl_bul.png", self.rect.centerx - 8, self.rect.centery - 8,
                                         self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y * -1, 'hrom',
                                         self)
                    all_sprites_group.add(self.bullet)
                    bullets_group.add(self.bullet)

            if self.name == 'zeus':
                if self.attack_cooldown <= 0:
                    self.attack_cooldown = 225
                    self.bullet = Bullet("images/Laser.png", self.rect.centerx - 8, self.rect.centery - 8,
                                        self.damage_type, self.atk, self.bullet_speed_x, 0,
                                        'ls', self)
                    all_sprites_group.add(self.bullet)
                    bullets_group.add(self.bullet)


    def update(self):
        self.delat_chtoto()
        

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1


class Bullet(SpriteGame): 
    def __init__(self, player_image, x, y, damage_type, damage, speed_x, speed_y, name, parent):
        super().__init__(player_image, x, y)
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

        
        
        if self.rect.x >= 1700:
            self.kill()

    def update(self):
        self.bullet_movement()

        if self.name == 'ls':
            if self.off > 0:
                self.off -= 1

class Enemy(SpriteGame):  # враг, он же "зомби"
    def __init__(self, player_image, x, y, group, name):
        super().__init__(player_image, x, y)
        self.is_dead = False
        self.group = group
        self.name = name
        self.stop = False

        # СТАТЫ начало
        if self.group == 'penis':  # тайное послание ---> зутшы
            
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

            self.stop = False # нужно чтобы в случае колизии останавливался, а если колизии не будет то шёл дальше. ОБЯЗАТЕЛЬНО ПОСЛЕ ПРОВЕРКИ СТОПА НО ПЕРЕД ПРОВЕРКОЙ КОЛИЗИИ
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

tower1 = Tower("images/slime_plr.png", 384, 320, 'attack', 'strelyatel')
tower2 = Tower("images/slime_plr.png", 1152, 320, 'attack', 'strelyatel')
tower3 = Tower("images/slime_plr.png", 384, 576, 'attack', 'strelyatel')
tower4 = Tower("images/terpila.png", 1152, 576, 'defend', 'terpila')
fury = Tower('images/Thunder(fury).png', 384, 192, 'attack', 'thunder')
orochi = Tower('images/zeus.png', 384, 320, 'attack', 'zeus',)

enemy1 = Enemy("images/goblin_en_flip.png", 1408, 320, 'penis', 'popusk')
enemy4 = Enemy("images/goblin_en_flip.png", 1608, 320, 'penis', 'popusk')
enemy2 = Enemy("images/blue_bullet.png", 1408, 192, 'penis', 'josky')
enemy3 = Enemy("images/yellow_bullet.png", 1408, 576, 'penis', 'sigma')


all_sprites_group = sprite.Group()
bullets_group = sprite.Group()
enemies_group = sprite.Group()
towers_group = sprite.Group()

all_sprites_group.add( tower4, tower1, tower2, tower3, fury, orochi, enemy1, enemy2, enemy3, enemy4)#tower1, tower2, tower3, fury,
enemies_group.add(enemy1, enemy2, enemy3, enemy4)
towers_group.add( tower4, tower1, tower2, tower3, fury, orochi)

running = True

while running:

    screen.blit(img, (0, 0))

    all_sprites_group.update()
    all_sprites_group.draw(screen)

    for bullet in bullets_group:
        if bullet.name == 'ls':
            for enemy in enemies_group:
                enemy.hp -= bullet.damage
            bullet.remove(bullets_group)
        for enemy in enemies_group:
            if sprite.collide_rect(enemy, bullet) and enemy.hp > 0:
                if bullet.name == 'default':
                    enemy.hp -= bullet.damage
                    bullet.kill()
                if bullet.name == 'hrom':
                    enemy.hp -= bullet.damage
                    bullet.kill()







    clock.tick(75)
    display.update()

    for e in event.get():
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            running = False
        if e.type == QUIT:
            running = False