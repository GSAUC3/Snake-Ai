from GA.population import Population
from game import Game

# _____________________________________________________________________________________
'''
[up, down, right, left] one hot encoding
up   ->    [1,0,0,0] -> idx = 0 -> (0,-1)
down ->    [0,1,0,0] -> idx = 1 -> (0,1)
right ->    [0,0,1,0] -> idx = 2 -> (1,0)
left->    [0,0,0,1] -> idx = 3 -> (-1,0)

dir_list = [(0,-1),(0,1),(1,0),(-1,0)]
'''
    


# ________________________RUN LOOP_____________________________________________________________

def check(popula):
    for saap in popula:
        for i in saap.brain.parameters():
            print(i)

def main():
    # score =0
    snakes = Population()
    for i in range(1000):
        # print('-'*100)
        
        # check(snakes.pop)

        for j,snake in enumerate(snakes.pop):
           Game(snake,i,j)
           
        #    x=
        #    if score<x:
        #     score=x

        best_snake = snakes.selection()
        # print(snakes.pop[0].SCORE)
        # break
        print(f'Generation {i+1} Best fitness {best_snake.SCORE}')

if __name__=='__main__':
    main()
