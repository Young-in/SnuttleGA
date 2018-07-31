import math
import random

class MapGenerator:
    # m : the number of stations
    # stations : locations of stations [tuple of 2 real numbers and name (x, y, name)] == map info
    # dists : matrix which has the distance info
    def __init__(self, m = 20):
        self.m = m
        self.stations = []
        for j in range(self.m) :
            sta = (random.random()*100, random.random()*100, j)
            while sta in self.stations :
                sta = (random.random() * 100, random.random() * 100, j)
            self.stations.append(sta)
        # To ensure all stations are different

        self.dists = self.getDists()
        pass

    def __str__(self):
        ret = ""
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
        return dists


    def getDistance(self, x, y): # get euclidean distance between station x and station y
        return math.sqrt((self.stations[x][0]-self.stations[y][0])**2
                         +(self.stations[x][1]-self.stations[y][1])**2)