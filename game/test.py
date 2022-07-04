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
BLUE = (0, 0, )
CYAN = (0, 255, 255)
SLATEGRAY = (198, 226, 255)

DISPLAYSURF = pygame.display.set_mode((800, 800))
# Kích cỡ màn hình
ngang = 800
cao = 800
screen = pygame.display.set_mode((ngang, cao))
# đặt tên 
pygame.display.set_caption('Dua Xe')


pygame.mixer.Channel(1).play(pygame.mixer.Sound('win.ogg'), -1)
pygame.mixer.Channel(0).play(pygame.mixer.Sound('music1.mp3'))
pygame.mixer.set_num_channels(2)

while 1:
    pass