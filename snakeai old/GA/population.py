from .individual import Snake
import torch,random,copy


class Population:
    def __init__(self,numpop=100):
        self.numpop=numpop
        self.pop =  [Snake() for _ in range(self.numpop)]
        self.prev_score=0

    def selection(self):
        self.pop = sorted(self.pop,key=lambda x:x.SCORE,reverse=True)
        # return best_snakes
        if self.prev_score<self.pop[0].SCORE:
            self.pop[0].brain.save()
            self.prev_score=self.pop[0].SCORE

        best_snake = self.pop[0]
  

        new_pop=[]
        # t=torch.tensor(fitnesses)
        # _,idx = t.topk(10)
        while len(new_pop)<=90:
            idx = random.randint(0,89)
            idx1 = random.randint(0,89)
            partnera = self.pop[:90][idx]
            partnerb = self.pop[:90][idx1]
            child =self.__crossover(partnera,partnerb)

            new_pop.append(child)

        new_pop.extend(self.pop[:10])
        self.pop = new_pop
        return best_snake

    def __crossover(self,ma,baba,mr=0.1):
        child = Snake()
        result = copy.deepcopy(ma.brain)
        with torch.no_grad():    
            for param in result.parameters():
                if len(param.shape) == 2: 
                    for i0 in range(param.shape[0]):
                        for i1 in range(param.shape[1]):
                            if i0 < (param.shape[0] / 2) and i1 < (param.shape[1]):
                                for p in baba.brain.parameters():
                                    if len(p.shape) == 2 and param.shape == p.shape:
                                        param[i0][i1] = p[i0][i1]
                            else:
                                for p in ma.brain.parameters():
                                    if len(p.shape) == 2 and param.shape == p.shape:
                                        param[i0][i1] = p[i0][i1]
                            
        # mutation
            for i in result.brain.parameters():
                if random.random()<mr:
                    i.data += random.random() * torch.randn_like(i)
                    # i.data += mr.power * torch.randn_like(i)
            
        child.brain=result
        return child              
                        
    
    

