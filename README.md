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

#EXEMPLOS DE USO
<img width="455" height="325" alt="image" src="https://github.com/user-attachments/assets/7bbb5949-6e82-4113-98d5-534cb35427ee" />

<img width="424" height="130" alt="image" src="https://github.com/user-attachments/assets/a946aaa4-4398-4fb5-9a70-94568c9b4bca" />

<img width="374" height="147" alt="image" src="https://github.com/user-attachments/assets/3e97a7f1-1f5e-42a7-a884-15ef45a22ed5" />

<img width="333" height="107" alt="image" src="https://github.com/user-attachments/assets/3bcef876-5f67-4c42-b13a-149ff8312d02" />

<img width="333" height="107" alt="image" src="https://github.com/user-attachments/assets/26e3bf78-da23-4a52-81f1-6638a570a681" />

<img width="260" height="103" alt="image" src="https://github.com/user-attachments/assets/36a07244-e06a-4a83-8706-fba77b803aa5" />

<img width="347" height="136" alt="image" src="https://github.com/user-attachments/assets/10650300-54a0-4789-8ee9-4f0d2f68b407" />

<img width="275" height="152" alt="image" src="https://github.com/user-attachments/assets/8681b9ac-3eee-4fe5-ad2f-30b59d032206" />

<img width="257" height="201" alt="image" src="https://github.com/user-attachments/assets/92ffbe09-20ad-45ef-8b3a-181a4a3c2e07" />

<img width="202" height="41" alt="image" src="https://github.com/user-attachments/assets/7193e660-9181-4a30-a187-9a25da49f3ed" />



