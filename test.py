import pygame




size = (1280, 720)
normal_color = (200, 50, 150)
on_color = (200, 100, 150)
buttom_size = (100, 70)
buttom_pos = (size[0]//2 - 50, size[1] - 220, buttom_size[0], buttom_size[1])

pygame.init()

window = pygame.display.set_mode(size)
pygame.display.set_caption("snake")

log = True
game = True
font = pygame.font.SysFont('Corbel', 35)
start_text = font.render('start', True, (255, 255, 255))
start_pos = (buttom_pos[0], buttom_pos[1])# + buttom_pos[2] // 2, buttom_pos[1] + buttom_pos[3] // 2)
#start_pos = (0, 10)


while log:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            log = False
            game = False
            
    mouse = pygame.mouse.get_pos()

    

    if (buttom_pos[0] <= mouse[0] <= buttom_pos[0] + buttom_pos[2] and buttom_pos[1] <= mouse[1] <= buttom_pos[1] + buttom_pos[3]):
        pygame.draw.rect(window, on_color, buttom_pos, 0)
        if(pygame.mouse.get_pressed()[0]):
            print("I'm out")
            log = False

    else: 
        pygame.draw.rect(window, normal_color, buttom_pos, 0)


    window.blit(start_text, start_pos)


    pygame.display.flip()


count_second = 1
start_ticks = pygame.time.get_ticks()
x = 600
y = 630
miku_icon = pygame.image.load("pic/miku_icon_resize.png")
snake_pos = 0
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            log = False
            game = False
    
    seconds = (pygame.time.get_ticks()-start_ticks)/1000

    pressed = pygame.key.get_pressed()

    
    #lis = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
    #x, y = move(pressed, lis, 3, x, y)
    if pressed[pygame.K_UP] and not snake_pos == 0: snake_pos = 0
    if pressed[pygame.K_DOWN]: snake_pos = 1
    if pressed[pygame.K_LEFT]: snake_pos = 2
    if pressed[pygame.K_RIGHT]: snake_pos = 3
    #print(count_second < seconds)
    if (count_second > seconds): continue
    count_second += 0.2
    

    if snake_pos == 0:  y = y - 10
    if snake_pos == 1:  y = y + 10
    if snake_pos == 2:  x = x - 10
    if snake_pos == 3:  x = x + 10



    window.fill((0, 0, 0))
    window.blit(miku_icon, (x, y))
    pygame.display.flip()

    


pygame.quit()