import os
from datasets.DatasetBase import DatasetBase
import pandas as pd
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


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

    def imagesfromcategory(self, categoryname, subset="train"):
        categoryname = categoryname.lower()
        assert (categoryname in self.categorynames), "The given category was not found in the dataset {}".format(self.name)
        assert(subset is not None),"You must provide subset as train, val or trainval for Pascal VOC 2012"
        categoryfilename = categoryname + '_' + subset + '.txt'

        df = pd.read_csv(os.path.join(self.__infopath, categoryfilename), header=None, delimiter=r'\s+')
        df.drop(df.columns[1], axis=1, inplace=True)
        dataseries = df.iloc[:,0] # Converts from DataFrame to Series
        dataseries.apply(lambda x: x + '.jpg')
        return dataseries

    def annotationdictfor(self, imagefile):
        fullimagefile = os.path.join(self.__imgpath, imagefile)
        assert(os.path.exists(fullimagefile)),"The image {} was not found in {}".format(imagefile, self.__imgpath)
        annotationfile = os.path.splitext(imagefile)[0] + '.xml'
        annotationfile = os.path.join(self.__annotations, annotationfile)
        assert(os.path.exists(annotationfile)),"The file {} was not found in {}".format(os.path.basename(annotationfile), self.__annotations)
        return None

    def readvocxml(self,xmlfilename):
        annotations = {}
        soup = BeautifulSoup(contents, 'xml')
        objects = soup.find_all('object')
        name = soup.find_all('name')
        xmin = soup.find_all('xmin')
        xmax = soup.find_all('xmax')
        ymin = soup.find_all('ymin')
        ymax = soup.find_all('ymax')
        for i in range(len(objects)):
            bbox = [xmin[i].get_text(), ymin[i].get_text(), xmax.get_text(), ymax.get_text()]
            bbox = map(int(bbox))
            objname = name[i].get_text().strip()
            if objname not in annotations:
                annotations[objname] = []
            annotations[objname].append(append(bbox)

        return annotations
