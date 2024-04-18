from pygame import * #мне не прикольно каждый раз писать pygame. и не говорите мне что так легче, это полный кал

clock = time.Clock()
screen = display.set_mode((1600, 900))
display.set_caption("Супер-мега игра")
screen.fill((255, 255, 255))
img = image.load("map2.png").convert_alpha()
class Sprite_game(sprite.Sprite):
    def __init__(self, player_image, x, y):
        super().__init__()
        self.image = image.load(player_image)
        self.player_image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Tower(Sprite_game):#башня, она же "растение"
    def __init__(self, player_image, x, y, group, name):
        super().__init__(player_image, x, y)
        self.is_dead = False
        self.group = group
        self.name = name

    def delat_chtoto(self):
        if self.group == 'attack': #пример из пвз: горохострел
            
            if self.name == 'strelyatel':#циферки поменять
                self.hp = 100
                self.atk = 20

        if self.group == 'defend': #пример из пвз: стеноорех
            pass

        if self.group == 'dengi_davatel': #пример из пвз: подсолнух
            pass

        if self.group == 'instant': #пример из пвз: вишня бомба 
            pass


class Enemy(Sprite_game):#враг, он же "зомби"
    def __init__(self, player_image, x, y, group, name):
        super().__init__(player_image, x, y)
        self.is_dead = False
        self.group = group
        self.name = name

    def delat_chtoto(self):
        if self.group == 'penis': # тайное послание ---> зутшы
            
            if self.name == 'popusk':#циферки поменять
                self.hp = 200
                self.atk = 5



tower1 = Tower("slime_plr.png", 50, 300, 'attack', 'strelyatel')
enemy1 = Enemy("goblin_en_flip.png", 1500, 300, 'penis', 'popusk')


running = True
while running:

    screen.blit(img, (0, 0))

    tower1.reset()
    enemy1.reset()

    clock.tick(75)
    display.update()

    for e in event.get():
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            running = False
        if e.type == QUIT:
            running = False
        

