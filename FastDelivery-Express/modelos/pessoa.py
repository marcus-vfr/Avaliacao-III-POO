class Pessoa:
    """
    Classe base para representar uma pessoa no sistema.
    """

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome.strip():
            raise ValueError("O nome não pode ser vazio.")

        self.__nome = novo_nome

    def __str__(self):
        return f"Nome: {self.__nome}"
