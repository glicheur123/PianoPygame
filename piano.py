# libs
import pygame
import time
import os
import threading
# initialising pygame and pygame.mixer(for sound effects)
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.init(22050, -16, 2, 1024)
# class that is used to place the keys at the right places


class Touche:
    pygame.time.delay(10)

    def __init__(self, img1, img2, coordonate, sound, clicked=False):
        self.img1 = img1
        self.img2 = img2
        self.coordonate = coordonate
        self.initialize()
        self.sound = sound
        self.clicked = clicked

    def getdata(self):
        return self.image

    def initialize(self):
        self.image = pygame.image.load(self.img1)

    def toucheclick(self):
        self.image = pygame.image.load(self.img2)

    def getImg(self):
        return self.img1

    def setco(self, cor):
        self.coordonate = cor

    def playsound(self):
        t = threading.Thread(target=self.soundThread)
        t.start()

    def soundThread(self):
        self.sound.play()

    def setclicked(self, stat):
        self.clicked = stat

    def getClicked(self):
        return self.clicked

    def getcoordonate(self):
        return self.coordonate


# useful variables
(width, height) = (1420, 525)
directory = os.path.split(os.path.abspath(__file__))[0]

font = pygame.font.Font("police.ttf", 110)
text = font.render("Piano", True, (255, 255, 255))
screen = pygame.display.set_mode((width, height))
screen.fill((127, 0, 255))
pygame.display.set_caption("piano")
piano = pygame.image.load("piano.png")
pygame.display.set_icon(piano)

# positioning all the white keys
keys = []
for i in range(0, 15):
    keys.append(Touche("{}.png".format(i+1), "{}a.png".format(i+1), (i*95, 150),
                       pygame.mixer.Sound(os.path.join(directory, "music", "{}.wav".format(i+1)))))
# positioning each black key
blackkeys = []
for i in range(0, 10):
    blackkeys.append(Touche("a.png", "b.png", (0, 0), pygame.mixer.Sound(
        os.path.join(directory, "music", "n{}.wav".format(i+1)))))

for i in range(0, 2):
    blackkeys[i].setco((i*115+56, 150))

for i in range(2, 4):
    blackkeys[i].setco((i*107+128, 150))

blackkeys[4].setco((554, 150))
blackkeys[5].setco((723, 150))
blackkeys[6].setco((833, 150))
blackkeys[7].setco((1007, 150))
blackkeys[8].setco((1114, 150))
blackkeys[9].setco((1219, 150))

# ------------------------------MainLoop--------------------------------------
playing = True
while playing:
    pygame.time.delay(5)

    # when an event happend on the keyboard
    for event in pygame.event.get():
        # close the window
        if event.type == pygame.QUIT:
            playing = False

        # when key is pressed down
        if event.type == pygame.KEYDOWN:
            # white
            if event.key == pygame.K_a:
                keys[0].playsound()
                keys[0].toucheclick()
            elif event.key == pygame.K_s:
                keys[1].playsound()
                keys[1].toucheclick()
            elif event.key == pygame.K_d:
                keys[2].playsound()
                keys[2].toucheclick()
            elif event.key == pygame.K_f:
                keys[3].playsound()
                keys[3].toucheclick()
            elif event.key == pygame.K_g:
                keys[4].playsound()
                keys[4].toucheclick()
            elif event.key == pygame.K_h:
                keys[5].playsound()
                keys[5].toucheclick()
            elif event.key == pygame.K_v:
                keys[6].playsound()
                keys[6].toucheclick()
            elif event.key == pygame.K_b:
                keys[7].playsound()
                keys[7].toucheclick()
            elif event.key == pygame.K_n:
                keys[8].playsound()
                keys[8].toucheclick()
            elif event.key == pygame.K_m:
                keys[9].playsound()
                keys[9].toucheclick()
            elif event.key == pygame.K_j:
                keys[10].playsound()
                keys[10].toucheclick()
            elif event.key == pygame.K_k:
                keys[11].playsound()
                keys[11].toucheclick()
            elif event.key == pygame.K_l:
                keys[12].playsound()
                keys[12].toucheclick()
            elif event.key == pygame.K_SEMICOLON:
                keys[13].playsound()
                keys[13].toucheclick()
            elif event.key == pygame.K_QUOTE:
                keys[14].playsound()
                keys[14].toucheclick()
            # black
            elif event.key == pygame.K_w:
                blackkeys[0].playsound()
                blackkeys[0].toucheclick()
            elif event.key == pygame.K_e:
                blackkeys[1].playsound()
                blackkeys[1].toucheclick()
            elif event.key == pygame.K_r:
                blackkeys[2].playsound()
                blackkeys[2].toucheclick()
            elif event.key == pygame.K_t:
                blackkeys[3].playsound()
                blackkeys[3].toucheclick()
            elif event.key == pygame.K_y:
                blackkeys[4].playsound()
                blackkeys[4].toucheclick()
            elif event.key == pygame.K_u:
                blackkeys[5].playsound()
                blackkeys[5].toucheclick()
            elif event.key == pygame.K_i:
                blackkeys[6].playsound()
                blackkeys[6].toucheclick()
            elif event.key == pygame.K_o:
                blackkeys[7].playsound()
                blackkeys[7].toucheclick()
            elif event.key == pygame.K_p:
                blackkeys[8].playsound()
                blackkeys[8].toucheclick()
            elif event.key == pygame.K_LEFTBRACKET:
                blackkeys[9].playsound()
                blackkeys[9].toucheclick()

        # when the key is released
        if event.type == pygame.KEYUP:
            # white
            if event.key == pygame.K_a:
                keys[0].setclicked(False)
                keys[0].initialize()
            elif event.key == pygame.K_s:
                keys[1].setclicked(False)
                keys[1].initialize()
            elif event.key == pygame.K_d:
                keys[2].setclicked(False)
                keys[2].initialize()
            elif event.key == pygame.K_f:
                keys[3].setclicked(False)
                keys[3].initialize()
            elif event.key == pygame.K_g:
                keys[4].setclicked(False)
                keys[4].initialize()
            elif event.key == pygame.K_h:
                keys[5].setclicked(False)
                keys[5].initialize()
            elif event.key == pygame.K_v:
                keys[6].setclicked(False)
                keys[6].initialize()
            elif event.key == pygame.K_b:
                keys[7].setclicked(False)
                keys[7].initialize()
            elif event.key == pygame.K_n:
                keys[8].setclicked(False)
                keys[8].initialize()
            elif event.key == pygame.K_m:
                keys[9].setclicked(False)
                keys[9].initialize()
            elif event.key == pygame.K_j:
                keys[10].setclicked(False)
                keys[10].initialize()
            elif event.key == pygame.K_k:
                keys[11].setclicked(False)
                keys[11].initialize()
            elif event.key == pygame.K_l:
                keys[12].setclicked(False)
                keys[12].initialize()
            elif event.key == pygame.K_SEMICOLON:
                keys[13].setclicked(False)
                keys[13].initialize()
            elif event.key == pygame.K_QUOTE:
                keys[14].setclicked(False)
                keys[14].initialize()
            # balck
            elif event.key == pygame.K_w:
                blackkeys[0].setclicked(False)
                blackkeys[0].initialize()
            elif event.key == pygame.K_e:
                blackkeys[1].setclicked(False)
                blackkeys[1].initialize()
            elif event.key == pygame.K_r:
                blackkeys[2].setclicked(False)
                blackkeys[2].initialize()
            elif event.key == pygame.K_t:
                blackkeys[3].setclicked(False)
                blackkeys[3].initialize()
            elif event.key == pygame.K_y:
                blackkeys[4].setclicked(False)
                blackkeys[4].initialize()
            elif event.key == pygame.K_u:
                blackkeys[5].setclicked(False)
                blackkeys[5].initialize()
            elif event.key == pygame.K_i:
                blackkeys[6].setclicked(False)
                blackkeys[6].initialize()
            elif event.key == pygame.K_o:
                blackkeys[7].setclicked(False)
                blackkeys[7].initialize()
            elif event.key == pygame.K_p:
                blackkeys[8].setclicked(False)
                blackkeys[8].initialize()
            elif event.key == pygame.K_LEFTBRACKET:
                blackkeys[9].setclicked(False)
                blackkeys[9].initialize()
    # showing the text
    screen.blit(text, (630, 25))
    # affichage des touches blanches
    for key in keys:
        screen.blit(key.getdata(), key.getcoordonate())

    # showing the blackeys
    for key in blackkeys:
        screen.blit(key.getdata(), key.getcoordonate())
    # refresh
    pygame.display.flip()
