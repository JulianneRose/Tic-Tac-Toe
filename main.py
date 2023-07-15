import pygame, json
from Classes import Button

pygame.init()

SCREEN = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic Tac Toe")
    
def get_font(size):
    return pygame.font.Font("font.ttf", size)

history = {}
with open("history.json", "a+") as f:
    f.seek(0)
    history = json.load(f)

blockX = pygame.image.load("X.png")
blockO = pygame.image.load("O.png")
active = pygame.image.load("active.png")
endscreen = pygame.image.load("endscreen.png")

clock = pygame.time.Clock()

buttons = []
for i in range(9):
    x = i % 3 * 200 + 100
    y = i // 3 * 200 + 100
    buttons.append(Button(pygame.image.load("button.png"), (x, y), get_font(40)))

diaX = 0
horX = 0
verX = 0
diaO = 0
horO = 0
verO = 0

count = 0

# Game loop
while True:
    board = [0, 0, 0,
             0, 0, 0,
             0, 0, 0]
    # Play loop
    Menu = True
    Play = True
    End = True
    draw = False
    playerturn = "X"

    while Menu:
        SCREEN.blit(active, (0, 0))

        clock.tick(100)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Menu = False

    diaX = 0
    horX = 0
    verX = 0
    diaO = 0
    horO = 0
    verO = 0

    while Play:

        SCREEN.blit(pygame.image.load("board.png"), (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()

        for i in range(0, 7, 3):
            if horX == 3 or horO == 3:
                break
            horX = 0
            horO = 0
            for j in range(i, i+3):
                if board[j] == "X":
                    horX = horX + 1
                elif board[j] == "O":
                    horO = horO + 1

        diaX = 0
        diaO = 0
        for i in range(0, 9, 4):
            if board[i] == "X":
                diaX += 1
            elif board[i] == "O":
                diaO += 1
        
        if diaX == 3 or diaO == 3:
            pass
        else:
            diaX = 0
            diaO = 0
            for i in range(2, 7, 2):
                if board[i] == "X":
                    diaX += 1
                elif board[i] == "O":
                    diaO += 1

        for i in range(3):
            if verX == 3 or verO == 3:
                break
            verX = 0
            verO = 0
            for j in range(i, i+7, 3):
                if board[j] == "X":
                    verX += 1
                elif board[j] == "O":
                    verO += 1 

        for i in range(9):
            if board[i] == "X":
                SCREEN.blit(blockX, (i % 3 * 200, i // 3 * 200))
            elif board[i] == "O":
                SCREEN.blit(blockO, (i % 3 * 200, i // 3 * 200))

        for button in buttons:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        con = diaX, horX, verX, diaO, horO, verO

        for i in con:
            if i == 3:
                Play = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(9):
                    if buttons[i].checkForInput(MOUSE_POS):
                        if board[i] in ("X", "O"):
                            break
                        board[i] = f"{playerturn}"
                        if playerturn == "X":
                            playerturn = "O"
                        elif playerturn == "O":
                            playerturn = "X"
        if 0 not in board and Play != False:
            draw = True
            Play = False

        clock.tick(100)
        pygame.display.update()

    else:
        if playerturn == "X":
            playerturn = "O"
        elif playerturn == "O":
            playerturn = "X"

    while End:
        SCREEN.blit(endscreen, (0, 0))

        if not draw:
            wintxt = get_font(100).render(f'{playerturn} Won!', True, "White")
            winrect = wintxt.get_rect(center=(300, 300))
        else:
            wintxt = get_font(50).render(f'It is a draw', True, "White")
            winrect = wintxt.get_rect(center=(300, 300))
        SCREEN.blit(wintxt, winrect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    End = False

        clock.tick(100)
        pygame.display.update()

    if draw:
        history['lastgames'].append("It was a draw!")
    elif playerturn == "O":
        history['lastgames'].append("0 Won!")
    elif playerturn == "X":
        history['lastgames'].append("X Won!")
    if len(history['lastgames']) > 9:
        history['lastgames'].pop(0)

    Past = True
    while Past:
        SCREEN.blit(endscreen, (0, 0))

        history_text = pygame.font.Font('font.ttf', 50).render("Last Few Games!", True, "white")
        SCREEN.blit(history_text, history_text.get_rect(center=(300, 50)))

        for i, game in enumerate(history['lastgames'][::-1]):
            game_render = pygame.font.Font('font.ttf', 40).render(game, True, "white")
            SCREEN.blit(game_render, game_render.get_rect(center=(300, 130 + i * 50)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Past = False

        clock.tick(100)
        pygame.display.update()

    with open("history.json", "w") as f:
        json.dump(history, f, indent=4)