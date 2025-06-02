# notas
# essa é a classe cliente. cada cliente insere seus dados pessoais (atributos) e a empresa utiliza-os quando um novo alugel ocorre 

class cliente():
    
    def __init__(self, nome, cpf, passaporte, idade, cnh, pid, email, telefone, endereco, senha, historico):
        self.nome = nome
        self.cpf = cpf
        self.passaporte = passaporte
        self.idade = idade
        self.cnh = cnh
        self.pid = pid
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.senha = senha
        self.historico = historico
        
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    
    def get_cpf(self):
        return self.cpf
    
    def set_cpf(self, cpf):
        self.cpf = cpf


    def get_passaporte(self):
        return self.passaporte
    
    def set_passaporte(self, passaporte):
        self.passaporte = passaporte


    def get_idade(self):
        return self.idade
    
    def set_idade(self, idade):
        self.idade = idade

    
    def get_cnh(self):
        return self.cnh
    
    def set_cnh(self, cnh):
        self.cnh = cnh


    def get_pid(self):
        return self.pid
    
    def set_pid(self, pid):
        self.pid= pid
    

    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email


    def get_telefone(self):
        return self.telefone
    
    def set_telefone(self, telefone):
        self.telefone = telefone

    
    def get_endereco(self):
        return self.endereco
    
    def set_endereco(self, endereco):
        self.endereco = endereco

      
    def get_senha(self):
        return self.senha
    
    def set_senha(self, senha):
        self.senha = senha


    def get_historico(self):
        return self.historico

    def set_historico(self, historico):
        self.historico = historico
