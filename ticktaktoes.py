import pygame
from random import randint as rnd

def swap_turn():
    global turn
    turn = 'X' if turn == 'O' else 'O'


def transpose_matrix(arr):
    if not arr:
        return []

    rows = len(arr)
    cols = len(arr[0])

    transposed = [[arr[j][i] for j in range(rows)] for i in range(cols)]

    return transposed


def one_turn_to_win(turn):
    for n, row in enumerate(arr):
        if row.count(turn) == 2 and row.count(0) == 1:
            return (row.index(0), n)
    for n, row in enumerate(transpose_matrix(arr)):
        if  row.count(turn) == 2 and row.count(0) == 1:
            return (n, row.index(0))
    diag = [[arr[0][0],arr[1][1],arr[2][2]], [arr[2][0], arr[1][1], arr[0][2]]]
    print(diag, 'diag')
    if diag[0].count(turn) == 2 and diag[0].count(0) == 1:
        print('glav diag', turn)
        return (diag[0].index(0), diag[0].index(0))
    elif diag[1].count(turn) == 2 and diag[1].count(0) == 1:
        match diag[1].index(0):
            case 0:
                return (0, 2)
            case 1:
                return (1, 1)
            case 2:
                return (2, 0)
    return False

    
def bot_simple():
    axes = (rnd(0, 2), rnd(0, 2))
    print(axes)     #отладка в консоль
    if 0 in arr[0] or 0 in arr[1] or 0 in arr[2]:
        while arr[axes[1]][axes[0]] != 0:  # Выбор рандомной клетки || ПРИ ОБРАЩЕНИИ К МАТРИЦЕ В ПАМЯТИ СВАПАТЬ X Y 
            axes = (rnd(0, 2), rnd(0, 2))
            print(axes)
    else:
        tie()

    screen.blit(bot_turn(*axes), get_coordinate(*axes))
    return axes


def bot_hard():
    axes = DIAGONAL[rnd(0,3)]
    if one_turn_to_win(turn):
        axes = (one_turn_to_win(turn))
    elif one_turn_to_win(opponent):
        axes = (one_turn_to_win(opponent))
    elif arr[1][1] == 0:
        axes = (1,1)
    else:
        if 0 in [arr[DIAGONAL[i][1]][DIAGONAL[i][0]] for i in range (4)]:
            while arr[axes[1]][axes[0]] != 0:
               axes = DIAGONAL[rnd(0,3)]
        elif 0 in [arr[HORIZONTAL[i][1]][HORIZONTAL[i][0]] for i in range (4)]:
            while arr[axes[1]][axes[0]] != 0:
                axes = HORIZONTAL[rnd(0,3)]
        else:
            tie()
        
    screen.blit(bot_turn(*axes), get_coordinate(*axes))
    return axes
    
    
def bot_first():
    global endgame
    #выбор стратегии бота
    
    # x, y = bot_simple()
    x, y = bot_hard()
    
    print(x, y)
    
    if is_winning(turn):
        screen.blit(background_soft, (0,0))
        screen.blit(won(), (0, HEIGHT/2 - text_size))
        endgame = True
    elif 0 not in arr[0] and 0 not in arr[1] and 0 not in arr[2]:       #ничья?
        tie()
    
    if not endgame:
        swap_turn()     #бот -> игрок
        
        if event.type == pygame.MOUSEBUTTONDOWN and not endgame:      #Тут начало
            x = int((event.pos[0] - INDENT_X) // BLOCK)     #ход игрока
            y = int((event.pos[1] - INDENT_Y) // BLOCK)
            if x in [0, 1, 2] and y in [0, 1, 2] and arr[y][x] == 0:
                arr[y][x] = turn        #занесение в матрицу
                char_drow(turn, x, y)   #отрисовка на экране
                
              
                # print(arr)  #отладка в консоль
                
                if is_winning(turn):
                    screen.blit(background_soft, (0,0))
                    screen.blit(won(), (0, HEIGHT/2 - text_size))
                    endgame = True
                elif 0 not in arr[0] and 0 not in arr[1] and 0 not in arr[2]:       #ничья?
                    tie()
                
                swap_turn()


def player_first():
    global endgame
    if event.type == pygame.MOUSEBUTTONDOWN and not endgame:      #Тут начало
        x = int((event.pos[0] - INDENT_X) // BLOCK)     #ход игрока
        y = int((event.pos[1] - INDENT_Y) // BLOCK)
        if x in [0, 1, 2] and y in [0, 1, 2] and arr[y][x] == 0:
            arr[y][x] = turn        #занесение в матрицу
            char_drow(turn, x, y)   #отрисовка на экране
            
            
            # print(arr)  #отладка в консоль
            
            if is_winning(turn):
                screen.blit(background_soft, (0,0))

                screen.blit(won(), (0, HEIGHT/2 - text_size))
                endgame = True
            elif 0 not in arr[0] and 0 not in arr[1] and 0 not in arr[2]:       #ничья?
                tie()
                
            if not endgame:    
                swap_turn()     #игрок -> бот
                
                
                #выбор стратегии бота
                
                # x, y = bot_simple()
                x, y = bot_hard()
                print(x, y)
                
                
                # print(arr)      #отладка хода бота
            
                if is_winning(turn):
                    screen.blit(background_soft, (0,0))
                    screen.blit(won(), (INDENT_X, HEIGHT/2 - text_size))
                    endgame = True
                
                swap_turn()     #бот -> игрок


def won():
    return text_font.render(f'  Победил игрок {turn}!', True, 'Black')


def bot_turn(x, y):
    arr[y][x] = turn
    return X if turn == 'X' else O


def lines_drow():   
    pygame.draw.line(screen, 'Black', (INDENT_X, INDENT_Y + BLOCK), (INDENT_X + BLOCK * 3, BLOCK + INDENT_Y), width=5)
    pygame.draw.line(screen, 'Black', (INDENT_X, INDENT_Y + BLOCK * 2), (INDENT_X + BLOCK * 3, INDENT_Y + BLOCK * 2), width=5)
    pygame.draw.line(screen, 'Black', (INDENT_X + BLOCK, INDENT_Y), (INDENT_X + BLOCK, INDENT_Y + BLOCK * 3), width=5)
    pygame.draw.line(screen, 'Black', (INDENT_X + BLOCK * 2, INDENT_Y), (INDENT_X + BLOCK * 2, INDENT_Y + BLOCK * 3), width=5)


def get_coordinate(x, y):
    char_pos_x = INDENT_X + x * BLOCK + BLOCK / 5  # координаты символа
    char_pos_y = INDENT_Y + y * BLOCK - BLOCK / 12
    return tuple([char_pos_x, char_pos_y])


def char_drow(turn, x, y):
    screen.blit(symbol_font.render(turn, True, 'Black'), get_coordinate(x, y))
    

def is_winning(whose_turn):
    is_win = False
    for row in arr:
        if not is_win:
            if whose_turn in row:
                if set(row) == {whose_turn}:
                    is_win = True
                elif arr[1][1] == whose_turn and (
                        arr[0][2] == arr[2][0] == whose_turn or arr[0][0] == arr[2][2] == whose_turn):  # коляска
                    is_win = True
    for row in transpose_matrix(arr):
        if not is_win:
            if whose_turn in row:
                if set(row) == {whose_turn}:
                    is_win = True
    return is_win
    

def tie():
    global endgame
    endgame = True
    screen.blit(background_soft, (0,0))
    
    screen.blit(text_font.render(f'              Ничья!', True, 'Black'), (INDENT_X, HEIGHT/2 - text_size))
    
 


WIDTH, HEIGHT = 600,600

if WIDTH >= HEIGHT:
    INDENT_Y = 0
    INDENT_X = (WIDTH - HEIGHT) / 2
elif HEIGHT > WIDTH:
    INDENT_X = 0
    INDENT_Y = (HEIGHT - WIDTH) / 2


BLOCK = min(WIDTH, HEIGHT) / 3


PINK = (224, 184, 184)
arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TikTak')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
text_size = int(min(WIDTH, HEIGHT)/400*120 / 3)
symbol_font = pygame.font.Font('fonts/Montserrat-VariableFont_wght.ttf', text_size * 3)
text_font = pygame.font.Font('fonts/Montserrat-VariableFont_wght.ttf', text_size)
background = pygame.image.load('images/back.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT)) 
background_soft = background.copy()
background_soft.set_alpha(200)

screen.blit(background, (0,0))

lines_drow()

X = symbol_font.render('X', True, 'Black')
O = symbol_font.render('0', True, 'Black')

# turn = input('Чей ход. (X/O)')      
turn = 'X'

endgame = False
HORIZONTAL = [(1, 0), (0, 1), (2, 1), (1, 2)]
DIAGONAL = [(0, 0), (2, 2), (2, 0), (0, 2)]
opponent = 'X' if turn == 'O' else 'X'

    


                
    
running = True
while running:
    fpsClock.tick(FPS)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:       #обработка выхода на крестик
            running = False
            pygame.quit()
        
        player_first()
