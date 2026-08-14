import pygame
from pathlib import Path

pygame.init()

base_dir = Path(__file__).resolve().parent
image_dir = base_dir / "Images"


pygame.display.set_icon(pygame.image.load(image_dir / "gameicon.png"))
pygame.display.set_caption("uhm")

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

maxspeed = 5

player_y_velocity = 0
player_x_velocity = 0
acceleration = 0.25

on_ground = False

jumps_available = 2
jump_power = -11.5
gravity = 0.5
coyote_time = 0.1
coyote_timer = 0.1

anim_timer = 0
anim_speed = 0.1
anim_frame = 0

playeridle = pygame.transform.scale(pygame.image.load(image_dir / "aple_idle.png"), (42, 48))
playerfall = pygame.transform.scale(pygame.image.load(image_dir / "aple_fall.png"), (42, 48))


player_right = [
    pygame.transform.scale(pygame.image.load(image_dir / "aple_right1.png"), (42, 48)),
    pygame.transform.scale(pygame.image.load(image_dir / "aple_right2.png"), (42, 48))
]

player_left = [
    pygame.transform.scale(pygame.image.load(image_dir / "aple_left1.png"), (42, 48)),
    pygame.transform.scale(pygame.image.load(image_dir / "aple_left2.png"), (42, 48))
]

player = playeridle

player_rect = player.get_rect()
player_rect.center = 400, 0 #spawn location

platforms = [
    pygame.Rect(200, 400, 200, 100),
    pygame.Rect(400, 300, 200, 100)
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed() # quit event

    dt = clock.tick(60) / 1000 

#--inputs
    if keys[pygame.K_a] or keys[pygame.K_d]:

        anim_timer += dt

        if anim_timer > anim_speed:
            anim_timer = 0
            anim_frame += 1

            if anim_frame >= 2:
                anim_frame = 0




    if keys[pygame.K_SPACE] and jumps_available > 0:
        if coyote_timer > 0 or on_ground or jumps_available < 2:
            if player_y_velocity >= 0:
                player_y_velocity = jump_power
                on_ground = False
                jumps_available -= 1

    if keys[pygame.K_a]:
        player_x_velocity -= acceleration

    if keys[pygame.K_d]:
        player_x_velocity += acceleration

#--X movement


#--friction
    if not keys[pygame.K_d] and not keys[pygame.K_a]: 
        if player_x_velocity > 0:
            player_x_velocity -= acceleration

        elif player_x_velocity < 0:
            player_x_velocity += acceleration
            
#--collision
    for platform in platforms:

        if player_rect.colliderect(platform):
            if player_x_velocity > 0:
                player_rect.right = platform.left
                

            elif player_x_velocity < 0:
                player_rect.left = platform.right

                
    player_x_velocity = max(-maxspeed, min(maxspeed, player_x_velocity)) #limiting max speed
    player_rect.x += player_x_velocity #moving the player along x
    
    screen.fill("#FDC086") #sky

    screen.blit(player, player_rect)

    for platform in platforms:
        pygame.draw.rect(screen, ("#73976A"), platform) #platforms

#--Y movement
    old_bottom = player_rect.bottom

#--move the player

    player_y_velocity += gravity
    player_rect.y += player_y_velocity

    on_ground = False


#--collisions
    for platform in platforms:
        if player_rect.colliderect(platform):
            if player_y_velocity > 0 and old_bottom <= platform.top:

                player_rect.bottom = platform.top

                player_y_velocity = 0
                on_ground = True
                jumps_available = 2
                coyote_timer = coyote_time
        else:
            on_ground = False
            coyote_timer = max(0, coyote_timer - dt)

#--animations
    if player_y_velocity > 0 and not on_ground or jumps_available < 1:
        player = playerfall
    elif player_x_velocity > 0:
        player = player_right[anim_frame]
    elif player_x_velocity < 0:
        player = player_left[anim_frame]
    else: 
        player = playeridle
        

#--stop the player from going out of bounds
    if player_rect.y > 600:
        player_rect.y = 0
        player_y_velocity = 0
    if player_rect.x > 800:
        player_rect.x = 0
    elif player_rect.x < 0:
        player_rect.x = 600

    print(jumps_available)
    pygame.display.flip()

pygame.quit()