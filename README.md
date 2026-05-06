### Sistema Bancário em Python

Um sistema simples de conta bancária desenvolvido em Python, utilizando conceitos de **Programação Orientada a Objetos (POO)**.

O projeto simula operações básicas de um banco, permitindo ao usuário acessar uma conta e realizar ações como depósito, saque e consulta de saldo diretamente pelo terminal.

### Funcionalidades

* Acesso a contas pré-cadastradas
* Depósito de valores
* Saque com validação de saldo
* Consulta de saldo em tempo real
* Navegação contínua com menu interativo

### Conceitos aplicados

* Classes e objetos (`class Conta`)
* Métodos (`deposito_saldo`, `sacar_saldo`, `mostrar_saldo`)
* Estruturas condicionais (`if`, `elif`, `else`)
* Laços de repetição (`while`)
* Manipulação de dicionários

### Estrutura do sistema

Cada conta é representada por um objeto da classe `Conta`, contendo:

* ID
* Nome do usuário
* CPF
* Endereço
* Saldo

As contas são armazenadas em um dicionário:

```python
contas = {
    0: Conta(...),
    1: Conta(...),
    2: Conta(...)
}
```

### Como executar

1. Certifique-se de ter o Python instalado (3.x)
2. Baixe ou clone este repositório
3. Execute o arquivo:

```bash
python contabancaria.py
```

### Como usar

1. Digite o número da conta (ex: `0`, `1`, `2`)
2. Escolha uma opção do menu:

```
1 = Depositar
2 = Mostrar saldo
3 = Sacar
4 = Sair
```

### Validações implementadas

* Não permite depósito de valores negativos ou zero
* Impede saque maior que o saldo disponível
* Bloqueia valores inválidos no saque

### Possíveis melhorias futuras

* Sistema de login com CPF e senha
* Persistência de dados (arquivo ou banco de dados)
* Interface gráfica (Tkinter ou web)
* Histórico de transações
* Cadastro de novas contas

### Objetivo

Este projeto foi desenvolvido com fins educacionais, com o objetivo de praticar lógica de programação e conceitos fundamentais de POO em Python.

Desenvolvido por [Dênis Bruno]

