
import pygame

pygame.init()

pygame.display.set_icon(pygame.image.load('images/gameicon.png'))
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("uhm")
clock = pygame.time.Clock()

maxspeed = 5
player_y_velocity = 0
player_x_velocity = 0
acceleration = 0.25
gravity = 0.5
on_ground = False
coyote_time = 0.1
coyote_timer = 0.1


playerleft = pygame.transform.scale(pygame.image.load("images/aple_left.png"), (48, 48))
playerright = pygame.transform.scale(pygame.image.load("images/aple_right.png"), (48, 48))

player = playerright

player_rect = player.get_rect()
player_rect.center = 400, 300

platforms = [
    pygame.Rect(200, 400, 200, 100),
    pygame.Rect(400, 300, 200, 100)
]






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
        
        player = playerleft

        player_x_velocity -= acceleration

        for platform in platforms:
            if player_rect.colliderect(platform):
                player_rect.left = platform.right


    if keys[pygame.K_d]:
        
        player = playerright

        player_x_velocity += acceleration

        for platform in platforms:
            if player_rect.colliderect(platform):
                player_rect.right = platform.left

    if not keys[pygame.K_d] and not keys[pygame.K_a]:
        if player_x_velocity > 0:
            player_x_velocity -= acceleration

        elif player_x_velocity < 0:
            player_x_velocity += acceleration


    player_x_velocity = max(-maxspeed, min(maxspeed, player_x_velocity))

    player_rect.x += player_x_velocity
    
    screen.fill("#FDC086")

    screen.blit(player, player_rect)
   #print("Player pos:", playerx, playery)


    for platform in platforms:
        pygame.draw.rect(screen, ("#73976A"), platform)

    player_y_velocity += gravity

    player_rect.y += player_y_velocity

    for platform in platforms:
        if player_rect.colliderect(platform):
            if player_y_velocity > 0:

                player_rect.bottom = platform.top

                player_y_velocity = 0

                on_ground = True
                coyote_timer = coyote_time

        else:
            on_ground = False
            coyote_timer = max(0, coyote_timer - dt)


    if player_rect.y > 600:
        player_rect.y = 0
        player_y_velocity = 0

    print(player_x_velocity)
    pygame.display.flip()

pygame.quit()