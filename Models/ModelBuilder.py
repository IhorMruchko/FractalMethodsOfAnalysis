import os.path
from abc import ABC
import pandas as pd
from matplotlib import pyplot as plt
from pandas import DataFrame
from Models.ModelVisualizer import ModelVisualizer
from Models.SourceFileSetter import SourceFileSetter
from Models.TargetDataSetter import TargetDataSetter
from Models.TestSizeSetter import TestSizeSetter
from Models.TrainModel import TrainModel


class ModelBuilder(SourceFileSetter,
                   TargetDataSetter,
                   TestSizeSetter,
                   TrainModel,
                   ModelVisualizer,
                   ABC):
    __TRAINING_COEFFICIENT_MIN = 0
    __TRAINING_COEFFICIENT_MAX = 1

    def __init__(self):
        self._dataset: DataFrame = DataFrame()
        self._target = ""
        self._file_source = ""
        self._training_amount = 0
        self._coefficient = .0
        self._training_data = None
        self._testing_data = None
        self._prediction = None
        self._model = None

    def set_source(self, source: str) -> TargetDataSetter:
        if not source.endswith('.csv'):
            raise Exception("Invalid file format. Expected '.csv' files")
        if not os.path.exists(source):
            raise FileNotFoundError(f"Cannot find file with source specified: {source}.")
        self._file_source = source
        self._dataset = pd.read_csv(source, index_col='Date', parse_dates=True)
        return self

    def to_target(self, target: str) -> TestSizeSetter:
        if target not in self._dataset:
            raise Exception(f"Invalid target data source. {target}.")

        self._target = target
        return self

    def with_test_size(self, coefficient: float) -> TrainModel:
        if self.__TRAINING_COEFFICIENT_MAX < coefficient < self.__TRAINING_COEFFICIENT_MIN:
            raise Exception(f"Invalid training coefficient state value. "
                            f"{self.__TRAINING_COEFFICIENT_MAX} < {coefficient} < {self.__TRAINING_COEFFICIENT_MIN}")

        self._coefficient = coefficient
        self._training_amount = int(len(self._dataset) * coefficient)
        self.split_data()
        return self

    def show(self):
        self._prediction.plot(figsize=(10, 5))
        self._training_data.loc[:, self._target].plot(figsize=(10, 5))
        self._testing_data.loc[:, self._target].plot(figsize=(10, 5))
        plt.show()

    def save(self):
        self._prediction.plot(figsize=(10, 5))
        self._training_data.loc[:, self._target].plot(figsize=(10, 5))
        self._testing_data.loc[:, self._target].plot(figsize=(10, 5))
        file_name = self._file_source.split('\\')[-1]
        current_type = str(type(self)).split('.')[-1].removesuffix('ModelBuilder\'>')
        name = f"{current_type}-{file_name.removesuffix('.csv')}[{self._target}]{self._coefficient}.png"
        plt.savefig(os.path.join(r"Results", name))
        plt.clf()

    def split_data(self):
        self._training_data, self._testing_data = \
            self._dataset[:self._training_amount], self._dataset[self._training_amount:]
