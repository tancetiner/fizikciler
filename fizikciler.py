import pygame
import sys
import random as rd
from pygame import transform
import tkinter as tk

root = tk.Tk()

# defining constant numbers
SCREEN_SIZE = WIDTH, HEIGHT = (root.winfo_screenwidth(), root.winfo_screenheight())
FPS = 60
BLUE = (51, 153, 255)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
BROWN = (102, 51, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
TAN_KAFA_WIDTH = 75
TAN_KAFA_HEIGHT = 120
PAMIR_KAFA_WIDTH = 90
PAMIR_KAFA_HEIGHT = 120
YAGIZ_WIDTH = 75
YAGIZ_HEIGHT = 120
TANC1_WIDTH = 90
TANC1_HEIGHT = 120
TANC2_WIDTH = 72
CAN2_WIDTH = 95
CAN1_WIDTH = 100
CHAR_VEL = 10
PAMIR_VEL = 8
YAKALANDIN = pygame.USEREVENT + 1
KURTARDIN = pygame.USEREVENT + 2
KAZANDIN = pygame.USEREVENT + 3
SHIFT = 40
SHIFT2 = 60
records = [0]
# --------------------------


# loading the images
WIN = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN)

TAN_KAFA = pygame.transform.scale(
    pygame.image.load("./assets/tan.png"), (TAN_KAFA_WIDTH, TAN_KAFA_HEIGHT),
)

PAMIR_KAFA = pygame.transform.scale(
    pygame.image.load("./assets/pamir.png"), (PAMIR_KAFA_WIDTH, PAMIR_KAFA_HEIGHT),
)

PAMIR_KAFA_FLIPPED = pygame.transform.flip(PAMIR_KAFA, True, False)

YAGIZ1 = pygame.transform.scale(
    pygame.image.load("./assets/ataturk.png"), (YAGIZ_WIDTH, YAGIZ_HEIGHT),
)

YAGIZ2 = pygame.transform.scale(
    pygame.image.load("./assets/yagiz.png"), (YAGIZ_WIDTH, YAGIZ_HEIGHT),
)

TANC1 = pygame.transform.scale(
    pygame.image.load("./assets/asiyan.png"), (TANC1_WIDTH, TANC1_HEIGHT),
)

TANC2 = pygame.transform.scale(
    pygame.image.load("./assets/ceto.png"), (TANC2_WIDTH, TANC1_HEIGHT),
)

CAN1 = pygame.transform.scale(
    pygame.image.load("./assets/can.png"), (CAN1_WIDTH, TANC1_HEIGHT),
)

CAN2 = pygame.transform.scale(
    pygame.image.load("./assets/can2.png"), (CAN2_WIDTH, TANC1_HEIGHT),
)

TANG = pygame.transform.scale(
    pygame.image.load("./assets/tanG.png"), (PAMIR_KAFA_WIDTH, TANC1_HEIGHT),
)

THEATER2 = pygame.transform.scale(
    pygame.image.load("./assets/theater1.jpeg"), (WIDTH, HEIGHT),
)

THEATER1 = pygame.transform.scale(
    pygame.image.load("./assets/theater2.jpeg"), (WIDTH, HEIGHT),
)

DARK_BACKGROUND = pygame.transform.scale(
    pygame.image.load("./assets/dark_background.jpeg"), (WIDTH, HEIGHT),
)

LIGHT_BACKGROUND = pygame.transform.scale(
    pygame.image.load("./assets/light.jpeg"), (WIDTH, HEIGHT),
)

FEDAILER = pygame.transform.scale(
    pygame.image.load("./assets/fedailer.jpeg"), (638, 638),
)

FIZIKCILER = pygame.transform.scale(
    pygame.image.load("./assets/fizikciler.jpeg"), (577, 469),
)
# --------------------------


# the list that will store the images
friend_faces_original = [
    {"face": YAGIZ1, "width": YAGIZ_WIDTH, "height": YAGIZ_HEIGHT,},
    {"face": YAGIZ2, "width": YAGIZ_WIDTH, "height": YAGIZ_HEIGHT},
    {"face": TANC1, "width": TANC1_WIDTH, "height": TANC1_HEIGHT,},
    {"face": TANC2, "width": TANC2_WIDTH, "height": TANC1_HEIGHT},
    {"face": CAN1, "width": CAN1_WIDTH, "height": TANC1_HEIGHT,},
    {"face": CAN2, "width": CAN2_WIDTH, "height": TANC1_HEIGHT},
    {"face": TAN_KAFA, "width": TAN_KAFA_WIDTH, "height": TAN_KAFA_HEIGHT,},
    {"face": TANG, "width": PAMIR_KAFA_WIDTH, "height": TANC1_HEIGHT},
]
# --------------------------


# loading sound effects and creating the list stores them
pygame.mixer.init()
BACKGROUND_MUSIC = pygame.mixer.Sound("./assets/background_music.mp3")
tan_ses = pygame.mixer.Sound("./assets/tan_ses2.mp3")
yagiz_ses = pygame.mixer.Sound("./assets/yagiz_ses.mp3")
can_ses = pygame.mixer.Sound("./assets/can_ses.mp3")
tang_ses = pygame.mixer.Sound("./assets/tang_ses.mp3")
entry_music = pygame.mixer.Sound("./assets/rhayader.mp3")
bad_ending_music = pygame.mixer.Sound("./assets/led.mp3")
good_ending_music = pygame.mixer.Sound("./assets/chord.mp3")
pygame.mixer.Sound.set_volume(BACKGROUND_MUSIC, 0.1)
pygame.mixer.Sound.set_volume(tan_ses, 0.6)
pygame.mixer.Sound.set_volume(yagiz_ses, 0.3)
pygame.mixer.Sound.set_volume(can_ses, 1)
pygame.mixer.Sound.set_volume(tang_ses, 0.5)
pygame.mixer.Sound.set_volume(entry_music, 0.4)
pygame.mixer.Sound.set_volume(bad_ending_music, 0.4)
pygame.mixer.Sound.set_volume(good_ending_music, 0.4)
ses_listesi_original = [yagiz_ses, tan_ses, can_ses, tang_ses]
# --------------------------


# text initialisations
pygame.font.init()
pygame.display.set_caption("Fizikçiler vs Pamir")
mesajFontu = pygame.font.SysFont("georgia", 60, bold=True)
bitisFontu = pygame.font.SysFont("georgia", 40)
zamanFontu = pygame.font.SysFont("georgia", 30)
# --------------------------


# starting from here, functions will be defined
def initializePamirs():
    pamir1 = pygame.Rect(0, 0, PAMIR_KAFA_WIDTH, PAMIR_KAFA_HEIGHT)
    pamir2 = pygame.Rect(
        WIDTH - PAMIR_KAFA_WIDTH, 0, PAMIR_KAFA_WIDTH, PAMIR_KAFA_HEIGHT
    )
    pamir3 = pygame.Rect(
        0, HEIGHT - PAMIR_KAFA_HEIGHT, PAMIR_KAFA_WIDTH, PAMIR_KAFA_HEIGHT
    )
    pamir4 = pygame.Rect(
        WIDTH - PAMIR_KAFA_WIDTH,
        HEIGHT - PAMIR_KAFA_HEIGHT,
        PAMIR_KAFA_WIDTH,
        PAMIR_KAFA_HEIGHT,
    )

    pamirler = [pamir1, pamir2, pamir3, pamir4]
    return pamirler


def charSelectionScreen(friend_faces):
    WIN.blit(THEATER1, (0, 0))
    baslikMesaji = mesajFontu.render("Fizikçiler vs Pamir", 1, YELLOW)
    WIN.blit(baslikMesaji, (WIDTH / 2 - baslikMesaji.get_width() / 2, 50))
    hosgeldinMesajı = bitisFontu.render("Pamirden kaçmaya hazır mısın?", 1, WHITE)
    WIN.blit(hosgeldinMesajı, (WIDTH / 2 - hosgeldinMesajı.get_width() / 2, HEIGHT / 4))
    karakterSecMesaji = bitisFontu.render(
        "Karakterini seçmek için yanında belirtilen tuşa bas!", 1, WHITE
    )
    WIN.blit(
        karakterSecMesaji,
        (
            WIDTH / 2 - karakterSecMesaji.get_width() / 2,
            HEIGHT / 4 + hosgeldinMesajı.get_height(),
        ),
    )
    WIN.blit(
        friend_faces[0]["face"],
        (
            WIDTH / 3 - friend_faces[0]["width"] / 2 - SHIFT2,
            HEIGHT / 2 - friend_faces[0]["height"] / 2,
        ),
    )
    karakter1 = bitisFontu.render("1'e Bas", 1, WHITE)
    WIN.blit(
        karakter1,
        (
            WIDTH / 3
            - friend_faces[0]["width"] / 2
            + friend_faces[0]["face"].get_width()
            + SHIFT
            - SHIFT2,
            HEIGHT / 2,
        ),
    )
    karakter1N = bitisFontu.render("Yağız", 1, WHITE)
    WIN.blit(
        karakter1N,
        (
            WIDTH / 3
            - friend_faces[0]["width"] / 2
            + friend_faces[0]["face"].get_width()
            + SHIFT
            - SHIFT2,
            HEIGHT / 2 - karakter1N.get_height(),
        ),
    )

    WIN.blit(
        friend_faces[2]["face"],
        (
            WIDTH * 2 / 3 - friend_faces[2]["width"] / 2 - SHIFT2,
            HEIGHT / 2 - friend_faces[2]["height"] / 2,
        ),
    )
    karakter2 = bitisFontu.render("2'ye Bas", 1, WHITE)
    WIN.blit(
        karakter2,
        (
            WIDTH * 2 / 3
            - friend_faces[2]["width"] / 2
            + friend_faces[2]["face"].get_width()
            + SHIFT
            - SHIFT2,
            HEIGHT / 2,
        ),
    )
    karakter2N = bitisFontu.render("Tan Ç", 1, WHITE)
    WIN.blit(
        karakter2N,
        (
            WIDTH * 2 / 3
            - friend_faces[2]["width"] / 2
            + friend_faces[2]["face"].get_width()
            + SHIFT
            - SHIFT2,
            HEIGHT / 2 - karakter2N.get_height(),
        ),
    )

    WIN.blit(
        friend_faces[4]["face"],
        (
            WIDTH / 3 - friend_faces[4]["width"] / 2 - 10 - SHIFT2,
            HEIGHT * 3 / 4 - friend_faces[4]["height"] / 2,
        ),
    )
    karakter3 = bitisFontu.render("3'e Bas", 1, WHITE)
    WIN.blit(
        karakter3,
        (
            WIDTH / 3
            - friend_faces[4]["width"] / 2
            + friend_faces[4]["face"].get_width()
            + SHIFT
            - 10
            - SHIFT2,
            HEIGHT * 3 / 4,
        ),
    )
    karakter3N = bitisFontu.render("Can", 1, WHITE)
    WIN.blit(
        karakter3N,
        (
            WIDTH / 3
            - friend_faces[4]["width"] / 2
            + friend_faces[4]["face"].get_width()
            + SHIFT
            - SHIFT2,
            HEIGHT * 3 / 4 - karakter3N.get_height(),
        ),
    )

    WIN.blit(
        friend_faces[6]["face"],
        (
            WIDTH * 2 / 3 - friend_faces[6]["width"] / 2 - SHIFT2,
            HEIGHT * 3 / 4 - friend_faces[6]["height"] / 2,
        ),
    )
    karakter4 = bitisFontu.render("4'e Bas", 1, WHITE)
    WIN.blit(
        karakter4,
        (
            WIDTH * 2 / 3
            - friend_faces[6]["width"] / 2
            + friend_faces[6]["face"].get_width()
            + SHIFT
            - SHIFT2,
            HEIGHT * 3 / 4,
        ),
    )
    karakter4N = bitisFontu.render("Tan G", 1, WHITE)
    WIN.blit(
        karakter4N,
        (
            WIDTH * 2 / 3
            - friend_faces[6]["width"] / 2
            + friend_faces[6]["face"].get_width()
            + SHIFT
            - SHIFT2,
            HEIGHT * 3 / 4 - karakter4N.get_height(),
        ),
    )
    pygame.display.update()


def characterSelector(key):
    if key[pygame.K_1]:
        return 1
    elif key[pygame.K_2]:
        return 2
    elif key[pygame.K_3]:
        return 3
    elif key[pygame.K_4]:
        return 4
    else:
        return -1


def characterMovement(keysPressed, char):
    if keysPressed[pygame.K_a] and char.x - CHAR_VEL > 0:
        char.x -= CHAR_VEL
    if keysPressed[pygame.K_s] and char.y + CHAR_VEL + char.height < HEIGHT:
        char.y += CHAR_VEL
    if keysPressed[pygame.K_d] and char.x + CHAR_VEL + char.width < WIDTH:
        char.x += CHAR_VEL
    if keysPressed[pygame.K_w] and char.y - CHAR_VEL > 0:
        char.y -= CHAR_VEL


def pamirMovement(pamir, direction):
    if direction == 1 and pamir.x - PAMIR_VEL > 0:
        pamir.x -= PAMIR_VEL
    if direction == 2 and pamir.y + PAMIR_VEL + pamir.height < HEIGHT:
        pamir.y += PAMIR_VEL
    if direction == 3 and pamir.x + PAMIR_VEL + pamir.width < WIDTH:
        pamir.x += PAMIR_VEL
    if direction == 4 and pamir.y - PAMIR_VEL > 0:
        pamir.y -= PAMIR_VEL


def createFriend(friendNo, friend_faces, character):
    # idx = rd.randint(0, len(friends) - 1)
    x_pos = rd.randint(SHIFT, WIDTH - SHIFT - friend_faces[friendNo]["width"])
    while abs(x_pos - character.x) < 300:
        x_pos = rd.randint(SHIFT, WIDTH - SHIFT - friend_faces[friendNo]["width"])
    y_pos = rd.randint(SHIFT, HEIGHT - SHIFT - friend_faces[friendNo]["height"])
    while abs(y_pos - character.y) < 300:
        y_pos = rd.randint(SHIFT, HEIGHT - SHIFT - friend_faces[friendNo]["height"])
    new_friend = pygame.Rect(
        x_pos, y_pos, friend_faces[friendNo]["width"], friend_faces[friendNo]["height"]
    )
    return new_friend


def createCharacter(charNo, friend_faces):
    x_pos = WIDTH / 2 - (friend_faces[charNo]["width"])
    y_pos = HEIGHT / 2 - friend_faces[charNo]["height"]
    character = pygame.Rect(
        x_pos, y_pos, friend_faces[charNo]["width"], friend_faces[charNo]["height"]
    )
    return character


def drawWindow(
    char,
    charImg,
    pamirler,
    pamirDirections,
    friend,
    charNo,
    friendNo,
    friend_faces,
    seconds=0,
    score=0,
):
    WIN.blit(THEATER2, (0, 0))

    WIN.blit(charImg["face"], (char.x, char.y))
    time_text = "Süre: " + str(seconds)
    countdown = zamanFontu.render(time_text, 1, BLUE)
    WIN.blit(
        countdown,
        (WIDTH / 4 - countdown.get_width() / 2, SHIFT - countdown.get_height(),),
    )
    score_text = "Puan: " + str(score)
    scoreT = zamanFontu.render(score_text, 1, BLUE)
    WIN.blit(
        scoreT, (WIDTH / 2 - scoreT.get_width() / 2, SHIFT - scoreT.get_height(),),
    )
    record = "Rekor: " + str(max(records))
    recordT = zamanFontu.render(record, 1, BLUE)
    WIN.blit(
        recordT,
        (WIDTH * 3 / 4 - recordT.get_width() / 2, SHIFT - recordT.get_height(),),
    )
    i = 0
    for pamir in pamirler:
        if pamirDirections[i] == 1 or pamirDirections[i] == 4:
            WIN.blit(PAMIR_KAFA, (pamir.x, pamir.y))
        elif pamirDirections[i] == 3 or pamirDirections[i] == 2:
            WIN.blit(PAMIR_KAFA_FLIPPED, (pamir.x, pamir.y))

    WIN.blit(friend_faces[friendNo]["face"], (friend.x, friend.y))
    pygame.display.update()


def pamirMoveCall(pamirler, count, pamirDirection):
    if count >= 15:
        for i in range(len(pamirDirection)):
            pamirDirection[i] = rd.randint(1, 4)
        count = 0

    for i in range(len(pamirler)):
        pamirMovement(pamirler[i], pamirDirection[i])
    # count += 1
    return count


def lastSelection(key):
    if key[pygame.K_7]:
        return 7
    elif key[pygame.K_8]:
        return 8
    else:
        return -1


def checkEvent(pamirler, char, friend, score, targetP):
    for pamir in pamirler:
        if char.colliderect(pamir):
            pygame.event.post(pygame.event.Event(YAKALANDIN))
    if char.colliderect(friend):
        pygame.event.post(pygame.event.Event(KURTARDIN))
    if score >= targetP:
        pygame.event.post(pygame.event.Event(KAZANDIN))


def displayGoodEnding(score):
    good_ending_music.play(-1)
    WIN.blit(LIGHT_BACKGROUND, (0, 0))
    WIN.blit(
        FIZIKCILER,
        (
            WIDTH / 2 - FIZIKCILER.get_width() / 2,
            HEIGHT / 2 - FIZIKCILER.get_height() / 2,
        ),
    )
    bitis_mesaji = bitisFontu.render(
        str(score) + " puana ulaştın ve Fizikçiler'i kurtardın!", 1, BLACK,
    )

    WIN.blit(
        bitis_mesaji,
        (WIDTH / 2 - bitis_mesaji.get_width() / 2, bitis_mesaji.get_height()),
    )

    bitis_mesaji7 = zamanFontu.render("Bir sonraki seviye", 1, BLACK)
    bitis_mesaji8 = zamanFontu.render("için 7'ye bas", 1, BLACK)
    bitis_mesaji9 = zamanFontu.render("Çıkmak için", 1, BLACK)
    bitis_mesaji10 = zamanFontu.render("8'e bas", 1, BLACK)
    pos = 140

    WIN.blit(
        bitis_mesaji7, (pos - bitis_mesaji7.get_width() / 2, HEIGHT / 2),
    )
    WIN.blit(
        bitis_mesaji8,
        (pos - bitis_mesaji8.get_width() / 2, HEIGHT / 2 + bitis_mesaji7.get_height(),),
    )
    WIN.blit(
        bitis_mesaji9, (WIDTH - pos - bitis_mesaji9.get_width() / 2, HEIGHT / 2,),
    )
    WIN.blit(
        bitis_mesaji10,
        (
            WIDTH - pos - bitis_mesaji10.get_width() / 2,
            HEIGHT / 2 + bitis_mesaji9.get_height(),
        ),
    )

    pygame.display.update()

    lastScreen = True
    while lastScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        lastPress = pygame.key.get_pressed()
        decision = lastSelection(lastPress)
        if decision != -1:
            lastScreen = False
    pygame.mixer.pause()
    return decision


def displayBadEnding(time, score):
    bad_ending_music.play(-1)
    WIN.blit(DARK_BACKGROUND, (0, 0))
    WIN.blit(
        FEDAILER,
        (
            WIDTH / 2 - FEDAILER.get_width() / 2,
            HEIGHT / 2 - FEDAILER.get_height() / 2 + 70,
        ),
    )
    bitis_mesaji = bitisFontu.render(
        "Pamir tüm Fizikçiler ekibini yakaladı ve fedaisi yaptı...", 1, GRAY,
    )
    bitis_mesaji2 = zamanFontu.render("Dayandığın", 1, GRAY)
    bitis_mesaji3 = zamanFontu.render("Süre: ", 1, GRAY)
    bitis_mesaji4 = zamanFontu.render(str(time), 1, GRAY)
    bitis_mesaji5 = zamanFontu.render("Skorun: ", 1, GRAY)
    bitis_mesaji6 = zamanFontu.render(str(score), 1, GRAY)

    bitis_mesaji7 = zamanFontu.render("Yeniden oynamak", 1, GRAY)
    bitis_mesaji8 = zamanFontu.render("için 7'ye bas", 1, GRAY)
    bitis_mesaji9 = zamanFontu.render("Çıkmak için", 1, GRAY)
    bitis_mesaji10 = zamanFontu.render("8'e bas", 1, GRAY)

    pos = 140
    WIN.blit(
        bitis_mesaji,
        (WIDTH / 2 - bitis_mesaji.get_width() / 2, bitis_mesaji.get_height()),
    )
    WIN.blit(
        bitis_mesaji2, (pos - bitis_mesaji2.get_width() / 2, HEIGHT / 3),
    )
    WIN.blit(
        bitis_mesaji3,
        (pos - bitis_mesaji3.get_width() / 2, HEIGHT / 3 + bitis_mesaji2.get_height()),
    )
    WIN.blit(
        bitis_mesaji4,
        (
            pos - bitis_mesaji4.get_width() / 2,
            HEIGHT / 3 + bitis_mesaji2.get_height() + bitis_mesaji3.get_height(),
        ),
    )
    WIN.blit(
        bitis_mesaji5,
        (
            pos - bitis_mesaji5.get_width() / 2,
            HEIGHT / 3
            + bitis_mesaji2.get_height()
            + bitis_mesaji3.get_height()
            + bitis_mesaji4.get_height()
            + pos,
        ),
    )
    WIN.blit(
        bitis_mesaji6,
        (
            pos - bitis_mesaji6.get_width() / 2,
            HEIGHT / 3
            + bitis_mesaji2.get_height()
            + bitis_mesaji3.get_height()
            + bitis_mesaji4.get_height()
            + bitis_mesaji5.get_height()
            + pos,
        ),
    )

    WIN.blit(
        bitis_mesaji7, (WIDTH - pos - bitis_mesaji7.get_width() / 2, HEIGHT / 3),
    )
    WIN.blit(
        bitis_mesaji8,
        (
            WIDTH - pos - bitis_mesaji8.get_width() / 2,
            HEIGHT / 3 + bitis_mesaji7.get_height(),
        ),
    )
    WIN.blit(
        bitis_mesaji9,
        (
            WIDTH - pos - bitis_mesaji9.get_width() / 2,
            HEIGHT / 3 + bitis_mesaji7.get_height() + bitis_mesaji8.get_height() + pos,
        ),
    )
    WIN.blit(
        bitis_mesaji10,
        (
            WIDTH - pos - bitis_mesaji10.get_width() / 2,
            HEIGHT / 3
            + bitis_mesaji7.get_height()
            + bitis_mesaji8.get_height()
            + bitis_mesaji9.get_height()
            + pos,
        ),
    )

    pygame.display.update()

    lastScreen = True
    while lastScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        lastPress = pygame.key.get_pressed()
        decision = lastSelection(lastPress)
        if decision != -1:
            lastScreen = False
    pygame.mixer.pause()
    return decision


#### end of defined functions #####


# main function
def main():
    mainCheck = True
    TARGETPOINT = 300
    firstScreen = True
    firstTime = True
    while mainCheck:
        clock = pygame.time.Clock()
        bugCheck = True
        friend_faces = friend_faces_original.copy()
        if firstScreen:
            entry_music.play(-1, fade_ms=2000)
        # loop for the first screen
        while firstScreen:
            charSelectionScreen(friend_faces)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keysPressed = pygame.key.get_pressed()
            charNo = characterSelector(keysPressed)
            if charNo != -1:
                firstScreen = False
                entry_music.stop()
        # --------------------------

        # setup and initilizations before the game loop
        BACKGROUND_MUSIC.play(-1)
        pamirler = initializePamirs()
        charIdx = (charNo - 1) * 2
        character = createCharacter(charIdx, friend_faces)
        charImg = friend_faces[charIdx]
        friend_faces.pop(charIdx)
        friend_faces.pop(charIdx)
        ses_listesi = ses_listesi_original.copy()
        ses_listesi.pop(charNo - 1)
        frNo = rd.randint(0, len(friend_faces) - 1)
        friend = createFriend(frNo, friend_faces, character)
        pamirCount = 0
        saveCount = 0
        pamirDirection = [0, 0, 0, 0]
        for i in range(len(pamirDirection)):
            pamirDirection[i] = rd.randint(1, 4)

        drawWindow(
            character,
            charImg,
            pamirler,
            pamirDirection,
            friend,
            charIdx,
            frNo,
            friend_faces,
        )
        baslangic_mesaji = bitisFontu.render(
            str(TARGETPOINT) + " puana ulaş ve Fizikçiler'i Pamir'den kurtar!",
            1,
            YELLOW,
        )
        WIN.blit(
            baslangic_mesaji,
            (
                WIDTH / 2 - baslangic_mesaji.get_width() / 2,
                HEIGHT / 3 - baslangic_mesaji.get_height() / 2 - 40,
            ),
        )
        baslangic_mesaji2 = bitisFontu.render(
            "W-A-S-D tuşlarını kullanarak hareket edebilirsin", 1, YELLOW,
        )

        if firstTime:  # will be executed only in the first try, for tutorial purposes
            WIN.blit(
                baslangic_mesaji2,
                (
                    WIDTH / 2 - baslangic_mesaji2.get_width() / 2,
                    HEIGHT * 2 / 3 - baslangic_mesaji2.get_height() / 2,
                ),
            )
            baslangic_mesaji3 = bitisFontu.render(
                "Geçirdiğin her saniye: +10P    Topladığın her kafa: +50P", 1, YELLOW,
            )
            WIN.blit(
                baslangic_mesaji3,
                (
                    WIDTH / 2 - baslangic_mesaji3.get_width() / 2,
                    HEIGHT * 2 / 3
                    - baslangic_mesaji3.get_height() / 2
                    + baslangic_mesaji2.get_height(),
                ),
            )
            pygame.display.update()
            pygame.time.delay(2000)
            firstTime = False

        pygame.display.update()
        pygame.time.delay(2000)
        start_time = pygame.time.get_ticks()
        seconds = 0
        score = 0
        run = True
        # game loop starts
        while run:
            clock.tick(FPS)  # will set the 60 FPS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == YAKALANDIN:
                    pygame.mixer.stop()
                    records.append(score)
                    bugCheck = False
                    firstScreen = True
                    TARGETPOINT = 300
                    choice = displayBadEnding(seconds, score)
                    if choice == 7:
                        run = False
                        choice = 0
                    elif choice == 8:
                        pygame.quit()
                        sys.exit()

                if event.type == KURTARDIN:
                    ses_listesi[frNo // 2].play()
                    frNo = rd.randint(0, len(friend_faces) - 1)
                    friend = createFriend(frNo, friend_faces, character)
                    saveCount += 1

                if event.type == KAZANDIN:
                    pygame.mixer.stop()
                    records.append(TARGETPOINT)
                    choice = displayGoodEnding(TARGETPOINT)
                    if choice == 7:
                        run = False
                        TARGETPOINT = TARGETPOINT * 2
                        choice = 0
                    elif choice == 8:
                        pygame.quit()
                        sys.exit()

            if bugCheck:
                keys = pygame.key.get_pressed()
                characterMovement(keys, character)
            pamirCount = pamirMoveCall(pamirler, pamirCount, pamirDirection) + 1

            seconds = (pygame.time.get_ticks() - start_time) // 1000
            score = seconds * 10 + saveCount * 50
            drawWindow(
                character,
                charImg,
                pamirler,
                pamirDirection,
                friend,
                charIdx,
                frNo,
                friend_faces,
                seconds,
                score,
            )
            checkEvent(pamirler, character, friend, score, TARGETPOINT)


# main part -only calls main function-
main()

