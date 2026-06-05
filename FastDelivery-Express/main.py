from services.cliente_service import ClienteService
from services.entregador_service import EntregadorService
from services.pedido_service import PedidoService
from services.entrega_service import EntregaService

from util.menu import Menu


cliente_service = ClienteService()
entregador_service = EntregadorService()
pedido_service = PedidoService()


while True:

    opcao = Menu.menu_principal()

    if opcao == "1":

        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")

        cliente_service.cadastrar_cliente(
            nome,
            cpf,
            telefone,
            endereco
        )

        print("Cliente cadastrado!")

    elif opcao == "2":

        clientes = cliente_service.listar_clientes()

        for cliente in clientes:
            print()
            print(cliente)
    elif opcao == "3":

        cpf = input("Informe o CPF do cliente: ")

        cliente = cliente_service.buscar_cliente_por_cpf(cpf)

        if cliente:
            print("\nCliente encontrado:")
            print(cliente)
        else:
            print("Cliente não encontrado.")

    elif opcao == "4":

        nome = input("Nome: ")
        veiculo = input("Veículo: ")
        cnh = input("CNH: ")

        entregador_service.cadastrar_entregador(
            nome,
            veiculo,
            cnh
        )

        print("Entregador cadastrado!")

    elif opcao == "5":

        entregadores = (
            entregador_service.listar_entregadores()
        )

        for entregador in entregadores:
            print()
            print(entregador)

    elif opcao == "6":

        codigo = input("Código: ")
        cpf = input(
            "CPF do cliente: "
        )

        cliente = (
            cliente_service.buscar_cliente_por_cpf(
                cpf
            )
        )

        if not cliente:
            print("Cliente não encontrado.")
            continue

        peso = float(
            input("Peso (kg): ")
        )

        distancia = float(
            input("Distância (km): ")
        )

        tipo = input(
            "Tipo (comum/expressa/premium): "
        )

        entrega = (
            EntregaService.criar_entrega(
                tipo,
                distancia
            )
        )

        pedido_service.criar_pedido(
            codigo,
            cliente,
            peso,
            distancia,
            entrega
        )

        print("Pedido criado!")

    elif opcao == "7":

        pedidos = (
            pedido_service.listar_pedidos()
        )

        for pedido in pedidos:
            print(pedido)

    elif opcao == "8":

        codigo = input(
            "Código do pedido: "
        )

        print("\nStatus disponíveis:")
        print("Em preparação")
        print("Saiu para entrega")
        print("Entregue")
        print("Cancelado")

        status = input(
            "\nNovo status: "
        )

        if pedido_service.atualizar_status(
            codigo,
            status
        ):
            print("Status atualizado!")
        else:
            print("Pedido não encontrado.")

    elif opcao == "0":

        print("Encerrando sistema...")
        break

    else:

        print("Opção inválida.")
