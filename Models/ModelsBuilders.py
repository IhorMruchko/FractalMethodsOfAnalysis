from Models.ArModelBuilder import ARModelBuilder
from Models.SourceFileSetter import SourceFileSetter
from Models.ArimaModelBuilder import ArimaModelBuilder


class ModelsBuilders:
    @staticmethod
    def create_arima() -> SourceFileSetter:
        return ArimaModelBuilder()

    @staticmethod
    def create_ar() -> SourceFileSetter:
        return ARModelBuilder()
