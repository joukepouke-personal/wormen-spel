import pygame
import sys
import random
EMPTY = 0
WALL = 1
WURM = 2
GRASS = 3
FLY = 4
HEAD_WURM = 5
fly_wurm = 6
len_fly = 7
len2_fly = 8
POOP = 9
#dit is de multiplayer versie
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
tick = 1
testing = False
class Game:
    def __init__(self):
        self.score = 0
        self.finished = False
        self.tick = 4
        self.tail_hight = 0
        self.turndown = False
        self.turnleft = False
        self.turnright = False
        self.turnup = False
        

    def pp_field(self):
        for y in range(24):
            chars = ''.join([' #ox.'[self.field[x][y]] for x in range(40)])
            print(chars)
            
        
    def init_field(self):
        self.bonus_at = self.score + 100
        self.crashed = False
        self.crashed1 = False
        self.direction = UP
        self.direction1 = UP
        self.field = [[EMPTY for y in range(100)] for x in range(100)]
        self.i_used = 39
        self.wurm = [(int(1), y_size_of_field - 6 + i) for i in range(5)]
        self.wurm1 = [(int(x_size_of_field - 1), y_size_of_field - 6 + i) for i in range(5)]
        for x,y in self.wurm:
                self.field[x][y] = WURM
        for x, y in self.wurm1:
            self.field[x][y] = WURM
        self.first = True
        for _ in range(random.randint(20, 50)):
            self.place_fly()
        self.first = False

    def place_fly(self):
        try:
            self.nonempty = 0
            while True:
                x = random.randrange(0, x_size_of_field)
                y = random.randrange(0, y_size_of_field)
                if self.field[x][y] == EMPTY:
                    self.field[x][y] = FLY
                    return
                elif self.field[x][y] == FLY:
                    self.field[x][y] = len2_fly
                    return
                elif self.field[x][y] == len2_fly:
                    self.field[x][y] = len_fly
                    return
                elif self.field[x][y] == len_fly:
                    self.field[x][y] = random.choice([POOP, len_fly])
                    return
                else:
                    self.nonempty += 1
                if self.nonempty >= 960:
                    return
        except:
            pass
    def nonempty_fields(self):
        for x, col in enumerate(self.field):
            for y, item in enumerate(col):
                if item != EMPTY:
                    yield (x, y), item
    def move_the_2nd_wurm(self):
        x, y = self.wurm1[0]
        dx, dy = { UP: (0, -1), DOWN: (0, 1), LEFT: (-1, 0), RIGHT: (1, 0) }[self.direction1]
        x = (x + dx) % x_size_of_field
        y = (y + dy) % y_size_of_field
        consume = self.field[x][y]
        consumeplace = [x, y]
        if self.turnup == False and self.turndown\
           == False and self.turnleft == False and self.turnright == False:
            pass
        else:
            self.turndown = False
            self.turnleft = False
            self.turnright = False
            self.turnup = False
            if consume == WURM or consume == WALL:
                self.direction = self.directionfirst
                return
            else:
                pass
        self.field[self.wurm1[0][0]][self.wurm1[0][1]] = WURM
        self.field[x][y] = HEAD_WURM
        self.wurm1.insert(0, (x, y))
        if consume == EMPTY:
               tail_x, tail_y = self.wurm1[-1]
               if self.tail_hight <= 0:
                self.field[tail_x][tail_y] = EMPTY
                self.wurm1.pop()
               else:
                   self.tail_hight = self.tail_hight - 1
        else:
              for i in range (5):
                   self.place_fly()
                   self.make_grass()
              if random.randint(0, 1) == 0:
                   self.make_grass()
        if consume == FLY:
               self.score += self.tick - 3
        elif consume == GRASS:
              self.score += self.tick + 3
        elif consume == len_fly:
             self.score += 3
             self.tail_hight += 3
        elif consume == len2_fly:
             self.score += 2
             self.tail_hight += 2
        elif consume == HEAD_WURM:
            self.crashed = True
        elif consume == WALL or consume == WURM:
           self.field[x][y] = fly_wurm
           if self.bonus_activated == False:
                if testing == False:
                    self.crashed1  = True
                else:
                    return
                if self.score < self.bonus_at:
                    self.finished = True
                else:
                    self.tick += 1
                    self.bonus_at = self.score + 100
           else:
                self.tick += 0.00000000000000000000001
                self.bonus_activated = False
        self.count = 0
        for position in self.wurm1:
             if self.field[position[0]][position[1]] == EMPTY:
                for x, y in self.wurm1[self.wurm1.index(position):]:
                    self.field[x][y] = EMPTY
                self.index = self.wurm1.index(position)
                self.wurm = self.wurm1[ :self.index]
                return
        false = [False, False, False, False]
        self.turnright, self.turnleft, self.turnup, self.turndown = false
    def move(self):
        x, y = self.wurm[0]
        dx, dy = { UP: (0, -1), DOWN: (0, 1), LEFT: (-1, 0), RIGHT: (1, 0) }[self.direction]
        x = (x + dx) % x_size_of_field
        y = (y + dy) % y_size_of_field
        consume = self.field[x][y]
        consumeplace = [x, y]
        if self.turnup == False and self.turndown\
           == False and self.turnleft == False and self.turnright == False:
            pass
        else:
            self.turndown = False
            self.turnleft = False
            self.turnright = False
            self.turnup = False
            if consume == WURM or consume == WALL:
                self.direction = self.directionfirst
                return
            else:
                pass
        self.field[self.wurm[0][0]][self.wurm[0][1]] = WURM
        self.field[x][y] = HEAD_WURM
        self.wurm.insert(0, (x, y))
        if consume == EMPTY:
               tail_x, tail_y = self.wurm[-1]
               if self.tail_hight <= 0:
                self.field[tail_x][tail_y] = EMPTY
                self.wurm.pop()
               else:
                   self.tail_hight = self.tail_hight - 1
        else:
              for i in range (1):
                   self.place_fly()
                   self.make_grass()
              if random.randint(0, 1) == 0:
                   self.make_grass()
        if consume == FLY:
               self.score += self.tick - 3
        elif consume == GRASS:
              self.score += self.tick + 1
        elif consume == len_fly:
             self.score += 3
             self.tail_hight += 3
        elif consume == len2_fly:
             self.score += 2
             self.tail_hight += 2
        elif consume == HEAD_WURM:
            self.crashed1 = True
        elif consume == WALL or consume == WURM:
           self.field[x][y] = fly_wurm
           if self.bonus_activated == False:
                if testing == False:
                    self.crashed  = True
                else:
                    return
                if self.score < self.bonus_at:
                    self.finished = True
                else:
                    self.tick += 1
                    self.bonus_at = self.score + 100
           else:
                self.tick += 0.00000000000000000000001
                self.bonus_activated = False
        self.count = 0
        for position in self.wurm:
             if self.field[position[0]][position[1]] == EMPTY:
                for x, y in self.wurm[self.wurm.index(position):]:
                    self.field[x][y] = EMPTY
                self.index = self.wurm.index(position)
                self.wurm = self.wurm[ :self.index]
                return
        false = [False, False, False, False]
        self.turnright, self.turnleft, self.turnup, self.turndown = false
        for x, col in enumerate(self.field):
            for y, item in enumerate(col):
                if item == POOP:
                    for i in range(7):
                        thing = random.randint(1, 8)
                        dx, dy = {1: (-1, -1), 2: (-1, 0), 3: (-1, 1), 4: (0, -1), 5:(0, 1), 6:(1, -1), 7:(1, 0), 8:(1, 1)} [thing]
                        xyx = (x+dx) %x_size_of_field
                        xyy = (y + dy) %y_size_of_field
                        if self.field[xyx][xyy] == EMPTY:
                            self.field[xyx][xyy] = FLY
                            break
    def make_grass(self):
        x_size = random.randint(60, 499)
        left_x = random.randrange(0 - x_size, x_size_of_field)
        right_x = min(left_x + x_size, x_size_of_field)
        left_x = max(left_x, 0)
        y_size = random.randint(60, 2599)
        top_y = random.randrange(0 - y_size, y_size_of_field)
        bottom_y = min(top_y + y_size, y_size_of_field)
        top_y = max(top_y, 0)

        for x in range(left_x, right_x, 2):
            for y in range(top_y, bottom_y, 2):
                if self.field[x][y] == WALL:
                    self.field[x][y] = GRASS

    def turn_left(self, wurm):
        if wurm:
            if self.direction != 1:
                self.directionfirst = self.direction
                self.direction = 3
                self.turnup = True
        else:
            if self.direction1 != 1:
                self.directionfirst1 = self.direction1
                self.direction1 = 3
                self.turnup = True

    def turn_right(self, wurm):
        if wurm:
            if self.direction != 3:
                self.directionfirst = self.direction
                self.direction = 1
                self.turnup = True
        else:
            if self.direction1 != 2:
                self.directionfirst1 = self.direction1
                self.direction1 = 0
                self.turnup = True
        
    def turn_up(self, wurm):
        if wurm:
            if self.direction != 2:
                self.directionfirst = self.direction
                self.direction = 0
                self.turnup = True
        elif wurm == False:
            if self.direction1 != 2:
                self.directionfirst1 = self.direction1
                self.direction1 = 0
                self.turnup = True
    def turn_down(self, wurm):
        if self.direction != 0:
            self.directionfirst = self.direction
            self.direction = 2
            self.turndown = True
    def make_wall(self, wurm='both'):
        if wurm == 'both' or wurm == 1:
            for x, y in self.wurm1[5:]:
                self.field[x][y] = WALL
                self.wurm1 = self.wurm1[:5]
        if wurm == 'both' or wurm == 0:
            for x, y in self.wurm[5:]:
                self.field[x][y] = WALL
                self.wurm = self.wurm[:5]
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-4,self.y-4,self.width+8,self.height+8),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            
            text = fnt.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
        
screen = pygame.display.set_mode((900, 600))
the_game = Game()
pygame.init()
fnt = pygame.font.SysFont("console,monospace", 32, bold=True)
ebutton = button([255, 0, 0], 300, 50
                 , 150, 50, 'mega')
bbutton = button([255, 0, 0], 300, 150
                 , 150, 50, 'groot')
mbutton = button([255, 0, 0], 300, 250
                 , 150, 50, 'middel')
sbutton = button([255, 0, 0], 300, 350
                 , 150, 50, 'klein')
ibutton = button([255, 0, 0], 300, 450
                 , 150, 50, 'mini')
clock = pygame.time.Clock()
def flip():
    ebutton.draw(screen, (0, 255, 0))
    bbutton.draw(screen, (0, 255, 0))
    mbutton.draw(screen, (0, 255, 0))
    sbutton.draw(screen, (0, 255, 0))
    ibutton.draw(screen, (0, 255, 0))
    hdr = fnt.render(
            "hoe groot wil je dat het veld is?", 
            0, # antialias
            (255,255,255), # color
            )
    screen.blit(hdr, (32, 0))
    hdr = fnt.render(
            words, 
            0, # antialias
            (255,255,255), # color
            )
    screen.blit(hdr, (50, 550))
    pygame.display.flip()
words = ''
breakTrue = None
mouse  = False
while True:
    flip()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bbutton.isOver(pygame.mouse.get_pos()):
                    x_size_of_field = 60
                    y_size_of_field = 31
                    breakTrue = True
            elif mbutton.isOver(pygame.mouse.get_pos()) is True:
                    x_size_of_field = 40
                    y_size_of_field = 24
                    breakTrue = True
            elif sbutton.isOver(pygame.mouse.get_pos()):
                    x_size_of_field = 20
                    y_size_of_field = 15
                    breakTrue = True
            elif ebutton.isOver(pygame.mouse.get_pos()):
                    x_size_of_field = 100
                    y_size_of_field = 40
                    breakTrue = True
            elif ibutton.isOver(pygame.mouse.get_pos()):
                    x_size_of_field = 3
                    y_size_of_field = 15
                    breakTrue = True
            mouse = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse = False
        elif event.type is pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.TEXTINPUT:
                words = words + event.text 
        elif event.type == pygame.KEYDOWN:
            if event.key == 8:
                words = words[:-1]
                screen.fill((0, 0, 0))
    clock.tick(8)
    if words == 'hack':
        testing = True
    if words == 'updownerror':
        pygame.K_DOWN = 6849586
        pygame.K_UP = 67657789
    if words == 'leftrighterror':
        pygame.K_LEFT = 'gjjjjjjjjjt'
        pygame.K_RIGHT = 85974
    if words == 'mouseerror':
        pygame.MOUSEBUTTONDOWN = 'tgf'
    if breakTrue:
        break
the_game = Game()
high_score = 0

pygame.init()
assert(pygame.font.get_init())
import pygame
pygame.init()
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True

# for al the connected joysticks
for i in range(0, pygame.joystick.get_count()):
    # create an Joystick object in our list
    joysticks.append(pygame.joystick.Joystick(i))
    # initialize them all (-1 means loop forever)
    joysticks[-1].init()
    # print a statement telling what the name of the controller is
    print ("Detected joystick "),joysticks[-1].get_name(),"'"
BX = 32

fnt = pygame.font.SysFont(("console,monospace"), BX, bold=True)

wall_img = pygame.Surface((BX, BX))
pygame.draw.rect(wall_img, (255,255,255), (0, 0, BX, BX), width=BX//10)

fly_img = pygame.Surface((BX, BX))
pygame.draw.lines(fly_img, (255, 25, 25), True, points=[
    (0, 0),
    (BX-1, BX-1),
    (BX-1, BX//2),
    (0, BX//2),
    ], width=BX//10)

len_fly_img = pygame.Surface((BX, BX))
pygame.draw.lines(len_fly_img, (85, 0, 145), True, points=[
    (0, 0),
    (BX-1, BX-1),
    (BX-1, BX//2),
    (0, BX//2),
    ], width=BX//10)
len2_fly_img = pygame.Surface((BX, BX))
pygame.draw.lines(len2_fly_img, (243.94921875, 169.66015625, 49.19140625), True, points=[
    (0, 0),
    (BX-1, BX-1),
    (BX-1, BX//2),
    (0, BX//2),
    ], width=BX//10)

grass_img = pygame.Surface((BX, BX))
grass_img_color = (10, 200, 10)
pygame.draw.line(grass_img, grass_img_color, (BX//10, BX//10), (9 * BX // 10, 9 * BX // 10), width=BX//10)
for n in 2, 4, 6, 8:
    pygame.draw.line(grass_img, grass_img_color, (n * BX // 10, 0), (n * BX // 10, n * BX // 10), width=BX//10)
    pygame.draw.line(grass_img, grass_img_color, (0, n * BX // 10), (n * BX // 10, n * BX // 10), width=BX//10)

wurm_img = pygame.Surface((BX, BX))
pygame.draw.rect(wurm_img, (100, 255, 100), (0, 0, BX, BX), border_radius=BX//3)
wurm_img1 = pygame.Surface((BX, BX))
pygame.draw.rect(wurm_img1, (0.0, 224.875, 217.84765625), (0, 0, BX, BX), border_radius=BX//3)
poop_img = pygame.Surface((BX, BX))
pygame.draw.rect(poop_img, (211.82421875, 153.59765625, 120.46875), (0, 0, BX, BX), border_radius=BX//3)
head_wurm_img = pygame.Surface((BX, BX))
pygame.draw.rect(head_wurm_img, (149, 0, 255), (0, 0, BX, BX), border_radius=BX//3)
pygame.draw.circle(head_wurm_img, (0, 0, 0), (9, 9,), 5)
pygame.draw.circle(head_wurm_img, (0, 0, 0), (23, 9,), 5)
pygame.draw.line(head_wurm_img, (0, 0, 0), (25, 25), (7, 25), 5)

fly_wurm_img = pygame.Surface((BX, BX))
pygame.draw.rect(fly_wurm_img, (255, 255, 255), (0, 0, BX, BX), border_radius=BX//3)
pygame.draw.circle(fly_wurm_img, (255, 25, 25), (9, 9,), 5)
pygame.draw.circle(fly_wurm_img, (255, 25, 25), (23, 9,), 5)
pygame.draw.line(fly_wurm_img, (255, 25, 25), (25, 25), (7, 25), 5)

screen = pygame.display.set_mode((x_size_of_field * BX, (y_size_of_field + 2) * BX), pygame.RESIZABLE)
down_head_wurm_img = pygame.transform.rotate(head_wurm_img, 180)
down_fly_wurm_img = pygame.transform.rotate(fly_wurm_img, 180)
right_head_wurm_img = pygame.transform.rotate(head_wurm_img, 270)
right_fly_wurm_img = pygame.transform.rotate(fly_wurm_img, 270)
left_head_wurm_img = pygame.transform.rotate(head_wurm_img, 90)
left_fly_wurm_img = pygame.transform.rotate(fly_wurm_img, 90)
real_fly_wurm_img = fly_wurm_img
real_head_wurm_img = head_wurm_img

def item_to_surface(item,x1,y1,self, init = False):
    if item == WALL:
        return wall_img
    if item == WURM:
        for x, y in self.wurm:
            if (x, y) == (x1, y1):
                init = True
        if init:
            return wurm_img
        else:
            return wurm_img1
    if item == GRASS:
        return grass_img
    if item == FLY:
        return fly_img
    if item == HEAD_WURM:
        return real_head_wurm_img
    if item == fly_wurm:
        return real_fly_wurm_img
    if item == len_fly:
        return len_fly_img
    if item == len2_fly:
        return len2_fly_img
    if item == POOP:
        return poop_img

def draw_screen(game):
    screen.fill((146, 25, 25))
    screen.blits(blit_sequence=(
        (item_to_surface(item, x, y, game), (x * BX, (y + 1) * BX))
        for (x, y), item in game.nonempty_fields()), doreturn=0)
    hdr = fnt.render(
            "score: %d     bonus at: %d " % (the_game.score, the_game.bonus_at),
            0, # antialias
            (255,255,255), # color
            )
    screen.blit(hdr, (BX, 0))
    hs = fnt.render("high score: %d" % high_score, 0, (255,255,255))
    screen.blit(hs, (BX * 39 - hs.get_width(), 0))
    hdr = fnt.render(
                        words, 
                        0, # antialias
                        (255,255,255), # color
                        )
    screen.blit(hdr, (50, (y_size_of_field + 1) * BX))

clock = pygame.time.Clock()
the_game.bonus_activated = False
first = True
pygame.display.set_icon(head_wurm_img)
pygame.display.set_caption('wurm spelletje')
self = the_game
def mainloop():
    pass
while True:
    the_game.init_field()
    the_game.bonus_activated = False
    while not the_game.crashed or not the_game.crashed1:
        draw_screen(the_game)
        
        if the_game.bonus_activated == True:
            pygame.Surface((BX, BX))
            pygame.draw.rect(wurm_img, (255, 255, 255), (0, 0, BX, BX), border_radius=BX//3)
        if the_game.bonus_activated == False:
            wurm_img = pygame.Surface((BX, BX))
            pygame.draw.rect(wurm_img, (100, 255, 100), (0, 0, BX, BX), border_radius=BX//3)
        pygame.display.flip()
        clock.tick(the_game.tick)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(1)
            if event.type == pygame.JOYHATMOTION:
                try:
                    if event.joy == 0:
                        if event.value == (1, 0):
                            the_game.direction = RIGHT
                        elif event.value == (-1, 0):
                            the_game.direction = LEFT
                        elif event.value == (0, 1):
                            the_game.direction = UP
                        elif event.value == (0, -1):
                            the_game.direction = DOWN
                    if event.joy == 1:
                        if event.value == (1, 0):
                            the_game.direction1 = RIGHT
                        if event.value == (-1, 0):
                            the_game.direction1 = LEFT
                        if event.value == (0, 1):
                            the_game.direction1 = UP
                        if event.value == (0, -1):
                            the_game.direction1 = DOWN
                except:
                    pass
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    the_game.make_wall(event.joy)
                elif event.button == 3:
                    if event.joy == 0:
                        if 2 == 2:
                            wurm = the_game.wurm
                            the_game.wurm = the_game.wurm1
                            the_game.wurm1 = wurm
                elif event.button == 2:
                    if the_game.score > self.bonus_at:
                        the_game.bonus_activated = True
                        the_game.bonus_at += 100
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    the_game.turn_left(True)
                    real_head_wurm_img = left_head_wurm_img
                    real_fly_wurm_img = left_fly_wurm_img
                elif event.key == pygame.K_RIGHT:
                    real_head_wurm_img = right_head_wurm_img
                    real_fly_wurm_img = right_fly_wurm_img
                    the_game.turn_right(True)
                elif event.key == pygame.K_DOWN:
                    real_head_wurm_img = down_head_wurm_img
                    real_fly_wurm_img = down_fly_wurm_img
                    the_game.turn_down(True)
                elif event.key == pygame.K_UP:
                    real_head_wurm_img = head_wurm_img
                    real_fly_wurm_img = fly_wurm_img
                    the_game.turn_up(True)
                elif event.key == 1073741920:
                    the_game.direction1 = UP
                elif event.key == 1073741918:
                    the_game.direction1 = RIGHT
                    
                elif event.key == 1073741916:
                    the_game.direction1 = LEFT
                elif event.key == 1073741917:
                    the_game.direction1 = DOWN
                elif event.key == 8:
                    words = words[:-1]
                    screen.fill((0, 0, 0))
                elif event.key == pygame.K_ESCAPE:
                     if not screenbig:
                         screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
                     else:
                         screen = pygame.display.set_mode((x_size_of_field, y_size_of_field))
                if event.key == 13:
                    wordlist = words.split(' ')
                    if wordlist[0] == 'screen':
                        try:
                            screen_x = int(wordlist[1])
                            screen_y = int(wordlist[2])
                        except Exception as error:
                            
                            screen_x, screen_y = [x_size_of_field, y_size_of_field]
                        words = ''
                        x_size_of_field = screen_x + 1
                        y_size_of_field = screen_y + 1
                        screen = pygame.display.set_mode((screen_x * BX + BX, screen_y * BX + BX))
            elif event.type == pygame.TEXTINPUT:
                words = words + event.text
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    the_game.make_wall()
                elif event.button == 3:
                   if the_game.bonus_at < the_game.score:
                    the_game.bonus_activated = True
                    the_game.bonus_at += 100
            elif event.type == pygame.WINDOWRESIZED:
                screen_size = pygame.display.get_surface()
                screen_x_size = screen_size.get_width()
                screen_y_size = screen_size.get_height()
                infox = int(screen_x_size / BX)
                infoy = int(screen_y_size / BX)
                y_size_of_field = infoy
                x_size_of_field = infox
                
        if not the_game.crashed1:
            the_game.move_the_2nd_wurm()
        if not the_game.crashed:
            the_game.move()
                    
            
                            

    for _ in range(5):
        draw_screen(the_game)
        pygame.display.flip()
        clock.tick(8)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    if the_game.finished:
        if the_game.score > high_score:
            high_score = the_game.score
        the_game = Game()

# pappa is lief
