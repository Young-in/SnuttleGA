from Chromosome import Chromosome
from Pool import Pool
import random

class DataGenerator:
    def __init__(self, dists, requests):
        self.dists = dists
        self.requests = requests
        self.m = len(dists) # number of stations
        self.n = len(requests) # number of requests

        self.L = self.makeL() # time ordered trip containing all requests
        self.CT = self.conflictTable() # == C , index = Rn -1 (start with 0)
        pass

    def __str__(self):
        ret = ""
        return ret

    def makeL(self):
        l = len(self.requests)
        L = list(range(1, l + 1)) + list(range(-l, 0))
        L.sort(key=lambda i: self.requests[abs(i) - 1][(abs(i) - i) // abs(i)])
        return L

    def subL(self, lst):
        trip = []
        for k in self.L:
            if abs(k) in lst: trip.append(k)
        return trip


    def conflictTable(self):
        l = len(self.requests)
        ct = [] # conflict table
        # -1 : conflict // 0 : i == j // 1 : available
        for i in range(l) :
            ct.append([])
            for j in range(l) :
                if i == j : ct[i].append(0)
                else :
                    trip = self.subL([i+1, j+1])
                    if self.available(trip) : ct[i].append(1)
                    else : ct[i].append(-1)
        return ct

    def chromoAble(self, chromo):
        trips = chromo.trips
        tripSet = []
        for trip in trips :
            if not self.available(trip) :
                print("unavailable trip")
                return False
            tripSet += trip
        for i in range(len(self.requests)) :
            i = i+1
            if i not in tripSet :
                print("there are no %d in trips" %i)
                return False
            if -i not in tripSet :
                print("there are no %d in trips" % -i)
                return False
            if tripSet.count(i) != 1 :
                print("there are more many %d in trips" % i)
                return False
            if tripSet.count(-i) != 1 :
                print("there are more many %d in trips" % -i)
                return False
        return True

    def available(self, trip):
        ts = []
        stas = []
        l = 0
        for i in trip :
            ia = abs(i)
            ts.append(self.requests[ia-1][(ia-i)//ia])
            stas.append(self.requests[ia-1][((ia-i)//ia)+1])
            l += 1

        ats = [ts[0]]  # arrival times
        i = 0
        while i < l-1 :
            d = self.dists[stas[i]][stas[i+1]]
            at = ats[i]+d # arrival time

            if trip[i+1] < 0 : # drop off
                if ts[i+1] < at : return False # arrival late
                else : ats.append(at)

            if trip[i+1] > 0 : # pick up
                if ts[i+1] > at : ats.append(ts[i+1]) # arrival earlier
                # can calculate slack time at here
                else : ats.append(at)
            i += 1

        return True

    def getCost(self, chromo):
        # need to change this function: trip has a request number not a station number
        COST_SHUTTLE = 1000
        cost = COST_SHUTTLE * len(chromo.trips)
        for trip in chromo.trips :
            l = len(trip)
            for i in range(l-1) :
                if trip[i]>0: staS = self.requests[trip[i]-1][1]
                else: staS = self.requests[-trip[i]-1][3]

                if trip[i+1]>0: staD = self.requests[trip[i+1]-1][1]
                else: staD = self.requests[-trip[i+1]-1][3]

                cost += self.dists[staS][staD]
        return cost

    def generateRAND(self):
        m, n = self.m, self.n
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


    def generateOTOC(self):
        requests = list(enumerate(self.requests[:]))
        requests.sort(key = lambda request : request[1][2])
        # sort by timeD

        trips = []
        lasttime = []

        for reqn, request in requests:
            v = -1
            t = 0
            for i, time in enumerate(lasttime):
                dist = time[1][request[1]]
                if time[0] + dist < request[0]:
                    if t < time[0]:
                        v, t = i, time[0]
                
            if v==-1:
                trips.append([(reqn+1), -(reqn+1)])
                lasttime.append((request[2], self.dists[request[3]]))
            else:
                trips[v].extend([(reqn+1), -(reqn+1)])
                lasttime[v] = (request[2], self.dists[request[3]])

        return Chromosome(trips)

    def generateCFSS(self):
        requests = list(enumerate(self.requests[:]))
        requests.sort(key=lambda request: request[1][2])
        trips = []

        # Cluster First
        routes = []

        for i in self.L :
            if i == self.L[0] : routes.append([i])
            elif i > 0 :
                random.shuffle(routes)
                l = len(routes); j =0
                while j < l :
                    route = routes[j]
                    mutab =True # Mutually available
                    for r in route :
                        if self.CT[i-1][r-1] < 0 : mutab = False
                    if mutab :
                        route.append(i)
                        break
                    else : j+= 1
                if j == l : routes.append([i])

        # Sweep Second
        for route in routes :
            rtrips = self.splitRoute(route)
            trips += rtrips

        return Chromosome(trips)

    def splitRoute(self, route):
        tripr = self.subL(route)
        if len(route) <= 2 : return [tripr]
        elif self.available(tripr) : return [tripr]
        else :
            routeO = route[::2]
            routeE = route[1::2]
            return self.splitRoute(routeO) + self.splitRoute(routeE)