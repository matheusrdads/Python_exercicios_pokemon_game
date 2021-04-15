import pickle               #transforma qualquer objeto em bytes
from pessoa import *


def escolher_pokemon_inicial(player):
    print('Olá {}, você poderá escolher agora o Pokemon que ira lhe acompanhar nessa jornada'.format(player))

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print('Você possui 3 escolhas')
    print('1 - ', pikachu)
    print('2 - ', charmander)
    print('3 - ', squirtle)

    while True:
        escolha = input('Escolha o seu Pokemon: ')

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break


def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)                        #salvando o objeto player como binario no arquivo database
            print('Jogo salvo com sucesso!')
    except Exception as error:
        print('Erro ao salvar o arquivo')
        print(error)


def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            print('Loading feito com sucesso - Treinador {}'.format(player))
            return player
    except Exception as error:
        print('Save não encontrado')


if __name__ == "__main__":
    print('-------------------------------------------')
    print('Bem-vindo ao game Pokemon RPG de terminal')
    print('-------------------------------------------')

    player = carregar_jogo()

    if not player:
        nome = input('Olá qual é o seu nome: ')
        player = Player(nome)
        print('Olá {}, esse é o mundo habitado por pokemons, a partir de agora sua missão será se tornar um mestre pokemon'.format(player))
        print('Capture o máximo de pokemons que conseguir e lute com seus inimigos')
        player.mostrar_dinheiro()

        if player.pokemons:
            print('Ja vi que você tem alguns pokemons')
        else:
            print('Você não possui nenhum pokemon, portanto precisa escolher um')
            escolher_pokemon_inicial(player)

        print('Pronto, agora que ja tem um pokemon enfrente seu inimigo desde o jardim de infância Gary')
        gary = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=34)])
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print('-------------------------------------------')
        print('O que deseja fazer?')
        print('1 - Explorar pelo mundão a fora?')
        print('2 - Lutar com um inimigo?')
        print('3 - Mostrar Pokeagenda')
        print('0 - Sair do jogo')
        escolha = input('Sua escolha: ')

        if escolha == '0':
            print('Fechando o jogo...')
            break
        if escolha == '1':
            player.explorar()
            salvar_jogo(player)
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == '3':
            player.mostrar_pokemons()
        else:
            print('Escolha inválida')
