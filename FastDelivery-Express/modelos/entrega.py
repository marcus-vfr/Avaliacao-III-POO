from interfaces.calculo_frete_interface import CalculoFreteInterface


class EntregaComum(CalculoFreteInterface):
    """
    Representa uma entrega comum.
    """

    def __init__(self, distancia):
        self.__distancia = distancia

    @property
    def distancia(self):
        return self.__distancia

    @distancia.setter
    def distancia(self, distancia):
        self.__distancia = distancia

    def calcular_frete(self):
        return self.__distancia * 1.5


class EntregaExpressa(CalculoFreteInterface):
    """
    Representa uma entrega expressa.
    """

    def __init__(self, distancia):
        self.__distancia = distancia

    @property
    def distancia(self):
        return self.__distancia

    @distancia.setter
    def distancia(self, distancia):
        self.__distancia = distancia

    def calcular_frete(self):
        return self.__distancia * 3


class EntregaPremium(CalculoFreteInterface):
    """
    Representa uma entrega premium.
    """

    def __init__(self, distancia):
        self.__distancia = distancia

    @property
    def distancia(self):
        return self.__distancia

    @distancia.setter
    def distancia(self, distancia):
        self.__distancia = distancia

    def calcular_frete(self):
        return (self.__distancia * 5) + 20
