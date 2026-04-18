#Conta Bancária

class Conta:
    def __init__(self,id,nome,cpf,endereco,saldo):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.saldo = saldo


'''def deposito_saldo (self, valor):
    valor = float(input ("Digite o valor do deposito: "))
    if valor > 0.00:
        self.saldo+=valor
        print (f" O valor de {self.valor} foi adicionado, agora você tem: {self.saldo}.")'''

'''def mostrar_saldo (self):
    print (f"Seu saldo atual é: {self.saldo}.")'''

'''def sacar_saldo (self, valor):
        valor = float(input("Digite o valor que deseja sacar: "))
        if valor > self.saldo:
            print(f"O valor do saque não pode ser superior ao do saldo.")
        elif valor <= 0.00:
            print(f"O valor de saque não pode ser zero ou inferior a zero.")
        else:
            print ("O valor do saque foi efetuado.")'''

    
contas ={  
    0: Conta (0,"Elliot","000.000.000-00","Avenida Brasil",200.00),
    1: Conta (1,"Shane","001.001.001-01","Rua dos Pericanos",50.00),
    2: Conta (2,"Viola","002.002.002-02","Rua Sem Nome",1000.00)
}
    
while (True):
    print("BEM-VINDO AO BANCO:")
    conta = int(input("Digite a conta de acesso: "))
    if conta in contas:
        print(f"Bem vindo {conta}\n Oque deseja fazer?")
        print("1 = depositar: \n2 = mostrar o saldo \n3 = sacar")
        
        escolha = int(input("digite o número: "))
        if escolha == 1:
            valor = float(input ("Digite o valor do deposito: "))
            if valor > 0.00:
                saldo+=valor
                print (f" O valor de {valor} foi adicionado, agora você tem: {conta.saldo}.")
            else:
                print("Valor inválido")

        elif escolha == 2:
            print (f"Seu saldo atual é: {conta.saldo}.")

        elif escolha == 3:
            valor = float(input("Digite o valor que deseja sacar: "))
            if valor > conta.saldo:
                print(f"O valor do saque não pode ser superior ao do saldo.")
            elif valor <= 0.00:
                print(f"O valor de saque não pode ser zero ou inferior a zero.")
            else:
                print ("O valor do saque foi efetuado.")
        else:
            print("\n\n\nOpção inválida\n\n\n")

    else:
        print("\n\n\nConta Invalida.\n\n\n")
        

