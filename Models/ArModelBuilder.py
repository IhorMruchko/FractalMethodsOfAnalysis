from statsmodels.tsa.ar_model import AutoReg
from Models.ModelBuilder import ModelBuilder
from Models.ModelVisualizer import ModelVisualizer


class ARModelBuilder(ModelBuilder):
    def train(self) -> ModelVisualizer:
        self._model = AutoReg(self._training_data[self._target], 1)
        fit = self._model.fit()
        self._prediction = fit.predict(start=len(self._training_data),
                                       end=len(self._training_data) + len(self._testing_data) - 1,
                                       dynamic=False)
        return self
