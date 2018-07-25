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

    def drawPoints(self, xs, ys, filestr):
        fig = plt.figure()
        plt.subplot(111)
        plt.plot(xs, ys, 'ro', label = 'coords of stations')
        plt.title('Stations')
        plt.legend()

        fig.savefig(filestr+'.png')