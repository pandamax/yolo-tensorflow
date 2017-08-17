from datasets.DatasetBase import DatasetBase


class PascalVOC(DatasetBase):
    def __init__(self, name):
        DatasetBase.__init__(self, name)


    def numcategories(self):
        return 20

    def categorynames(self):
        categories = ["Aeroplane", "Bicycle", "Bird", "Boat", "Bus", "Car",
                      "Cat", "Chair", "Cow", "Dininttable", "Dog", "Horse",
                      "Motorbike", "Person", "Pottedplant", "Sheep", "Sofa",
                      "Train", "Tvmonitor"]
        return categories



