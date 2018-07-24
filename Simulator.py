from DataGenerator import DataGenerator
from Visualization import Visualization

def main():
    DG = DataGenerator(n = 50, m = 10)
    print(DG)
    V = Visualization()
    V.drawPoints([coord[0] for coord in DG.stations], [coord[1] for coord in DG.stations], 'stations')
    pass

if __name__ == "__main__": # execute when python Simulator.py executed
    main()