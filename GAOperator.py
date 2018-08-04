from DataGenerator import DataGenerator
import Chromosome
import Pool
import random

class GAOperator:
    def __init__(self, DG: DataGenerator, initial: str):
        genes = []
        costs = []

        Ngene = 1000 # the number of genes
        Nggene = 20 # the number of genes which can survive


        if initial == 'RAND':
            for i in range(20):
                genes.append(DG.generateRAND())
        elif initial == 'OTOC':
            for i in range(20):
                genes.append(DG.generateOTOC())
        elif initial == 'CFSS':
            for i in range(20):
                genes.append(DG.generateCFSS())

        
        for i in range(Nggene, Ngene):
            i1 = random.randrange(Nggene)
            i2 = random.randrange(Nggene)
            genes.append(genes[i1].crossover(genes[i2]))

        genes.sort(key = lambda gene : DG.getCost(gene))
        costs.append(DG.getCost(genes[0]))

        Nstep = 100 # the number of steps of evolution

        for i in range(Nstep):
            print("{idx} step is running".format(idx = i))
            
            genes = genes[:Nggene]

            for j in range(Nggene, Ngene):
                i1 = random.randrange(Nggene)
                i2 = random.randrange(Nggene)
                genes.append(genes[i1].crossover(genes[i2]))

            for j in range(Nggene, Ngene):
                if random.random() < 1:
                    i1 = random.randrange(DG.m) + 1
                    # i2 = random.randrange(DG.m) + 1
                    i2 = DG.getSimilarRequest(i1 - 1) + 1
                    genes[j].mutation(i1, i2)
            
            genes.sort(key = lambda gene : DG.getCost(gene))
            costs.append(DG.getCost(genes[0]))
        print(costs)

    def __str__(self):
        pass