# Avaliacao-III-POO

# FastDelivery Express

## Descrição do Projeto

O FastDelivery Express é um sistema de gerenciamento de entregas urbanas desenvolvido utilizando Programação Orientada a Objetos (POO) com Python.

O sistema permite:

* Cadastro de clientes
* Cadastro de entregadores
* Criação de pedidos
* Cálculo de frete
* Controle de status dos pedidos
* Listagem e consulta de informações

O sistema é executado via terminal (console).

---

## Tecnologias Utilizadas

* Python 3
* Git
* GitHub

---

## Estrutura de Pastas

```text
fast_delivery/
│
├── main.py
│
├── modelos/
│   ├── __init__.py
│   ├── pessoa.py
│   ├── cliente.py
│   ├── entregador.py
│   ├── pedido.py
│   └── entrega.py
│
├── interfaces/
│   ├── __init__.py
│   └── calculo_frete_interface.py
│
├── services/
│   ├── __init__.py
│   ├── cliente_service.py
│   ├── entregador_service.py
│   ├── pedido_service.py
│   └── entrega_service.py
│
├── util/
│   ├── __init__.py
│   ├── validador.py
│   ├── formatador.py
│   └── menu.py
│
└── README.md
```

### Descrição das Pastas

#### modelos

Contém as entidades principais do sistema.

#### interfaces

Contém as interfaces e contratos utilizados pelas classes.

#### services

Contém as regras de negócio do sistema.

#### util

Contém funcionalidades auxiliares.

---

## Conceitos de POO Utilizados

### Herança

A classe Pessoa é a superclasse das classes Cliente e Entregador.

```text
Pessoa
├── Cliente
└── Entregador
```

---

### Encapsulamento

Os atributos das classes são privados utilizando:

```python
self.__atributo
```

O acesso é realizado através de propriedades (`@property`) e setters.

---

### Interface

Foi criada a interface:

```python
CalculoFreteInterface
```

Todas as classes de entrega implementam essa interface.

---

### Polimorfismo

O método:

```python
calcular_frete()
```

possui comportamentos diferentes para cada tipo de entrega.

Exemplos:

* Entrega Comum
* Entrega Expressa
* Entrega Premium

---

