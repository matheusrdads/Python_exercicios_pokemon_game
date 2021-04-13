import random

class Pokemon:
    def __init__(self, especie, level=None, nome=None):  # construtor
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return "{}({})".format(self.nome, self.level)

    def atacar(self,
               pokemon):  # o parametro pokemon retorna nome e level, pois tambem é um objeto do tipo pokemon e sempre retorna o metodo __str__
        print('{} atacou {}!'.format(self, pokemon))  # esse self esta pegando o retorno da função str


class PokemonEletrico(Pokemon):
    tipo = 'eletrico'

    def atacar(self, pokemon):
        print('{} lancou um raio do trovão em {}'.format(self, pokemon))


class PokemonFogo(Pokemon):
    tipo = 'fogo'

    def atacar(self, pokemon):
        print('{} lancou uma bole de fogo na cabeça de {}'.format(self, pokemon))


class PokemonAgua(Pokemon):
    tipo = 'agua'

    def atacar(self, pokemon):
        print('{} lancou um jato d`água em {}'.format(self, pokemon))
