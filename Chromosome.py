import random

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

    # trip : gean array of requests in order of visits (positive value: ride, negative value: drop off)
    # trips : [trip1, trip2, trip3, .. tripm]

    def __init__(self, trips):
        self.trips = trips

    def __str__(self):
        ret = ""
        for idx, trip in enumerate(self.trips):
            ret += "Shuttle {i}: {t}\n".format(i = idx, t = trip)
        return ret

    def mutation(self):
        m = len(self.trips) # the number of shuttles

        for i in range(m) : # 반복 횟수는 추후에 수정
            i = random.randrange(1, m+1)
            j = (i+random.randrange(1, m))%m

            tripi = self.trips[i]
            tripj = self.trips[j]

            inst1rem1(tripi, tripj)
            # 디른 mutation method 도 나중에 추가
        pass

    def crossover(self, chromo):
        trips1 = self.trips
        trips2 = chromo.trips

        # cross process

        # over process

        pass

def inst1rem1(trip1, trip2) :
    l1 = len(trip1)
    l2 = len(trip2)
    # insert 1 remove 1