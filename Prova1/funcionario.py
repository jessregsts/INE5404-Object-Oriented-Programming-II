# notas
# essa é a classe funcionário. cada funcionário recebe uma matrícula ao ser contrato e utiliza seus dados pessoais cpf, nome e email (atributos) em seu cadastro de usuário

class funcionario():
   
    def __init__(self, matricula, cpf, nome, email, senha):
        self.matricula = matricula
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.senha = senha

    
    def get_matricula(self):
        return self.matricula
    
    def set_matricula(self, matricula):
        self.matricula = matricula
    
    
    def get_cpf(self):
        return self.cpf
    
    def set_cpf(self, cpf):
        self.cpf = cpf

    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email

    
    def get_senha(self):
        return self.senha
    
    def set_senha(self, senha):
        self.senha = senha


# notas
# essas são as classes admistrativo, vendas e manutençao
# essas três classes herdam atributos "principais" da classe funcionario

class administrativo(funcionario):

    def __init__(self, matricula, cpf, nome, email, senha):
        super().__init__(matricula, cpf, nome, email, senha)


class vendas(funcionario):

    def __init__(self, matricula, cpf, nome, email, senha):
        super().__init__(matricula, cpf, nome, email, senha)


class manutencao(funcionario):

    def __init__(self, matricula, cpf, nome, email, senha):
        super().__init__(matricula, cpf, nome, email, senha)

# breve lógica organizacional (⊃; símbolo matemático para contém):
#           funcionarios ⊃ funcionarios do administrativo ⊃ recepcionistas, gerente
#           funcionarios ⊃ funcionarios de vendas ⊃ vendedores
#           funcionarios ⊃ funcionarios de manutencoes ⊃ mecanicos, hegienizadores             
# logo, as classes recepcionista, gerente, vendedor, mecanico e higienizador também herdam atributos das suas respectivas classes "mães"
# optei por essa organização para haver uma organização simples mas lógica entre classes


# funcionários da parte administrativa da empresa
class recepcionista(administrativo):

    def __init__(self, matricula, cpf, nome, email, senha, cargo, salario):
        super().__init__(matricula, cpf, nome, email, senha)
        self. cargo = cargo
        self.salario = salario

    
    def get_cargo(self):
        return self.cargo
    
    def set_cargo(self, cargo):
        self.cargo = cargo
    
    
    def get_salario(self):
        return self.salario
    
    def set_salario(self, salario):
        self.salario = salario

class gerente(administrativo):

    def __init__(self, matricula, cpf, nome, email, senha, cargo, salario):
        super().__init__(matricula, cpf, nome, email, senha)
        self. cargo = cargo
        self.salario = salario

    
    def get_cargo(self):
        return self.cargo
    
    def set_cargo(self, cargo):
        self.cargo = cargo
    
    
    def get_salario(self):
        return self.salario
    
    def set_salario(self, salario):
        self.salario = salario


# funcionários da parte de aluguel veicular da empresa
class vendedor(vendas):

    def __init__(self, matricula, cpf, nome, email, senha, cargo, salario, comissao):
        super().__init__(matricula, cpf, nome, email, senha)
        self. cargo = cargo
        self.salario = salario
        self.comissao = comissao

    
    def get_cargo(self):
        return self.cargo
    
    def set_cargo(self, cargo):
        self.cargo = cargo
    
    
    def get_salario(self):
        return self.salario
    
    def set_salario(self, salario):
        self.salario = salario

    
    def get_comissao(self):
        return self.comissao
    
    def set_comissao(self, comissao):
        self.comissao = comissao


# funcionários da parte de manutenção veicular da empresa
class mecanico(manutencao):

    def __init__(self, matricula, cpf, nome, email, senha, cargo, salario, placa_veicular):
        super().__init__(matricula, cpf, nome, email, senha)
        self. cargo = cargo
        self.salario = salario
        self.placa_veicular = placa_veicular

    
    def get_cargo(self):
        return self.cargo
    
    def set_cargo(self, cargo):
        self.cargo = cargo
    
    
    def get_salario(self):
        return self.salario
    
    def set_salario(self, salario):
        self.salario = salario

    
    def get_placa_veicular(self):
        return self.placa_veicular
    
    def set_placa_veicular(self, placa_veicular):
        self.placa_veicular = placa_veicular

class higienizador(manutencao):

    def __init__(self, matricula, cpf, nome, email, senha, cargo, salario, placa_veicular):
        super().__init__(matricula, cpf, nome, email, senha)
        self. cargo = cargo
        self.salario = salario
        self.placa_veicular = placa_veicular

    
    def get_cargo(self):
        return self.cargo
    
    def set_cargo(self, cargo):
        self.cargo = cargo
    
    
    def get_salario(self):
        return self.salario
    
    def set_salario(self, salario):
        self.salario = salario

    
    def get_placa_veicular(self):
        return self.placa_veicular
    
    def set_placa_veicular(self, placa_veicular):
        self.placa_veicular = placa_veicular
