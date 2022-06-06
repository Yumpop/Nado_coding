import pygame
###################################################################################
# 기본 초기화 (반드시 해야 할 것)
pygame.init()

screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기 

# 화면 만들기
screen = pygame.display.set_mode((screen_width, screen_height)) 

# FPS
clock = pygame.time.Clock()

###################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트, 속도,  등)


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


    pygame.display.update() # 게임화면 다시 그리기

pygame.quit() # 끝내기