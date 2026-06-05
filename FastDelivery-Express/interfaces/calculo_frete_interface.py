from abc import ABC, abstractmethod


class CalculoFreteInterface(ABC):
    """
    Interface responsável pelo cálculo de frete.
    """

    @abstractmethod
    def calcular_frete(self):
        pass
