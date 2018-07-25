import Chromosome
import Pool
import random
import math

class DataGenerator:
    # n : the number of requests
    # requests : locations and time windows of requests [tuple of 4 positive integers(timeS, stationS, timeD, stationD)]
    # m : the number of stations
    # stations : locations of stations [tuple of 2 real numbers(x, y)]
    # T : the maximum time of the simulation
    def __init__(self, n = 1000, m = 20, T = 1440):
        self.m = m
        self.stations = []
        for j in range(self.m) :
            sta = (random.random()*100, random.random()*100)
            while sta in self.stations :
                sta = (random.random() * 100, random.random() * 100)
            self.stations.append(sta)
        # To ensure all stations are different
        
        self.n = n
        self.requests = []
        for i in range(self.n) :
            # sta0 = sta1 = random.randrange(m)+1
            # while sta0 == sta1 :
            #     sta1 = random.randrange(m)+1
            # t0 = t1 = random.randrange(T)
            # while t0 == t1 :
            #     t1 = random.randrange(T)
            # if(t1 < t0) :
            #     temp = t0
            #     t0 = t1
            #     t1 = temp

            # new version without using loop
            sta0 = random.randrange(m)+1
            sta1 = (sta0 + random.randrange(m-1)) % m + 1
            t0 = random.randrange(T)
            t1 = (t0 + random.randrange(T-1) + 1) % T
            if t1 < t0: t0, t1 = t1, t0
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

    def getDistance(self, x, y): # get euclidean distance between station x and station y
        return math.sqrt((self.stations[x][0]-self.stations[y][0])**2+(self.stations[x][1]-self.stations[y][1])**2)