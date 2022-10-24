def transpose(lista1, lista2):
    for lin in range(0, len(lista1[0])):
        lista2.append([])
        for col in range(0, len(lista1)):
            lista2[lin].append(lista1[col][lin])


def mean_flow_time_rules(pj):
    lista_fim = []
    mean_flow_time = 0
    for c in range(0, len(pj)):
        if c == 0:
            lista_fim.append(pj[c])
            mean_flow_time += lista_fim[c]
        else:
            lista_fim.append(pj[c] + lista_fim[c - 1])
            mean_flow_time += lista_fim[c]
    mean_flow_time = mean_flow_time / len(pj)
    return mean_flow_time


def mean_flow_time_methods(pj):
    lista_fim = []  # lista fim
    mean_flow_time = 0
    for lin in range(0, len(pj)):
        lista_fim.append([])
        for col in range(0, len(pj[0])):
            lista_fim[lin].append(0)
    for lin in range(0, len(pj)):
        for col in range(0, len(pj[0])):
            if lin == 0 and col == 0:
                lista_fim[lin][col] = pj[lin][col]
            elif lin == 0 and col > 0:
                lista_fim[0][col] = lista_fim[lin][col - 1] + pj[lin][col]
            elif col == 0:
                lista_fim[lin][col] = lista_fim[lin - 1][col] + pj[lin][col]
            else:
                if lista_fim[lin - 1][col] >= lista_fim[lin][col - 1]:
                    lista_fim[lin][col] = lista_fim[lin - 1][col] + pj[lin][col]
                else:
                    lista_fim[lin][col] = lista_fim[lin][col - 1] + pj[lin][col]
            mean_flow_time += lista_fim[lin][col]
    mean_flow_time = mean_flow_time / (len(pj) * len(pj[0]))
    return mean_flow_time


def makespan(pj):
    lista_fim = []  # lista fim
    for l in range(0, len(pj)):
        for c in range(0, len(pj[0])):
            if c == 0:
                lista_fim.append([])
            lista_fim[l].append(0)
    for l in range(0, len(pj)):
        for c in range(0, len(pj[0])):
            if l == 0 and c == 0:
                lista_fim[l][c] = pj[l][c]
            elif l == 0 and c > 0:
                lista_fim[0][c] = lista_fim[l][c - 1] + pj[l][c]
            elif c == 0:
                lista_fim[l][c] = lista_fim[l - 1][c] + pj[l][c]
            else:
                if lista_fim[l - 1][c] >= lista_fim[l][c - 1]:
                    lista_fim[l][c] = lista_fim[l - 1][c] + pj[l][c]
                else:
                    lista_fim[l][c] = lista_fim[l][c - 1] + pj[l][c]

    makespan1 = lista_fim[len(lista_fim) - 1][len(pj[0]) - 1]
    return makespan1


def max_lateness(pj, dj):
    lmax = 0
    final_pj = []
    for c in range(0, len(pj)):
        if c == 0:
            final_pj.append(pj[c])
            lmax = final_pj[c] - dj[c]
        else:
            final_pj.append(pj[c] + final_pj[c - 1])
            if lmax < final_pj[c] - dj[c]:
                lmax = final_pj[c] - dj[c]
    if lmax < 0:
        lmax = 0
    return lmax


def average_lateness(pj, dj):
    final_pj = []
    lateness = []
    average_lateness1 = 0
    for c in range(0, len(pj)):
        if c == 0:
            final_pj.append(pj[c])
            lateness.append(final_pj[c] - dj[c])
            average_lateness1 += lateness[c]
        else:
            final_pj.append(pj[c] + final_pj[c - 1])
            lateness.append(final_pj[c] - dj[c])
            average_lateness1 += lateness[c]
    average_lateness1 = average_lateness1 / len(pj)
    return average_lateness1


def average_tardiness(pj, dj):
    final_pj = []
    lateness = []
    average_tardiness1 = 0
    for c in range(0, len(pj)):
        if c == 0:
            final_pj.append(pj[c])
            lateness.append(final_pj[c] - dj[c])
            if lateness[c] > 0:
                average_tardiness1 += lateness[c]
        else:
            final_pj.append(pj[c] + final_pj[c - 1])
            lateness.append(final_pj[c] - dj[c])
            if lateness[c] > 0:
                average_tardiness1 += lateness[c]
    average_tardiness1 = average_tardiness1 / len(pj)
    return average_tardiness1


def average_earliness(pj, dj):
    final_pj = []
    earliness = []
    average_earliness1 = 0
    for c in range(0, len(pj)):
        if c == 0:
            final_pj.append(pj[c])
            earliness.append(final_pj[c] - dj[c])
            if earliness[c] < 0:
                average_earliness1 += earliness[c]
        else:
            final_pj.append(pj[c] + final_pj[c - 1])
            earliness.append(final_pj[c] - dj[c])
            if earliness[c] < 0:
                average_earliness1 += earliness[c]
    average_earliness1 = average_earliness1 / len(pj)
    return average_earliness1


def number_tardy_jobs(pj, dj):
    final_pj = []
    lateness = []
    number_tardy_jobs1 = 0
    for c in range(0, len(pj)):
        if c == 0:
            final_pj.append(pj[c])
            lateness.append(final_pj[c] - dj[c])
            if lateness[c] > 0:
                number_tardy_jobs1 += 1
        else:
            final_pj.append(pj[c] + final_pj[c - 1])
            lateness.append(final_pj[c] - dj[c])
            if lateness[c] > 0:
                number_tardy_jobs1 += 1
    return number_tardy_jobs1


# Regras e Métodos
def fifo(pj, dj):
    n = len(pj)  # Tamanho da sequência
    seq = []
    for c in range(0, n):
        seq.append('J' + str(c + 1))
    return seq, pj, dj


def spt(pj, dj):  # pj = Tempo de processamento, dj = data de entrega, wj = importância do serviço
    n = len(pj)  # Tamanho da sequência
    seq = []
    for c in range(0, n):
        seq.append('J' + str(c + 1))
    for c in range(0, n - 1):  # Bubblesort de pj
        for i in range(0, n - 1):
            if pj[i] > pj[i + 1]:
                pj[i], pj[i + 1] = pj[i + 1], pj[i]
                dj[i], dj[i + 1] = dj[i + 1], dj[i]
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
    return seq, pj, dj


def edd(pj, dj):
    n = len(pj)  # Tamanho da sequência
    seq = []
    for c in range(0, n):
        seq.append('J' + str(c + 1))
    for c in range(0, n - 1):  # Bubblesort de dj
        for i in range(0, n - 1):
            if dj[i] > dj[i + 1]:
                dj[i], dj[i + 1] = dj[i + 1], dj[i]
                pj[i], pj[i + 1] = pj[i + 1], pj[i]
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
    return seq, pj, dj


def str1(pj, dj):
    n = len(pj)  # Tamanho da sequência
    strs = []  # Lista strs
    seq = []
    for c in range(0, n):  # Para todos os itens da sequência
        strs.append(dj[c] - pj[c])  # Lista str adiciona o valor de data de entrega dj - tempo de processamento pj
        seq.append('J' + str(c + 1))
    for c in range(0, n - 1):  # Bubblesort dj - pj = strs
        for i in range(0, n - 1):
            if strs[i] > strs[i + 1]:
                strs[i], strs[i + 1] = strs[i + 1], strs[i]
                pj[i], pj[i + 1] = pj[i + 1], pj[i]
                dj[i], dj[i + 1] = dj[i + 1], dj[i]
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
    return seq, pj, dj


def crr(pj, dj):
    n = len(pj)  # Tamanho da sequência
    crr = []  # Lista crr
    seq = []
    for c in range(0, n):  # Para todos os itens da sequência
        crr.append(dj[c] / pj[c])  # Lista ccr adiciona menor tempo de entrega dj / menor tempo de processamento pj
        seq.append('J' + str(c + 1))
    for c in range(0, n - 1):
        for i in range(0, n - 1):  # Bubblesort dj - pj = ccr
            if crr[i] > crr[i + 1]:
                crr[i], crr[i + 1] = crr[i + 1], crr[i]
                pj[i], pj[i + 1] = pj[i + 1], pj[i]
                dj[i], dj[i + 1] = dj[i + 1], dj[i]
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
    return seq, pj, dj


def neh(pj):
    new_pj = []
    transpose(pj, new_pj)
    pj = new_pj[:]
    seq = []
    for c in range(0, len(pj)):
        seq.append("J" + str(c + 1))
    x = 2
    lista_rep = [0]
    for c in range(0, 100):  # Lista rep adiciona 2, 5, 9, 14... // 2 + 3 = 5; 5 + 4 = 9; 9 + 5 = 14 e etc.
        lista_rep.append(x + lista_rep[c])
        x += 1
    qt = lista_rep[len(pj) - 1]
    maior_lista = []
    pj_aux = pj[:]
    total = 0
    sim_pj = []
    sim_pj_db = []

    for lin in range(0, len(pj)):
        for col in range(0, len(pj[0])):
            total += pj[lin][col]
        maior_lista.append(total)
        total = 0
    for c in range(0, len(pj) - 1):  # Bubblesort de pj
        for i in range(0, len(pj) - 1):
            if pj_aux[i] < pj_aux[i + 1]:
                pj_aux[i], pj_aux[i + 1] = pj_aux[i + 1], pj_aux[i]
                maior_lista[i], maior_lista[i + 1] = maior_lista[i + 1], maior_lista[i]

    makespan = []
    pos_pj_aux = 2
    sim_pj.append(pj_aux[0])
    sim_pj.append(pj_aux[1])

    for cont in range(0, qt):
        if cont in lista_rep and cont > 0:
            sim_pj_db.clear()
            makespan.clear()
            sim_pj.append(pj_aux[pos_pj_aux])
            pos_pj_aux += 1
        lista_fim = []  # lista fim
        for l in range(0, len(sim_pj)):
            for c in range(0, len(sim_pj[0])):
                if c == 0:
                    lista_fim.append([])
                lista_fim[l].append(0)
        for l in range(0, len(sim_pj)):
            for c in range(0, len(sim_pj[0])):
                if l == 0 and c == 0:
                    lista_fim[l][c] = sim_pj[l][c]
                elif l == 0 and c > 0:
                    lista_fim[0][c] = lista_fim[l][c - 1] + sim_pj[l][c]
                elif c == 0:
                    lista_fim[l][c] = lista_fim[l - 1][c] + sim_pj[l][c]
                else:
                    if lista_fim[l - 1][c] >= lista_fim[l][c - 1]:
                        lista_fim[l][c] = lista_fim[l - 1][c] + sim_pj[l][c]
                    else:
                        lista_fim[l][c] = lista_fim[l][c - 1] + sim_pj[l][c]

        makespan.append(lista_fim[len(lista_fim) - 1][len(pj[0]) - 1])
        sim_pj_db_1 = sim_pj[:]  # bug
        sim_pj_db.append(sim_pj_db_1)

        n = len(sim_pj) - 1
        if cont in lista_rep:
            aux_sim_pj = sim_pj[n]
            sim_pj.pop(len(sim_pj) - 1)
            sim_pj.insert(0, aux_sim_pj)
        elif cont > 1:
            for c in range(0, len(sim_pj)):
                sim_pj[c - 1], sim_pj[c] = sim_pj[c], sim_pj[c - 1]
        menor = 0
        for c in range(0, len(makespan)):
            if c == 0:
                menor = makespan[0]
            elif menor > makespan[c]:
                menor = makespan[c]

        if (cont + 1) in lista_rep and cont > 0:

            for c in range(0, len(makespan) - 1):  # Bubblesort de pj
                for i in range(0, len(makespan) - 1):
                    if makespan[i] > makespan[i + 1]:
                        makespan[i], makespan[i + 1] = makespan[i + 1], makespan[i]
                        sim_pj_db[i], sim_pj_db[i + 1] = sim_pj_db[i + 1], sim_pj_db[i]
            sim_pj.clear()
            for c in range(0, len(makespan)):
                sim_pj.append(sim_pj_db[0][c])
                pass

    pj_aux = sim_pj[:]

    for c in range(0, len(pj) - 1):
        for x in range(0, len(pj)):
            if pj[c] == pj_aux[x]:
                seq[c], seq[x] = seq[x], seq[c]
    pj.clear()
    transpose(pj_aux, pj)


    return seq, pj


def johnson(pj):

    pij1 = pj[0].copy()
    pij2 = pj[1].copy()

    f_pij1 = []  # Lista final dos resultados para máquina 1
    f_pij2 = []  # Lista final dos resultados para máquina 2
    qt = len(pij1)
    seq = []
    for c in range(0, qt):  # Atribuição do valor 0 às listas finais
        f_pij1.append(0)
        f_pij2.append(0)
        seq.append(0)
    
    pos_pij1 = 0  # Posição na lista pij1
    pos_pij2 = 0  # Posição na lista pij2
    menor1 = int(0)  # Menor valor para comparação (lista pij1)
    menor2 = int(0)  # Menor valor para comparação (lista pij2)
    pos_f_pij1 = 0  # Varíavel contadora para saber a posição a atribuir os valores na lista f_pij1
    pos_f_pij2 = len(pij1) - 1  # Varíavel contadora para saber a posição a atribuir os valores na lista f_pij2
    for cont in range(0, qt):  # Quantidade de vezes que o código roda
        if cont == 0:
            pass
        for c in range(0, len(pij1)):  # Pij1
            if c == 0:  # Caso c = 0
                if pij1[c] != 0:
                    menor1 = pij1[c]  # Variável menor1 recebe o primeiro valor da lista pij1
                    pos_pij1 = c  # Variável pos_pij1 recebe a posição na qual o menor1 se encontra na lista pij1
                else:
                    x = 0
                    while x <= len(pij1):
                        menor1 = pij1[x]
                        pos_pij1 = x  # Variável pos_pij2 recebe a posição na qual o menor2 se encontra na lista pij2
                        x += 1
                        if menor1 != 0:
                            break
            elif pij1[c] < menor1 and pij1[c] != 0:  # Demais casos
                menor1 = pij1[c]  # Variável menor1 recebe o c valor da lista pij1
                pos_pij1 = c  # Variável pos_pij1 recebe a posição na qual o menor1 se encontra na lista pij1
        for c in range(0, len(pij2)):  # Pij2
            if c == 0:  # Caso c = 0
                if pij2[c] != 0:
                    menor2 = pij2[c]  # Variável menor2 recebe o primeiro valor da lista pij2
                    pos_pij2 = c  # Variável pos_pij2 recebe a posição na qual o menor2 se encontra na lista pij2
                else:
                    x = 0
                    while x <= len(pij2):
                        menor2 = pij2[x]
                        pos_pij2 = x  # Variável pos_pij2 recebe a posição na qual o menor2 se encontra na lista pij2
                        x += 1
                        if menor2 != 0:
                            break
            elif pij2[c] < menor2 and pij2[c] != 0:  # Demais casos
                menor2 = pij2[c]  # Variável menor2 recebe o c valor da lista pij2
                pos_pij2 = c  # Variável pos_pij2 recebe a posição na qual o menor2 se encontra na lista pij2
        if menor1 <= menor2:  # Condição menor valor entre as duas listas
            seq[pos_f_pij1] = 'J' + str(pos_pij1 + 1)
            f_pij1[pos_f_pij1] = pij1[pos_pij1]  # f_pij1 adiciona o valor na posição pos_f_pij1 que está na lista pij1 posição pos_pij1
            f_pij2[pos_f_pij1] = pij2[pos_pij1]  # f_pij2 adiciona o valor na posição pos_f_pij1 que está na lista pij2 posição pos_pij1
            pij1[pos_pij1] = 0  # Deleta os valores utilizados da lista pij1
            pij2[pos_pij1] = 0  # Deleta os valores utilizados da lista pij2
            pos_f_pij1 += 1  # Váriavel pos_f_pij1 adiciona 1 ao seu valor
        elif menor1 > menor2:
            seq[pos_f_pij2] = 'J' + str(pos_pij2 + 1)
            f_pij2[pos_f_pij2] = pij2[pos_pij2]  # f_pij2 adiciona o valor na posição pos_f_pij2 que está na lista pij2 posição pos_lista2
            f_pij1[pos_f_pij2] = pij1[pos_pij2]  # f_pij1 adiciona o valor na posição pos_f_pij2 que está na lista pij1 posição pos_lista2
            pij2[pos_pij2] = 0  # Deleta os valores utilizados da lista pij2
            pij1[pos_pij2] = 0  # Deleta os valores utilizados da lista pij1
            pos_f_pij2 -= 1  # Váriavel pos_fpij2 subtrai 1 de seu valor
        menor1 = 0
        menor2 = 0

    pj_final = [f_pij1, f_pij2]
    pj = pj_final[:]

    return seq, pj


