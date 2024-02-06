from abc import ABC
from abc import abstractclassmethod


class Step(ABC):
    def __init__(self):
        pass

    @abstractclassmethod
    def process(self, data, input, utils):
        pass


class StepException(Exception):
    pass