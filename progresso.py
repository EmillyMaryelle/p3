progresso = []



inicio = int(input('Digite o número de partida: ')) #O usuário digita o número de partida da lista.

salto = int(input('Digite a razão: ')) #O valor que você quer pular na lista.

quantidade_num = int(input('Digite a quantidade de números da PA: ')) # a quantidade de números após o salto.

def progressaoAritmetica(a, r, n):
    condicao(a, r, n, progresso)
    return progresso


def condicao(a, r, n, progressao):
    if n == 0:
        return progressao
    cont = a
    progressao.append(cont)
    cont += r
    return condicao(cont, r, n-1, progressao)