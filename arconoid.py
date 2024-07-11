import pygame
pygame.init()
#global variable
ligth_blue = (200,255,255)
game_over = True
racket_x = 200
racket_y = 330
dx = 3
dy = 3
move_right = False
move_left = False
#global variable
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = ligth_blue
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def coliderect(self, rect):
        return self.rect.coliderect(rect)
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10, color=None):
        super().__init__(x=x, y=y, width=width, height=height, color=None)
        self.img = pygame.image.load(filename)
    def draw(self):
        window.blit(self.img, (self.rect.x, self.rect.y))
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
window = pygame.display.set_mode((500,500))
window.fill(ligth_blue)
clock = pygame.time.Clock()
#veriables with picture
ball = Picture('ball.png', 160,200,50,50)
platform = Picture('platform.png', racket_x, racket_y,100,30)
#veriables with picture
#draw monster
start_x = 5
start_y=5
count = 9
monsters = []
for i in range(3):
    y = start_y+(55*i)
    x = start_x+(27.5 *i)
    for j in range(count):
        m = Picture('enemy1.png', x, y, 50, 50)
        monsters.append(m)
        x+=55
    count-=1
#draw monsters
while game_over:
    ball.fill()
    platform.fill()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False
    #move platformer
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_LEFT:
                move_left= True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_LEFT:
                move_left= False
    if move_right:
        platform.rect.x +=3
    if move_left:
        platform.rect.x -=3
    #move platformer
    #move ball
    ball.rect.x+=dx
    ball.rect.y+=dy
    if ball.rect.y<0:
        dy*=-1
    if ball.rect.colliderect(platform.rect):
        dy*=-1
    if ball.rect.x >450 or ball.rect.x<0:
        dx*=-1
    for m in monsters:
        m.draw()
        if m.rect.colliderect(ball.rect):
            monsters.remove(m)
            m.fill()
            dy*=-1
    if ball.rect.y>350:
        win_text = Label(150,150,50,50, ligth_blue)
        win_text.set_text('You died!!!', 60, (200,0,0))
        win_text.draw()
        game_over=False
    if len(monsters) == 0:
        died_text = Label(150,150,50,50, ligth_blue)
        died_text.set_text('You win!!!', 60, (0,200,0))
        died_text.draw()
        game_over=False

    platform.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(40)