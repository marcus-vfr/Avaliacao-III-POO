from modelos.cliente import Cliente


class ClienteService:
    """
    Responsável por gerenciar os clientes do sistema.
    """

    def __init__(self):
        self.__clientes = []

    def cadastrar_cliente(self, nome, cpf, telefone, endereco):
        """
        Cadastra um novo cliente.
        """

        cliente = Cliente(nome, cpf, telefone, endereco)
        self.__clientes.append(cliente)

        return cliente

    def listar_clientes(self):
        """
        Retorna todos os clientes cadastrados.
        """

        return self.__clientes

    def buscar_cliente_por_cpf(self, cpf):
        """
        Busca um cliente pelo CPF.
        """

        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente

        return None
