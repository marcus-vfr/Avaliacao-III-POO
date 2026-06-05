from modelos.pessoa import Pessoa


class Entregador(Pessoa):
    """
    Classe responsável por representar um entregador.
    """

    def __init__(self, nome, veiculo, cnh):
        super().__init__(nome)

        self.__veiculo = veiculo
        self.__cnh = cnh

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, veiculo):
        self.__veiculo = veiculo

    @property
    def cnh(self):
        return self.__cnh

    @cnh.setter
    def cnh(self, cnh):
        self.__cnh = cnh

    def __str__(self):
        return (
            f"Entregador: {self.nome}\n"
            f"Veículo: {self.__veiculo}\n"
            f"CNH: {self.__cnh}"
        )
