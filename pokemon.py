class Pokemon:
    def __init__(self, tipo, especie, level=1, nome=None):                                                #construtor
        self.tipo = tipo
        self.especie = especie
        self.level = level

        if(nome):
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return "{}({})".format(self.nome, self.level)

    def atacar(self, pokemon):
        print('{} atacou {}!'.format(self, pokemon))                   #esse self esta pegando o retorno da função str

meu_pokemon = Pokemon('folha', 'bubasauro', level=24, nome='matheus')
pokemon_amigo = Pokemon('eletrico', 'pikachu')

print(meu_pokemon.nome, meu_pokemon.level)