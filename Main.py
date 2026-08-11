import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("uhm")
clock = pygame.time.Clock()

playerspeed = 3
player_y_velocity = 0
gravity = 0.5
on_ground = False

playerimg = pygame.image.load("images/player2.png")

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

    if keys[pygame.K_SPACE] and on_ground == True:
        player_y_velocity = -12
        on_ground = False

    if keys[pygame.K_a]:
        player_rect.x -= playerspeed
    if keys[pygame.K_d]:
        player_rect.x += playerspeed
    if keys[pygame.K_LSHIFT]:
        playerspeed = 6


    
    screen.fill("#321E48")

    screen.blit(player, player_rect)
   #print("Player pos:", playerx, playery)

    pygame.draw.rect(screen, ("#65DCD5"), platform_one)



    if player_rect.colliderect(platform_one):
        on_ground = True
        player_y_velocity = 0
        player_rect.bottom = platform_one.top

    if on_ground == False:
        player_y_velocity += gravity
        player_rect.y += player_y_velocity



    pygame.display.flip()

    clock.tick(60)

pygame.quit()