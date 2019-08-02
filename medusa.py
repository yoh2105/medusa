import pygame, sys
from pygame.locals import *



#Cannot move while inventory is opening or closing or showing


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



def run_game():
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    x = 220
    y = 360
    width = 53
    height = 77
    vel = 13

    forest = False
    room = False
    cave = False

    walkLeft = ['l1.png', 'l2.png', 'l3.png']

    walkRight = ['r1.png', 'r2.png', 'r3.png']

    walkUp = ['b1.png', 'b2.png', 'b3.png']

    walkDown = ['f1.png', 'f2.png', 'f3.png']

    character="f2.png"
    player=pygame.image.load(character).convert_alpha()
    player = pygame.transform.scale(player, (53,77))

    mapy = pygame.image.load("bedroom.png")
    mapy = pygame.transform.scale(mapy, (1200,950))


    CameraX = 30
    CameraY = 160
    boundary_x_lower = 0
    boundary_x_upper = 500


##################################3
    clock = pygame.time.Clock()

    counter = 0
    run = True

    iv = pygame.sprite.Group(Circle(400,50, win,"sword.jpg"))
    iv2 = pygame.sprite.Group(Circle(400,50, win,"boy.jpg"))
    iv3 = pygame.sprite.Group(Circle(400, 50, win,"letter.jpg"))
    iv4 = pygame.sprite.Group(Circle(400,50, win,"apple.png"))
    iv5 = pygame.sprite.Group(Circle(400,50, win, "backpack.png"))

    open_iv = False
    closed_iv = False


    while run:
        print(x,y)
        iv5.draw(win)
        pygame.display.update()
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player = pygame.image.load(walkLeft[counter])
            player =  pygame.transform.scale(player, (53,77))
            counter = (counter + 1) % len(walkLeft)
            x -= vel
            CameraX -= 10
            if x <= 0:
                x += 14
            if CameraX <= 0:
                CameraX += 10

        if keys[pygame.K_RIGHT]:
            player = pygame.image.load(walkRight[counter])
            player =  pygame.transform.scale(player, (53,77))
            counter = (counter + 1) % len(walkRight)
            x += vel
            CameraX += 10
            if x >= 1080:
                x -= 14
            if CameraX >= 650:
                CameraX -= 10

        if keys[pygame.K_UP]:
            player = pygame.image.load(walkUp[counter])
            player =  pygame.transform.scale(player, (53,77))
            counter = (counter + 1) % len(walkUp)
            y -= vel
            CameraY -= 10
            if y <= 0:
                y += 14
            if CameraY <= 0:
                CameraY += 10

        if keys[pygame.K_DOWN]:
            player = pygame.image.load(walkDown[counter])
            player =  pygame.transform.scale(player, (53,77))
            counter = (counter + 1) % len(walkDown)
            y += vel
            CameraY += 10
            if y >= 880:
                y -= 14
            if CameraY >= 450:
                CameraY -= 10

        if keys[pygame.K_TAB]:
            for i in range(0,150):
                iv.update(.1,0,2)
                iv2.update(.2,100,2)
                iv3.update(.3,200,2)
                iv4.update(.4,300,2)
                win.fill((0,0,0))  # Fills the win with black
                win.blit(mapy,(0 -CameraX,0 -CameraY))
                win.blit(player,(x -CameraX,y -CameraY))
                iv.draw(win)
                iv2.draw(win)
                iv3.draw(win)
                iv4.draw(win)
                iv5.draw(win)

                pygame.display.update()
                clock.tick(60)

        if keys[pygame.K_SPACE]:
            for i in range(0,100):
                iv.update(.1,0,1)
                iv2.update(.2,100,1)
                iv3.update(.3,200,1)
                iv4.update(.4,300,1)
                win.fill((0,0,0))  # Fills the win with black
                win.blit(mapy,(0 -CameraX,0 -CameraY))
                win.blit(player,(x -CameraX,y -CameraY))
                iv.draw(win)
                iv2.draw(win)
                iv3.draw(win)
                iv4.draw(win)
                iv5.draw(win)

                pygame.display.flip()
                clock.tick(60)


        if x >=650 and x <= 800 and y >= 850 and forest == False and room == False and cave== False:  #room start to town
            room = True
            forest = True
            mapy = pygame.image.load("ntown.png")
            player=pygame.image.load(character).convert_alpha()
            player = pygame.transform.scale(player, (53,77))
            mapy = pygame.transform.scale(mapy, (1200,950))
            x = 130
            y = 400
            CameraX = 0
            CameraY = 240
            pygame.display.update()
        if x >= 140 and x <= 160 and y <= 360 and room == True and forest == True and cave == False: #swith from town to room
            room = False
            forest = False
            x = 775
            y = 840
            CameraX = 550
            CameraY = 450
            mapy = pygame.image.load("bedroom.png")
            mapy = pygame.transform.scale(mapy, (1200,950))
            player=pygame.image.load(character).convert_alpha()
            player = pygame.transform.scale(player, (53,77))
            pygame.display.update()
        if x >= 720 and x <= 740 and y <= 180 and forest == True and room == True and cave == False: #switch from town to forest
            room = False
            x = 100 #starting location after mapy change
            y = 175
            CameraX = 0
            CameraY = 0
            player=pygame.image.load(character).convert_alpha()
            player = pygame.transform.scale(player, (53,77))
            mapy = pygame.image.load("nforest.png")
            mapy = pygame.transform.scale(mapy, (1200,950))
            pygame.display.update()
        if x >= 0 and x <= 50 and y >=180  and y <=220 and cave == False and room == False and forest == True: #swith from forest to town
            forest = True
            room = True
            x = 720
            y = 200
            CameraX = 500
            CameraY = 0
            mapy = pygame.image.load("ntown.png")
            mapy = pygame.transform.scale(mapy, (1200,950))
            player=pygame.image.load(character).convert_alpha()
            player = pygame.transform.scale(player, (53,77))
            pygame.display.update()
        if x >= 550 and x <= 800 and y >= 875 and cave == False and room == False and forest == True: #swith from froest to cave
            cave = True
            forest = False
            x = 200
            y = 250
            CameraX = 50
            CameraY = 50
            mapy = pygame.image.load("cave.png")
            mapy = pygame.transform.scale(mapy, (1200,950))
            player=pygame.image.load(character).convert_alpha()
            player = pygame.transform.scale(player, (53,77))
            pygame.display.update()
        if x >= 100 and x <= 200 and y <= 200 and room == False and forest == False and cave == True: #swith from cave to forest
            cave = False
            forest = True
            x = 710
            y = 750
            CameraX = 500
            CameraY = 500
            mapy = pygame.image.load("nforest.png")
            mapy = pygame.transform.scale(mapy, (1200,950))
            player=pygame.image.load(character).convert_alpha()
            player = pygame.transform.scale(player, (53,77))
            pygame.display.update()

        win.fill((0,0,0))  # Fills the win with black
        win.blit(mapy,(0 -CameraX,0 -CameraY))
        win.blit(player,(x -CameraX,y -CameraY))
        pygame.display.flip()


run_game()
pygame.quit()
