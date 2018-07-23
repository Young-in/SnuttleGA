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
        self.requests = [(random.randrange(T), random.randrange(m)+1, random.randrange(T), random.randrange(m)+1) for i in range(self.n)]
        self.m = m
        self.stations = [(random.random()*100, random.random()*100) for i in range(self.m)]
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