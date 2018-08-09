from MapGenerator import MapGenerator
from RequestGenerator import RequestGenerator
from DataGenerator import DataGenerator
from Visualization import Visualization
from Chromosome import Chromosome
from GAOperator import GAOperator

def main():
    INF = 10000000

    MAP = MapGenerator(m=10, typ = 'clust')
    Reqs = RequestGenerator(Map = MAP, typ = 'CS', n = 50, T = 1000)
    DG = DataGenerator(MG = MAP, RG = Reqs)
    cfss = DG.generateCFSS() # for available map test

    while DG.getCost(cfss) == INF :
        print('Map Regenerating..')
        MAP = MapGenerator(m=10, typ = 'clust')
        Reqs = RequestGenerator(Map = MAP, typ = 'CS', n = 50, T = 1000)
        DG = DataGenerator(MG = MAP, RG = Reqs)
        cfss = DG.generateCFSS() # for available map test
    print('------------------------------------')

    print(MAP)
    print(Reqs)
    V = Visualization()
    V.drawPoints([coord[0] for coord in MAP.stations], [coord[1] for coord in MAP.stations], 'stations', 'ro')

    # print("generating otoc...")
    # otoc = DG.generateOTOC()
    # print("generating cfss...")
    # cfss = DG.generateCFSS()
    # gr = DG.generateRAND()

    # print("\nOTOC Initial Result")
    # print(otoc)
    # print("OTOC Cost")
    # print(DG.getCost(otoc))
    # print(DG.chromoAble(otoc))

    # print(DG.mergeTrips([1,-1],[2,-2]))

    GAOP = GAOperator(DG, 'CFSS')

    V.drawPoints(range(len(GAOP.costs)), GAOP.costs, 'costs for each generation', 'r-')

    unavoid = 0

    for request in Reqs.requests:
        unavoid += MAP.dists[request[1]][request[3]]

    print("unavoid: {d}".format(d = unavoid))

    print("INIT: {c}".format(c = DG.getCost(GAOP.init) - unavoid))
    print("FINAL: {c}".format(c = DG.getCost(GAOP.genes[0]) - unavoid))

    print(GAOP.init);

    for (i, trip) in enumerate(GAOP.init.trips):
        points = []
        for request in trip:
            if request > 0:
                points.append(MAP.stations[Reqs.requests[request-1][1]][0:2])
            else:
                points.append(MAP.stations[Reqs.requests[-request-1][3]][0:2])
        V.drawPoints(list(map(lambda p: p[0], points)), list(map(lambda p: p[1], points)), 'routes/init/stations of shuttle {i}'.format(i = i), 'r-')

    print(GAOP.genes[0]);

    for (i, trip) in enumerate(GAOP.genes[0].trips):
        points = []
        for request in trip:
            if request > 0:
                points.append(MAP.stations[Reqs.requests[request-1][1]][0:2])
            else:
                points.append(MAP.stations[Reqs.requests[-request-1][3]][0:2])
        V.drawPoints(list(map(lambda p: p[0], points)), list(map(lambda p: p[1], points)), 'routes/final/stations of shuttle {i}'.format(i = i), 'r-')


    # print("\nCFSS Initial Result")
    # print(cfss)
    # print("CFSS Cost")
    # print(DG.getCost(cfss))
    # print(DG.chromoAble(cfss))

    # print("\nRAND Initial Result")
    # print(gr)
    # print("RAND Cost")
    # print(DG.getCost(gr))
    # print(DG.chromoAble(gr))

    # cr = otoc.crossover(gr)
    # print("\nOTOC + RAND")
    # print(cr)
    # print(DG.getCost(cr))
    # print(DG.chromoAble(cr))

    # print("\nmutation")
    # cr.mutation(1, 2)
    # print(cr)
    # print(DG.getCost(cr))
    # print(DG.chromoAble(cr))

    # crr = cfss.crossOver(otoc)
    # print("\nCFSS + OTOC")
    # print(crr)
    # print(DG.getCost(crr))
    # print(DG.chromoAble(crr))

    # print("\nmutation")
    # crr.mutation(1, 2)
    # print(crr)
    # print(DG.getCost(crr))
    # print(DG.chromoAble(crr))

    # cfsss = DG.generateCFSS()
    # crs = cfss.crossover(cfsss)
    # print("\nCFSS + CFSS")
    # print(crs)
    # print(DG.getCost(crs))
    # print(DG.chromoAble(crs))

    # print("\nmutation")
    # crs.mutation(1, 2)
    # print(crs)
    # print(DG.getCost(crs))
    # print(DG.chromoAble(crs))

    # print("\nCFSS/OTOC")
    # print(DG.getCost(cfss)/DG.getCost(otoc))
    pass


if __name__ == "__main__": # execute when python Simulator.py executed
    main()
    # print(Chromosome.generateRandomly(10,3))
