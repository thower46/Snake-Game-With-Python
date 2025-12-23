import pygame
import random

sw = 1920
sh = 1080
    
# System Variables
tile = 40
gw = sw // tile
gh = sh // tile
x = 960
y = 540
snake = [(x,y)]
dx = 0
dy = 0
move_delay = 120
last_move = 0
max_x = sw - tile
max_y = sh - tile
pygame.init()
pygame.display.set_caption("My Snake Game")
screen = pygame.display.set_mode((sw, sh))
clock = pygame.time.Clock()

apple = pygame.Surface((tile, tile))
apple.fill("Red")

player = pygame.Surface((tile, tile))
player.fill("White")
def aaple():
   while True:
        ax = random.randint(0, (sw - tile) // tile) * tile
        ay = random.randint(0, (sh - tile) // tile) * tile
        if (ax, ay) not in snake:
            return ax, ay
    
ax, ay = aaple()
# Main Loop
running = True
while running:
    screen.fill("Black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        dx = -tile
        dy = 0

    if keys[pygame.K_d]:
        dx = tile
        dy = 0
    
    if keys[pygame.K_s]:
        dx = 0
        dy = tile

    if keys[pygame.K_w]:
        dx = 0
        dy = -tile
    now = pygame.time.get_ticks()
    if now - last_move >= move_delay:
        x += dx
        y += dy

        last_move = now
        
        snake.insert(0, (x,y))
        
        player_rect = pygame.Rect(x, y, tile, tile)
        apple_rect = pygame.Rect(ax, ay, tile, tile)
        print(ax)
        print(ay)
        
        if player_rect.colliderect(apple_rect):
            ax, ay = aaple()
            # grow → do NOT pop
        else:
            snake.pop()

    for segment in snake:
        screen.blit(player, segment)

    screen.blit(apple, (ax, ay))
    
    pygame.display.update()

    clock.tick(60)
pygame.quit()
