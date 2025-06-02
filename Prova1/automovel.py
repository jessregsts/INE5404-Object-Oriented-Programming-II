# notas
# essas são as classes automovel e aluguel. cada automovel tem respectivas unidades, placa própria, modelo e diaria
# um aluguel herda um automovel e, além disso, adiciona a forma de pagamento e o preço total

class automovel():
    
    def __init__(self, unidades, placa, ano, marca, diaria, extra):
        self.unidades = unidades
        self.placa = placa
        self.ano = ano
        self.marca = marca
        self.diaria = diaria
        self.extra = extra


    def get_unidades(self):
        return self.unidades
    
    def set_unidades(self, unidades):
        self.unidades = unidades
    
    
    def get_placa(self):
        return self.placa
    
    def set_placa(self, placa):
        self.placa = placa
    
    
    def get_ano(self):
        return self.ano
    
    def set_ano(self, ano):
        self.ano = ano

    
    def get_marca(self):
        return self.marca
    
    def set_marca(self, marca):
        self.marca = marca

    
    def get_diaria(self):
        return self.diaria
    
    def set_diaria(self, diaria):
        self.diaria = diaria

    
    def get_extra(self):
        return self.extra
    
    def set_extra(self, extra):
        self.extra = extra


    def get_listaAutomoveis(self):
        return self.listaAutomoveis
    
    def set_listaAutomoveis(self, listaAutomoveis):
        self.listaAutomoveis = listaAutomoveis


class aluguel(automovel):
    
    def __init__(self, unidades, placa, ano, marca, diaria, extra, forma_pagamento, desconto, taxa, total):
        super().__init__(unidades, placa, ano, marca, diaria, extra)
        self.forma_pagamento = forma_pagamento
        self.desconto = desconto
        self.taxa = taxa
        self.total = total


    
    def get_forma_pagamento(self):
        return self.forma_pagamento
    
    def set_forma_pagamento(self, forma_pagamento):
        self.forma_pagamento = forma_pagamento

    
    def get_desconto(self):
        return self.desconto
    
    def set_desconto(self, desconto):
        self.desconto = desconto

    
    def get_taxa(self):
        return self.taxa
    
    def set_taxa(self, taxa):
        self.taxa = taxa

    
    def get_total(self):
        return self.total
    
    def set_total(self, total):
        self.total = total


# notas
# a partir daqui, temos as classes dos tipos de carro
# basicamente, um automovel pode ser eletrico ou a combustao
# ao alugar um automovel eletrico, o cliente recebe um desconto; e, ao alugar um automovel a combustao, o cliente paga uma taxa
# os grupos de carros eletricos ou a combustao são: compactos, economicos, sedans, suvs, executivos, de luxo, minivans, pickups, furgoes, 4x4 e vans
# existem 4 tipos de serviços extras (taxado): ar condicionado, cambio automático, adaptado pessoa c/ deficiência, blindagem

class eletrico(automovel):

    def __init__(self, unidades, placa, ano, marca, diaria, extra, desconto):
        super().__init__(unidades, placa, ano, marca, diaria, extra)
        self.desconto = desconto

    def get_desconto(self):
        return self.desconto
    
    def set_desconto(self, desconto):
        self.desconto = desconto


class combustao(automovel):

    def __init__(self, unidades, placa, ano, marca, diaria, extra, taxa):
        super().__init__(unidades, placa, ano, marca, diaria, extra)
        self.taxa = taxa

    def get_taxa(self):
        return self.taxa
    
    def set_taxa(self, taxa):
        self.taxa = taxa


# -- grupos de carros disponíveis para alugel --
class compacto(eletrico):

    def __init__(self, unidades, placa, ano, marca, diaria, extra, desconto):
        super().__init__(unidades, placa, ano, marca, diaria, extra, desconto)

class economico(eletrico):

    def __init__(self, unidades, placa, ano, marca, diaria, extra, desconto):
        super().__init__(unidades, placa, ano, marca, diaria, extra, desconto)

class sedan(eletrico):

    def __init__(self, unidades, placa, ano, marca, diaria, extra, desconto):
        super().__init__(unidades, placa, ano, marca, diaria, extra, desconto)

class executivo(eletrico):

    def __init__(self, unidades, placa, ano, marca, diaria, extra, desconto):
        super().__init__(unidades, placa, ano, marca, diaria, extra, desconto)

class luxo(combustao):

    def __init__(self, unidades, placa, ano, marca, diaria, extra, taxa):
        super().__init__(unidades, placa, ano, marca, diaria, extra, taxa)

class minivan(combustao):

    def __init__(self, unidades, placa, ano, marca, diaria, extra, taxa):
        super().__init__(unidades, placa, ano, marca, diaria, extra, taxa)

class pickup(combustao):

    def __init__(self, unidades, placa, ano, marca, diaria, extra, taxa):
        super().__init__(unidades, placa, ano, marca, diaria, extra, taxa)

class furgao(eletrico):

    def __init__(self, unidades, placa, ano, marca, diaria, extra, desconto):
        super().__init__(unidades, placa, ano, marca, diaria, extra, desconto)

class quatro_x_quatro(combustao):

    def __init__(self, unidades, placa, ano, marca, diaria, extra, taxa):
        super().__init__(unidades, placa, ano, marca, diaria, extra, taxa)

class van(combustao):

    def __init__(self, unidades, placa, ano, marca, diaria, extra, taxa):
        super().__init__(unidades, placa, ano, marca, diaria, extra, taxa)
