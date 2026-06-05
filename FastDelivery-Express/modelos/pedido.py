class Pedido:
    """
    Classe responsável por representar um pedido.
    """

    STATUS_DISPONIVEIS = [
        "Em preparação",
        "Saiu para entrega",
        "Entregue",
        "Cancelado"
    ]

    def __init__(self, codigo, cliente, peso, distancia, tipo_entrega):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__peso = peso
        self.__distancia = distancia
        self.__tipo_entrega = tipo_entrega

        self.__status = "Em preparação"

    @property
    def codigo(self):
        return self.__codigo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def peso(self):
        return self.__peso

    @property
    def distancia(self):
        return self.__distancia

    @property
    def tipo_entrega(self):
        return self.__tipo_entrega

    @property
    def status(self):
        return self.__status

    def atualizar_status(self, novo_status):
        if novo_status in Pedido.STATUS_DISPONIVEIS:
            self.__status = novo_status
        else:
            raise ValueError("Status inválido.")

    def calcular_frete(self):
        return self.__tipo_entrega.calcular_frete()

    def __str__(self):
        return (
            f"\nCódigo: {self.__codigo}\n"
            f"Cliente: {self.__cliente.nome}\n"
            f"Peso: {self.__peso} kg\n"
            f"Distância: {self.__distancia} km\n"
            f"Frete: R$ {self.calcular_frete():.2f}\n"
            f"Status: {self.__status}"
        )
