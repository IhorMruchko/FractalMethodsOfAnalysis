from abc import ABC, abstractmethod
from Models.ModelVisualizer import ModelVisualizer


class TrainModel(ABC):
    @abstractmethod
    def train(self) -> ModelVisualizer:
        pass
