import os
from datasets.DatasetBase import DatasetBase
import pandas as pd
from bs4 import BeautifulSoup


class PascalVOC(DatasetBase):
    def __init__(self, name, basepath):
        DatasetBase.__init__(self, name)
        self.basepath = basepath
        
    @property
    def basepath(self):
        return self.__basepath

    @basepath.setter
    def basepath(self, basepath):
        assert(os.path.exists(basepath)),"The path {} does not exist".format(basepath)
        self.__basepath = basepath

        assert(os.path.exists(os.path.join(self.__basepath, 'Annotations'))),"The annotations path was not found in {}".format(self.__basepath)
        
        self.__annotations = os.path.join(self.__basepath, 'Annotations')
        assert(os.path.exists(os.path.join(self.__basepath, 'JPEGImages'))),"The images path was not found in {}".format(self.__basepath)
        self.__imgpath = os.path.join(self.__basepath, 'JPEGImages')

        assert(os.path.exists(os.path.join(self.__basepath, 'ImageSets/Main'))),"The information path was not found in {}".format(self.__basepath)
        self.__infopath = os.path.join(self.__basepath, 'ImageSets','Main')


    def numcategories(self):
        return 20

    def categorynames(self):
        categories = ["Aeroplane", "Bicycle", "Bird", "Boat", "Bus", "Car",
                      "Cat", "Chair", "Cow", "Dininttable", "Dog", "Horse",
                      "Motorbike", "Person", "Pottedplant", "Sheep", "Sofa",
                      "Train", "Tvmonitor"]
        categories = list(map(lambda x: x.lower(), categories))
        return categories

    def imagesfromcategory(self, categoryname, **kwargs):
        assert (categoryname in self.categorynames), "The given category was not found in the dataset {}".format(self.name)
        
        
        








