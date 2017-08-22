import abc

class DatasetBase(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def annotationdictfor(self, imagefile):
        """Retrieve bounding box annotations for an imagefile.
           Return a dictionary with keys as category names and
           their annotations as the corresponding values.
        """
        pass

    @abc.abstractmethod
    def numcategories(self):
        """Return the number of categories in the dataset.
        """
        pass

    @abc.abstractproperty
    def categorynames(self):
        pass

    @abc.abstractmethod
    def imagesfromcategory(self, categoryname, **kwargs):
        pass



