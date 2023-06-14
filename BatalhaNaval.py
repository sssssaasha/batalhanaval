import random
from tabulate import tabulate

# Matrizes
jogadorCoordenadas = [
    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"]
]

computadorCoordenadas = [
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

# Configurações linhas e colunas
jogadasRestantesJogador = 5
jogadasRestantesComputador = 5

print("----- Batalha Naval 🛥️ -----")
jogador = input("Olá jogador, digite seu nome: ")

print(f"Comandante {jogador}, você tem 5 embarcações, escolha suas posições")

# Posições jogador humano
for jogadas in range(jogadasRestantesJogador):
    print(" ")
    jogadorLinha = int(input("Digite uma linha de 0 a 4: "))
    jogadorColuna = int(input("Digite uma coluna de 0 a 9: "))
    jogadorCoordenadas[jogadorLinha][jogadorColuna] = 'X'

# Posições computador
for jogadas in range(jogadasRestantesComputador):
    computadorLinha = random.randint(0, 4)
    computadorColuna = random.randint(0, 9)
    computadorCoordenadas[computadorLinha][computadorColuna] = 'X'

# Exibir tabuleiro formatado
print(" ")
print("TABULEIROS:")
print(" ")
print(f"Tabuleiro de {jogador}")
print(tabulate(jogadorCoordenadas, tablefmt="grid", showindex=True, headers=list(range(10)), stralign="center"))
print(" ")
print("Tabuleiro do Computador")
print(tabulate(computadorCoordenadas, tablefmt="grid", showindex=True, headers=list(range(10)), stralign="center"))
