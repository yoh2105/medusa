import hitbox
import pygame, sys
from pygame.locals import *
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

x = 220
y = 360
width = 53
height = 77
vel = 25

forest = False
room = False
cave = False
town = False
rocks = False
appleininv = False
journalquest = False

walkLeft = ["l1.png", "l2.png", "l3.png"]

walkRight = ['r1.png', 'r2.png', 'r3.png']

walkUp = ['b1.png', 'b2.png', 'b3.png', 'b2.png']

walkDown = ['f1.png', 'f2.png', 'f3.png', 'f2.png']

class Circle(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y,win, pic):
        super().__init__()
        self.win = win
        self.open_close = 1
        self.image = pygame.image.load(pic).convert()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = win.blit( self.image, ( pos_x,pos_y))
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.speed_y = 0

    def update(self, GRAVITY, posy,open_close):
        if open_close == 1:
            self.speed_y += GRAVITY
            self.pos_y += self.speed_y
            self.rect.y = self.pos_y
            if self.pos_y > self.win.get_height()-posy-50:
                self.speed_y = -1
        elif open_close == 2:
            self.speed_y += GRAVITY
            self.pos_y -= self.speed_y
            self.rect.y = self.pos_y

            if self.pos_y < self.win.get_height()-400:
                self.pos_y = 50
                self.speed_y = 0




questbegin = False

Atext = ["Hey did you hear they stopped making socks?", "Crazy stuff right?", "Kinda weird they stopped now, I mean...", "...socks were so popular!", "Oh yea also there's a monster in the woods.", "But I mean, socks! What's up with that?", "this isn't meant to be shown"]
Mtext = ["You don't look like you're from around here...", "...my name is Mimi!", "My sister bakes the most wonderful macarons...", "...but they're not for you! Hahaha!", "They say there's creatures in those woods.", "Normally I wouldn't care...", "...but one time a girl went in and never came back.", "this isn't meant to be shown"]
Ktext1 = ["Duuuuuuuuuuuuuuuuuuude!", "I heard there’s some sick fruit in the woods.", "Would you, like, mind grabbing me an apple?", "It’ll go great with my Monster energy drink!", "There's a little tree on the border of the forest.", "You'll find apples there.", "this isn't meant to be shown"]
Ktext2 = ["Please grab me an apple from the woods.", "There's a little tree on the border of the forest.", "You'll find apples there.", "this isn't meant to be shown"]
Ktext3 =["YOOOOOOOOOOOOOOOOOOOOOOO!", "BROSKI! THANKS A BUNCH!", "I think there’s a way from the forest into…", "...the cave where that foul little dude lives.", "Now if you’ll excuse me, I have some drywall to punch.", "this isn't meant to be shown"]
Rtextwrong = ["You look under the rock for an apple.", "There is nothing underneath.", "this isn't meant to be shown"]
Rtextright= ["Score! You found the apple.", "Bring the apple back to Kyle!", "this isn't meant to be shown"]
Medtext1 = ["Oh, a visitor… I don’t get many of those nowadays… ", "I wasn’t always like this, you know.", "I used to live in the village with the others.", "One day I wandered into the woods and a witch cursed me.", "Everytime I go into the village they get scared.", "I miss my mom.", "I need you to help me.", "Oh, you found my journal! Haven't seen that in ages.", "Give it to my friend Kyle for me.", "this isn't meant to be shown"]

player = pygame.sprite.Group(hitbox.Sprite([200, 200], "f2.png"))
mob = hitbox.npc([845, 632], "mimi.png")
mob_group = pygame.sprite.Group()
mob_group.add(mob)

aziz_group = pygame.sprite.Group()
kyle_group = pygame.sprite.Group()
rock1_group = pygame.sprite.Group()
rock2_group = pygame.sprite.Group()
tree_group = pygame.sprite.Group()
rock3_group = pygame.sprite.Group()
medusa_group = pygame.sprite.Group()

character="f2.png"
#player = pygame.image.load(character).convert_alpha()
#player = pygame.transform.scale(player, (53,77))

mapy = pygame.image.load("bedroom.png")
mapy = pygame.transform.scale(mapy, (1200,950))
pygame.mixer.music.load("house.mp3")
pygame.mixer.music.play(-1,0.0)
pygame.display.update()


CameraX = 30
CameraY = 160

counter = 0

run = True

boundary_x_lower = 0
boundary_x_upper = 500

clock = pygame.time.Clock()
counter = 0
run = True
fps = 60
#win.blit(mapy,(0 -CameraX,0 -CameraY))
#pygame.display.flip()


#iv = pygame.sprite.Group(Circle(400,50, win,"sword.jpg"))
#iv2 = pygame.sprite.Group(Circle(400,50, win,"boy.jpg"))
#iv3 = pygame.sprite.Group(Circle(400, 50, win,"letter.jpg"))
iv4 = pygame.sprite.Group(Circle(400,50, win,"apple.png"))
iv5 = pygame.sprite.Group(Circle(400,50, win, "backpack.png"))
open_iv = False
closed_iv = False

while run:
    iv5.draw(win)
    pygame.display.update()
    pygame.time.delay(40)

    event = pygame.event.get()

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    #hit = pygame.sprite.groupcollide(player, mob_group, False, False)
    win.blit(mapy,(0 -CameraX,0 -CameraY))
    #mob_group.draw(mapy)

    player.draw(win)
    if keys[pygame.K_SPACE] and x>=800 and x<=880 and y >= 580 and y <= 660 and town == True:
        #win.blit(mapy,(0 -CameraX,0 -CameraY))
        hitbox.dialogue(Mtext, "Mimi")
    if keys[pygame.K_SPACE] and x>=90 and x<=150 and y >= 748 and y <= 828 and town == True:
        #win.blit(mapy,(0 -CameraX,0 -CameraY))
        hitbox.dialogue(Atext, "Aziz")
    if keys[pygame.K_SPACE] and x>=623 and x<=703 and y >= 146 and y <= 246 and questbegin == False and town == True:
        #win.blit(mapy,(0 -CameraX,0 -CameraY))
        hitbox.dialogue(Ktext1, "Kyle")
        questbegin = True
    elif keys[pygame.K_SPACE] and x>=623 and x<=703 and y >= 146 and y <= 246 and questbegin == True and town == True and appleininv == False:
        hitbox.dialogue(Ktext2, "Kyle")
    if keys[pygame.K_SPACE] and x>=623 and x<=703 and y >= 298 and y <= 388 and questbegin == True and rocks == True:
        #win.blit(mapy,(0 -CameraX,0 -CameraY))
        hitbox.dialogue(Rtextwrong, "")
    if keys[pygame.K_SPACE] and x>=823 and x<=903 and y >= 498 and y <= 588 and questbegin == True and rocks == True:
        #win.blit(mapy,(0 -CameraX,0 -CameraY))
        hitbox.dialogue(Rtextwrong, "")
    if keys[pygame.K_SPACE] and x>=1023 and x<=1103 and y >= 398 and y <= 488 and questbegin == True and rocks == True:
        #win.blit(mapy,(0 -CameraX,0 -CameraY))
        hitbox.dialogue(Rtextright, "")
        appleininv = True
    elif keys[pygame.K_SPACE] and x>=623 and x<=703 and y >= 146 and y <= 246 and questbegin == True and town == True and appleininv == True:
        hitbox.dialogue(Ktext3, "Kyle")
    elif keys[pygame.K_SPACE] and x>=613 and x<=703 and y >= 498 and y <= 588 and cave == True and questbegin == True and appleininv == True:
        hitbox.dialogue(Medtext1, "Medusa")
        journalquest = True

    pygame.display.update()
    clock.tick(fps)
    #win.blit(mapy,(0 -CameraX,0 -CameraY))
    #pygame.display.flip()

    clock.tick(fps)




    if keys[pygame.K_LEFT]:

        ###
    #    player.update(walkLeft[counter])

        ##
        counter = (counter + 1) % len(walkLeft)
        old_x = x
        old_y = y
        x -= vel
        CameraX -= 20
        if x <= 0:
            x += 14
        if CameraX <= 0:
            CameraX += 20
        #win.fill(0,0,0)
        player.empty()
        player.add(hitbox.Sprite([old_x-CameraX, old_y-CameraY], walkLeft[counter]))
        win.fill((0,0,0))
        win.blit(mapy,(0 -CameraX,0 -CameraY))
        #mob_group.draw(mapy)
        player.draw(win)
        #player.remove()


        pygame.display.flip()

    if keys[pygame.K_RIGHT]:

        ###

        ##


        counter = (counter + 1) % len(walkRight)
        old_x = x
        old_y = y
        x += vel
        CameraX += 20
        if x >= 1080:
            x -= 14
        if CameraX >= 650:
            CameraX -= 20

        player.empty()
        player.add(hitbox.Sprite([old_x-CameraX, old_y-CameraY], walkRight[counter]))
        win.fill((0,0,0))
        win.blit(mapy,(0 -CameraX,0 -CameraY))
        #mob_group.draw(mapy)
        player.draw(win)
        #player.remove()

        pygame.display.flip()

    if keys[pygame.K_UP]:

        ###

        ##

        counter = (counter + 1) % len(walkUp)
        old_x = x
        old_y = y
        y -= vel
        CameraY -= 20
        if y <= 0:
            y += 14
        if CameraY <= 0:
            CameraY += 20

        player.empty()
        player.add(hitbox.Sprite([old_x-CameraX, old_y-CameraY], walkUp[counter]))
        win.fill((0,0,0))
        win.blit(mapy,(0 -CameraX,0 -CameraY))
        #mob_group.draw(mapy)
        player.draw(win)
        #player.remove()

        pygame.display.flip()

    if keys[pygame.K_DOWN]:

        ###

        ##

        counter = (counter + 1) % len(walkDown)
        old_x = x
        old_y = y
        y += vel
        CameraY += 20
        if y >= 880:
            y -= 14
        if CameraY >= 450:
            CameraY -= 20

        player.empty()
        player.add(hitbox.Sprite([old_x-CameraX, old_y-CameraY], walkDown[counter]))
        win.fill((0,0,0))
        win.blit(mapy,(0 -CameraX,0 -CameraY))
        #mob_group.draw(mapy)
        player.draw(win)
        #player.remove()

        pygame.display.flip()



    if keys[pygame.K_TAB]:
        for i in range(0,150):
            iv.update(.1,0,2)
            iv2.update(.2,100,2)
            iv3.update(.3,20,2)
            iv4.update(.4,30,2)
            win.fill((0,0,0))  # Fills the win with black
            win.blit(mapy,(0 -CameraX,0 -CameraY))
            #win.blit(player,(x -CameraX,y -CameraY))
            player.draw(win)
            #iv.draw(win)
            #iv2.draw(win)
            #iv3.draw(win)
            iv4.draw(win)
            iv5.draw(win)

            pygame.display.update()
            clock.tick(60)

    if keys[pygame.K_i]:
        for i in range(0,100):
            iv.update(.1,0,1)
            iv2.update(.2,100,1)
            iv3.update(.3,200,1)
            iv4.update(.4,300,1)
            win.fill((0,0,0))  # Fills the win with black
            win.blit(mapy,(0 -CameraX,0 -CameraY))
            #win.blit(player,(x -CameraX,y -CameraY))
            player.draw(win)
            #iv.draw(win)
            #iv2.draw(win)
            #iv3.draw(win)
            if appleininv == True:
                iv4.draw(win)
            iv5.draw(win)

            pygame.display.flip()
            clock.tick(60)












    if x >=650 and x <= 800 and y >= 850 and forest == False and room == False and cave== False:  #room start to town
        room = True
        town = True
        forest = True
        rocks = False
        mapy = pygame.image.load("ntown.png")
        pygame.mixer.music.load("lofty8bit.mp3")
        pygame.mixer.music.play(-1,0.0)
        pygame.display.update()



        ###
        player.update(character)
        player.draw(win)

        mapy = pygame.transform.scale(mapy, (1200,950))
        x = 130
        y = 400
        CameraX = 0
        CameraY = 240
        hitbox.check_npc(town,845, 632,"mimi.png", mapy, mob_group)
        hitbox.check_npc(town,130, 788,"aziz.png", mapy, aziz_group)
        hitbox.check_npc(town,663, 196,"kyle.png", mapy, kyle_group)
        hitbox.check_npc(rocks,663, 338,"rock1.png", mapy, rock1_group)
        hitbox.check_npc(rocks,863, 538,"rock1.png", mapy, rock2_group)
        hitbox.check_npc(rocks,1063, 438,"tree.png", mapy, tree_group)
        hitbox.check_npc(cave,663, 538,"medusa.png", mapy, medusa_group)

        ##
        pygame.display.update()



        ##specify x and y
    if x >= 140 and x <= 160 and y <= 360 and room == True and forest == True and cave == False: #swith from town to room
        room = False
        forest = False
        town = False
        rocks = False
        x = 775
        y = 840
        CameraX = 550
        CameraY = 450
        mapy = pygame.image.load("bedroom.png")
        mapy = pygame.transform.scale(mapy, (1200,950))
        pygame.mixer.music.load("house.mp3")
        pygame.mixer.music.play(-1,0.0)
        pygame.display.update()

        ###
        player.update(character)
        player.draw(win)
        hitbox.check_npc(town,845, 632,"mimi.png", mapy, mob_group)
        hitbox.check_npc(town,130, 788,"aziz.png", mapy, aziz_group)
        hitbox.check_npc(town,663, 196,"kyle.png", mapy, kyle_group)
        hitbox.check_npc(rocks,663, 338,"rock1.png", mapy, rock1_group)
        hitbox.check_npc(rocks,863, 538,"rock1.png", mapy, rock2_group)
        hitbox.check_npc(rocks,1063, 438,"tree.png", mapy, tree_group)
        hitbox.check_npc(cave,663, 538,"medusa.png", mapy, medusa_group)
        ##
        ##
        pygame.display.update()
    if x >= 720 and x <= 740 and y <= 180 and forest == True and room == True and cave == False: #switch from town to forest
        room = False
        town = False
        forest = True
        rocks = True
        x = 100 #starting location after mapy change
        y = 175
        CameraX = 0
        CameraY = 0

        ###
        mapy = pygame.image.load("nforest.png")
        mapy = pygame.transform.scale(mapy, (1200,950))
        pygame.mixer.music.load("forest.mp3")
        pygame.mixer.music.play(-1,0.0)
        pygame.display.update()

        player.update(character)
        player.draw(win)
        hitbox.check_npc(town,845, 632,"mimi.png", mapy, mob_group)
        hitbox.check_npc(town,130, 788,"aziz.png", mapy, aziz_group)
        hitbox.check_npc(town,663, 196,"kyle.png", mapy, kyle_group)
        hitbox.check_npc(rocks,663, 338,"rock1.png", mapy, rock1_group)
        hitbox.check_npc(rocks,863, 538,"rock1.png", mapy, rock2_group)
        hitbox.check_npc(rocks,1063, 438,"tree.png", mapy, tree_group)
        hitbox.check_npc(cave,663, 538,"medusa.png", mapy, medusa_group)

        ##
        ##

        pygame.display.update()
    if x >= 0 and x <= 50 and y >=180  and y <=220 and cave == False and room == False and forest == True: #swith from forest to town
        forest = False
        room = True
        town = True
        rocks = False
        x = 720
        y = 200
        CameraX = 500
        CameraY = 0
        mapy = pygame.image.load("ntown.png")
        mapy = pygame.transform.scale(mapy, (1200,950))
        pygame.mixer.music.load("lofty8bit.mp3")
        pygame.mixer.music.play(-1,0.0)
        pygame.display.update()

        ###
        player.update(character)
        player.draw(win)
        hitbox.check_npc(town,845, 632,"mimi.png", mapy, mob_group)
        hitbox.check_npc(town,130, 788,"aziz.png", mapy, aziz_group)
        hitbox.check_npc(town,663, 196,"kyle.png", mapy, kyle_group)
        hitbox.check_npc(rocks,663, 338,"rock1.png", mapy, rock1_group)
        hitbox.check_npc(rocks,863, 538,"rock1.png", mapy, rock2_group)
        hitbox.check_npc(rocks,1063, 438,"tree.png", mapy, tree_group)
        hitbox.check_npc(cave,663, 538,"medusa.png", mapy, medusa_group)
        ##
        ##
        pygame.display.update()
    if x >= 550 and x <= 800 and y >= 875 and cave == False and room == False and forest == True: #swith from froest to cave
        cave = True
        forest = False
        town = False
        rocks = False
        x = 200
        y = 250
        CameraX = 50
        CameraY = 50
        mapy = pygame.image.load("cave.png")
        mapy = pygame.transform.scale(mapy, (1200,950))
        pygame.mixer.music.load("cave.mp3")
        pygame.mixer.music.play(-1,0.0)
        pygame.display.update()

        ###
        player.update(character)
        player.draw(win)
        hitbox.check_npc(town,845, 632,"mimi.png", mapy, mob_group)
        hitbox.check_npc(town,130, 788,"aziz.png", mapy, aziz_group)
        hitbox.check_npc(town,663, 196,"kyle.png", mapy, kyle_group)
        hitbox.check_npc(rocks,663, 338,"rock1.png", mapy, rock1_group)
        hitbox.check_npc(rocks,863, 538,"rock1.png", mapy, rock2_group)
        hitbox.check_npc(rocks,1063, 438,"tree.png", mapy, tree_group)
        hitbox.check_npc(cave,663, 538,"medusa.png", mapy, medusa_group)
    ##
        pygame.display.update()
    if x >= 100 and x <= 200 and y <= 200 and room == False and forest == False and cave == True: #swith from cave to forest
        cave = False
        forest = True
        town = False
        rocks = True
        x = 710
        y = 750
        CameraX = 500
        CameraY = 500
        mapy = pygame.image.load("nforest.png")
        mapy = pygame.transform.scale(mapy, (1200,950))
        pygame.mixer.music.load("forest.mp3")
        pygame.mixer.music.play(-1,0.0)
        pygame.display.update()

        ###
        player.update(character)
        player.draw(win)
        hitbox.check_npc(town,845, 632,"mimi.png", mapy, mob_group)
        hitbox.check_npc(town,130, 788,"aziz.png", mapy, aziz_group)
        hitbox.check_npc(town,663, 196,"kyle.png", mapy, kyle_group)
        hitbox.check_npc(rocks,663, 338,"rock1.png", mapy, rock1_group)
        hitbox.check_npc(rocks,863, 538,"rock1.png", mapy, rock2_group)
        hitbox.check_npc(rocks,1063, 438,"tree.png", mapy, tree_group)
        hitbox.check_npc(cave,663, 538,"medusa.png", mapy, medusa_group)
        pygame.display.update()

#
##player is black box
#    mob_group.draw(mapy)
#    player.draw(win)
#    win.fill((0,0,0))  # Fills the screen with black
    #win.blit(mapy,(0 -CameraX,0 -CameraY))
    #player.draw(win)
    #win.blit(player,(x -CameraX,y -CameraY))
    #pygame.display.flip()



pygame.quit()
