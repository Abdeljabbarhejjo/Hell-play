import pygame
import sys

pygame.init()

game_active = False
main_screen = True

font = pygame.font.Font(None,32)
font1 = pygame.font.Font(None,64)
font2 = pygame.font.Font(None,72)

screenWidth = 800
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.toggle_fullscreen()
pygame.display.set_caption("Circle Move to Click")

setting_icon = pygame.image.load('settings.png').convert_alpha()
setting_rect = setting_icon.get_rect(topleft = (720,50))

RED = (255, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# Circle properties
circle_radius = 5
circle_color = RED
circle_position = pygame.math.Vector2(screenWidth // 2, screenHeight // 2)  # Initial position
click_position = None  # Initialize click position

while True:
    mouse_pos = pygame.mouse.get_pos()
    screen.fill(BLACK)
    setting_icon = pygame.transform.scale(setting_icon,(30,30))
    screen.blit(setting_icon,setting_rect)

    if setting_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            game_active = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_active = not game_active
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button clicked
                click_position = pygame.math.Vector2(event.pos)

    if main_screen == True:
        screen.fill((40,70,50))
        text2 = font2.render("Help !",True,(40,120,50))
        text3 = font2.render("Start",True,(40,20,50))

        text2_rect = pygame.Rect(310,340,200,60)
        pygame.draw.rect(screen,(40,120,100),text2_rect)
        screen.blit(text2,(340,250))

        if text2_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (40, 150, 100), text2_rect)
            if pygame.mouse.get_pressed()[0]:
                game_active = True
                main_screen = False

        else:
            pygame.draw.rect(screen, (40, 120, 100), text2_rect)
        screen.blit(text3, text2_rect.topleft)
    else:
        pass
                # Store the click position
    if game_active:
        # Move the circle towards the click position if it exists
        if click_position is not None:
            direction = click_position - circle_position
            distance = direction.length()
            if distance > 1:  # Only move if the distance is greater than 1 pixel to avoid teleporting
                direction.normalize_ip()
                circle_position += direction

        # Draw the circle
        pygame.draw.circle(screen, circle_color, (int(circle_position.x), int(circle_position.y)), circle_radius)
    if game_active == False and main_screen == False:
        screen.fill((200,200,200))
        text = font.render("Game is paused",True,(20,20,30))
        text1 = font1.render("Exit",True,(200,200,200))
        text3 = font.render("Resume", True, (200, 200, 200))
        screen.blit(text,(310,280))
        button_1 = pygame.Rect(349,320,100,50)

        button_2 = pygame.Rect(349, 380, 100, 50)
        if button_1.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (80, 80, 100), button_1)
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(screen, (40, 40, 60), button_1)
        screen.blit(text1,button_1.topleft)
        if button_2.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (80, 80, 100), button_2)
            if pygame.mouse.get_pressed()[0]:
                game_active = True
        else :
            pygame.draw.rect(screen, (40, 40, 60), button_2)
        screen.blit(text3, button_2.midleft)




    pygame.display.flip()
    clock.tick(60)
