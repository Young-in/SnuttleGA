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
        
        return trips



    # trips : an array of an array of requests in order of visits (positive value: ride, negative value: drop off)
    # 하나의 유전자가 여러대의 셔틀의 경로를 모두 나타내고 있어야 될거 같아서 trip 보단 trips로 이차원 배열을 가지고 있는게 맞는거 같다
    # 논문에 나와있는 remove one insert one 같은 변화들은 mutation으로 나타내는게 맞는거 같고,
    # crossover는 두 유전자에서 각 셔틀이 어느 유전자의 trip을 선택할지 확률적으로 결정하면 될거 같다(물론 requests가 겹치지 않도록 후처리도 해야되고)
    def __init__(self, trips):
        self.trips = trips
        pass

    def __str__(self):
        pass

    def mutation(self):
        pass

    def crossover(self, chromo):
        pass