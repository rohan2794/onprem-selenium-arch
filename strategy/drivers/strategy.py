from __future__ import annotations
from abc import ABC, abstractmethod
from selenium import webdriver
import os


class WebDriverStrategy(ABC):
    @abstractmethod
    def _create_web_driver(self):
        pass

# <TBD>
# pass the webdriver name as param iP
class ConcreteStrategyChrome(WebDriverStrategy):
    def _create_web_driver(self):
        driver = webdriver.Chrome()
        return driver


class ConcreteStrategyFireFox(WebDriverStrategy):
    def _create_web_driver(self):
        driver = webdriver.Firefox()
        return driver


class WebContextClass:
    def __init__(self, web_driver_strategy: WebDriverStrategy) -> None:
        self._web_driver_strategy = web_driver_strategy

    @property
    def web_driver_strategy(self) -> None:
        return self._web_driver_strategy

    @web_driver_strategy.setter
    def web_driver_strategy(self, web_driver_strategy: WebDriverStrategy) -> None:
        self._web_driver_strategy = web_driver_strategy

    def execute_web_driver_strategy(self):
        driver = self._web_driver_strategy._create_web_driver()
        return driver
