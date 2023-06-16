import random

# Matrizes
jogadorCoordenadas = [
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "],
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "],
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "],
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "],
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "]
]

computadorCoordenadas = [
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "],
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "],
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "],
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "],
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "]
]

tabuleiroJogador = [
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "],
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "],
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "],
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "],
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "]
]

tabuleiroComputador = [
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "],
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "],
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "],
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "],
    [" ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ ", " ~ "]
]

# Configurações linhas e colunas
navegacoesJogador = 5
navegacoesComputador = 5

print("----- Batalha Naval 🛥️ -----")
jogador = input("Olá jogador, digite seu nome: ")
print (" ")
print ("Você tem 10 chances para afundar a frota inimiga")
print(" ")
print(f"Comandante {jogador}, você tem 5 embarcações, escolha suas posições")

# Posições jogador humano
for navegacoes in range(navegacoesJogador):
    print(" ")
    jogadorLinha = int(input("Digite uma linha de 0 a 4: "))
    jogadorColuna = int(input("Digite uma coluna de 0 a 9: "))
    jogadorCoordenadas[jogadorLinha][jogadorColuna] = 'X'

# Posições computador
for navegacoes in range(navegacoesComputador):
    computadorLinha = random.randint(0, 4)
    computadorColuna = random.randint(0, 9)
    computadorCoordenadas[computadorLinha][computadorColuna] = 'X'


def jogada(coordenadas, tabuleiro, linha, coluna):
    if coordenadas[linha][coluna] == 'X':
        tabuleiro[linha][coluna] = 'X'
        print("Você acertou! :D")
        return 1
    else:
        tabuleiro[linha][coluna] = 'o'
        print("Que pena, você errou... :c")
        return 0


def mostrarTabuleiros():
    # Exibir tabuleiro formatado
    print(" ")
    print("TABULEIROS:")
    print(" ")
    print(f"Tabuleiro de {jogador}")
    for linha in range(5):
        print("".join(jogadorCoordenadas[linha]))
    print(f'Suas Embarcações Restantes: {navegacoesJogador}')
    print(" ")
    print("Tabuleiro do Computador")
    for linha in range(5):
        print("".join(tabuleiroComputador[linha]))
    print(f'Embarcações Restantes: {navegacoesComputador}')

#rodadas
rodada = 1

while rodada <= 10 and navegacoesComputador != 0 and navegacoesJogador != 0:
    mostrarTabuleiros()

    print(f"Rodada {rodada}")

    linhaJogador = int(input("Digite a linha da jogada: "))
    colunaJogador = int(input("Digite a coluna da jogada: "))

    # Jogador
    if jogada(computadorCoordenadas, tabuleiroComputador, linhaJogador, colunaJogador):
        navegacoesComputador -= 1

    # Computador
    linhaComputador = random.randint(0, 4)
    colunaComputador = random.randint(0, 9)

    if jogada(jogadorCoordenadas, tabuleiroJogador, linhaComputador, colunaComputador):
        navegacoesJogador -= 1

    rodada += 1

# fim de jogo
mostrarTabuleiros()

if rodada > 10:
    print("Game Over! Acabaram as rodadas")
elif navegacoesComputador == 0:
    print(f"Parabéns Comandante {Jogador}! Você afundou a frota inimiga!")
elif navegacoesJogador == 0:
    print("Que pena {Jogador}. Todos seus barcos agora estão embaixo d´água. Você perdeu...")
