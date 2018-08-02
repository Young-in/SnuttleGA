import random
import math

class RequestGenerator() :
    # requests : locations and time windows of requests [tuple of 4 positive integers(timeS, stationS, timeD, stationD)]
    # n : the number of requests
    # T : the maximum time of the simulation
    def __init__(self, Map, typ = 'AR', n = 1000, T = 1440):
        self.n = n
        self.T = T

        self.m = Map.m
        self.dists = Map.dists

        self.requests = []
        if(typ == 'AR') :
            self.requests = self.rand()
        elif(typ == 'CM') :
            self.request = self.camel()
        elif(typ == 'EX') :
            self.request = self.exp()
        elif(typ == 'UN') :
            self.requests = self.uni()
        else :
            print("ERROR : Requests Type Unavailable")
        pass

    def __str__(self):
        ret = ""
        ret += "The number of requests : {n}\n".format(n=self.n)
        for request in self.requests: ret += "{r}\n".format(r=request)
        ret += "------------------------------------\n"
        return ret

    def rand(self):
        lst = []
        for i in range(self.n):
            # new version without using loop
            sta0 = random.randrange(self.m)
            sta1 = (sta0 + random.randrange(1, self.m)) % self.m
            # change index 1~m to 0~m-1 for easy access of dist[][]

            d = self.dists[sta0][sta1] * (
                        1 + random.random())  # make time interval random value between distance and 2*distance
            t0 = random.randrange(math.floor(self.T - d))
            t1 = t0 + d
            lst.append((t0, sta0, t1, sta1))
            # To ensure two stations, times are different
        return lst

    def camel(self):
        t1, t2 = self.T/3, 2*self.T/3
        lst = []
        return lst

    def exp(self, t1):
        lst = []
        return lst

    def uni(self):
        lst = []
        return lst
