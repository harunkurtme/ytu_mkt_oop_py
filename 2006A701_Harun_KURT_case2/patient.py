
from abc import abstractmethod,ABC
from typing import Dict, Generic, TypeVar

# T = TypeVar("T")
# class Patient(ABC,Generic[T]):
class Patient(ABC):
    def __init__(self, first_name, last_name, ssn):
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    
    @abstractmethod
    def calculate_cost(self):
        pass
    
    @property
    def ssn(self):
        return self._ssn
    
    def _repr_(self):
        return "{} {} {}".format(self.first_name,self.last_name,self.ssn)