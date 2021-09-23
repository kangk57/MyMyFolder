from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
ball = load_image('ball21x21xgo.png')

x = 0
frameC = 0
frameB = 0
while x < 800:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frameC * 100, 100, 100, 100, x, 90)  # clip_draw(왼쪽좌표,아래좌표,너비,높이,캔버스상의 좌표 x,캔버스상의 좌표y)
    ball.clip_draw(frameB * 23, 0, 23, 23, x+30, 60)
    update_canvas()
    frameB = (frameB + 1) % 4
    frameC = (frameC + 1) % 8  # 프레임이 계속 증가하면 이미지 영역을 벗어나기 때문에 다시 0번으로 가기 위해서 %(나머지연산) 사용
    x += 5
    delay(0.05)
    get_events()  # 나중에 설명

close_canvas()