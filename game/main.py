# thư viện
import pygame

pygame.init()
import sys, random
from pygame.locals import *
from random import randint
from time import sleep
import math
import os
from collections import deque

# Set Color
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0,)
CYAN = (0, 255, 255)
SLATEGRAY = (198, 226, 255)

DISPLAYSURF = pygame.display.set_mode((800, 800))
# Kích cỡ màn hình
ngang = 800
cao = 800
screen = pygame.display.set_mode((ngang, cao))
# đặt tên 
pygame.display.set_caption('Dua Xe')

# Set flag
start_menu = True
huongdan_menu = False
bangdiem_menu = False
quit_game = True
start_game_menu_flag = True
gameplay_flag = False
chonmap_menu = False
minigame_flag = False
gamef1 = False
gamesky = False
gameghost = False
help_menu = False

# Âm nhạc
pygame.mixer.Channel(1).play(pygame.mixer.Sound('music1.mp3'), -1)

# tien
tienCuaTao = 10000
tien1, tien2, tien3, tien4, tien5 = 0, 0, 0, 0, 0
tienCuoc = 0
soTranThang = 0
soTranDaChoi = 0

nhanPham1 = 1000
spell1x = 1500
spell1y = 0

nhanPham2 = 1000
spell2x = 1500
spell2y = 0

nhanPham3 = 1000
spell3x = 1500
spell3y = 0

nhanPham4 = 1000
spell4x = 1500
spell4y = 0

nhanPham5 = 1000
spell5x = 1500
spell5y = 0

nhanPham6 = 1000
spell6x = 1500
spell6y = 0

mouse_x, mouse_y = 0, 0
mouse_pos = [mouse_x, mouse_y]


# kiểm tra vị trí mouse có nằm trong khung ko
def checkMouse(a, b, c, d):
    mouse = pygame.mouse.get_pos()
    if (mouse[0] < a or mouse[0] > c):
        return 0
    if (mouse[1] < b or mouse[1] > d):
        return 0
    return 1


def start_game_menu(event):
    global bangdiem_menu
    global start_menu
    global huongdan_menu
    global start_game_menu_flag
    global quit_game
    global gameplay
    global gameplay_flag
    global chonmap_menu
    global minigame_flag
    global gamef1
    global gamesky
    global gameghost
    global help_menu
    global mouse_x, mouse_y

    if start_menu == True:
        background = pygame.image.load('start_menu.png')
        screen.blit(background, (0, 0))

    if huongdan_menu == True:
        background = pygame.image.load('huongdan.png')
        screen.blit(background, (0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x >= 700 and mouse_x <= 800 and mouse_y >= 710 and mouse_y <= 760:
                    start_menu = True
                    huongdan_menu = False
                    bangdiem_menu = False

    if bangdiem_menu == True:
        background = pygame.image.load('bangdiem.png')
        screen.blit(background, (0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x >= 700 and mouse_x <= 800 and mouse_y >= 750 and mouse_y <= 800:
                    start_menu = True
                    bangdiem_menu = False
                    huongdan_menu = False
    if chonmap_menu == True:
        background = pygame.image.load('chonmap.png')
        screen.blit(background, (0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x >= 200 and mouse_x <= 420 and mouse_y >= 380 and mouse_y <= 520:
                    gamef1 = True
                    chonmap_menu = False
                if mouse_x >= 550 and mouse_x <= 780 and mouse_y >= 380 and mouse_y <= 520:
                    gamesky = True
                    chonmap_menu = False
                if mouse_x >= 380 and mouse_x <= 570 and mouse_y >= 565 and mouse_y <= 690:
                    gameghost = True
                    chonmap_menu = False
                if mouse_x >= 700 and mouse_x <= 800 and mouse_y >= 710 and mouse_y <= 760:
                    start_menu = True
                    chonmap_menu = False
                    huongdan_menu = False
                    help_menu = False

    if help_menu == True:
        background = pygame.image.load('help.png')
        screen.blit(background, (0, 0))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if mouse_x >= 700 and mouse_x <= 800 and mouse_y >= 710 and mouse_y <= 760:
                start_menu = True
                bangdiem_menu = False
                huongdan_menu = False
                help_menu = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            # Strat Game
            if mouse_x >= 350 and mouse_x <= 530 and mouse_y >= 380 and mouse_y <= 420:
                chonmap_menu = True
                start_menu = False
            # Instruction
            if mouse_x >= 280 and mouse_x <= 600 and mouse_y >= 440 and mouse_y <= 470:
                start_menu = False
                huongdan_menu = True
            # help
            if mouse_x >= 370 and mouse_x <= 510 and mouse_y >= 590 and mouse_y <= 620:
                start_menu = False
                help_menu = True
            # minigame
            if mouse_x >= 300 and mouse_x <= 570 and mouse_y >= 540 and mouse_y <= 580:
                start_menu = False
                minigame_flag = True


WINDOWWIDTH = 1200
WINDOWHEIGHT = 700
BGSPEED = 10
BGIMG = pygame.image.load('img/nen.jpg')

car1 = pygame.image.load("img/car1.png")
car2 = pygame.image.load("img/car2.png")
car3 = pygame.image.load("img/car3.png")
car4 = pygame.image.load("img/car4.png")
car5 = pygame.image.load("img/car5.png")

so1 = pygame.image.load("img/so1.png")
so2 = pygame.image.load("img/so2.png")
so3 = pygame.image.load("img/so3.png")
so4 = pygame.image.load("img/so4.png")
so5 = pygame.image.load("img/so5.png")

dichChuyen = pygame.image.load("spell/dich chuyen.png")
dungYen = pygame.image.load("spell/dung yen.png")
horror = pygame.image.load("spell/horror.png")
lamCham = pygame.image.load("spell/lam cham.png")
quayLai = pygame.image.load("spell/quay lai.png")
tangToc = pygame.image.load("spell/tang toc.png")
veDich = pygame.image.load("spell/ve dich.png")
chonXe = pygame.image.load("Chon xe.png")


def changeCharacter2():
    global BGIMG, car1, car2, car3, car4, car5, chonXe
    chonXe = pygame.image.load("Chon xe.png")
    BGIMG = pygame.image.load('img/nen.jpg')
    car1 = pygame.image.load("img/car1.png")
    car2 = pygame.image.load("img/car2.png")
    car3 = pygame.image.load("img/car3.png")
    car4 = pygame.image.load("img/car4.png")
    car5 = pygame.image.load("img/car5.png")


so = [dungYen, so1, so2, so3, so4, so5]
speed1, speed2, speed3, speed4, speed5 = 1, 1, 1, 1, 1

FPS = 60
fpsClock = pygame.time.Clock()
a = 0
b = 0
c = 0
d = 0
e = 0


def changeCharacter():
    global BGIMG, car1, car2, car3, car4, car5, chonXe
    chonXe = pygame.image.load("Chon xe1.png")
    BGIMG = pygame.image.load('img/nen1.jpg')
    car1 = pygame.image.load("img/bay1.png")
    car2 = pygame.image.load("img/bay2.png")
    car3 = pygame.image.load("img/bay3.png")
    car4 = pygame.image.load("img/bay4.png")
    car5 = pygame.image.load("img/bay5.png")


so = [dungYen, so1, so2, so3, so4, so5]
speed1, speed2, speed3, speed4, speed5 = 1, 1, 1, 1, 1

FPS = 60
fpsClock = pygame.time.Clock()
a = 0
b = 0
c = 0
d = 0
e = 0


def changeCharacter1():
    global BGIMG, car1, car2, car3, car4, car5, chonXe
    chonXe = pygame.image.load("Chon xe2.png")
    BGIMG = pygame.image.load('img/nen2.jpg')
    car1 = pygame.image.load("img/huy.png")
    car2 = pygame.image.load("img/hoai.png")
    car3 = pygame.image.load("img/duy.png")
    car4 = pygame.image.load("img/hoang.png")
    car5 = pygame.image.load("img/hung1.png")


so = [dungYen, so1, so2, so3, so4, so5]
speed1, speed2, speed3, speed4, speed5 = 1, 1, 1, 1, 1

FPS = 60
fpsClock = pygame.time.Clock()
a = 0
b = 0
c = 0
d = 0
e = 0


class Background():
    def __init__(self):
        self.h = 6930 + 100
        self.a = 50
        self.b = 50
        self.c = 50
        self.d = 50
        self.e = 50
        self.x = 0
        self.y = 0
        self.speed = BGSPEED
        self.img = BGIMG
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.dem = 0
        self.ok1, self.ok2, self.ok3, self.ok4, self.ok5 = 0, 0, 0, 0, 0
        self.tienThangCuoc = 0
        self.luu = 0

        global nhanPham1, nhanPham2, nhanPham3, nhanPham4, nhanPham5, nhanPham6
        global spell1y, spell2y, spell3y, spell4y, spell5y, spell6y
        global spell1x, spell2x, spell3x, spell4x, spell5x, spell6x
        global speed1, speed2, speed3, speed4, speed5

        speed1 = speed2 = speed3 = speed4 = speed5 = 1
        nhanPham1 = 1000
        spell1x = 1500
        spell1y = 0

        nhanPham2 = 1000
        spell2x = 1500
        spell2y = 0

        nhanPham3 = 1000
        spell3x = 1500
        spell3y = 0

        nhanPham4 = 1000
        spell4x = 1500
        spell4y = 0

        nhanPham5 = 1000
        spell5x = 1500
        spell5y = 0

        nhanPham6 = 1000
        spell6x = 1500
        spell6y = 0

    def draw(self):
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption('RACING')
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
        #  DISPLAYSURF.blit(self.img, (int(self.x + self.width), int(self.y)))
        DISPLAYSURF.blit(car1, (self.a, 110))
        DISPLAYSURF.blit(car2, (self.b, 210))
        DISPLAYSURF.blit(car3, (self.c, 315))
        DISPLAYSURF.blit(car4, (self.d, 420))
        DISPLAYSURF.blit(car5, (self.e, 530))

    def update(self):
        global tienCuaTao, tien1, tien2, tien3, tien4, tien5
        global speed1, speed2, speed3, speed4, speed5
        global soTranThang

        if self.x > int(-6500):
            self.x -= self.speed
            self.h -= self.speed

        if self.dem == 5:
            if self.luu == 0:
                tienCuaTao += self.tienThangCuoc
                if (self.tienThangCuoc != 0):
                    soTranThang += 1
                if (self.tienThangCuoc != 0):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('win.ogg'), -1)
                else:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('fail.ogg'), -1)
                self.luu = 1
            DISPLAYSURF.blit(
                pygame.font.SysFont('consolas', 40).render('ăn cược : ' + str(self.tienThangCuoc) + '$', True,
                                                           ('orange')), (500, 20))

    def xe(self):
        global tienCuaTao, tien1, tien2, tien3, tien4, tien5
        global speed1, speed2, speed3, speed4, speed5
        if self.x <= (-6500):
            speed1 = 20
            speed2 = 20
            speed3 = 20
            speed4 = 20
            speed5 = 20
        if self.a < self.h:

            if (speed1 < 0):
                self.a = -100
                speed1 = 1
            if (speed1 == 50):
                self.a += 100
                speed1 = 1

            self.a += random.uniform(0.5 * speed1, 1 * speed1)
        else:
            if (self.a < 2000):
                self.a += random.uniform(0.5 * speed1, 1 * speed1)
            if (self.ok1 == 0):
                self.dem += 1
                self.ok1 = self.dem
                if (self.ok1 == 1):
                    self.tienThangCuoc += tien1 * 3

                if (self.ok1 == 2):
                    self.tienThangCuoc += tien1 * 2
            tien1 = 0
            DISPLAYSURF.blit(so[self.ok1], (300, 120))

        if self.b < self.h:
            if (speed2 < 0):
                self.b = -1003
                speed2 = 1
            if (speed2 == 50):
                self.b += 100
                speed2 = 1

            self.b += random.uniform(0.5 * speed2, 1 * speed2)
        else:
            if (self.b < 2000):
                self.b += random.uniform(0.5 * speed2, 1 * speed2)
            if (self.ok2 == 0):
                self.dem += 1
                self.ok2 = self.dem
                if (self.ok2 == 1):
                    self.tienThangCuoc += tien2 * 3

                if (self.ok2 == 2):
                    self.tienThangCuoc += tien2 * 2
            tien2 = 0
            DISPLAYSURF.blit(so[self.ok2], (300, 220))

        if self.c < self.h:
            if (speed3 < 0):
                self.c = -100
                speed3 = 1
            if (speed3 == 50):
                self.c += 100
                speed3 = 1

            self.c += random.uniform(0.5 * speed3, 1 * speed3)
        else:
            if (self.c < 2000):
                self.c += random.uniform(0.5 * speed3, 1 * speed3)
            if (self.ok3 == 0):
                self.dem += 1
                self.ok3 = self.dem
                if (self.ok3 == 1):
                    self.tienThangCuoc += tien3 * 3

                if (self.ok3 == 2):
                    self.tienThangCuoc += tien3 * 2
            tien3 = 0
            DISPLAYSURF.blit(so[self.ok3], (300, 320))

        if self.d < self.h:
            if (speed4 < 0):
                self.d = -100
                speed4 = 1
            if (speed4 == 50):
                self.d += 100
                speed4 = 1

            self.d += random.uniform(0.5 * speed4, 1 * speed4)
        else:
            if (self.d < 2000):
                self.d += random.uniform(0.5 * speed4, 1 * speed4)
            if (self.ok4 == 0):
                self.dem += 1
                self.ok4 = self.dem
                if (self.ok4 == 1):
                    self.tienThangCuoc += tien4 * 3

                if (self.ok4 == 2):
                    self.tienThangCuoc += tien4 * 2
            tien4 = 0
            DISPLAYSURF.blit(so[self.ok4], (300, 420))

        if self.e < self.h:
            if (speed5 < 0):
                self.e = -100
                speed5 = 1
            if (speed5 == 50):
                self.e += 100
                speed5 = 1

            self.e += random.uniform(0.5 * speed5, 1 * speed5)
        else:
            if (self.e < 2000):
                self.e += random.uniform(0.5 * speed5, 1 * speed5)
            if (self.ok5 == 0):
                self.dem += 1
                self.ok5 = self.dem
                if (self.ok5 == 1):
                    self.tienThangCuoc += tien5 * 3

                if (self.ok5 == 2):
                    self.tienThangCuoc += tien5 * 2
            tien5 = 0
            DISPLAYSURF.blit(so[self.ok5], (300, 520))


def gameStart(bg):
    global tienCuaTao, soTranDaChoi, soTranThang
    global tienCuoc
    global tien1, tien2, tien3, tien4, tien5
    global DISPLAYSURF

    while True:
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    save()
                    return True
            if (event.type == pygame.QUIT):
                save()
                pygame.quit()
                sys.exit()
        DISPLAYSURF.blit(chonXe, (0, 0))
        DISPLAYSURF.blit(
            pygame.font.SysFont('consolas', 30).render('Hiện có: ' + str(tienCuaTao) + ' $', True, (255, 0, 0)),
            (300, 300))

        DISPLAYSURF.blit(pygame.font.SysFont('consolas', 60).render('            ' + str(tienCuoc), True, (255, 0, 0)),
                         (150, 600))
        DISPLAYSURF.blit(pygame.font.SysFont('consolas', 60).render('Tiền cược <       >', True, (255, 0, 0)),
                         (150, 600))
        DISPLAYSURF.blit(pygame.font.SysFont('consolas', 60).render('Start', True, (255, 0, 0)), (615, 700))

        DISPLAYSURF.blit(pygame.font.SysFont('consolas', 20).render(str(tien1), True, (255, 0, 0)), (220, 350))
        DISPLAYSURF.blit(pygame.font.SysFont('consolas', 20).render(str(tien2), True, (255, 0, 0)), (330, 350))
        DISPLAYSURF.blit(pygame.font.SysFont('consolas', 20).render(str(tien3), True, (255, 0, 0)), (450, 350))
        DISPLAYSURF.blit(pygame.font.SysFont('consolas', 20).render(str(tien4), True, (255, 0, 0)), (570, 350))
        DISPLAYSURF.blit(pygame.font.SysFont('consolas', 20).render(str(tien5), True, (255, 0, 0)), (690, 350))

        # in tọa độ chuột

        click = pygame.mouse.get_pressed()

        # giam
        if click == (1, 0, 0) and checkMouse(490, 600, 560, 650) == 1:
            if tienCuoc >= 100:
                tienCuoc -= 100
                tienCuaTao += 100
        # tang
        if click == (1, 0, 0) and checkMouse(740, 600, 780, 650) == 1:
            if tienCuaTao >= 100:
                tienCuoc += 100
                tienCuaTao -= 100

        # chon xe 1
        if click == (1, 0, 0) and checkMouse(197, 379, 293, 569) == 1:
            tien1 += tienCuoc
            tienCuoc = 0

        if click == (1, 0, 0) and checkMouse(293, 379, 415, 569) == 1:
            tien2 += tienCuoc
            tienCuoc = 0
        if click == (1, 0, 0) and checkMouse(415, 379, 533, 569) == 1:
            tien3 += tienCuoc
            tienCuoc = 0
        if click == (1, 0, 0) and checkMouse(533, 379, 660, 569) == 1:
            tien4 += tienCuoc
            tienCuoc = 0
        if click == (1, 0, 0) and checkMouse(660, 379, 760, 569) == 1:
            tien5 += tienCuoc
            tienCuoc = 0
        # bat dau
        if click == (1, 0, 0) and checkMouse(615, 700, 800, 760) == 1:
            soTranDaChoi += 1
            gamePlay(bg)
            DISPLAYSURF = pygame.display.set_mode((800, 800))

        pygame.display.update()
        fpsClock.tick(FPS)
    return True


motcaimang = [0, 80, 200, 310, 410, 530]


# where1, where2, where3, where4, where5
# otherSpell, 1 la bua ve dich, 2 la bua die, 3 la bua dich chuyen
def tangCMNtoc(bg, speed, hinhve, nhanPham1, spell1y, spell1x, otherSpell=0, nhanPham=2000):
    global speed1, speed2, speed3, speed4, speed5
    if nhanPham1 > 10:
        nhanPham1 = randint(1, nhanPham)
    else:
        if spell1y <= 0:
            spell1y = randint(1, 5)
        spell1x -= 10

        if spell1y == 1:
            if (bg.a < spell1x):
                DISPLAYSURF.blit(hinhve, (spell1x, motcaimang[spell1y]))
            if (abs(bg.a - spell1x) <= 10):
                speed1 = speed
                if otherSpell == 1:
                    speed1 = 200
                if otherSpell == 2:
                    speed1 = -1000
                if otherSpell == 3:
                    speed1 = 50
            if (spell1x <= -400):
                speed1 = 1
                nhanPham1 = 1000
                spell1x = 1500
                spell1y = 0

        if spell1y == 2:
            if (bg.b < spell1x):
                DISPLAYSURF.blit(hinhve, (spell1x, motcaimang[spell1y]))
            if (abs(bg.b - spell1x) <= 10):
                speed2 = speed
                if otherSpell == 1:
                    speed2 = 200
                if otherSpell == 2:
                    speed2 = -1000
                if otherSpell == 3:
                    speed2 = 50
            if (spell1x <= -400):
                speed2 = 1
                nhanPham1 = 1000
                spell1x = 1500
                spell1y = 0

        if spell1y == 3:
            if (bg.c < spell1x):
                DISPLAYSURF.blit(hinhve, (spell1x, motcaimang[spell1y]))
            if (abs(bg.c - spell1x) <= 10):
                speed3 = speed
                if otherSpell == 1:
                    speed3 = 200
                if otherSpell == 2:
                    speed3 = -1000
                if otherSpell == 3:
                    speed3 = 50
            if (spell1x <= -400):
                speed3 = 1
                nhanPham1 = 1000
                spell1x = 1500
                spell1y = 0

        if spell1y == 4:
            if (bg.d < spell1x):
                DISPLAYSURF.blit(hinhve, (spell1x, motcaimang[spell1y]))
            if (abs(bg.d - spell1x) <= 10):
                speed4 = speed
                if otherSpell == 1:
                    speed4 = 200
                if otherSpell == 2:
                    speed4 = -1000
                if otherSpell == 3:
                    speed4 = 50
            if (spell1x <= -400):
                speed4 = 1
                nhanPham1 = 1000
                spell1x = 1500
                spell1y = 0

        if spell1y == 5:
            if (bg.e < spell1x):
                DISPLAYSURF.blit(hinhve, (spell1x, motcaimang[spell1y]))
            if (abs(bg.e - spell1x) <= 10):
                speed5 = speed
                if otherSpell == 1:
                    speed5 = 200
                if otherSpell == 2:
                    speed5 = -1000
                if otherSpell == 3:
                    speed5 = 50
            if (spell1x <= -400):
                speed5 = 1
                nhanPham1 = 1000
                spell1x = 1500
                spell1y = 0
    return (nhanPham1, spell1y, spell1x)


def gamePlay(bg):
    global nhanPham1, nhanPham2, nhanPham3, nhanPham4, nhanPham5, nhanPham6
    global spell1y, spell2y, spell3y, spell4y, spell5y, spell6y
    global spell1x, spell2x, spell3x, spell4x, spell5x, spell6x
    bg.__init__()
    while True:
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('music1.mp3'), -1)
                    save()
                    return True
            if event.type == pygame.QUIT:
                save()
                pygame.quit()
                sys.exit()
        bg.draw()
        if (bg.update()):
            return
        bg.xe()

        DISPLAYSURF.blit(
            pygame.font.SysFont('consolas', 30).render(str(str(data[player]).split('\n')[0]), True, ('White')),
            (50, 20))
        DISPLAYSURF.blit(
            pygame.font.SysFont('consolas', 20).render('Số trận thắng ' + str(soTranThang), True, ('orange')),
            (1000 - 10, 10))
        DISPLAYSURF.blit(
            pygame.font.SysFont('consolas', 20).render('Số trận đã chơi ' + str(soTranDaChoi), True, ('orange')),
            (1000 - 10, 30))
        (nhanPham1, spell1y, spell1x) = tangCMNtoc(bg, 2, tangToc, nhanPham1, spell1y, spell1x)
        (nhanPham2, spell2y, spell2x) = tangCMNtoc(bg, 0, dungYen, nhanPham2, spell2y, spell2x)
        (nhanPham3, spell3y, spell3x) = tangCMNtoc(bg, 0.5, lamCham, nhanPham3, spell3y, spell3x)
        (nhanPham4, spell4y, spell4x) = tangCMNtoc(bg, 1, veDich, nhanPham4, spell4y, spell4x, 1, 20000)
        (nhanPham5, spell5y, spell5x) = tangCMNtoc(bg, 1, horror, nhanPham5, spell5y, spell5x, 2, 20000)
        (nhanPham6, spell6y, spell6x) = tangCMNtoc(bg, 1, dichChuyen, nhanPham6, spell6y, spell6x, 3, 5000)

        pygame.display.update()
        fpsClock.tick(FPS)


def gameOver():
    pass


def minigame():
    WINDOWWIDTH = 400
    WINDOWHEIGHT = 600

    BIRDWIDTH = 60
    BIRDHEIGHT = 45
    G = 0.4
    SPEEDFLY = -5
    BIRDIMG = pygame.image.load('img1/bird.png')

    COLUMNWIDTH = 60
    COLUMNHEIGHT = 500
    BLANK = 160
    DISTANCE = 200
    COLUMNSPEED = 2
    COLUMNIMG = pygame.image.load('img1/column.png')

    BACKGROUND = pygame.image.load('img1/background.png')

    pygame.init()
    FPS = 60
    fpsClock = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Flappy Bird')

    class Bird():
        def __init__(self):
            self.width = BIRDWIDTH
            self.height = BIRDHEIGHT
            self.x = (WINDOWWIDTH - self.width) / 2
            self.y = (WINDOWHEIGHT - self.height) / 2
            self.speed = 0
            self.suface = BIRDIMG

        def draw(self):
            DISPLAYSURF.blit(self.suface, (int(self.x), int(self.y)))

        def update(self, mouseClick):
            self.y += self.speed + 0.5 * G
            self.speed += G
            if mouseClick == True:
                self.speed = SPEEDFLY

    class Columns():
        def __init__(self):
            self.width = COLUMNWIDTH
            self.height = COLUMNHEIGHT
            self.blank = BLANK
            self.distance = DISTANCE
            self.speed = COLUMNSPEED
            self.surface = COLUMNIMG
            self.ls = []
            for i in range(3):
                x = WINDOWWIDTH + i * self.distance
                y = random.randrange(60, WINDOWHEIGHT - self.blank - 60, 20)
                self.ls.append([x, y])

        def draw(self):
            for i in range(3):
                DISPLAYSURF.blit(self.surface, (self.ls[i][0], self.ls[i][1] - self.height))
                DISPLAYSURF.blit(self.surface, (self.ls[i][0], self.ls[i][1] + self.blank))

        def update(self):
            for i in range(3):
                self.ls[i][0] -= self.speed

            if self.ls[0][0] < -self.width:
                self.ls.pop(0)
                x = self.ls[1][0] + self.distance
                y = random.randrange(60, WINDOWHEIGHT - self.blank - 60, 10)
                self.ls.append([x, y])

    def rectCollision(rect1, rect2):
        if rect1[0] <= rect2[0] + rect2[2] and rect2[0] <= rect1[0] + rect1[2] and rect1[1] <= rect2[1] + rect2[3] and \
                rect2[1] <= rect1[1] + rect1[3]:
            return True
        return False

    def isGameOver(bird, columns):
        for i in range(3):
            rectBird = [bird.x, bird.y, bird.width, bird.height]
            rectColumn1 = [columns.ls[i][0], columns.ls[i][1] - columns.height, columns.width, columns.height]
            rectColumn2 = [columns.ls[i][0], columns.ls[i][1] + columns.blank, columns.width, columns.height]
            if rectCollision(rectBird, rectColumn1) == True or rectCollision(rectBird, rectColumn2) == True:
                return True
        if bird.y + bird.height < 0 or bird.y + bird.height > WINDOWHEIGHT:
            return True
        return False

    class Score():
        def __init__(self):
            self.score = 0
            self.addScore = True

        def draw(self):
            font = pygame.font.SysFont('consolas', 40)
            scoreSuface = font.render(str(self.score), True, (0, 0, 0))
            textSize = scoreSuface.get_size()
            DISPLAYSURF.blit(scoreSuface, (int((WINDOWWIDTH - textSize[0]) / 2), 100))

        def update(self, bird, columns):
            collision = False
            for i in range(3):
                rectColumn = [columns.ls[i][0] + columns.width, columns.ls[i][1], 1, columns.blank]
                rectBird = [bird.x, bird.y, bird.width, bird.height]
                if rectCollision(rectBird, rectColumn) == True:
                    collision = True
                    break
            if collision == True:
                if self.addScore == True:
                    self.score += 1
                self.addScore = False
            else:
                self.addScore = True

    def gameStart(bird):
        bird.__init__()

        font = pygame.font.SysFont('consolas', 60)
        headingSuface = font.render('FLAPPY BIRD', True, (255, 0, 0))
        headingSize = headingSuface.get_size()

        font = pygame.font.SysFont('consolas', 20)
        commentSuface = font.render('Click to start', True, (0, 0, 0))
        commentSize = commentSuface.get_size()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    save()
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    return

            DISPLAYSURF.blit(BACKGROUND, (0, 0))
            bird.draw()
            DISPLAYSURF.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0]) / 2), 100))
            DISPLAYSURF.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0]) / 2), 500))

            pygame.display.update()
            fpsClock.tick(FPS)

    def gamePlay(bird, columns, score):
        bird.__init__()
        bird.speed = SPEEDFLY
        columns.__init__()
        score.__init__()
        while True:
            mouseClick = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    save()
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouseClick = True

            DISPLAYSURF.blit(BACKGROUND, (0, 0))
            columns.draw()
            columns.update()
            bird.draw()
            bird.update(mouseClick)
            score.draw()
            score.update(bird, columns)

            if isGameOver(bird, columns) == True:
                return

            pygame.display.update()
            fpsClock.tick(FPS)

    def gameOver(bird, columns, score):
        global tienCuaTao
        font = pygame.font.SysFont('consolas', 60)
        headingSuface = font.render('GAMEOVER', True, (255, 0, 0))
        headingSize = headingSuface.get_size()

        font = pygame.font.SysFont('consolas', 20)
        commentSuface = font.render('Press "space" to replay', True, (0, 0, 0))
        commentSize = commentSuface.get_size()

        font = pygame.font.SysFont('consolas', 30)
        scoreSuface = font.render('Score: ' + str(score.score), True, (0, 0, 0))
        tienCuaTao += score.score * 120

        scoreSize = scoreSuface.get_size()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    save()
                    pygame.quit()
                    sys.exit()
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        return False
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        save()
                        return True

            DISPLAYSURF.blit(BACKGROUND, (0, 0))
            columns.draw()
            bird.draw()
            DISPLAYSURF.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0]) / 2), 100))
            DISPLAYSURF.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0]) / 2), 500))
            DISPLAYSURF.blit(scoreSuface, (int((WINDOWWIDTH - scoreSize[0]) / 2), 160))

            pygame.display.update()
            fpsClock.tick(FPS)

    def main():
        bird = Bird()
        columns = Columns()
        score = Score()
        loop = True
        while loop:
            gameStart(bird)
            gamePlay(bird, columns, score)
            if gameOver(bird, columns, score):
                return True

    if __name__ == '__main__':
        if (main()):
            return True


def resetData():
    global start_menu, huongdan_menu, ngang, cao, bangdiem_menu, start_game_menu_flag
    global gameplay_flag, chonmap_menu, gamef1, gamesky, gameghost, help_menu, quit_game, minigame_flag
    DISPLAYSURF = pygame.display.set_mode((800, 800))
    # Kích cỡ màn hình
    ngang = 800
    cao = 800
    screen = pygame.display.set_mode((ngang, cao))
    # đặt tên
    pygame.display.set_caption('Dua Xe')

    # Set flag
    start_menu = True
    huongdan_menu = False
    bangdiem_menu = False
    quit_game = True
    start_game_menu_flag = True
    gameplay_flag = False
    chonmap_menu = False
    minigame_flag = False
    gamef1 = False
    gamesky = False
    gameghost = False
    help_menu = False


# menu
def menu():
    global start_menu, huongdan_menu, ngang, cao, bangdiem_menu, start_game_menu_flag
    global gameplay_flag, chonmap_menu, gamef1, gamesky, gameghost, help_menu, quit_game, minigame_flag
    global mouse_x, mouse_y
    resetData()
    while quit_game:

        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pos = [mouse_x, mouse_y]
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    save()
                    return
            if (event.type == pygame.QUIT):
                save()
                pygame.quit()
                sys.exit()
            if start_game_menu_flag == True:
                start_game_menu(event)
            if gamef1 == True:
                changeCharacter2()
                if gameStart(Background()):
                    resetData()
            if gamesky == True:
                changeCharacter()
                if gameStart(Background()):
                    resetData()
            if gameghost == True:
                changeCharacter1()
                if gameStart(Background()):
                    resetData()
            if minigame_flag == True:
                if minigame():
                    resetData()
        pygame.display.flip()


import pygame as pg


def box():
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(330, 400, 400, 32)
    color_inactive = pg.Color('orange')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = not False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # if event.type == pg.MOUSEBUTTONDOWN:
            #     # If the user clicked on the input_box rect.
            #     if input_box.collidepoint(event.pos):
            #         # Toggle the active variable.
            #         active = not active
            #     else:
            #         active = False
            #     # Change the current color of the input box.
            #     color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        return text
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        DISPLAYSURF.blit(pygame.image.load('nguoidung.png'), (0, 0))
        DISPLAYSURF.blit(pygame.font.SysFont('consolas', 30).render('Nhập tên tay đua', True, ('orange')), (320, 350))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)


def update(i):
    global tienCuaTao, player, data
    global soTranThang, soTranDaChoi
    player = i
    tienCuaTao = int(data[i + 3])
    soTranDaChoi = int(data[i + 6])
    soTranThang = int(data[i + 9])


def save():
    global tienCuaTao, player, data
    data[player + 3] = int(tienCuaTao)
    data[player + 6] = int(soTranDaChoi)
    data[player + 9] = int(soTranThang)
    print(data)
    with open('SaveGame.txt', 'w') as f:
        for i in data:
            f.write(str(str(i).split('\n')[0]) + '\n')
        # f.write(str(newData))


data = [*open('SaveGame.txt', 'r')]
player = -1
# reset file saveGame, vô thư mục sửa thành 12 số 0 (nhớ xuống dòng)
# 0
# 0
# 0
# ...
print(data)

while 1:

    click = (0, 0, 0)

    DISPLAYSURF.blit(pygame.image.load('nguoidung.png'), (0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = (1, 0, 0)

    ok = False

    for i in range(3):
        if str(str(data[i]).split('\n')[0]) == '0':

            if click == (1, 0, 0) and checkMouse(340, 310 + i * 120, 540, 380 + i * 120) == 1:
                data[i] = box()
                data[i + 3] = 10000
                update(i)
                resetData()
                menu()
                resetData()
            else:
                DISPLAYSURF.blit(pygame.font.SysFont('consolas', 40).render('New Game', True, (255, 255, 255)),
                                 (350, 320 + i * 120))
        else:
            if click == (1, 0, 0) and checkMouse(340, 310 + i * 120, 540, 380 + i * 120) == 1:
                update(i)
                resetData()
                menu()
                resetData()
            else:
                DISPLAYSURF.blit(
                    pygame.font.SysFont('consolas', 40).render(str(str(data[i]).split('\n')[0]), True, (255, 255, 255)),
                    (350, 320 + i * 120))
                DISPLAYSURF.blit(
                    pygame.font.SysFont('consolas', 20).render(str(int(data[i + 3])) + ' $', True, (255, 255, 255)),
                    (370, 320 + i * 120 + 40))
                DISPLAYSURF.blit(
                    pygame.font.SysFont('consolas', 20).render('Số trận đã chơi: ' + str(int(data[i + 6])), True,
                                                               (255, 255, 255)), (370, 320 + i * 120 + 60))
                DISPLAYSURF.blit(
                    pygame.font.SysFont('consolas', 20).render('Số trận thắng:   ' + str(int(data[i + 9])), True,
                                                               (255, 255, 255)), (370, 320 + i * 120 + 80))

    pygame.display.flip()

# reset file saveGame, vô thư mục sửa thành 12 số 0 (nhớ xuống dòng)
# 0
# 0
# 0
# ...