import random 

#parte de apresentação da tela do jogo
print("-----Batalha Naval🛥️-----")
jogador = input("Olá jogador, digite seu nome: ")

#matrizes 

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

#configurações linhas e colunas

jogadasRestantesJogador = 5
jogadasRestantesComputador = 5
ataques= 5

#posições jogador humano
for jogadas in range (jogadasRestantesJogador):
    jogadorLinha = int(input("Digite a linha que gostaria jogar: "))
    jogadorColuna = int(input("Digite a coluna que gostaria jogar: "))
    tabuleiroJogador[jogadorLinha][jogadorColuna] = 'X'
    #aqui nao sei como fazer o looping acabar 

#posições computador
for jogadas in range (jogadasRestantesComputador):
    computadorLinha = random.randint (0,5)
    computadorColuna = random.randint (0,9)
    tabuleiroComputador[computadorLinha][jogadorColuna] = 'X'




print(f'Tabuleiro de {jogador}')
print(tabuleiroJogador)
print(f'Jogadas restantes: {jogadasRestantesJogador}')
print('Tabuleiro do Computador')
print(tabuleiroComputador)
print(f'Jogadas restantes: {jogadasRestantesComputador}')


