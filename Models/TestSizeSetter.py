from abc import ABC, abstractmethod
from Models import TrainModel


class TestSizeSetter(ABC):
    @abstractmethod
    def with_test_size(self, coefficient: float) -> TrainModel:
        pass
