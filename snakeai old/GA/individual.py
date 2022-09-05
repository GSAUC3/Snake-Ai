import random,math
from .model import Snakenet
import pygame

scale = 2
BODY_SIZE=10
WIDTH,HEIGHT = 320,240 # 240p

# _______________________________SNAKE________________________________________________________
class block:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
       
class Snake:
    score = 0
    def __init__(self) -> None:
        self.SCORE = 0
        self.brain = Snakenet()
        self.dir = (0,0)
        self.steps=500
        
        x,y = random.randint(20,WIDTH-20),random.randint(20,HEIGHT-20)
        self.nagin = [block(i + x,y) for i in range(10)]

    def reset(self):
        x,y = random.randint(20,WIDTH-20),random.randint(20,HEIGHT-20)
        self.nagin = [block(i + x,y) for i in range(10)]
        
        self.dir=(0,0)
        self.score=0
        
        self.steps=500
    
    def update_score(self,time):
        self.SCORE= self.score
            

    def draw(self,screen):
        for i,body in enumerate(self.nagin):
            snake = pygame.Rect(body.x,body.y,BODY_SIZE,BODY_SIZE)
            pygame.draw.rect(screen,(255,0,(i*10)%255),snake)

    def move(self,screen):
        self.nagin[-1].x+=self.dir[0]*scale
        self.nagin[-1].y+=self.dir[1]*scale
        
        for i in range(len(self.nagin)-1):
            self.nagin[i].x = self.nagin[i+1].x
            self.nagin[i].y = self.nagin[i+1].y
        self.draw(screen)

    def moreche_ki(self):
        for i in self.nagin[:-2]:
            if collide(self.nagin[-1],i)<1:
                
                return True
        if self.nagin[-1].x>(WIDTH-1) or self.nagin[-1].x<1:
            
            return True
        if self.nagin[-1].y>(HEIGHT-1) or self.nagin[-1].y<1:
            
            return True
        return False
                
    def vision(self,foodx,foody):
        '''
        (0,-1) -> UP
        (0,1) -> down
        (1,0) -> right
        (-1,0) -> left
        '''
        x,y=self.nagin[-1].x,self.nagin[-1].y #current location

        encodings=[ 
            #for only direction
            (self.dir==(0,-1)), 
            (self.dir==(0,1)),
            (self.dir==(1,0)),
            (self.dir==(-1,0)),
            # for danger
            (self.dir==(0,-1) and y<15), 
            (self.dir==(0,1) and y>229),
            (self.dir==(1,0) and x>309),
            (self.dir==(-1,0) and x<15),
            # food
            (y>foody),
            (y<foody),
            (x>foodx),
            (x<foodx),
            ]

        collision = 0
        for i in self.nagin[:-2]:
            if collide(self.nagin[-1],i)<20:
                collision =1
            else:
                collision=0
        
        encodings.append(collision)
        encodings=list(map(int,encodings))
        return encodings

# _______________________________APPLE________________________________________________________

class Food:
    def __init__(self) -> None:
        self.x = random.randint(0,WIDTH-10)
        self.y = random.randint(0,HEIGHT-10)

    def draw(self,screen):
        food = pygame.Rect(self.x,self.y,BODY_SIZE,BODY_SIZE)
        pygame.draw.rect(screen,pygame.Color('green'),food)
    
    def reset(self,screen):
        self.__init__()
        self.draw(screen)


def collide(obj1,obj2):
    (o1x,o1y) = ((obj1.x+BODY_SIZE)>>1,(obj1.y+BODY_SIZE)>>1)
    (o2x,o2y) = ((obj2.x+BODY_SIZE)>>1,(obj2.y+BODY_SIZE)>>1)
    
    return math.sqrt((o1x-o2x)**2+(o1y-o2y)**2) 
    