#-------------Initialize the pygame____________

import pygame
import math
import random
from pygame import mixer

pygame.init()
game_over = False
#-------------create the screen_____________
screen = pygame.display.set_mode((900,600))

#------------background-------------------
background = pygame.image.load("background.jpg")

#-------------background soound------
mixer.music.load("background.wav")
mixer.music.play(-1)

# #--------------Title and Icon__________>>Flaticon.com

title = pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo-flying.png")
pygame.display.set_icon(icon )

  
#---------------Variables and functions---------------

    #---------functions-----------


def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x,y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16, y + 10 ))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2)) +  (math.pow(enemyY - bulletY, 2)))
    if distance <27:
        return True
    else:
        return False
    
def show_score(x,y):
    score = font.render("Score :" + str(score_value), True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text(x,y):
    over_text = font.render("GAME OVER", True,(255,255,255))
    screen.blit(over_text, (200,250))


    #--------score-------

score_value= 0
font = pygame.font.Font("freesansbold.ttf",32)

textX = 10
textY = 10


#----------Game Over text-------
over_font = pygame.font.Font("freesansbold.ttf",70)


    #-------Player-----------
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0
#playerY_change = 0

  

    #----------Enemy---------

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)


    #--------Bullet--------

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change =0
bulletY_change =5
bullet_state = "ready"





#-------------game loop_________
running = True
while running:

    #--------------RGB------------
    screen.fill((0,0,0))
    #--------Background Image--------------
    screen.blit(background, (0,0))

 


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #-------------Check keystroke is pressed__________
                #KEYDOWN == pressed the key
                #KEYUP == released the key

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
                playerX_change = -20
            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
                playerX_change = 20

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound("laser.wav")
                    bullet_Sound.play()

                    #current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)



        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
        #         print("Up arrow is pressed")
        #         playerY_change = -5
        #     if event.key == pygame.K_DOWN:
        #         print("Down arrow is pressed")
        #         playerY_change = 5

        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0





    #----------------Boundries-------------------#
        playerX += playerX_change
        #playerY += playerY_change

        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736
        # if enemyX <= 0:  
        #     enemyX = 0
        # if enemyX >= 736:
        #     enemyX = 736

    #---------------enemy movement-----------------
    for i in range(num_of_enemies):

        #---------Game Over------

        if game_over:
            game_over_text(250,250)
            pygame.display.update()
            continue  # skip everything else


        if enemyY[i] > 500:
            # for j in range(num_of_enemies):
            #     enemyY[j] = 2000
            game_over = True
            break
            

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX[i] = 0
            enemyX_change[i] *= -1      #bounce
            enemyY[i] += 30          #move down
         

        elif enemyX[i] >= 736:
            enemyX [i]= 736
            enemyX_change[i] *= -1  #bounce
            enemyY[i] += 30        #move down
            # enemyX_change[i] *= 1.1#speed up
            enemyY_change[i] = -.3


            # ---------Collision-----------
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            collision_Sound = mixer.Sound("explosion.wav")
            collision_Sound.play()


            bulletY = 480
            bullet_state = "ready"
            score_value+= 1
            print(score_value)
            enemyX[i] = random.randint(0,800)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i], enemyY[i],i)

    #---------Bullet movement------
    if bulletY <= 0:
        bulletY = 480 
        bullet_state = "ready"



    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change  



    player(playerX, playerY)
    show_score(textX,textY)
    # game_over_text(200,250)
 
    pygame.display.update() 