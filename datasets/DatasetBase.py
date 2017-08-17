import abc

class DatasetBase(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def annotationdictfor(self, imagefile):
        pass

    @abc.abstractmethod
    def numcategories(self):
        pass

    @abc.abstractmethod
    def categorynames(self):
        pass


