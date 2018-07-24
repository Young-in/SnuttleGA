import Chromosome
import Pool
import random

class DataGenerator:
    # n : the number of requests
    # requests : locations and time windows of requests [tuple of 4 positive integers(timeS, stationS, timeD, stationD)]
    # m : the number of stations
    # stations : locations of stations [tuple of 2 real numbers(x, y)]
    # T : the maximum time of the simulation
    def __init__(self, n = 1000, m = 20, T = 1440):
        self.n = n
        self.requests = []
        for i in range(self.n) :
            sta0 = sta1 = random.randrange(m)+1
            while sta0 == sta1 :
                sta1 = random.randrange(m)+1
            t0 = t1 = random.randrange(T)
            while t0 == t1 :
                t1 = random.randrange(T)
            if(t1 < t0) :
                temp = t0
                t0 = t1
                t1 = temp
            self.requests.append((t0, sta0, t1, sta1))
        # To ensure two stations, times are different

        self.m = m
        self.stations = []
        for j in range(self.m) :
            sta = (random.random()*100, random.random()*100)
            while sta in self.stations :
                sta = (random.random() * 100, random.random() * 100)
            self.stations.append(sta)
        # To ensure all stations are different
        pass

    def __str__(self):
        ret = ""
        ret += "The number of requests : "+str(self.n)+"\n"
        for request in self.requests: ret += str(request)+"\n"
        ret += "------------------------------------\n"
        ret += "The number of stations : "+str(self.m)+"\n"
        for coord in self.stations: ret += str(coord)+"\n"
        ret += "------------------------------------\n"

        return ret