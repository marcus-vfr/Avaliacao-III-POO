from modelos.entregador import Entregador


class EntregadorService:

    def __init__(self):
        self.__entregadores = []

    def cadastrar_entregador(self, nome, veiculo, cnh):

        entregador = Entregador(
            nome,
            veiculo,
            cnh
        )

        self.__entregadores.append(entregador)

        return entregador

    def listar_entregadores(self):
        return self.__entregadores

    def buscar_entregador_por_cnh(self, cnh):

        for entregador in self.__entregadores:
            if entregador.cnh == cnh:
                return entregador

        return None
