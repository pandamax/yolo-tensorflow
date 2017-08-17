import abc

class DatasetBase(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def annotationdictfor(self, imagefile):
        pass

    @abc.abstractmethod
    def numclasses(self):
        pass


