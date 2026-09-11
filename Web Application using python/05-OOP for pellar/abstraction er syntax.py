from abc import ABC, abstractmethod

class ClassName(ABC):
    @abstractmethod
    def method_name(self):
        pass

#example
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass