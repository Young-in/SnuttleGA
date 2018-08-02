from MapGenerator import MapGenerator
from RequestGenerator import RequestGenerator
from DataGenerator import DataGenerator
from Visualization import Visualization
from Chromosome import Chromosome

def main():
    MAP = MapGenerator(m=10)
    Reqs = RequestGenerator(Map = MAP, typ = 'rand', n = 50)

    DG = DataGenerator(dists = MAP.dists, requests = Reqs.requests)

    print(MAP)
    print(Reqs)
    V = Visualization()
    V.drawPoints([coord[0] for coord in MAP.stations], [coord[1] for coord in MAP.stations], 'stations')
    print("generating otoc...")
    otoc = DG.generateOTOC()
    print("generating cfss...")
    cfss = DG.generateCFSS()
    gr = DG.generateRAND()

    print("\nOTOC Initial Result")
    print(otoc)
    print("OTOC Cost")
    print(DG.getCost(otoc))
    print(DG.chromoAble(otoc))

    print("\nCFSS Initial Result")
    print(cfss)
    print("CFSS Cost")
    print(DG.getCost(cfss))
    print(DG.chromoAble(cfss))

    print("\nGR Initial Result")
    print(gr)
    print("GR Cost")
    print(DG.getCost(gr))
    print(DG.chromoAble(gr))

    cr = otoc.crossover(gr)
    print("\nOTOC + GR")
    print(cr)
    print(DG.getCost(cr))
    print(DG.chromoAble(cr))

    print("\nmutation")
    cr.mutation(1, 2)
    print(cr)
    print(DG.getCost(cr))
    print(DG.chromoAble(cr))

    crr = cfss.crossOver(otoc)
    print("\nCFSS + OTOC")
    print(crr)
    print(DG.getCost(crr))
    print(DG.chromoAble(crr))

    print("\nmutation")
    crr.mutation(1, 2)
    print(crr)
    print(DG.getCost(crr))
    print(DG.chromoAble(crr))

    cfsss = DG.generateCFSS()
    crs = cfss.crossOver(cfsss)
    print("\nCFSS + CFSS")
    print(crs)
    print(DG.getCost(crs))
    print(DG.chromoAble(crs))

    print("\nmutation")
    crs.mutation(1, 2)
    print(crs)
    print(DG.getCost(crs))
    print(DG.chromoAble(crs))

    print("\nCFSS/OTOC")
    print(DG.getCost(cfss)/DG.getCost(otoc))
    pass


if __name__ == "__main__": # execute when python Simulator.py executed
    main()
    # print(Chromosome.generateRandomly(10,3))