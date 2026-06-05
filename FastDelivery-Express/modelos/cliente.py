from modelos.pessoa import Pessoa


class Cliente(Pessoa):
    """
    Classe responsável por representar um cliente.
    """

    def __init__(self, nome, cpf, telefone, endereco):
        super().__init__(nome)

        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    def __str__(self):
        return (
            f"Cliente: {self.nome}\n"
            f"CPF: {self.__cpf}\n"
            f"Telefone: {self.__telefone}\n"
            f"Endereço: {self.__endereco}"
        )
