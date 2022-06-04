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


running  = True 
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임수를 나타냄
    
    # 2. 이벤트 처리 (키보드,  마우스)
    for event in pygame.event.get():# 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: # 창이 닫히는가? (QUIT == 창닫기 버튼)
            running = False # 게임이 진행중인가 == 아님

    # 3. 게임 케릭터 위치 정의
    
    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(stage,(0,screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임화면 다시 그리기

pygame.quit() # 끝내기