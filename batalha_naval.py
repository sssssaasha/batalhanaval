import random
print("-----Batalha Naval-----")

jogador = input("Olá jogador, digite seu nome: ")

jogadorCoordenadas= [
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"]
]    

computadorCoordenadas= [
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                        ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"]
]   

tabuleiroJogador = [
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"]
                ]
                                      

tabuleiroComputador = [
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"]
                ]

navegacoesJogador = random.randint(tabuleiroJogador(0,9))
navegacoesComputador = random.randint(tabuleiroComputador(0,9))

jogadasRestantesJogador = 5
jogadasRestantesComputador = 5

for navio in range(navioHumano):
    jogadorLinha = int(input("Digite a linha que gostaria jogar: "))
    jogadorColuna = int(input("Digite a coluna que gostaria jogar: "))
    tabuleiroJogador[jogadorLinha][jogadorColuna] = 'X'


print(f'Tabuleiro de {jogador}')
print(tabuleiroJogador)
print(f'Jogadas restantes: {jogadasRestantesJogador}')
print('Tabuleiro do Computador')
print(tabuleiroComputador)
print(f'Jogadas restantes: {jogadasRestantesComputador}')


