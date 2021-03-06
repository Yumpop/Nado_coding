import pygame

pygame.init() # 반드시 필요!!

screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기 

# 화면 만들기
screen = pygame.display.set_mode((screen_width, screen_height)) 

# FPS
clock = pygame.time.Clock()

# 배경화면 만들기 
background = pygame.image.load("C:/Users/dbals/Desktop/pythonworkspace/pygame_basic/background.png")

# 캐릭터 만들기
character  = pygame.image.load("C:/Users/dbals/Desktop/pythonworkspace/pygame_basic/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구함
character_width = character_size[0] # 이미지의 가로크기를 구함
character_height = character_size[1] # 이미지의 세로 크기를 구함
character_x_pos = (screen_width /2) - (character_width /2) # 화면에서 케릭터의 가로위치를 구함
character_y_pos = screen_height - character_height  # 화면에서 케릭터의 세로위치를 구함

# 적 만들기 
enemy  = pygame.image.load("C:/Users/dbals/Desktop/pythonworkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구함
enemy_width = enemy_size[0] # 이미지의 가로크기를 구함
enemy_height = enemy_size[1] # 이미지의 세로 크기를 구함
enemy_x_pos = (screen_width /2) - (enemy_width /2) # 화면에서 케릭터의 가로위치를 구함
enemy_y_pos = (screen_height/2) - (enemy_height/2)  # 화면에서 케릭터의 세로위치를 구함

pygame.display.set_caption('minkyu game') # 게임 이름 만들기

# 이동할 좌표 
to_x = 0
to_y = 0
character_speed = 0.6

# 폰트정의
game_font = pygame.font.Font(None, 40) #  폰트객체생성

# 시간계산 
start_tick = pygame.time.get_ticks() # 현재 ticks를 받아올 수 있음

# 총 시간
total_time = 10

# 이벤트루프
running  = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임수를 나타냄

    for event in pygame.event.get():# 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: # 창이 닫히는가? (QUIT == 창닫기 버튼)
            running = False # 게임이 진행중인가 == 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러져 있을 때 
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            if event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            if event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
            if event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: # 키가 떼져 있을 때 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos >screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 세로 경계값 처리 
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


# frame에 따라 게임 캐릭터의 이동속도가 달라지면 안 되기 때문에 dt를 곱해줌
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 충돌처리를 위한 rect 정보 업데이트 
    character_rect =character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌처리 
    if character_rect.colliderect(enemy_rect):
        print('충돌났음')
        running = False 

    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 타이머 집어넣기 - 경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_tick) / 1000
    # 경과 시간(ms)을 나누어서 초(s)로 만듬

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))

    screen.blit(timer, (10,10))

    # 만약 시간이 0초 이하로 가면 게임종료
    if total_time - elapsed_time <0:
        print('타임아웃')
        running = False

    pygame.display.update() # 게임화면 다시 그리기

# 게임이 끝나고 잠시 대기
pygame.time.delay(2000)

pygame.quit() # 끝내기