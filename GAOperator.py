from DataGenerator import DataGenerator
import Chromosome
import Pool
import random

class GAOperator:
    def __init__(self, DG, initial):
        genes = []
        self.costs = []

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
        self.costs.append(DG.getCost(genes[0]))

        Nstep = 50 # the number of steps of evolution

        for i in range(Nstep):
            print("{idx} step is running".format(idx = i+1))
            
            genes = genes[:Nggene]

            # Crossover
            for j in range(Nggene, Ngene):
                i1 = random.randrange(Nggene)
                i2 = random.randrange(Nggene)
                genes.append(genes[i1].crossover(genes[i2]))

            # Mutation
            for j in range(Nggene, Ngene):
                if random.random() < 0.1:
                    i1 = random.randrange(DG.n) + 1
                    # i2 = random.randrange(DG.m) + 1
                    i2 = DG.getSimilarRequest(i1 - 1) + 1
                    genes[j].mutation(i1, i2)

            for j in range(Nggene, Ngene):
                self.optimize(genes[j], DG)
            
            genes.sort(key = lambda gene : DG.getCost(gene))
            self.costs.append(DG.getCost(genes[0]))
            if(self.costs[i] > self.costs[i+1]) :
                print("{}% improved".format((1-(self.costs[i+1]/self.costs[i]))*100))

        print("\nresults.....")
        for i in range(Nstep+1):
            print("%f %d th" %(self.costs[i], i+1))

    def __str__(self):
        pass

    def optimize(self, chromo, DG):
        pass
