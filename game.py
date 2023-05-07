from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x=0, y=0, width=50, height=50):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, sprite_image, x=0, y=0, width=50, height=50, speed=5, key_up=K_w, key_down=K_s):
        super().__init__(sprite_image, x, y, width, height)
        self.speed = speed
        self.key_up = key_up
        self.key_down = key_down

    def update(self):
        keys = key.get_pressed()
        if keys[self.key_up]:
            self.rect.y -= self.speed
        if keys[self.key_down]:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, sprite_image, x=0, y=0, width=32, height=32, speed=5):
        super().__init__(sprite_image, x, y, width, height)
        self.dx = speed
        self.dy = speed

    def update(self):
        if self.rect.y < 0 or self.rect.y > HEIGHT:
            self.dy *= -1
        self.rect.x += self.dx
        self.rect.y += self.dy

    def player_collide(self, player):
        if sprite.collide_rect(self, player):
            self.dx *= -1


BG_COLOR = (220, 100, 220)
WIDTH, HEIGHT = 600, 480
FPS = 60

mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Пинг-Понг')
mw.fill(BG_COLOR)
clock = time.Clock()

player_1 = Player('platform.jpg', 10, 200, 30, 90, 5, K_w, K_s)
player_2 = Player('platform.jpg', 560, 200, 30, 90, 5, K_UP, K_DOWN)
ball = Ball('ball.png', WIDTH//2, HEIGHT//4, 32, 32, 3)

run = True
while run:
    mw.fill(BG_COLOR)
    player_1.update()
    player_2.update()
    player_1.reset()
    player_2.reset()
    ball.update()
    ball.player_collide(player_1)
    ball.player_collide(player_2)
    ball.reset()

    for e in event.get():
        if e.type == QUIT:
            run = False
    
    display.update()
    clock.tick(FPS)
    
    from pygame import *
from button import Button
font.init()
stage = 'menu'


class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x=0, y=0, width=50, height=50):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, sprite_image, x=0, y=0, width=50, height=50, speed=5, key_up=K_w, key_down=K_s):
        super().__init__(sprite_image, x, y, width, height)
        self.speed = speed
        self.key_up = key_up
        self.key_down = key_down

    def update(self):
        keys = key.get_pressed()
        if keys[self.key_up]:
            self.rect.y -= self.speed
        if keys[self.key_down]:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, sprite_image, x=0, y=0, width=32, height=32, speed=5):
        super().__init__(sprite_image, x, y, width, height)
        self.dx = speed
        self.dy = speed

    def update(self):
        if self.rect.y < 0 or self.rect.y > HEIGHT - self.rect.height:
            self.dy *= -1
        self.rect.x += self.dx
        self.rect.y += self.dy

    def player_collide(self, player):
        if sprite.collide_rect(self, player):
            self.dx *= -1

BG_COLOR = (220, 100, 220)
WIDTH, HEIGHT = 600, 480
FPS = 60

mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Пинг-Понг')
mw.fill(BG_COLOR)
clock = time.Clock()

player_1 = Player('platform.png', 10, 200, 30, 90, 5, K_w, K_s)
player_2 = Player('platform.png', 560, 200, 30, 90, 5, K_UP, K_DOWN)
ball = Ball('ball.png', WIDTH//2, HEIGHT//4, 32, 32, 3)

btn_start = Button(y=200, width=150, height=40, text='Начать игру', font_size=26)
btn_credits = Button(y=250, width=150, height=40, text='Разработчики', font_size=26)
btn_exit = Button(y=300, width=150, height=40, text='Выход', font_size=26)

btn_continue = Button(y=200, width=150, height=40, text='Продолжить', font_size=26)
btn_to_menu = Button(y=250, width=150, height=40, text='Вернуться в меню', font_size=26)

btn_restart = Button(y=200, width=150, height=40, text='Начать заного', font_size=26)


def game():
    mw.fill(BG_COLOR)
    player_1.update()
    player_2.update()
    player_1.reset()
    player_2.reset()
    ball.update()
    ball.player_collide(player_1)
    ball.player_collide(player_2)
    ball.reset()

def menu(events):
    mw.fill(BG_COLOR)
    # обработка наведения
    btn_start.update(events)
    btn_credits.update(events)
    btn_exit.update(events)
    # отрисовка
    btn_start.draw(mw)
    btn_credits.draw(mw)
    btn_exit.draw(mw)
    # проверка на нажатие
    global stage
    if btn_exit.is_clicked(events):
        stage = 'off'
    if btn_start.is_clicked(events):
        restart()
        stage = 'game'

def pause(events):
    mw.fill(BG_COLOR)
    btn_continue.update(events)
    btn_to_menu.update(events)
    btn_continue.draw(mw)
    btn_to_menu.draw(mw)
    global stage
    if btn_continue.is_clicked(events):
        restart()
        stage = 'game'
    if btn_to_menu.is_clicked(events):
        stage = 'menu'

def restart():
    player_1 = Player('platform.png', 10, 200, 30, 90, 5, K_w, K_s)
    player_2 = Player('platform.png', 560, 200, 30, 90, 5, K_UP, K_DOWN)
    ball = Ball('ball.png', WIDTH//2, HEIGHT//4, 32, 32, 3)

def check_game_status():
    global stage
    if ball.rect.x < -ball.rect.width:
        stage = '2 win'
    if ball.rect.x > WIDTH:
        stage = '1 win'

def win_screen(events):
    global stage
    if stage == '2 win':
        print('Второй победил')
    elif stage == '1 win':
        print('Первой победил')
    btn_restart.update(events)
    btn_to_menu.update(events)
    btn_restart.draw(mw)
    btn_to_menu.draw(mw)
    if btn_restart.is_clicked(events):
        restart()
        stage = 'game'
    if btn_to_menu.is_clicked(events):
        stage = 'menu'

while stage != 'off':
    events = event.get()
    for e in events:
        if e.type == QUIT:
            stage = 'off'
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                stage = 'pause'

    if stage == 'menu':
        menu(events)
    elif stage == 'game':
        game()
    elif stage == 'pause':
        pause(events)
    

while stage != 'off':
    events = event.get()
    for e in events:
        if e.type == QUIT:
            stage = 'off'



    if stage == 'menu':
        menu(events)
    elif stage == 'game':
        game()
    elif stage == 'pause':
        pause(events)

    display.update()
    clock.tick(FPS)
    
    
