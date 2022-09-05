# Snake Ai (using Genetic Algorithm)

Libraries Required:
- Pygame: to create the snake game
- PyTorch: to create the "brain" of the snake a.k.a a neural net

## Demo

<a href="https://www.youtube.com/watch?v=omZq7bOftdw"><img src="https://github.com/GSAUC3/Snake-Ai/blob/master/img/gif.gif" width="300" height="300"></a>

## What is Genetic Algorithm is all about?
Genetic algorithm is a guided search algorithm, which is inspired by Darwin's theory of natural selection. In this context, we are searching for that one snake 🐍, that can survive in any given environment. 

### Steps involved in the algorithm:
- POPULATION | initialize a population 
- FITNESS    | calculate the fitness of each and every snake
- SELECTION  | select the snakes with higher fitness value
- CROSSOVER  | after selection, pick randomly two snakes and produce a child using crossover method
- MUTATION   | then the child will go through a mutation process, based on a mutation rate, usually lower than 0.1

### Flowchart:

<img src="https://github.com/GSAUC3/Snake-Ai/blob/master/img/chart.png" width="364" height="534">


## Neural Network Architecture
```
Snakenet(
  (brain): Sequential(
    (0): Linear(in_features=13, out_features=16, bias=False)
    (1): ReLU()
    (2): Linear(in_features=16, out_features=8, bias=False)
    (3): ReLU()
    (4): Linear(in_features=8, out_features=4, bias=False)
  )
)
```
<img src="https://github.com/GSAUC3/Snake-Ai/blob/master/img/nn.svg">


Click the image below to see it on youtube:
<a href="https://www.youtube.com/watch?v=BjQBL59C5Ms&t=1s"><img src="https://github.com/GSAUC3/Snake-Ai/blob/master/img/sap.png"></a>




