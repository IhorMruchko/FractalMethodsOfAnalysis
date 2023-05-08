from abc import ABC, abstractmethod


class ModelVisualizer(ABC):
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def save(self):
        pass
