import pygame,torch,time
from GA.individual import Food,block,collide


WIDTH,HEIGHT = 320,240 # 240p

dir_list = [(0,-1),
            (0,1),
            (1,0),
            (-1,0)]

def Game(snake,i,js):
    
    fruit = Food()
    # __score__= 0
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    # clock = pygame.time.Clock()
    run=True
    stime = time.time()
    while run:
        pygame.display.update()
        screen.fill((0,0,0))
        fruit.draw(screen)     
        
        encode = snake.vision(fruit.x,fruit.y)
        encode = torch.tensor(encode)
        
        preds=snake.brain(encode.float())
        ids = torch.argmax(preds)
        snake.dir = dir_list[ids]
        snake.move(screen)
        snake.steps+=1
        # eating the fruit logic
        if collide(snake.nagin[-1],fruit)<5:
            snake.score+=5
            snake.steps=0
            snake.nagin.append(block(fruit.x,fruit.y))
            fruit.reset(screen)

        if snake.score < snake.score+5 and snake.steps>5000:
            snake.deaths +=3
            stime=time.time()
            run=False

        b = snake.moreche_ki()   
        
        snake.update_score(time.time()-stime)

        title_font = pygame.font.SysFont("comicsans", 20)
        title_label = title_font.render(f'{str(snake.score)} sID: {js}', 1, (255,255,255))
        _label = title_font.render(f'{str(snake.steps)} Gen {i+1}', 1, (255,255,255))
        screen.blit(title_label,(10,10))
        screen.blit(_label,(200,10))
        
        # clock.tick(60)
            
        if b or run==False:
            # __score__ = snake.score
            snake.reset()
            run=False
    # return __score__

