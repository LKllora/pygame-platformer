#color pallete

#111844   --darkest blue
#4B5694   --blue
#7288AE   --light blue
#EAE0CF   --sandy

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("uhm")
clock = pygame.time.Clock()

playerspeed = 3
player_y_velocity = 0
gravity = 0.5
on_ground = False
coyote_time = 0.15
coyote_timer = 0.1


playerimg = pygame.image.load("images/player.png")

player = pygame.transform.scale(playerimg, (100, 100))

player_rect = player.get_rect()
player_rect.center = 400, 300

platform_one = pygame.Rect(200, 400, 200, 100) 


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    dt = clock.tick(60) / 1000

    if keys[pygame.K_SPACE] and coyote_timer > 0:
        if player_y_velocity >= 0:
            player_y_velocity = -12
            on_ground = False


    if keys[pygame.K_a]:
        player_rect.x -= playerspeed

        if player_rect.colliderect(platform_one):
            player_rect.left = platform_one.right

    if keys[pygame.K_d]:
        player_rect.x += playerspeed

        if player_rect.colliderect(platform_one):
            player_rect.right = platform_one.left


    if keys[pygame.K_LSHIFT]:
        playerspeed = 6


    
    screen.fill("#111844")

    screen.blit(player, player_rect)
   #print("Player pos:", playerx, playery)

    pygame.draw.rect(screen, ("#EAE0CF"), platform_one)

    player_y_velocity += gravity

    player_rect.y += player_y_velocity


    if player_rect.colliderect(platform_one):
        if player_y_velocity > 0:

            player_rect.bottom = platform_one.top

            player_y_velocity = 0

            on_ground = True
            coyote_timer = coyote_time

    else:
        on_ground = False
        coyote_timer = max(0, coyote_timer - dt)


    if player_rect.y > 600:
        player_rect.y = 0
        player_y_velocity = 0

    print(coyote_timer)
    pygame.display.flip()

pygame.quit()