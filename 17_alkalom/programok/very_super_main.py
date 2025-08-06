from classes.Ember import Ember as e
from dataprocess.NberDataProcess import NberDataProcess as ndp

if __name__ == "__main__":
    ember = e()
    print(ember)

    e.koszon()
    ndp.process_nber()