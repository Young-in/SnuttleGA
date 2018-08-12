import Chromosome
import Pool
import matplotlib
matplotlib.use('Agg') # because there is no display for this program
import matplotlib.pyplot as plt
import numpy as np

class Visualization:
    def __init__(self):
        pass
    
    def __str__(self):
        pass

    def drawPoints(self, xs, ys, filestr, opts):
        fig = plt.figure()
        plt.subplot(111)
        plt.plot(xs, ys, opts, label = 'coords of stations')
        plt.axis([0,100,0,100])
        plt.title('Stations')
        plt.legend()

        fig.savefig(filestr+'.png')

    def drawTrips(self, MAP, Reqs, chromo):
        V = Visualization()
        for (i, trip) in enumerate(chromo.trips):
            points = []
            for request in trip:
                if request > 0:
                    points.append(MAP.stations[Reqs.requests[request - 1][1]][0:2])
                else:
                    points.append(MAP.stations[Reqs.requests[-request - 1][3]][0:2])
            V.drawPoints([p[0] for p in points], [p[1] for p in points],
                         'routes/final/stations of shuttle {i}'.format(i=i), 'r-')
        pass