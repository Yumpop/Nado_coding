from random import random


import random
import pygame
###################################################################################
# 기본 초기화 (반드시 해야 할 것)
pygame.init()

screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기 

# 화면 만들기
screen = pygame.display.set_mode((screen_width, screen_height)) 

# 화면 title
pygame.display.set_caption('똥 피하기 게임')

# 배경 만들기
background = pygame.image.load('C:/Users/dbals/Desktop/pythonworkspace/pygame_basic/w_background.png')

# 캐릭터 
character = pygame.image.load('C:/Users/dbals/Desktop/pythonworkspace/pygame_basic/character.png')
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width /2) - (character_width /2)
character_y_pos = screen_height - character_height

#적
enemy = pygame.image.load('C:/Users/dbals/Desktop/pythonworkspace/pygame_basic/ddong.png')
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0,screen_width - enemy_width)
enemy_y_pos = -(enemy_height)

# FPS
clock = pygame.time.Clock()

###################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트, 속도 등)

# 캐릭터 속도
to_x = 0
to_y = 0
character_speed = 0.6

# 적 속도
to_x_enemy = 0
to_y_enemy = 0
enemy_speed = 0.6

running  = True 
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임수를 나타냄
    
    # 2. 이벤트 처리 (키보드,  마우스)
    for event in pygame.event.get():# 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: # 창이 닫히는가? (QUIT == 창닫기 버튼)
            running = False # 게임이 진행중인가 == 아님

    # 3. 게임 케릭터 위치 정의
        # 키다운할때 움직임구현
        if event.type == pygame.KEYDOWN: # 키가 눌러져 있을 때 
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            if event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
        
        # 키가 떼져 있을 때
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    # 적 움직임 구현
    enemy_y_pos += enemy_speed * dt
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0,screen_width - enemy_width)

    # 캐릭터 움직임
    character_x_pos += to_x *dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos >screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print('The End')
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update() # 게임화면 다시 그리기

pygame.quit() # 끝내기