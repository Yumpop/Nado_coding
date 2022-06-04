# 공 튕기기 부터 듣기
from xml.dom.minidom import CharacterData
import pygame
import os
###################################################################################
# 기본 초기화 (반드시 해야 할 것)
pygame.init()

screen_width = 640  # 가로 크기
screen_height = 480  # 세로 크기 

# 화면 만들기
screen = pygame.display.set_mode((screen_width, screen_height)) 

# 화면 타이틀 설정
pygame.display.set_caption('pang')

# FPS
clock = pygame.time.Clock()

###################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트, 속도,  등)
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'images')

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, 'background.jpg'))

# 스테이지 만들기
stage =  pygame.image.load(os.path.join(image_path, 'stage.png'))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, 'character.png'))
character_size = character.get_rect().size
character_weight = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_weight)
character_y_pos = screen_height - character_height - stage_height

# 캐릭터 이동
character_to_x = 0

# 캐릭터 이동속도
character_speed = 5

# 무기 만들기 
weapon = pygame.image.load(os.path.join(image_path, 'weapon.png'))
weapon_size = weapon.get_rect().size
weapon_height = weapon_size[1]
weapon_weight = weapon_size[0]

# 무기 한번에 여러개 발사
weapons = []

# 무기이동속도
weapon_speed = 10

# 공 만들기 
ball_images = [
    pygame.image.load(os.path.join(image_path, 'ball1.png')),
    pygame.image.load(os.path.join(image_path, 'ball1.png')),
    pygame.image.load(os.path.join(image_path, 'ball1.png')),
    pygame.image.load(os.path.join(image_path, 'ball1.png'))
]

# 공 크기에 따른 최초 스피드 
ball_speed_y = [-18, -15, -12, -9] # 인덱스로 표현

# 최초 발생하는 큰 공 추가
balls = []

balls.append({
    'pos_x' : 50,
    'pos_y' : 50,
    'img_inx' : 0, # 공의 이미지 인덱스, 첫번째 공
    'to_x' : 3,
    'to_y' : -6,
    'init_spd_y' : ball_speed_y[0]})

running  = True 
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임수를 나타냄
    
    # 2. 이벤트 처리 (키보드,  마우스)
    for event in pygame.event.get():# 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: # 창이 닫히는가? (QUIT == 창닫기 버튼)
            running = False # 게임이 진행중인가 == 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            if event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_weight/2) -(weapon_weight/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos]) 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
               
    # 3. 게임 케릭터 위치 정의
    character_x_pos += character_to_x
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_weight:
        character_x_pos = screen_width - character_weight

    # 무기 이동
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] >0]

    # 4. 충돌 처리

    # 5. 화면에 그리기 - 먼저 blit한 순서대로 그려짐
    screen.blit(background, (0,0))
    
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage,(0,screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))


    pygame.display.update() # 게임화면 다시 그리기

pygame.quit() # 끝내기