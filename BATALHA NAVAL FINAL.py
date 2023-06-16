import random
import time

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
print ("Ganha quem afundar a frota inimiga primeiro")
print(" ")

time.sleep(1)
print(f"Comandante {jogador}, você tem 5 embarcações, escolha suas posições")

# Posições jogador humano
for navegacoes in range(navegacoesJogador):
    print(" ")
    jogadorLinha = int(input("Digite uma linha de 0 a 4: "))
    jogadorColuna = int(input("Digite uma coluna de 0 a 9: "))
    jogadorCoordenadas[jogadorLinha][jogadorColuna] = 'X'
    time.sleep(1)

# Posições computador
for navegacoes in range(navegacoesComputador):
    computadorLinha = random.randint(0, 4)
    computadorColuna = random.randint(0, 9)
    computadorCoordenadas[computadorLinha][computadorColuna] = 'X'


def erroOuAcerto(coordenadas, tabuleiro, linha, coluna):
    if coordenadas[linha][coluna] == 'X':
        tabuleiro[linha][coluna] = ' ✯ '
        print("Você acertou! :D")
        time.sleep(1)
        return 1
    else:
        tabuleiro[linha][coluna] = ' ● '
        print("Que pena, você errou... :c")
        time.sleep(1)
        return 0


def mostrarTabuleiros():
    # Exibir tabuleiro formatado
    print(" ")
    print("TABULEIROS:")
    print(" ")
    time.sleep(1)
    print(f"Tabuleiro de {jogador}")
    time.sleep(1)
    for linha in range(5):
        print("".join(tabuleiroJogador[linha]))
    print(f'Navegações restantes: {navegacoesJogador}')
    print(" ")
    time.sleep(1)
    print("Tabuleiro do Computador")
    time.sleep(1)
    for linha in range(5):
        print("".join(tabuleiroComputador[linha]))
    print(f'Navegações restantes: {navegacoesComputador}')
    time.sleep(1)


def jogadaJogador(navegacoesComputador):
    mostrarTabuleiros()
    if navegacoesComputador == 0:
        return 0

    jogadorAtaqueLinha = int(input("Digite a linha que deseja atacar: "))
    jogadorAtaqueColuna = int(input("Digite a coluna que deseja atacar: "))
    time.sleep(1)

    if erroOuAcerto(computadorCoordenadas, tabuleiroComputador, jogadorAtaqueLinha, jogadorAtaqueColuna) == 1:
        return 1
    else:
        return 2


def jogadaComputador(navegacoesJogador):
    mostrarTabuleiros()
    if navegacoesComputador == 0:
        return 0

    computadorAtaqueLinha = random.randint(0, 4)
    computadorAtaqueColuna = random.randint(0, 9)

    print(f'Computador escolheu a linha {computadorAtaqueLinha} e a coluna {computadorAtaqueColuna}')
    time.sleep(1)

    if erroOuAcerto(jogadorCoordenadas, tabuleiroJogador, computadorAtaqueLinha, computadorAtaqueColuna) == 1:
        return 1
    else:
        return 2


while navegacoesComputador != 0 and navegacoesJogador != 0:
    jogada = jogadaJogador(navegacoesComputador)
    if jogada == 0:
        break
    while jogada == 1:
        navegacoesComputador -= 1
        jogada = jogadaJogador(navegacoesComputador)
    if jogada == 0:
        break

    jogada = jogadaComputador(navegacoesJogador)
    if jogada == 0:
        break
    while jogada == 1:
        navegacoesJogador -= 1
        jogada = jogadaComputador(navegacoesJogador)
    if jogada == 0:
        break

if navegacoesComputador == 0:
    vencedor = jogador
if navegacoesJogador == 0:
    vencedor = "Computador"

print("----- 🛥️  FIM DO JOGO 🛥️ -----")
print(" ")
time.sleep(1)
print(f'O vencedor é ⋆.ೃ࿔*:･ {vencedor} ⋆.ೃ࿔*:･!!!!!')
print(" ")
time.sleep(1)
print("꘎♡━━━━━♡꘎ Obrigado por jogar!! ꘎♡━━━━━♡꘎")
print(" ")
time.sleep(1)
print(".⋅ ۵♡۵ ⋅. Desenvolvido por Alex, Mariana e Nicole .⋅ ۵♡۵ ⋅.")
print(" ")