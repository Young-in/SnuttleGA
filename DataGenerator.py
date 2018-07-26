import Chromosome
import Pool
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
            sta0 = random.randrange(1, m+1)
            sta1 = (sta0 + random.randrange(1, m)) % m
            t0 = random.randrange(T)
            t1 = (t0 + random.randrange(T-1) + 1) % T
            if t1 < t0 : t0, t1 = t1, t0
            self.requests.append((t0, sta0, t1, sta1))
        # To ensure two stations, times are different
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
        dists = []
        n = len(self.stations) # number of sta
        for i in range(n) :
            for j in range(i, n) :
                d = self.getDistance(i, j)
                dists[i][j] = d
                dists[j][i] = d
        return dists


    def getDistance(self, x, y): # get euclidean distance between station x and station y
        return math.sqrt((self.stations[x][0]-self.stations[y][0])**2
                         +(self.stations[x][1]-self.stations[y][1])**2)

    def getCost(self, chromo):
        cost = 0
        for trip in chromo.trips :
            l = len(trip)
            for i in l-1 :
                cost += self.dists[trip[i]][trip[i+1]]
        return cost
    # get the chomosome's cost