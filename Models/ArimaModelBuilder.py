from statsmodels.tsa.arima.model import ARIMA
from Models.ModelBuilder import ModelBuilder
from Models.ModelVisualizer import ModelVisualizer


class ArimaModelBuilder(ModelBuilder):
    def train(self) -> ModelVisualizer:
        self._model = ARIMA(self._training_data[self._target], order=(2, 1, 1))
        fit = self._model.fit()
        self._prediction = fit.forecast(len(self._testing_data))
        return self
