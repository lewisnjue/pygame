# exmaple file showing a basic pygame game loop 

import pygame 

pygame.init() 

scren = pygame.display.set_mode((1280,720))# the tuple inside the the size of the window 
clock = pygame.time.Clock() 

running = True
dt = 0 
player_pos = pygame.Vector2(scren.get_width() / 2, scren.get_height() /2 ) 
print(player_pos)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    scren.fill("purple")
    pygame.draw.circle(scren,'red',player_pos,40)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt 
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt 
    if keys[pygame.K_a]:
        player_pos.x -= 300 *  dt 
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt 

    pygame.display.flip()
    dt = clock.tick(60) / 1000 
    clock.tick(60) 

pygame.quit()
