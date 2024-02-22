from abc import ABC
from abc import abstractclassmethod


# Abstract Base Class
# This is a class that is meant to be inherited from, but not instantiated
# It is used to define a blueprint for other classes to follow
class Step(ABC):
    def __init__(self):
        pass

    # This is a method that is meant to be overridden by the child class
    # It is used to define the behavior of the child class
    @abstractclassmethod
    def process(self, data, input, utils):
        pass


class StepException(Exception):
    pass
