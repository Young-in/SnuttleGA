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

    print("\nOTOC Initial Result")
    print(otoc)
    print("OTOC Cost")
    print(DG.getCost(otoc))
    print(DG.chromoAble(otoc, DG.requests))

    print("\nCFSS Initial Result")
    print(cfss)
    print("CFSS Cost")
    print(DG.getCost(cfss))
    print(DG.chromoAble(cfss, DG.requests))

    print("\nGR Initial Result")
    print(gr)
    print("GR Cost")
    print(DG.getCost(gr))
    print(DG.chromoAble(gr, DG.requests))

    cr = otoc.crossover(gr)
    print("\nOTOC + GR")
    print(cr)
    print(DG.getCost(cr))
    print(DG.chromoAble(cr, DG.requests))

    print("\nmutation")
    cr.mutation(1, 2)
    print(cr)
    print(DG.getCost(cr))
    print(DG.chromoAble(cr, DG.requests))

    crr = cfss.crossOver(otoc)
    print("\nCFSS + OTOC")
    print(crr)
    print(DG.getCost(crr))
    print(DG.chromoAble(crr, DG.requests))

    print("\nmutation")
    crr.mutation(1, 2)
    print(crr)
    print(DG.getCost(crr))
    print(DG.chromoAble(crr, DG.requests))

    cfsss = DG.generateCFSS(DG.requests)
    crs = cfss.crossOver(cfsss)
    print("\nCFSS + CFSS")
    print(crs)
    print(DG.getCost(crs))
    print(DG.chromoAble(crs, DG.requests))

    print("\nmutation")
    crs.mutation(1, 2)
    print(crs)
    print(DG.getCost(crs))
    print(DG.chromoAble(crs, DG.requests))

    print("\nCFSS/OTOC")
    print(DG.getCost(cfss)/DG.getCost(otoc))
    pass


if __name__ == "__main__": # execute when python Simulator.py executed
    main()
    # print(Chromosome.generateRandomly(10,3))