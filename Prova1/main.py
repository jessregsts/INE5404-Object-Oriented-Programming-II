# notas
# sisteminha locação de automóveis

# imports
import re
from cliente import cliente 
from automovel import automovel
from funcionario import higienizador
from funcionario import mecanico
from funcionario import vendedor
from funcionario import gerente
from funcionario import recepcionista

lista_veiculos = []
lista_clientes = []
lista_funcionarios = []


# menu principal
def agencia():
    
    print('//', 'locadorazinha', '//')
    print('/', "menu", '/')
    print("0 - sair")
    print("1 - login")
    print("2 - cadastrar cliente")
    print("3 - cadastrar veículo")
    print("4 - cadastrar funcionário")
    print("5 - listar cliente")
    print("6 - listar veículo")
    print("7 - listar funcionário")
    print("8 - alterar cadastro cliente")
    print("9 - alterar cadastro veículo")
    print("10 - alterar cadastro funcionário")
    print("11 - remover cadastro cliente") 
    print("12 - remover cadastro veículo")
    print("13 - remover cadastro funcionário")
    print('/', '/')

    acao = int(input("digite a ação desejada:"))
    return acao



# verifica se a senha é alfanumérica
def verifica_senha(str):
    if re.search('[a-zA-Z]', str) and re.search('[0-9]', str):
        return True
    else:
        return False
    


#def login():
    
#    email = input("digite email: ")
#    senha = input("digite senha: ")
    
#    for i in lista_clientes:
        
#        if email == i.get_email() and senha == i.getSenha():
            
#            while True:
#                print("bem vind@ ", i.get_nome(),"!")                
#                print("0 - sair")
#                print("1 - alugar")
#                print("2 - consultar aluguéis")
#                acao = int(input("digite a ação desejada:"))
#                
#                if opcao == 0:
#                    break
                
#                elif opcao == 1:
# downloading...



# função para cadastro de novo cliente
def cadastrar_cliente():

    print("/ cadastro cliente /")        

    nome = input("digite nome: ")
    cpf = int(input("digite cpf: "))
    passaporte = int(input("digite passaporte: "))
    idade = int(input("digite idade: "))
    cnh = int(input("digite cnh: "))
    pid = int(input("digite pid: "))
    email = input("digite email: ")
    telefone = int(input("digite telefone: "))
    endereco = input("digite endereco: ")
    senha = input("digite senha alfanumérica: ")
    while verifica_senha(senha) == False:
        print("inválido!")
        senha = input("digite senha alfanumérica: ")
    historico = []
    
    lista_clientes.append(cliente(nome, cpf, passaporte, idade, cnh, pid, email, telefone, endereco, senha, historico))



# função para cadastro de novo veículo
def cadastrar_veiculo():
    
    print("/ cadastro veicular /")
    
    unidades = int(input("digite a quantia: "))
    while unidades <= 0:
        print("quantia inválida! tente novamente.")
        unidades = int(input("digite a quantia: "))

    placa = input("digite a placa: ")
    for i in lista_veiculos:
        while i.get_placa() == placa:
            print("veículo já cadastrado! por favor, escolha outro.")
            placa = input("digite a placa: ")
    
    ano = input("digite o ano: ")
    while ano < 2018:
        print("inválido! carro fora de linha.")
        ano = input("digite o departamento: ")

    marca = input("digite a marca: ")
    
    diaria = float(input("digite valor diaria: "))
    while diaria <= 0:
        print("inválido! tente novamente.")
        diaria = float(input("digite valor diaria: "))
    
    extra = float(input("digite o extra: "))
    while extra < 0:
        print("inválido! tente novamente.")
        preco = float(input("digite valor diaria: "))

    lista_veiculos.append(automovel(unidades, placa, ano, marca, diaria, extra))
    print("veiculo cadastrado!")



# função para cadastro de novo funcionário
def cadastrar_funcionario():
    
    print('/ cargos /')
    print('1 - higienizador')
    print('2 - mecanico')
    print('3 - vendedor')
    print('4 - gerente')
    print('5 - recepcionista')
    
    cargo = int(input('digite o cargo: '))
    while cargo < 1 or cargo > 5:
        print('inválido!')
        cargo = int(input('digite o cargo: '))
    
    if cargo == 1:
        cargo = 'higienizador'
    elif cargo == 2:
        cargo = 'mecanico'
    elif cargo == 3:
        cargo = 'vendedor'
    elif cargo == 4:
        cargo = 'gerente'
    elif cargo == 5:
        cargo = 'recepcionista'

    matricula = int(input('digite matricula: '))
    cpf = int(input('digite cpf: '))
    nome = input('digite nome: ')
    email = input('digite email: ')
    senha = input('digite senha: ')
    salario = float(input('digite salario: '))
    
    if cargo == 'higienizador':
        placa_veicular = input('digite placa: ')
        higienizador = higienizador(matricula, cpf, nome, email, senha, cargo, salario, placa_veicular)
        lista_funcionarios.append(higienizador)
    
    elif cargo == 'mecanico':
        placa_veicular = input('digite placa: ')
        mecanico = mecanico(matricula, cpf, nome, email, senha, cargo, salario, placa_veicular)
        lista_funcionarios.append(mecanico)
    
    elif cargo == 'vendedor':
        comissao = float(input('comissão: '))
        vendedor = vendedor(matricula, cpf, nome, email, senha, cargo, salario, comissao)
        lista_funcionarios.append(vendedor)
    
    elif cargo == 'gerente':
        gerente = gerente(matricula, cpf, nome, email, senha, cargo, salario)
        lista_funcionarios.append(gerente)
    
    elif cargo == 'recepcionista':
        recepcionista = recepcionista(matricula, cpf, nome, email, senha, cargo, salario)
        lista_funcionarios.append(recepcionista)
    
    print('funcionario cadastrado!')



# função para listar cliente
def listar_cliente():
    
    for i in lista_clientes:
        print("/ dados cliente /")
        print("nome: ", i.get_nome())
        print("cpf: ", i.get_cpf())
        print("passaporte: ", i.get_passaporte())
        print("idade: ", i.get_idade())
        print("cnh: ", i.get_cnh())
        print("pid: ", i.get_pid()) 
        print("email: ", i.get_email())
        print("telefone: ", i.get_telefone())
        print("endereço: ", i.get_endereco())



# função para listar veiculo
def listar_veiculo():

    for w in lista_veiculos:
        print("/ dados veículo /")
        print("unidades: ", w.get_unidades())
        print("placa: ", w.get_placa())
        print("ano: ", w.get_ano())
        print("marca: ", w.get_marca())
        print("diaria: ", w.get_diaria())
        print("extra: ", w.get_extra())



# função para listar funcionário
def listar_funcionario():

    for i in lista_funcionarios:
        print('/ dados funcionário: /')
        print('matricula: ', i.get_matricula())
        print('cpf: ', i.get_cpf())
        print('nome: ', i.get_nome())
        print('email: ', i.get_email())
        print('salario: ', i.get_salario())
        print('cargo: ', i.get_cargo())
        
        if i.get_cargo() == 'vendedor':
            print('comissao: ', i.get_comissao())
        
        if i.get_cargo() == 'mecanico':
            print('placa: ', i.placa_veicular())
        
        if i.get_cargo() == 'higienizador':
            print('placa: ', i.placa_veicular())



# função para alterar cliente
def alterar_cliente():
    
    j = int(input("cpf do cliente: "))
    
    for i in lista_clientes:
        if i.get_cpf() == j:            
            print("0 - sair")
            print("1 - alterar nome")
            print("2 - alterar cpf")
            print("3 - alterar passaporte")
            print("4 - alterar idade")
            print("5 - alterar cnh")
            print("6 - alterar pid")            
            print("7 - alterar endereço")
            print("8 - alterar telefone")
            print("9 - alterar email")
            print("10 - alterar senha")


            acao = int(input("digite a ação desejada: "))
           
            while acao < 0 or acao > 10:
                    print("inválido")
                    acao = int(input("digite novamente: "))
            
            while acao != 0:
                if acao == 1:
                    novo_nome = input("novo nome: ")
                    i.set_nome(novo_nome)
                elif acao == 2:
                    novo_cpf = int(input("novo cpf: "))
                    i.set_cpf(novo_cpf)
                elif acao == 3:
                    novo_passaporte = int(input("novo passaporte: "))
                    i.set_passaporte(novo_passaporte)
                elif acao == 4:
                    nova_idade = int(input("nova idade: "))
                    i.set_idade(nova_idade)
                elif acao == 5:
                    nova_cnh = int(input("nova cnh: "))
                    i.set_cnh(nova_cnh)
                elif acao == 6:
                    novo_pid = int(input("novo pid: "))
                    i.set_pid(novo_pid)
                elif acao == 7:
                    novo_endereco = input("novo endereço: ")
                    i.set_endereco(novo_endereco)
                elif acao == 8:
                    novo_telefone = int(input("novo telefone: "))
                    i.set_telefone(novo_telefone)
                elif acao == 9:
                    novo_email = input("novo email: ")
                    i.set_email(novo_email)
                elif acao == 10:
                    nova_senha = input("nova senha: ")
                    i.set_senha(nova_senha)
            
            break
        
        else:
            print("cliente não listado!")



# função para alterar veículo
def alterar_veiculo():
    print("/ alterar veículo /")
    
    placa = input("digite a placa: ")
    
    for i in lista_clientes:
        
        if i.get_placa() == placa:
            
            while True:                
                print("0 - sair")
                print("1 - alterar unidades")
                print("2 - alterar placa")
                print("3 - alterar ano")
                print("4 - alterar marca")
                print("5 - alterar diaria")
                print("6 - alterar extra")

                acao = int(input("digite a ação desejada: "))
                
                if acao == 0:
                    break
                elif acao == 1:
                    nova_unidade = int(input("nova quantia: "))
                    i.set_unidades(nova_unidade)
                elif acao == 2:
                    nova_placa = input("nova placa: ")
                    i.set_placa(nova_placa)
                elif acao == 3:
                    novo_ano = int(input("novo ano: "))
                    while novo_ano < 2018:
                        print("ano inválido! tente novamente.")
                        novo_ano = int(input("novo ano: "))
                    i.set_ano(novo_ano)
                elif acao == 4:
                    nova_marca = input("nova marca: ")
                    i.set_marca(nova_marca)
                elif acao == 5:
                    nova_diaria = float(input("nova diaria: "))
                    i.set_diaria(nova_diaria)
                elif acao == 6:
                    novo_extra = float(input("novo extra: "))
                    i.set_extra(novo_extra)
                else:
                    print("inválido!")
                    continue
        else:
            print("veículo não listado!")



# função para alterar funcionário
def alterar_funcionario():
    
    print("/ alterar funcionário /")
    
    x = int(input("digite matrícula funcionário: "))
    
    for i in lista_funcionarios:
        if i.get_matricula() == x:
            print("0 - sair")
            print("1 - alterar matrícula")
            print("2 - alterar cpf")
            print("3 - alterar nome")
            print("4 - alterar email")
            print("5 - alterar senha")
            
            acao = int(input("digite a ação desejada: "))
            
            if acao == 0:
                break
            elif acao == 1:
                    nova_matricula = int(input("nova matrícula: "))
                    i.set_matricula(nova_matricula)
            elif acao == 2:
                    novo_cpf = int(input("novo cpf: "))
                    i.set_cpf(novo_cpf)
            elif acao == 3:
                    novo_nome = input("novo nome: ")
                    i.set_nome(novo_nome)
            elif acao == 4:
                    novo_email = input("novo email: ")
                    i.set_email(novo_email)
            elif acao == 5:
                    nova_senha = input("nova senha: ")
                    i.set_senha(nova_senha)
        else:
            print("funcionario não listado!")



# função para remover cliente
def remover_cliente():
    
    print("/ remover cliente /")
    
    cpf = int(input("cpf do cliente: "))
    for i in lista_clientes:
        if i.get_cpf() == cpf:
            lista_clientes.remove(i)
            print("cliente removido!")
        else:
            print("cliente não encontrado!")



# função para remover veículo
def remover_veiculo():
    
    print("/ remover produto /")
    
    placa = input("placa do veículo: ")
    for i in lista_veiculos:
        if i.get_placa() == placa:
            lista_veiculos.remove(i)
            print("veículo removido!")
        else:
            print("veículo não encontrado!")



# função para remover funcionário
def remover_funcionario():
    
    print("/ remover funcionário /")
    
    matricula = int(input("matrícula do funcionário: "))
    for i in lista_funcionarios:
        if i.get_matricula() == matricula:
            lista_funcionarios.remove(i)
            print("funcionário removido!")
        else:
            print("funcionário não encontrado!")



#ações
while True:
    
    acao = agencia()
    
    if acao == 0:
        break

    elif acao == 1:
        login()
    
    elif acao == 2:
        cadastrar_cliente()
    
    elif acao == 3:
        cadastrar_veiculo()
    
    elif acao == 4:
        cadastrar_funcionario()
    
    elif acao == 5:
        listar_cliente()
    
    elif acao == 6:
        listar_veiculo()
    
    elif acao == 7:
        listar_funcionario()
    
    elif acao == 8:
        alterar_cliente()
    
    elif acao == 9:
        alterar_veiculo()
    
    elif acao == 10:
        alterar_funcionario()
    
    elif acao == 11:
        remover_cliente()
    
    elif acao == 12:
        remover_veiculo()
    
    elif acao == 13:
        remover_funcionario()
    
    else: 
        print("ação inválida!")