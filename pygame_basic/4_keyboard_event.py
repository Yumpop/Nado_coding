import pygame

pygame.init() # 반드시 필요!!

screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기 

screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 만들기

# 배경화면 만들기 
background = pygame.image.load("C:/Users/dbals/Desktop/pythonworkspace/pygame_basic/background.png")

# 캐릭터 만들기
character  = pygame.image.load("C:/Users/dbals/Desktop/pythonworkspace/pygame_basic/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구함
character_width = character_size[0] # 이미지의 가로크기를 구함
character_height = character_size[1] # 이미지의 세로 크기를 구함
character_x_pos = (screen_width /2) - (character_width /2) # 화면에서 케릭터의 가로위치를 구함
character_y_pos = screen_height - character_height  # 화면에서 케릭터의 세로위치를 구함


pygame.display.set_caption('minkyu game') # 게임 이름 만들기

# 이동할 좌표 
to_x = 0
to_y = 0

running  = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():# 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: # 창이 닫히는가? (QUIT == 창닫기 버튼)
            running = False # 게임이 진행중인가 == 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러져 있을 때 
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= 3
            if event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += 3
            if event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= 3
            if event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += 3

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
    if character_y_pos <0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    character_x_pos += to_x
    character_y_pos += to_y

    screen.blit(background, (0,0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터그리기

    pygame.display.update() # 게임화면 다시 그리기

pygame.quit() # 끝내기