from util.formatador import Formatador


class Menu:

    @staticmethod
    def menu_principal():

        Formatador.titulo(
            "FastDelivery Express"
        )

        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Buscar cliente")

        print("4 - Cadastrar entregador")
        print("5 - Listar entregadores")

        print("6 - Criar pedido")
        print("7 - Listar pedidos")

        print("8 - Atualizar status")

        print("0 - Sair")

        return input(
            "\nEscolha uma opção: "
        )
