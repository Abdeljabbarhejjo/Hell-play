import pygame
import sys

pygame.init()

bg = pygame.image.load("sand3.jpg")
walk_down = [pygame.image.load("walk down1.png"), pygame.image.load("walk down2.png"), pygame.image.load("walk down3.png"), pygame.image.load("walk down4.png")]

walk_left = [pygame.image.load("walk left1.png"), pygame.image.load("walk left2.png"), pygame.image.load("walk left3.png"), pygame.image.load("walk left4.png")]

walk_right = [pygame.image.load("walk right1.png"), pygame.image.load("walk right2.png"), pygame.image.load("walk right3.png"), pygame.image.load("walk right4.png")]

walk_up = [pygame.image.load("walk up1.png"), pygame.image.load("walk up2.png"), pygame.image.load("walk up3.png"), pygame.image.load("walk up4.png")]

idle_up = [pygame.image.load("idle up1.png"), pygame.image.load("idle up2.png"), pygame.image.load("idle up3.png"), pygame.image.load("idle up4.png")]

idle_down = [pygame.image.load("idle down1.png"), pygame.image.load("idle down2.png"), pygame.image.load("idle down3.png"), pygame.image.load("idle down4.png")]

idle_left = [pygame.image.load("idle left1.png"), pygame.image.load("idle left2.png"), pygame.image.load("idle left3.png"), pygame.image.load("idle left4.png")]

idle_right = [pygame.image.load("idle right1.png"), pygame.image.load("idle right2.png"), pygame.image.load("idle right3.png"), pygame.image.load("idle right4.png")]

screenWidth = 800
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Brawl hell")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

moves = 0

class Player():
    def __init__(self, x, y, width, height, step):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.step = step
        self.direction = "down"
        self.standing = True  # تعيين متغير standing لتحديد حالة الوقوف

man = Player(400, 300, 64, 64, 2)

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
            screen.blit(idle_up[moves // 10], (man.x, man.y))
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

    pygame.display.update()

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and man.x - man.step >= 0:
        man.x -= man.step
        man.direction = "left"
        man.standing = False  # تحديث حالة الوقوف
    elif keys[pygame.K_RIGHT] and man.x + man.width + man.step <= screenWidth:
        man.x += man.step
        man.direction = "right"
        man.standing = False  # تحديث حالة الوقوف
    elif keys[pygame.K_UP] and man.y - man.step >= 0:
        man.y -= man.step
        man.direction = "up"
        man.standing = False  # تحديث حالة الوقوف
    elif keys[pygame.K_DOWN] and man.y + man.height + man.step <= screenHeight:
        man.y += man.step
        man.direction = "down"
        man.standing = False  # تحديث حالة الوقوف
    else:
        man.standing = True  # إذا لم تتم الحركة، فاللاعب في وضع الوقوف

    redrawGame()
                
                
                
                