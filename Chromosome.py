import random
import copy

class Chromosome:
    @staticmethod
    def generateRandomly(n, m): # n : the number of requests, m : the number of shuttles
        requests = list(range(1,n+1))
        random.shuffle(requests)
        divs = random.sample(range(1,n+1), m)
        divs.sort()

        trips = [requests[divs[-1]:]+requests[:divs[0]]]
        for i in range(1,m):
            trips.append(requests[divs[i-1]:divs[i]])
        # print(trips)

        for i in range(m):
            for j in range(len(trips[i]),0,-1):
                k = random.randrange(j,len(trips[i])+1)
                trips[i] = trips[i][:k] + [-trips[i][j-1]] + trips[i][k:]
        
        return Chromosome(trips)

    # trip : an array of requests in order of visits (positive value: ride, negative value: drop off)
    # trips : [trip1, trip2, trip3, .. tripm]

    def __init__(self, trips):
        self.trips = trips

    def __str__(self):
        ret = ""
        for idx, trip in enumerate(self.trips):
            ret += "Shuttle {i}: {t}\n".format(i = idx, t = trip)
        return ret

    def mutation(self, x, y): # exchange the position of x and y
        for trip in self.trips:
            for i in range(len(trip)):
                if trip[i] == x:
                    trip[i] = y
                elif trip[i] == -x:
                    trip[i] = -y
                elif trip[i] == y:
                    trip[i] = x
                elif trip[i] == -y:
                    trip[i] = -x
        pass

    def crossover(self, chromo): # remain half trips1, eleminate them from trips2 and merge two
        trips1 = copy.deepcopy(self.trips)
        trips2 = copy.deepcopy(chromo.trips)

        rettrips = copy.deepcopy(trips1[:int((len(trips1)+1)/2)])
        contained = set()
        
        for trip in rettrips:
            for r in trip:
                contained.add(r)

        for trip in trips2:
            tr = list(filter(lambda r: r not in contained, trip))
            if len(tr) > 0:
                rettrips.append(tr)
        
        return Chromosome(rettrips)

    def crossOver(self, chromo):
        trips = self.trips + chromo.trips
        ntrips = []
        rn = len(self.trips)/2 # number of requests
        markTable = set(range(1, rn+1))

        # search longest trip
        for i in range(rn) :
            i = i+1
            if i in markTable : # not in ntrips
                idx = searchLongest(i, trips)
                ntrips.append(trips[idx])
                markTable -= set(trips[idx])

        return Chromosome(ntrips)

def searchLongest(a, lsts) :
    M = -1
    i = 0
    while i < len(lsts) :
        if a in lsts[i] :
            if M < 0 : M = i
            elif len(lsts[i]) > len(lsts[M]) : M = i
        i += 1
    return M