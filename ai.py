import pygame as pp
import time
import random
import math
from pygame import mixer
import time
import pyautogui

def rectangle(X, Y):
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    #                        X     Y   sizeX   sizeY
    pp.draw.rect(scr, BLUE, (X,    Y,   35  ,   20))

def rectangle2(X, Y):
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    #                        X     Y   sizeX   sizeY
    pp.draw.rect(scr, BLUE, (X,    Y,   40  ,   20))

def rectangle3(X, Y):
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    #                        X     Y   sizeX   sizeY
    pp.draw.rect(scr, BLUE, (X,    Y,   25  ,   20))

def motion_right():
    pyautogui.keyDown('right')
    # time.sleep(timeslp)
    # pyautogui.keyUp('right')

def motion_left(rang):
    player_x += rang





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
    score2 = over_font.render("THE END", True, (0, 127, 255))
    scr.blit(score2, (x, y))
    score2 = over_font.render("press q = quit", True, (0, 127, 255))
    scr.blit(score2, (80, 100))

def show_score(x, y):
    score2 = font.render("Score : " + str(score33), True, (255, 255, 255))
    scr.blit(score2, (x, y))

def level2(x, y):
    score2 = over_font.render("Level 2", True, (255, 255, 255))
    scr.blit(score2, (x, y))

def level3(x, y):
    score2 = over_font.render("Level 3", True, (255, 255, 255))
    scr.blit(score2, (x, y))

def leveler(whatever):
    score2 = over_font.render(str(whatever), True, (255, 255, 255))
    scr.blit(score2, (70, 250))

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
sdd = 0

while running:
    scr.fill((0, 0, 0))
    scr.blit(back,(0,0))
    for event in pp.event.get():
        if event.type == pp.QUIT:
            running = False
        if event.type == pp.KEYDOWN:
            if event.key == pp.K_RIGHT:
                player_c += 4
            if event.key == pp.K_LEFT:
                player_c += -4
            if event.key == pp.K_d:
                score33 = 50
            # if event.key == pp.K_ESCAPE:

        if event.type == pp.KEYUP:
            player_c = 0
        
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
    if score33 == 5:
        leveler("level 1")
        qq = mixer.music.load("Ego.mp3")
        mixer.music.play(-1)
    if score33 == 100:
        leveler("level 2")
        qq = mixer.music.load("dm.mp3")
        mixer.music.play(-1)

    if score33 == 200:
        leveler("level 3")
        qq = mixer.music.load("fs.mp3")
        mixer.music.play(-1)

    if score33 == 300:
        leveler("level 4")
        qq = mixer.music.load("orig.mp3")
        mixer.music.play(-1)

    if score33 == 450:
        leveler("level 5")
        qq = mixer.music.load("te.mp3")
        mixer.music.play(-1)

    if score33 == 500:
        qq = mixer.music.load("video.mp4")
        mixer.music.play(-1)
        running = False
        the(70, 250)
        back = pp.image.load('color.png')
        scr.blit(back,(0,100))



    collision = isCollision(pla_x ,pla_y,player_x ,player_y )
    if collision:
        game_over_text()
        score33 = 0
        # running = False
    collision = isCollision(pl_x ,pl_y,player_x ,player_y )
    if collision:
        game_over_text()
        # running = False
        score33 = 0
    collision = isCollision(plx ,ply,player_x ,player_y )
    if collision:
        game_over_text()
        # running = False
        score33 = 0
    collision = isCollision(pa_x ,pa_y,player_x ,player_y )
    if collision:
        # running = False
        game_over_text()
        score33 = 0
    show_score(0, 0)

    recty12 = 100

    rectx = 215

    recty = 50

    rectx1 = 260

    rectx2 = 120

    rectx3 = 170

    rectx4 = 310

    recty1 = 70

    rectx5 = 355

    rectx55 = 355

    rectx11 = 260

    rectangle2(rectx1,recty)#4

    # rectangle(rectx2,recty)#1

    # rectangle(rectx3,recty)#2

    # rectangle(rectx,recty)#3

    rectangle(rectx4,recty)#5

    rectangle(rectx5,recty)#6

    rectangle(rectx55,recty1)

    rectangle2(rectx11,recty1)
    

    rectx13 = 290
    rectx12 = 355


    rectx22 = 255
    rectx21 = 330
    recty3 = 130

    rectangle(rectx13,recty12)

    rectangle(rectx12,recty12)



    # rectangle3(rectx22,recty3)

    # rectangle3(rectx21,recty3)

    # qw1 = 0
    # qww1 = 0

    # collision = isCollision(pl_x ,pl_y,rectx22 ,recty3)
    # collision2 = isCollision(pl_x ,pl_y,rectx21 ,recty3)
    # if collision :
    #     qw1 = 3
    
    # collision = isCollision(pa_x ,pa_y,rectx22 ,recty3)
    # collision2 = isCollision(pa_x ,pa_y,rectx21 ,recty3)
    # if collision :
    #     qw1 = 3


    # collision = isCollision(pl_x ,pl_y,rectx22 ,recty3)
    # collision2 = isCollision(pl_x ,pl_y,rectx21 ,recty3)
    # if collision2 :
    #     qww1 = 3
    
    # collision = isCollision(pa_x ,pa_y,rectx22 ,recty3)
    # collision2 = isCollision(pa_x ,pa_y,rectx21 ,recty3)
    # if collision2 :
    #     qww1 = 3



    # if qw1 == 3 and qww1 ==3:
    #     player_x = rectx2-20






    qw = 0
    qww = 0


    collision = isCollision(pl_x ,pl_y,rectx13 ,recty12)
    collision2 = isCollision(pl_x ,pl_y,rectx12 ,recty12)
    if collision :
        qw = 3
    
    collision = isCollision(pa_x ,pa_y,rectx13 ,recty12)
    collision2 = isCollision(pa_x ,pa_y,rectx12 ,recty12)
    if collision :
        qw = 3


    collision = isCollision(pl_x ,pl_y,rectx13 ,recty12)
    collision2 = isCollision(pl_x ,pl_y,rectx12 ,recty12)
    if collision2 :
        qww = 3
    
    collision = isCollision(pa_x ,pa_y,rectx13 ,recty12)
    collision2 = isCollision(pa_x ,pa_y,rectx12 ,recty12)
    if collision2 :
        qww = 3



    if qw == 3 and qww ==3:
        player_x = rectx1-20







    collision = isCollision(pl_x ,pl_y,rectx1 ,recty)
    if collision:
        player_x = rectx5-10
    
    collision = isCollision(pa_x ,pa_y,rectx1 ,recty)
    if collision:
        player_x = rectx5-10
        
    


    aaq = 2
    bq = 2





    
    collision = isCollision(pl_x ,pl_y,rectx11 ,recty1)
    collision2 = isCollision(pl_x ,pl_y,rectx55 ,recty1)
    if collision :
        aaq = 3
    
    collision = isCollision(pa_x ,pa_y,rectx11 ,recty1)
    collision2 = isCollision(pa_x ,pa_y,rectx55 ,recty1)
    if collision :
        aaq = 3
        




    
    collision = isCollision(pa_x ,pa_y,rectx2 ,recty1)
    collision2 = isCollision(pl_x ,pl_y,rectx ,recty1)
    if collision2 :
        bq = 3
    
    collision = isCollision(pl_x ,pl_y,rectx2 ,recty1)
    collision2 = isCollision(pa_x ,pa_y,rectx ,recty1)
    if collision2 :
        bq = 3


    if aaq==3   and   bq==3:
        player_x = rectx4-25


    



    collision2 = isCollision(pa_x ,pa_y,rectx4 ,recty)
    if collision :
        player_x = rectx1-10

    collision2 = isCollision(pl_x ,pl_y,rectx4 ,recty)
    if collision2 :
        player_x = rectx1-10





    


   
    collision = isCollision(pl_x ,pl_y,rectx5 ,recty)
    if collision:
        player_x = rectx1-10
        
    
    collision = isCollision(pa_x ,pa_y,rectx5 ,recty)
    if collision:
        player_x = rectx1-10
        


        
    pp.display.update()
Exit = True
while Exit:
    for event in pp.event.get():
        if event.type == pp.QUIT:
            quit()
        if event.type == pp.KEYUP:
            pass
quit()


