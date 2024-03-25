import pygame
import sys

pygame.init()

bg = pygame.image.load("background.jpg")
walk_down = [pygame.image.load("walk down1.png"), pygame.image.load("walk down2.png"), pygame.image.load("walk down3.png"), pygame.image.load("walk down4.png")]
walk_left = [pygame.image.load("walk left1.png"), pygame.image.load("walk left2.png"), pygame.image.load("walk left3.png"), pygame.image.load("walk left4.png")]
walk_right = [pygame.image.load("walk right1.png"), pygame.image.load("walk right2.png"), pygame.image.load("walk right3.png"), pygame.image.load("walk right4.png")]
walk_up = [pygame.image.load("walk up1.png"), pygame.image.load("walk up2.png"), pygame.image.load("walk up3.png"), pygame.image.load("walk up4.png")]
idle_up = [pygame.image.load("idle up1.png"), pygame.image.load("idle up2.png"), pygame.image.load("idle up3.png"), pygame.image.load("idle up4.png")]
idle_down = [pygame.image.load("idle down1.png"), pygame.image.load("idle down2.png"), pygame.image.load("idle down3.png"), pygame.image.load("idle down4.png")]
idle_left = [pygame.image.load("idle left1.png"), pygame.image.load("idle left2.png"), pygame.image.load("idle left3.png"), pygame.image.load("idle left4.png")]
idle_right = [pygame.image.load("idle right1.png"), pygame.image.load("idle right2.png"), pygame.image.load("idle right3.png"), pygame.image.load("idle right4.png")]

screenWidth = 1280
screenHeight = 720

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Brawl hell")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

bullets = []
enemies = []

moves = 0

class Player():
    def __init__(self, x, y, width, height, step):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.step = step
        self.direction = "down"
        self.standing = True  

class Object():  
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

man = Player(400, 300, 64, 64, 2)
target = Object(0, 0, 50, 50, pygame.image.load("cursor.png"))


def shoot():
    bullet = Object(man.x, man.y, 10, 10, pygame.image.load("bullet.png"))
    bullet.velocity = [0, -1] 
    bullets.append(bullet)


def check_collisions(obj1, obj2):
    rect1 = pygame.Rect(obj1.x, obj1.y, obj1.width, obj1.height)
    rect2 = pygame.Rect(obj2.x, obj2.y, obj2.width, obj2.height)
    return rect1.colliderect(rect2)


def redrawGame():
    global moves

    screen.blit(bg, (0, 0))

    if man.standing:
        if man.direction == "down":
            screen.blit(idle_down[moves // 10], (man.x, man.y))
        elif man.direction == "left":
            screen.blit(idle_left[moves // 10], (man.x, man.y))
        elif man.direction == "right":
            screen.blit(idle_right[moves // 10], (man.x, man.y))
        elif man.direction == "up":
            screen.blit(idle_up[moves // 10], (man.x,man.y))
    else:
        if man.direction == "down":
            screen.blit(walk_down[moves // 10], (man.x, man.y))
        elif man.direction == "left":
            screen.blit(walk_left[moves // 10], (man.x, man.y))
        elif man.direction == "right":
            screen.blit(walk_right[moves // 10], (man.x, man.y))
        elif man.direction == "up":
            screen.blit(walk_up[moves // 10], (man.x, man.y))


    moves += 1
    if moves == 40:
        moves = 0

    for bullet in bullets:
        screen.blit(bullet.image, (bullet.x, bullet.y))

    pygame.display.update()

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          
            pass

    
    mousePos = pygame.mouse.get_pos()
    target.x = mousePos[0] - target.width / 2
    target.y = mousePos[1] - target.height / 2

 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and man.x - man.step >= 0:
        man.x -= man.step
        man.direction = "left"
        man.standing = False  
    elif keys[pygame.K_RIGHT] and man.x + man.width + man.step <= screenWidth:
        man.x += man.step
        man.direction = "right"
        man.standing = False  
    elif keys[pygame.K_UP] and man.y - man.step >= 0:
        man.y -= man.step
        man.direction = "up"
        man.standing = False  
    elif keys[pygame.K_DOWN] and man.y + man.height + man.step <= screenHeight:
        man.y += man.step
        man.direction = "down"
        man.standing = False 
    else:
        man.standing = True 

 
    for bullet in bullets:
        for enemy in enemies:
            if check_collisions(bullet, enemy):
                bullets.remove(bullet)


    redrawGame()                
                
                
                