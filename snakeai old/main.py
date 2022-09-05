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
    snakes = Population()
    for i in range(1000):
        score__ =0
        for j,snake in enumerate(snakes.pop):
            score = Game(snake,i,j)
            if score>score__:
                score__=score
        best_snake = snakes.selection()
        print(f'Generation {i+1} Best fitness {best_snake.SCORE} Highest Score {score__}')

if __name__=='__main__':
    main()
