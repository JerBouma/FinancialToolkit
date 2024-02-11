"""Risk Controller Tests""" ""
import pandas as pd

from financetoolkit import Toolkit

historical = pd.read_pickle("tests/datasets/historical_dataset.pickle")

toolkit = Toolkit(
    tickers=["AAPL", "MSFT"], historical=historical, convert_currency=False
)

risk_module = toolkit.risk

# pylint: disable=missing-function-docstring


def test_get_value_at_risk(recorder):
    recorder.capture(risk_module.get_value_at_risk())
    recorder.capture(risk_module.get_value_at_risk(within_period=False))
    recorder.capture(risk_module.get_value_at_risk(period="monthly"))
    recorder.capture(risk_module.get_value_at_risk(growth=True))
    recorder.capture(risk_module.get_value_at_risk(growth=True, lag=[1, 2, 3]))


def test_get_conditional_value_at_risk(recorder):
    recorder.capture(risk_module.get_conditional_value_at_risk())
    recorder.capture(risk_module.get_conditional_value_at_risk(within_period=False))
    recorder.capture(risk_module.get_conditional_value_at_risk(period="monthly"))
    recorder.capture(risk_module.get_conditional_value_at_risk(growth=True))
    recorder.capture(
        risk_module.get_conditional_value_at_risk(growth=True, lag=[1, 2, 3])
    )


def test_get_entropic_value_at_risk(recorder):
    recorder.capture(risk_module.get_entropic_value_at_risk())
    recorder.capture(risk_module.get_entropic_value_at_risk(within_period=False))
    recorder.capture(risk_module.get_entropic_value_at_risk(period="monthly"))
    recorder.capture(risk_module.get_entropic_value_at_risk(growth=True))
    recorder.capture(risk_module.get_entropic_value_at_risk(growth=True, lag=[1, 2, 3]))


def test_get_garch(recorder):
    recorder.capture(risk_module.get_garch())
    recorder.capture(risk_module.get_garch(period="monthly"))
    recorder.capture(risk_module.get_garch(growth=True))
    recorder.capture(risk_module.get_garch(growth=True, lag=[1, 2, 3]))


def test_get_garch_forecast(recorder):
    recorder.capture(risk_module.get_garch_forecast())
    recorder.capture(risk_module.get_garch_forecast(period="monthly"))
    recorder.capture(risk_module.get_garch_forecast(growth=True))
    recorder.capture(risk_module.get_garch_forecast(growth=True, lag=[1, 2, 3]))


def test_get_maximum_drawdown(recorder):
    recorder.capture(risk_module.get_maximum_drawdown())
    recorder.capture(risk_module.get_maximum_drawdown(within_period=False))
    recorder.capture(risk_module.get_maximum_drawdown(period="monthly"))
    recorder.capture(risk_module.get_maximum_drawdown(growth=True))
    recorder.capture(risk_module.get_maximum_drawdown(growth=True, lag=[1, 2, 3]))


def test_get_ulcer_index(recorder):
    recorder.capture(risk_module.get_ulcer_index())
    recorder.capture(risk_module.get_ulcer_index(rolling=5))
    recorder.capture(risk_module.get_ulcer_index(period="monthly"))
    recorder.capture(risk_module.get_ulcer_index(growth=True))
    recorder.capture(risk_module.get_ulcer_index(growth=True, lag=[1, 2, 3]))


def test_get_skewness(recorder):
    recorder.capture(risk_module.get_skewness())
    recorder.capture(risk_module.get_skewness(within_period=False))
    recorder.capture(risk_module.get_skewness(period="monthly"))
    recorder.capture(risk_module.get_skewness(growth=True))
    recorder.capture(risk_module.get_skewness(growth=True, lag=[1, 2, 3]))


def test_get_kurtosis(recorder):
    recorder.capture(risk_module.get_kurtosis())
    recorder.capture(round(risk_module.get_kurtosis(within_period=False), 4))
    recorder.capture(risk_module.get_kurtosis(period="monthly"))
    recorder.capture(risk_module.get_kurtosis(growth=True))
    recorder.capture(risk_module.get_kurtosis(growth=True, lag=[1, 2, 3]))
