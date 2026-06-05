from modelos.pedido import Pedido


class PedidoService:
    """
    Responsável pelo gerenciamento dos pedidos.
    """

    def __init__(self):
        self.__pedidos = []

    def criar_pedido(
        self,
        codigo,
        cliente,
        peso,
        distancia,
        tipo_entrega
    ):
        pedido = Pedido(
            codigo,
            cliente,
            peso,
            distancia,
            tipo_entrega
        )

        self.__pedidos.append(pedido)

        return pedido

    def listar_pedidos(self):
        return self.__pedidos

    def buscar_pedido(self, codigo):

        for pedido in self.__pedidos:
            if pedido.codigo == codigo:
                return pedido

        return None

    def atualizar_status(self, codigo, novo_status):

        pedido = self.buscar_pedido(codigo)

        if pedido:
            pedido.atualizar_status(novo_status)
            return True

        return False
