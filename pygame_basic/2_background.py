import pygame

pygame.init() # 반드시 필요!!

screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기 

screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 만들기

# 배경화면 만들기 
background = pygame.image.load("C:/Users/dbals/Desktop/pythonworkspace/pygame_basic/background.png")

pygame.display.set_caption('minkyu game') # 게임 이름 만들기

running  = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():# 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: # 창이 닫히는가?
            running = False # 게임이 진행중인가 == 아님
    # screen.fill((0,0,255))
    screen.blit(background, (0,0)) # 화면 그리기

    pygame.display.update() # 게임화면 다시 그리기

pygame.quit() # 