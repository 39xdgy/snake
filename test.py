import pygame, random




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

star_x = random.randint(20, 1260)
star_y = random.randint(20, 700)

space = 20
snack_list = [(x, y)]#, (x+20, y + 30), (x+20, y + 60)]

#testing
#for i in range(1, 3):
#    snack_list.append((x, y + space * i))

miku_icon = pygame.image.load("pic/miku_icon_resize.png")
girl_icon = pygame.image.load("pic/girl.png")

changed = False

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
    if pressed[pygame.K_UP] and not snake_pos <= 1 and not changed: 
        changed = True
        snake_pos = 0
    if pressed[pygame.K_DOWN] and not snake_pos <= 1 and not changed: 
        changed = True
        snake_pos = 1
    if pressed[pygame.K_LEFT] and not snake_pos >= 2 and not changed: 
        changed = True
        snake_pos = 2
    if pressed[pygame.K_RIGHT] and not snake_pos >= 2 and not changed: 
        changed = True
        snake_pos = 3
    
    if (count_second > seconds): continue
    count_second += 0.2
    changed = False


    if snake_pos == 0:  y = y - space
    if snake_pos == 1:  y = y + space
    if snake_pos == 2:  x = x - space
    if snake_pos == 3:  x = x + space

    #snack_list = [(x, y)] + snack_list[0:len(snack_list)-1]
    #snack_list[0] = (snack_list[0][0], snack_list[0][1])
    window.fill((0, 0, 0))

    for pos in snack_list[0:len(snack_list)-1]:
        green_square = pygame.Rect(pos[0], pos[1], 20, 20)
        pygame.draw.rect(window, (0, 255, 0), green_square)
        #window.blit(girl_icon, pos)


    #window.blit(miku_icon, (x, y))
    red_square = pygame.Rect(x, y, 20, 20)
    pygame.draw.rect(window, (255, 0, 0), red_square)
    snack_list = [(x, y)] + snack_list[0:len(snack_list)-1]

    star = pygame.image.load("pic/star_resize.png")

    if(abs(x - star_x) < space and abs(y - star_y) < space):
        star_x = random.randint(20, 1260)
        star_y = random.randint(20, 700)
        snack_list.append((snack_list[-1][0], snack_list[-1][1] + space * len(snack_list)))

    window.blit(star, (star_x, star_y))

    pygame.display.flip()

    


pygame.quit()