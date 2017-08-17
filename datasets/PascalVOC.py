from datasets.DatasetBase import DatasetBase
import pandas as pd
from bs4 import BeautifulSoup


class PascalVOC(DatasetBase):
    def __init__(self, name, basepath):
        DatasetBase.__init__(self, name)
        self.basepath = basepath


    def numcategories(self):
        return 20

    def categorynames(self):
        categories = ["Aeroplane", "Bicycle", "Bird", "Boat", "Bus", "Car",
                      "Cat", "Chair", "Cow", "Dininttable", "Dog", "Horse",
                      "Motorbike", "Person", "Pottedplant", "Sheep", "Sofa",
                      "Train", "Tvmonitor"]
        return categories

    






