import pygame
from random import randint as rnd


def is_winning(whose_turn):
    is_win = False
    if not is_win:
        for row in arr:
            if whose_turn in row:
                if set(row) == {whose_turn}:
                    is_win = True
                elif set([arr[j][x] for j in range(3)]) == {whose_turn}:
                    is_win = True
                elif arr[1][1] == whose_turn and (
                        arr[0][2] == arr[2][0] == whose_turn or arr[0][0] == arr[2][2] == whose_turn):  # коляска
                    is_win = True
    return is_win


def swap_turn():
    global turn
    turn = 'X' if turn == 'O' else 'O'


def won():
    return my_font_big.render(f'Победил игрок {turn}!', True, 'Black')


def get_coordinate(x, y):
    char_pos_x = indent + x * block + block / 5  # координаты символа
    char_pos_y = indent + y * block - block / 12
    return tuple([char_pos_x, char_pos_y])


def bot_turn(x, y):
    X = my_font.render('X', True, 'Black')
    O = my_font.render('0', True, 'Black')
    arr[y][x] = turn
    return X if turn == 'X' else O


def tie():
    return my_font_big.render(f'Ничья!', True, 'Black')





def bot_simple():
    axes = (rnd(0, 2), rnd(0, 2))
    print(axes)
    if 0 in arr[0] or 0 in arr[1] or 0 in arr[2]:
        while arr[axes[1]][axes[0]] != 0:  # Выбор рандомной клетки
            axes = (rnd(0, 2), rnd(0, 2))
            print(axes)
    else:
        screen.blit(tie(), (block * 0.8, block + indent))

    screen.blit(bot_turn(*axes), get_coordinate(*axes))
    return axes


WIDTH, HEIGHT = 500, 500
sq = WIDTH if WIDTH == HEIGHT else 0
indent = sq / 8
block = indent * 2
PINK = (224, 184, 184)
arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TikTak')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
my_font = pygame.font.Font('fonts/Montserrat-VariableFont_wght.ttf', 120)
my_font_big = pygame.font.Font('fonts/Montserrat-VariableFont_wght.ttf', 45)

X = my_font.render('X', True, 'Black')
O = my_font.render('0', True, 'Black')

turn = input('Чей ход. (X/O)')
# turn = 'X'
endgame = False
horizontal = [(1, 0), (0, 1), (2, 1), (1, 2)]
diagonal = [(0, 0), (2, 2), (2, 0), (0, 2)]
opponent = 'X' if turn == 'O' else 'X'

screen.fill(PINK)
pygame.draw.line(screen, 'Black', (indent, indent + block), (indent + block * 3, block + indent), width=5)
pygame.draw.line(screen, 'Black', (indent, indent + block * 2), (indent + block * 3, indent + block * 2), width=5)
pygame.draw.line(screen, 'Black', (indent + block, indent), (indent + block, WIDTH - indent), width=5)
pygame.draw.line(screen, 'Black', (indent + block * 2, indent), (indent + block * 2, WIDTH - indent), width=5)

running = True
while running:
    fpsClock.tick(FPS)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not endgame:
            x = int((event.pos[0] - indent) // block)
            y = int((event.pos[1] - indent) // block)
            if x in [0, 1, 2] and y in [0, 1, 2] and arr[y][x] == 0:
                arr[y][x] = turn
                if turn == 'X':
                    screen.blit(X, get_coordinate(x, y))  # отрисовка X или O
                else:
                    screen.blit(O, get_coordinate(x, y))
                print(arr)
                if is_winning(turn):
                    # screen.fill(PINK)
                    screen.blit(won(), (indent * 0.8, block + indent))
                    endgame = True

                swap_turn()
                x, y = bot_simple()

                # x,y = bot_hard()

                print(arr)
                if is_winning(turn):
                    # screen.fill(PINK)
                    screen.blit(won(), (indent * 0.8, block + indent))
                    endgame = True
                swap_turn()
