from abc import ABCMeta


class DatasetBase(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name