import random
print("-----Batalha Naval-----")
jogador = input("Olá, jogador, digite seu nome: ")

tabuleiroJogador = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]

tabuleiroComputador = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]

navegacoesJogador = random.randint(tabuleiroJogador(0,9))
navegacoesComputador = random.randint(tabuleiroComputador(0,9))

jogadasRestantesJogador = 5
jogadasRestantesComputador = 5

jogadorLinha = int(input("Digite a linha que gostaria jogar: "))
jogadorColuna = int(input("Digite a coluna que gostaria jogar: "))
tabuleiroJogador[jogadorLinha][jogadorColuna] = 'X'

print(f'Tabuleiro de {jogador}')
print(tabuleiroJogador)
print(f'Jogadas restantes: {jogadasRestantesJogador}')
print('Tabuleiro do Computador')
print(tabuleiroComputador)
print(f'Jogadas restantes: {jogadasRestantesComputador}')

