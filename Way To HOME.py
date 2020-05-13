import pygame as pp
import random
import math
from pygame import mixer
import time
pp.init()

scr = pp.display.set_mode((512,512))
pp.display.set_caption('Way To HOME')
over_font = pp.font.Font('freesansbold.ttf', 59)
back = pp.image.load('dff.png')

running = True
qq = mixer.music.load("dd.mp3")
mixer.music.play(-1)

playerr = pp.image.load('racer1.png')
player_x = 300
player_y = 400
player_c = 0
def play(x,y):
    scr.blit(playerr,(x,y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    scr.blit(over_text, (70, 250))



# 381, 227
pla = pp.image.load('transport.png')
pla_x = random.randint(120,150)
pla_y = 0
def plad(x,y):
    scr.blit(pla,(x,y))


font = pp.font.Font('freesansbold.ttf', 55)
score33 = 0
def the(x, y):
    score2 = over_font.render("THE END", True, (255, 255, 255))
    scr.blit(score2, (x, y))

def show_score(x, y):
    score2 = font.render("Score : " + str(score33), True, (255, 255, 255))
    scr.blit(score2, (x, y))

def level2(x, y):
    score2 = over_font.render("Level 2", True, (255, 255, 255))
    scr.blit(score2, (x, y))

def level3(x, y):
    score2 = over_font.render("Level 3", True, (255, 255, 255))
    scr.blit(score2, (x, y))


pl = pp.image.load('transport.png')
pl_x = random.randint(210,300)
pl_y = 0
def po(x,y):
    scr.blit(pl,(x,y))
pad = pp.image.load('transport.png')
plx = random.randint(155,200)
ply = 0
def pot(x,y):
    scr.blit(pad,(x,y))

a = pp.image.load('transport.png')
pa_x = random.randint(310,345)
pa_y = 0
def p(x,y):
    scr.blit(a,(x,y))


while running:
    scr.fill((0, 0, 0))
    scr.blit(back,(0,0))
    for event in pp.event.get():
        if event.type == pp.QUIT:
            running = False
        if event.type == pp.KEYDOWN:
            if event.key == pp.K_RIGHT:
                player_c += 2
            if event.key == pp.K_LEFT:
                player_c += -2
        if event.type == pp.KEYUP:
            player_c = 0
        print(event)
    if player_x == 389:
        player_x = 389
    if player_x == 120:
        player_x = 120
    pla_y +=3
    pl_y += 3
    pa_y += 3
    ply +=  3
    player_x += player_c
    if player_x >= 345:
        player_x = 345
    if player_x <= 105:
        player_x = 105
        
    if pla_y >= 512:
        pla_y = 0
        plaa = -30
        pla_x+=plaa
        score33 += 1
    if pl_y >= 512:
        pl_y = 0 
        paa = -30
        pl_x+=paa
    if pa_y >= 512:
        pa_y = 0
        laa = -30
        pa_x+=laa
    if ply >= 512:
        ply = 0
        laa = -30
        plx+=laa
        if pla_x <= 105:
            pla_x = 150
    if plx <= 155:
        plx = 200
    if pl_x <= 210:
        pl_x = 300
    if pa_x <= 310:
        pa_x = 345
    plad(pla_x, pla_y)
    play(player_x,player_y)
    po(pl_x, pl_y)
    p(pa_x, pa_y)
    pot(plx, ply)
    if score33 == 20:
        level2(70, 250)
        pl_y +=4
        ply += 4
        pa_y +=4
        pl_y +=4
        qq = mixer.music.load("Ego.mp3")
        mixer.music.play(-1)
    if score33 == 35:
        level3(70, 250)
        pl_y +=5
        ply += 5
        pa_y +=5
        pl_y +=5
        qq = mixer.music.load("dm.mp3")
        mixer.music.play(-1)
    if score33 == 50:
        qq = mixer.music.load("orig.mp3")
        mixer.music.play(-1)
        the(70, 250)
        running = False
        back = pp.image.load('color.png')




    collision = isCollision(pla_x ,pla_y,player_x ,player_y )
    if collision:
        game_over_text()
        running = False
    collision = isCollision(pl_x ,pl_y,player_x ,player_y )
    if collision:
        game_over_text()
        running = False
    collision = isCollision(plx ,ply,player_x ,player_y )
    if collision:
        game_over_text()
        running = False
    collision = isCollision(pa_x ,pa_y,player_x ,player_y )
    if collision:
        running = False
        game_over_text()
    show_score(0, 0)
    pp.display.update()
Exit = True
while Exit:
    for event in pp.event.get():
        if event.type == pp.KEYDOWN:
            if event.key == pp.K_q:
                Exit = False
            if event.key == pp.K_UP:
                pass
        if event.type == pp.KEYUP:
            pass
quit()