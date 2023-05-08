from abc import ABC, abstractmethod

from Models.TestSizeSetter import TestSizeSetter


class TargetDataSetter(ABC):
    @abstractmethod
    def to_target(self, target: str) -> TestSizeSetter:
        pass
