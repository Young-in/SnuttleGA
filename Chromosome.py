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

    # trip : an array of an array of requests in order of visits (positive value: ride, negative value: drop off)
    # trips : [trip1, trip2, trip3, .. tripm]
    # 하나의 유전자가 여러대의 셔틀의 경로를 모두 나타내고 있어야 될거 같아서 trip 보단 trips로 이차원 배열을 가지고 있는게 맞는거 같다
    # 논문에 나와있는 remove one insert one 같은 변화들은 mutation으로 나타내는게 맞는거 같고,
    # crossover는 두 유전자에서 각 셔틀이 어느 유전자의 trip을 선택할지 확률적으로 결정하면 될거 같다(물론 requests가 겹치지 않도록 후처리도 해야되고)

    def __init__(self, trips):
        self.trips = trips

    def __str__(self):
        ret = ""
        for idx, trip in enumerate(self.trips):
            ret += "Shuttle {i}: {t}\n".format(i = idx, t = trip)
        return ret

    def otos(self, requests):
        # One Trip One Service
        trips = []
        return Chromosome(trips)

    def cfss(self, requests):
        # Cluster First Sweep Second
        trips = []
        return Chromosome(trips)

    def mutation(self):
        m = len(self.trips) # the number of shuttles

        while i in range(m) : # 반복 횟수는 추후에 수정
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