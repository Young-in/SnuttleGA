from DataGenerator import DataGenerator
from Visualization import Visualization
from Chromosome import Chromosome

def main():
    DG = DataGenerator(n = 50, m = 10)
    print(DG)
    V = Visualization()
    V.drawPoints([coord[0] for coord in DG.stations], [coord[1] for coord in DG.stations], 'stations')
    print("generating otoc...")
    otoc = DG.generateOTOC(DG.requests)
    print("generating cfss...")
    cfss = DG.generateCFSS(DG.requests)
    gr = Chromosome.generateRandomly(50, 10)

    print("\nOTOC Result")
    print(otoc)
    print("OTOC Cost")
    print(DG.getCost(otoc))

    print("\nCFSS Result")
    print(cfss)
    print("CFSS Cost")
    print(DG.getCost(cfss))


    print(gr)
    print(DG.getCost(gr))

    cr = otoc.crossover(gr)
    print(cr)
    print(DG.getCost(cr))

    cr.mutation(1,2)
    print(cr)
    print(DG.getCost(cr))
    pass

if __name__ == "__main__": # execute when python Simulator.py executed
    main()
    # print(Chromosome.generateRandomly(10,3))