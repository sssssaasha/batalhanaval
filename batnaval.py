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
    if coordenadas[linha][coluna] == 'x':
        tabuleiro[linha][coluna] = 'x'
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
        print("".join(tabuleiroJogador[linha]))
    print(f'Jogadas restantes: {navegacoesJogador}')
    print(" ")
    print("Tabuleiro do Computador")
    for linha in range(5):
        print("".join(tabuleiroComputador[linha]))
    print(f'Jogadas restantes: {navegacoesComputador}')

while navegacoesComputador != 0 and navegacoesJogador != 0:
    mostrarTabuleiros()

