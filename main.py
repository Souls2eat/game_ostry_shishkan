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
                self.hp = 100
                self.atk = 20
                self.bullet_speed = 5
                self.attack_cooldown = 75
                self.damage_type = ''

        elif self.group == 'defend':  # пример из пвз: стеноорех
            pass

        elif self.group == 'dengi_davatel':  # пример из пвз: подсолнух
            pass

        elif self.group == 'instant':  # пример из пвз: вишня бомба 
            pass
        # СТАТЫ конец


    def delat_chtoto(self):# тут надо будет написать условие при котором башня стреляет
        self.is_shooting()

    
    def is_shooting(self):
        #keys = key.get_pressed() если нужно будет затестить по нажатию
        if self.attack_cooldown <= 0:
            self.attack_cooldown = 75
            self.bullet = Bullet("images/blue_bullet.png", self.rect.centerx-8, self.rect.centery-8, self.damage_type, self.atk, self.bullet_speed)
            all_sprites_group.add(self.bullet)
            bullets_group.add(self.bullet)

    def update(self):
        self.delat_chtoto()
        

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1


class Bullet(SpriteGame): 
    def __init__(self, player_image, x, y, damage_type, damage, speed):
        super().__init__(player_image, x, y)
        self.is_dead = False
        self.damage_type = damage_type
        self.damage = damage
        self.speed = speed

    def bullet_movement(self):
        self.rect.x += self.speed

        if self.rect.x >= 1700:
            self.kill()

    def update(self):
        self.bullet_movement()

class Enemy(SpriteGame):  # враг, он же "зомби"
    def __init__(self, player_image, x, y, group, name):
        super().__init__(player_image, x, y)
        self.is_dead = False
        self.group = group
        self.name = name


        # СТАТЫ начало
        if self.group == 'penis':  # тайное послание ---> зутшы
            
            if self.name == 'popusk':  # циферки поменять
                self.hp = 200
                self.atk = 5
                self.speed = 1
        # СТАТЫ конец

    def delat_chtoto(self):
        if self.is_dead != True:
            self.rect.x -= self.speed

            if self.hp <= 0:
                self.is_dead = True
        
    def update(self):
        self.delat_chtoto()


tower1 = Tower("images/slime_plr.png", 50, 300, 'attack', 'strelyatel')
enemy1 = Enemy("images/goblin_en_flip.png", 1500, 300, 'penis', 'popusk')

all_sprites_group = sprite.Group()
bullets_group = sprite.Group()
enemies_group = sprite.Group()

all_sprites_group.add(tower1, enemy1)
enemies_group.add(enemy1)
running = True
while running:

    screen.blit(img, (0, 0))

    all_sprites_group.update()
    all_sprites_group.draw(screen)
    

    for enemy in enemies_group:
            for bullet in bullets_group:
                if sprite.collide_rect(enemy, bullet) and enemy.hp > 0:
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
        

