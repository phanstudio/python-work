import pygame
from pygame import display
from pygame import draw
from pygame import mouse
from pygame import key
from pygame.constants import K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_KP_ENTER, K_SPACE
from pygame import font
from soduku_solver import valid, find_empty


"""
if True:
    pygame.init()
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Game Cube")

    x = 50
    y = 50
    width = 40
    height = 40
    vel = 5
    is_jump = False
    jump_count = 10

    def main():
        pygame.time.delay(100)
        #Ready methods
        global x
        global y
        global width
        global height
        global vel
        global is_jump
        global jump_count
        
        #Key inputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
        if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - width - vel:
            x += vel
        if not (is_jump):
            if keys[pygame.K_UP] and x > vel:
                y -= vel
            if keys[pygame.K_DOWN] and x < SCREEN_HEIGHT - width - vel:
                y += vel
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            #Jump code
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1
                y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 10

        #Draw function
        win.fill((0,0,0))
        pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
        pygame.display.update()
    
    if True:
        running = True
        init = False
        while running:
            main()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
"""
pygame.init()
SCREEN_WIDTH = (450, 450)
win = display.set_mode(SCREEN_WIDTH)
display.set_caption("Sudoku")
selected = False
posz = (0, 0)
ft = font.Font("freesansbold.ttf", 32)
fs = font.Font("freesansbold.ttf", 16)
f =[]
solv = True

board = [
    [7,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,2,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def draw_grid(w, rows, surface):
    size_btw1 = w // rows[0]
    size_btw2 = w // rows[1]
    x1 = 1
    y1 = 1
    x2 = 2
    y2 = 2

    if True:
        z = 3
        draw.line(surface, (0,0,0), (0, 0 + (z - 2)), (w, 0 + (z - 2)), z)
        draw.line(surface, (0,0,0), (0 + (z - 2), 0), (0 + (z - 2), w), z)
        draw.line(surface, (0,0,0), (w - (z - 1), 0), (w - (z - 1), w), z)
        draw.line(surface, (0,0,0), (0, w - (z - 1)), (w, w - (z - 1)), z)
    for i in range(rows[0]):
        x1 = x1 + size_btw1
        y1 = y1 + size_btw1
        draw.line(surface, (0,0,0), (x1, 0), (x1, w), 2)
        draw.line(surface, (0,0,0), (0, y1), (w, y1), 2)
    for i in range(rows[1]):
        x2 = x2 + size_btw2
        y2 = y2 + size_btw2
        draw.line(surface, (0,0,0), (x2, 0), (x2, w))
        draw.line(surface, (0,0,0), (0, y2), (w, y2))

    return size_btw2

def get_mouse_pos():
    keys = mouse.get_pos()
    square_pos = (0, 0)
    pos = (0, 0)

    if (keys[0] // 50) != (square_pos[0] // 50):
        square_pos = (keys[0] // 50,square_pos[1])
        pos = (square_pos[0] * 50, pos[1])
    if (keys[1] // 50) != (square_pos[1] // 50):
        square_pos = (square_pos[0], keys[1] // 50)
        pos = (pos[0], square_pos[1] * 50)

    return pos

def get_mouse_click(pos):
    global selected, posz, f
    mouses = mouse.get_pressed()
    keys = key.get_pressed()
    
    
    if mouses[0]:
        if board[int(pos[1] / 50)][int(pos[0] / 50)] == 0:
            selected = True
            posz = pos
    if keys[K_KP_ENTER]:
        if f != []:
            check()
        f = []
        selected = False

def get_input():
    global f, win, solv
    k = "0"
    if selected == True:
        keys = key.get_pressed()
        if keys[K_1]: k = key.name(K_1)
        if keys[K_2]: k = key.name(K_2)
        if keys[K_3]: k = key.name(K_3)
        if keys[K_4]: k = key.name(K_4)
        if keys[K_5]: k = key.name(K_5)
        if keys[K_6]: k = key.name(K_6)
        if keys[K_7]: k = key.name(K_7)
        if keys[K_8]: k = key.name(K_8)
        if keys[K_9]: k = key.name(K_9)

        if k != "0":
            if [posz[0],posz[1],k] not in f:
                if f != []:
                    for j, i in enumerate(f):
                        if i[0] == posz[0] and i[1] == posz[1]:
                            f[j] = ([posz[0],posz[1], k])
                            break
                    else:
                        f.append([posz[0],posz[1], k])
                else:
                    f.append([posz[0],posz[1], k])
        
        if f != []:
            for i in f:
                fonts = fs.render(i[2], True, (20,20,20))
                win.blit(fonts, ((i[0]) + 8, (i[1]) + 8))
    solv = solver()

def check():
    global f
    for i in f:
        if valid(board, int(i[2]), (int(i[1] / 50), int(i[0] / 50))):
            board[int(i[1] / 50)][ int(i[0] / 50)] = int(i[2])

def solver():
    keys = key.get_pressed()
    if keys[K_SPACE]:
        return solve(board)

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        fonts = ft.render(str(i), True, (20,20,20))
        if valid(bo, i, (row, col)):
            #win.blit(fonts, ((col * 50) + 8, (row * 50) + 8))
            #display.update()
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0
    
    return False

run = True
while run:
    #Draw function
    win.fill((255, 255, 255))
    square_size = draw_grid(SCREEN_WIDTH[0], (3, 9), win)
    pos = get_mouse_pos()
    s = get_mouse_click(pos)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                fonts = ft.render(str(board[i][j]), True, (0, 0, 0))
                win.blit(fonts, ((50 * j) + 8, (50 * i) + 8))

        if not 0 in board[i] or solv == False:
            run = False
            print("Thanks for playing!")

    if selected == False:
        if board[int(pos[1] / 50)][int(pos[0] / 50)] == 0:
            if pos == (SCREEN_WIDTH[0] - square_size, SCREEN_WIDTH[1] - square_size):
                draw.rect(win, (255, 255, 0), (4 + pos[0],4 + pos[1],square_size - 9,square_size - 9), 2)
            elif pos[0] == SCREEN_WIDTH[0] - square_size:
                draw.rect(win, (255, 255, 0), (4 + pos[0],4 + pos[1],square_size - 9,square_size - 4), 2)
            elif pos[1] == SCREEN_WIDTH[0] - square_size:
                draw.rect(win, (255, 255, 0), (4 + pos[0],4 + pos[1],square_size - 4,square_size - 9), 2)
            else:
                draw.rect(win, (255, 255, 0), (4 + pos[0],4 + pos[1],square_size - 4,square_size - 4), 2)
            posz = pos
        else:
            if pos == (SCREEN_WIDTH[0] - square_size, SCREEN_WIDTH[1] - square_size):
                draw.rect(win, (255, 0, 0), (3 + pos[0],3 + pos[1],square_size - 7,square_size - 7), 2)
            elif pos[0] == SCREEN_WIDTH[0] - square_size:
                draw.rect(win, (255, 0, 0), (3 + pos[0],3 + pos[1],square_size - 7,square_size - 2), 2)
            elif pos[1] == SCREEN_WIDTH[0] - square_size:
                draw.rect(win, (255, 0, 0), (3 + pos[0],3 + pos[1],square_size - 2,square_size - 7), 2)
            else:
                draw.rect(win, (255, 0, 0), (3 + pos[0],3 + pos[1],square_size - 2,square_size - 2), 2)
    else:
        get_input()
        draw.rect(win, (0, 255, 0), (3 + posz[0],3 + posz[1],square_size - 2,square_size - 2), 2)
    
    display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False