import pygame

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("COSC Final Project")

premises = [["1.", "(C -> N) ^ E", "D v (N -> D)", "~D", "/ ~C v P"],
["2.", "F -> (~T ^ A)",  "(~T v G) -> (H -> T)",  "F ^ O",  "/ ~H ^ ~T"],
["3.", "(~S v B) -> (S v K)", "(K v ~D) -> (H -> S)", "~S ^ W", "/ ~H"]]

# answers = [["N -> D DS 2, 3", "C -> N SIMP 1", "C -> D HS 5, 4", "~C MT 6, 3", "~C v P ADD 7"], 
# ["F SIMP 3", "~T ^ A MP 1, 4", "~T SIMP 5", "~T v G ADD 6", "H -> T MP 2, 7", "~H MT 8, 6", "~H ^ ~T CONJ 9, 6"],
# ["~S SIMP 3", "~S v B ADD 4", "S v K MP 1, 5", "K DS 6, 4", "K v ~D ADD 7", "H -> S MP 2, 8", "~H MT 9, 4"]]

answers = ["~C v P ADD 7", "~H ^ ~T CONJ 9, 6", "~H MT 9, 4"]
answersnum = [5, 7, 7]
clock = pygame.time.Clock()

def get_font(size):
    return pygame.font.Font("font.ttf", size)

titletxt = get_font(100).render("Rules of Implication", True, "#000000")
titlerect = titletxt.get_rect(center=(640, 100))
quiztxt = get_font(100).render("Quiz", True, "#000000")
quizrect = quiztxt.get_rect(center=(640, 300))
quizbutton_rect = pygame.Rect(485, 240, 300, 120)
quizbutton_color = (255, 255, 255)
quittxt = get_font(100).render("Quit", True, "#000000")

# instead of this
quitrect = quittxt.get_rect(center=(640, 560))
quitbutton_rect = pygame.Rect(485, 500, 300, 120)
quitbutton_color = (255, 255, 255)

# do this instead
quitrect = quittxt.get_rect(center=(640, 560))
s = pygame.Surface((300,120), pygame.SRCALPHA)   # per-pixel alpha
s.fill((255,255,255,0))                         # notice the alpha value in the color

Menu = True

while Menu:

    SCREEN.fill((0, 255, 255))
    
    # instead of this
    pygame.draw.rect(SCREEN, quizbutton_color, quizbutton_rect)
    # do this instead   
    SCREEN.blit(s, (485, 500))
    SCREEN.blit(quizbutton_rect, (0,0))

    pygame.draw.rect(SCREEN, quitbutton_color, quitbutton_rect)
    SCREEN.blit(titletxt, titlerect)
    SCREEN.blit(quiztxt, quizrect)
    SCREEN.blit(quittxt, quitrect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Menu = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if quizbutton_rect.collidepoint(event.pos):
                    SCREEN.fill((255, 255, 255))
                    Menu = False
                if quitbutton_rect.collidepoint(event.pos):
                    Menu = False
                    pygame.quit()

    pygame.display.update()

Answer = True
i = 0
disptext = ""
x = 50
disptextlist = []
n = 0
num = 0
score = 0
dispnum = -1

while Answer:
    SCREEN.fill((255, 255, 255))
    # SCREEN.blit(pygame.image.load("background (2).png"), (0, 0))
    y = 20

    scoretxt = get_font(80).render("Score: " + str(score) + " / 10", True, "#000000")
    scorerect = scoretxt.get_rect(center=(1130, 50))
    SCREEN.blit(scoretxt, scorerect)

    for j in range(len(premises[i])):
        premisetext = get_font(40).render(premises[i][j], True, "#000000")
        SCREEN.blit(premisetext, (x, y))
        y += 40
        dispnum += 1
   
    for text in disptextlist:
        SCREEN.blit(get_font(40).render(str(dispnum) + ". " + text, True, "#000000"), (x, y))
        dispnum += 1
        y += 40

    SCREEN.blit(get_font(40).render(str(dispnum) + ". " + disptext, True, "#000000"), (x, y))
    dispnum = -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Answer = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha() or event.unicode.isdigit():
                    disptext += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    disptext = disptext[:-1]
                elif event.key == pygame.K_SPACE:
                    disptext += " "
                elif event.key == pygame.K_MINUS:
                    disptext += "-"
                elif event.key == pygame.K_LEFTBRACKET:
                    disptext += "["
                elif event.key == pygame.K_RIGHTBRACKET:
                    disptext += "]"
                elif event.key == pygame.K_COMMA:
                    disptext += ","
                elif event.key == pygame.K_BACKQUOTE:
                    disptext += "~"
                elif event.key == pygame.K_6 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    disptext += "^"
                elif event.key == pygame.K_9 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    disptext += "("
                elif event.key == pygame.K_0 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    disptext += ")"
                elif event.key == pygame.K_PERIOD and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    disptext += ">"
                elif event.key == pygame.K_RETURN:
                    disptextlist.append(disptext)
                    n += 1
                    if n == answersnum[num]:
                        if disptext.upper() == answers[num].upper():
                            score += 1
                        num += 1
                        i += 1
                        disptextlist = []
                        n = 0
                    disptext = ""
                    if i >= len(premises) or num >= len(answers):
                        Answer = False

    clock.tick(200)
    pygame.display.update()

titletxt = get_font(100).render("Score", True, "#000000")
titlerect = titletxt.get_rect(center=(640, 200))
scoretxt = get_font(100).render(str(score) + " / 10", True, "#000000")
scorerect = scoretxt.get_rect(center=(640, 300))
if score == 10:
    msg = "You answered all problems correctly!"
elif score > 8:
    msg = "You did really well. Congrats!"
elif score > 5:
    msg = "It's alright but you can do better."
else:
    msg = "Study better next time."

msgtxt = get_font(100).render(msg, True, "#000000")
msgrect = msgtxt.get_rect(center=(640, 400))
scorecon = True

while scorecon:
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(titletxt, titlerect)
    SCREEN.blit(scoretxt, scorerect)
    SCREEN.blit(msgtxt, msgrect)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Answer = False
                pygame.quit()
    clock.tick(200)
    pygame.display.update()