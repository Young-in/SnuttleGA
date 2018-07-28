from Chromosome import Chromosome
from Pool import Pool
import random
import math

class DataGenerator:
    # n : the number of requests
    # requests : locations and time windows of requests [tuple of 4 positive integers(timeS, stationS, timeD, stationD)]
    # m : the number of stations
    # stations : locations of stations [tuple of 2 real numbers(x, y)] == map info
    # T : the maximum time of the simulation
    # dists : matrix which has the distance info
    def __init__(self, n = 1000, m = 20, T = 1440):
        self.m = m
        self.stations = []
        for j in range(self.m) :
            sta = (random.random()*100, random.random()*100)
            while sta in self.stations :
                sta = (random.random() * 100, random.random() * 100)
            self.stations.append(sta)
        # To ensure all stations are different
        self.dists = self.getDists()
        
        self.n = n
        self.requests = []
        for i in range(self.n) :
            # new version without using loop
            sta0 = random.randrange(m)
            sta1 = (sta0 + random.randrange(1, m)) % m
            # change index 1~m to 0~m-1 for easy access of dist[][]
            
            # t0 = random.randrange(T)
            # t1 = (t0 + random.randrange(T-1) + 1) % T
            # if t1 < t0 : t0, t1 = t1, t0

            d = self.dists[sta0][sta1] * (1 + random.random()) # make time interval random value between distance and 2*distance
            t0 = random.randrange(math.floor(T - d))
            t1 = t0 + d
            self.requests.append((t0, sta0, t1, sta1))
        # To ensure two stations, times are different

        self.T = T
        pass

    def __str__(self):
        ret = ""
        ret += "The number of requests : {n}\n".format(n = self.n)
        for request in self.requests: ret += "{r}\n".format(r = request)
        ret += "------------------------------------\n"
        ret += "The number of stations : {m}\n".format(m = self.m)
        for coord in self.stations: ret += "{c}\n".format(c = coord)
        ret += "------------------------------------\n"

        return ret

    def getDists(self):
        m = self.m # number of sta
        dists = [[None] * m for i in range(m)]
        for i in range(m) :
            for j in range(m) :
                d = self.getDistance(i, j)
                dists[i][j] = d
        # made code simpler
        return dists


    def getDistance(self, x, y): # get euclidean distance between station x and station y
        return math.sqrt((self.stations[x][0]-self.stations[y][0])**2
                         +(self.stations[x][1]-self.stations[y][1])**2)

    def getCost(self, chromo): # ## need to change this function: trip has a request number not a station number
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

    def generateOTOC(self):
        requests = list(enumerate(self.requests[:]))
        requests.sort(key = lambda request : request[1][2])

        trips = []
        lasttime = []

        for reqn, request in requests:
            v = -1
            t = self.T
            for i, time in enumerate(lasttime):
                dist = self.dists[request[1]][request[3]]
                if time + dist < request[0]:
                    if t > time:
                        v, t = i, time
                
            if v==-1:
                trips.append([(reqn+1), -(reqn+1)])
                lasttime.append(request[2])
            else:
                trips[v].extend([(reqn+1), -(reqn+1)])
                lasttime[v] = request[2]
        # print(lasttime)
        # print(trips)

        return Chromosome(trips)
    # get the chomosome's cost