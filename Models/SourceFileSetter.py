from abc import ABC, abstractmethod
from Models.TargetDataSetter import TargetDataSetter


class SourceFileSetter(ABC):
    @abstractmethod
    def set_source(self, source: str) -> TargetDataSetter:
        pass
