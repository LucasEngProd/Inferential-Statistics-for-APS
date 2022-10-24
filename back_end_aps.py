import aps
from random import randint
from numpy import std, round, mean
from tabulate import tabulate
from math import sqrt


def int_conf_media(result: list, n1: int, z1: float):
    return str(round(mean(result), 2)) + " ± " + str(round(std(result, ddof=1) * z1 / sqrt(n1), 2))


def rules_results(p_start, p_end, d_start, d_end, j_size, n, z):
    pjRules = []
    djRules = []

    fluxoMedFifo = []
    fluxoMedSpt = []
    fluxoMedEdd = []
    fluxoMedCrr = []
    fluxoMedStr1 = []

    atrasoMaxFifo = []
    atrasoMaxSpt = []
    atrasoMaxEdd = []
    atrasoMaxCrr = []
    atrasoMaxStr1 = []

    earlinessFifo = []
    earlinessSpt = []
    earlinessEdd = []
    earlinessCrr = []
    earlinessStr1 = []

    tardinessFifo = []
    tardinessSpt = []
    tardinessEdd = []
    tardinessCrr = []
    tardinessStr1 = []

    tarefasFifo = []
    tarefasSpt = []
    tarefasEdd = []
    tarefasCrr = []
    tarefasStr1 = []

    for qt in range(0, n):

        for j in range(0, j_size):
            pj = randint(p_start, p_end)
            if d_start <= pj < d_end:
                dj = randint(pj + 1, d_end)
            elif d_start <= pj and pj > d_end:
                dj = pj + 1
            else:
                dj = randint(d_start, d_end)

            pjRules.append(pj)
            djRules.append(dj)

        pj_fifo = pjRules[:]
        dj_fifo = djRules[:]
        pj_spt = pjRules[:]
        dj_spt = djRules[:]
        pj_edd = pjRules[:]
        dj_edd = djRules[:]
        pj_crr = pjRules[:]
        dj_crr = djRules[:]
        pj_str1 = pjRules[:]
        dj_str1 = djRules[:]

        aps.fifo(pj_fifo, dj_fifo)
        aps.spt(pj_spt, dj_spt)
        aps.edd(pj_edd, dj_edd)
        aps.crr(pj_crr, dj_crr)
        aps.str1(pj_str1, dj_str1)

        fluxoMedFifo.append(aps.mean_flow_time_rules(pj_fifo))
        fluxoMedSpt.append(aps.mean_flow_time_rules(pj_spt))
        fluxoMedEdd.append(aps.mean_flow_time_rules(pj_edd))
        fluxoMedCrr.append(aps.mean_flow_time_rules(pj_crr))
        fluxoMedStr1.append(aps.mean_flow_time_rules(pj_str1))

        atrasoMaxFifo.append(aps.max_lateness(pj_fifo, dj_fifo))
        atrasoMaxSpt.append(aps.max_lateness(pj_spt, dj_spt))
        atrasoMaxEdd.append(aps.max_lateness(pj_edd, dj_edd))
        atrasoMaxCrr.append(aps.max_lateness(pj_crr, dj_crr))
        atrasoMaxStr1.append(aps.max_lateness(pj_str1, dj_str1))

        earlinessFifo.append(aps.average_earliness(pj_fifo, dj_fifo))
        earlinessSpt.append(aps.average_earliness(pj_spt, dj_spt))
        earlinessEdd.append(aps.average_earliness(pj_edd, dj_edd))
        earlinessCrr.append(aps.average_earliness(pj_crr, dj_crr))
        earlinessStr1.append(aps.average_earliness(pj_str1, dj_str1))

        tardinessFifo.append(aps.average_tardiness(pj_fifo, dj_fifo))
        tardinessSpt.append(aps.average_tardiness(pj_spt, dj_spt))
        tardinessEdd.append(aps.average_tardiness(pj_edd, dj_edd))
        tardinessCrr.append(aps.average_tardiness(pj_crr, dj_crr))
        tardinessStr1.append(aps.average_tardiness(pj_str1, dj_str1))

        tarefasFifo.append(aps.number_tardy_jobs(pj_fifo, dj_fifo))
        tarefasSpt.append(aps.number_tardy_jobs(pj_spt, dj_spt))
        tarefasEdd.append(aps.number_tardy_jobs(pj_edd, dj_edd))
        tarefasCrr.append(aps.number_tardy_jobs(pj_crr, dj_crr))
        tarefasStr1.append(aps.number_tardy_jobs(pj_str1, dj_str1))

        pjRules.clear()
        djRules.clear()

    medFluxoMedFifo = int_conf_media(fluxoMedFifo, n, z)
    medFluxoMedSpt = int_conf_media(fluxoMedSpt, n, z)
    medFluxoMedEdd = int_conf_media(fluxoMedEdd, n, z)
    medFluxoMedCrr = int_conf_media(fluxoMedCrr, n, z)
    medFluxoMedStr1 = int_conf_media(fluxoMedStr1, n, z)

    medAtrasoMaxFifo = int_conf_media(atrasoMaxFifo, n, z)
    medAtrasoMaxSpt = int_conf_media(atrasoMaxSpt, n, z)
    medAtrasoMaxEdd = int_conf_media(atrasoMaxEdd, n, z)
    medAtrasoMaxCrr = int_conf_media(atrasoMaxCrr, n, z)
    medAtrasoMaxStr1 = int_conf_media(atrasoMaxStr1, n, z)

    medEarlinessFifo = int_conf_media(earlinessFifo, n, z)
    medEarlinessSpt = int_conf_media(earlinessSpt, n, z)
    medEarlinessEdd = int_conf_media(earlinessEdd, n, z)
    medEarlinessCrr = int_conf_media(earlinessCrr, n, z)
    medEarlinessStr1 = int_conf_media(earlinessStr1, n, z)

    medTardinessFifo = int_conf_media(tardinessFifo, n, z)
    medTardinessSpt = int_conf_media(tardinessSpt, n, z)
    medTardinessEdd = int_conf_media(tardinessEdd, n, z)
    medTardinessCrr = int_conf_media(tardinessCrr, n, z)
    medTardinessStr1 = int_conf_media(tardinessStr1, n, z)

    medTarefasFifo = int_conf_media(tarefasFifo, n, z)
    medTarefasSpt = int_conf_media(tarefasSpt, n, z)
    medTarefasEdd = int_conf_media(tarefasEdd, n, z)
    medTarefasCrr = int_conf_media(tarefasCrr, n, z)
    medTarefasStr1 = int_conf_media(tarefasStr1, n, z)

    dataRules = [["FIFO ", medFluxoMedFifo, medAtrasoMaxFifo,
                  medEarlinessFifo, medTardinessFifo, medTarefasFifo],
                 ["SPT", medFluxoMedSpt, medAtrasoMaxSpt,
                  medEarlinessSpt, medTardinessSpt, medTarefasSpt],
                 ["EDD", medFluxoMedEdd, medAtrasoMaxEdd,
                  medEarlinessEdd, medTardinessEdd, medTarefasEdd],
                 ["CRR", medFluxoMedCrr, medAtrasoMaxCrr,
                  medEarlinessCrr, medTardinessCrr, medTarefasCrr],
                 ["STR", medFluxoMedStr1, medAtrasoMaxStr1,
                  medEarlinessStr1, medTardinessStr1, medTarefasStr1]]
    print(tabulate(dataRules, headers=["Média/Regra", "Fluxo Médio",
                                       "Atraso Máximo", "Earliness",
                                       "Tardiness", "Tarefas em atraso"]))
    print('')


def johnson_results(p_start, p_end, j_size, n, z):
    pjJohnsonMethod = []
    makespanJohnson = []
    fluxoMedJohnson = []
    makespanFifoJohnson = []
    fluxoMedFifoJohnson = []
    makespanNehJohnson = []
    fluxoMedNehJohnson = []

    for qt in range(0, n):

        for list_size in range(0, 2):
            pjJohnsonMethod.append([])
        for j in range(0, j_size):
            pjJohnsonMethod[0].append(randint(p_start, p_end))
            pjJohnsonMethod[1].append(randint(p_start, p_end))

        pj_johnson = pjJohnsonMethod[:]
        pj_fifo_johnson = pjJohnsonMethod[:]
        pj_neh_johnson = pjJohnsonMethod[:]

        pj_johnson = aps.johnson(pj_johnson)[1]
        pj_neh_johnson = aps.neh(pj_neh_johnson)[1]

        makespanJohnson.append(aps.makespan(pj_johnson))
        fluxoMedJohnson.append(aps.mean_flow_time_methods(pj_johnson))
        makespanFifoJohnson.append(aps.makespan(pj_fifo_johnson))
        fluxoMedFifoJohnson.append(aps.mean_flow_time_methods(pj_fifo_johnson))
        makespanNehJohnson.append(aps.makespan(pj_neh_johnson))
        fluxoMedNehJohnson.append(aps.mean_flow_time_methods(pj_neh_johnson))

        pjJohnsonMethod.clear()

    medMakespanJohnson = int_conf_media(makespanJohnson, n, z)
    medFluxoMedJohnson = int_conf_media(fluxoMedJohnson, n, z)
    medMakespanFifoJohnson = int_conf_media(makespanFifoJohnson, n, z)
    medFluxoMedFifoJohnson = int_conf_media(fluxoMedFifoJohnson, n, z)
    medMakespanNehJohnson = int_conf_media(makespanNehJohnson, n, z)
    medFluxoMedNehJohnson = int_conf_media(fluxoMedNehJohnson, n, z)

    dataJohnsonMethod = [["JOHNSON ", medMakespanJohnson, medFluxoMedJohnson],
                         ["NEH", medMakespanNehJohnson, medFluxoMedNehJohnson],
                         ["FIFO", medMakespanFifoJohnson, medFluxoMedFifoJohnson]]

    print(tabulate(dataJohnsonMethod, headers=["Média/Médodo", "Makespan",
                                               "Fluxo Médio"]))
    print('')


def neh_results(p_start, p_end, j_size, m_size, n, z):
    pjNehMethod = []
    makespanNeh = []
    fluxoMedNeh = []
    makespanFifoNeh = []
    fluxoMedFifoNeh = []

    for qt in range(0, n):

        for list_size in range(0, m_size):
            pjNehMethod.append([])
        for j in range(0, j_size):
            for m in range(0, m_size):
                pjNehMethod[m].append(randint(p_start, p_end))

        pj_neh = pjNehMethod[:]
        pj_fifo_neh = pjNehMethod[:]

        pj_neh = aps.neh(pj_neh)[1]

        makespanNeh.append(aps.makespan(pj_neh))
        fluxoMedNeh.append(aps.mean_flow_time_methods(pj_neh))
        makespanFifoNeh.append(aps.makespan(pj_fifo_neh))
        fluxoMedFifoNeh.append(aps.mean_flow_time_methods(pj_fifo_neh))

        pjNehMethod.clear()

    medMakespanNeh = int_conf_media(makespanNeh, n, z)
    medFluxoMedNeh = int_conf_media(fluxoMedNeh, n, z)
    medMakespanFifoNeh = int_conf_media(makespanFifoNeh, n, z)
    medFluxoMedFifoNeh = int_conf_media(fluxoMedFifoNeh, n, z)

    dataNehMethod = [["NEH ", medMakespanNeh, medFluxoMedNeh],
                     ["FIFO", medMakespanFifoNeh, medFluxoMedFifoNeh]]

    print(tabulate(dataNehMethod, headers=["Média/Médodo", "Makespan",
                                           "Fluxo Médio"]))
    print('')


def neh_result_table(p_start1, p_end1,
                     p_start2, p_end2,
                     p_start3, p_end3,
                     j_size, m_size, n, z):
    dataNehMethodFluxoMed = [["NEH "], ["FIFO"]]
    dataNehMethodMakespan = [["NEH "], ["FIFO"]]
    pjNehMethod = []
    makespanNeh = []
    fluxoMedNeh = []
    makespanFifoNeh = []
    fluxoMedFifoNeh = []

    for cont in range(0, 3):
        for qt in range(0, n):

            for list_size in range(0, m_size):
                pjNehMethod.append([])
            for j in range(0, j_size):
                for m in range(0, m_size):
                    if cont == 0:
                        pjNehMethod[m].append(randint(p_start1, p_end1))
                    elif cont == 1:
                        pjNehMethod[m].append(randint(p_start2, p_end2))
                    elif cont == 2:
                        pjNehMethod[m].append(randint(p_start3, p_end3))

            pj_neh = pjNehMethod[:]
            pj_fifo_neh = pjNehMethod[:]

            pj_neh = aps.neh(pj_neh)[1]

            makespanNeh.append(aps.makespan(pj_neh))
            fluxoMedNeh.append(aps.mean_flow_time_methods(pj_neh))
            makespanFifoNeh.append(aps.makespan(pj_fifo_neh))
            fluxoMedFifoNeh.append(aps.mean_flow_time_methods(pj_fifo_neh))

            pjNehMethod.clear()

        medMakespanNeh = int_conf_media(makespanNeh, n, z)
        medFluxoMedNeh = int_conf_media(fluxoMedNeh, n, z)
        medMakespanFifoNeh = int_conf_media(makespanFifoNeh, n, z)
        medFluxoMedFifoNeh = int_conf_media(fluxoMedFifoNeh, n, z)

        dataNehMethodFluxoMed[0].append(medFluxoMedNeh)
        dataNehMethodFluxoMed[1].append(medFluxoMedFifoNeh)
        dataNehMethodMakespan[0].append(medMakespanNeh)
        dataNehMethodMakespan[1].append(medMakespanFifoNeh)

    print('')
    print('-' * 35, '  Fluxo Médio  ', '-' * 32)
    print('')
    print(tabulate(dataNehMethodFluxoMed, headers=["Média/Médodo", "Cenário 1",
                                                   "Cenário 2", "Cenário 3", "Cenário 4", "Cenário 5"]))
    print('')
    print('-' * 35, '  Makespan  ', '-' * 35)
    print('')
    print(tabulate(dataNehMethodMakespan, headers=["Média/Médodo", "Cenário 1",
                                                   "Cenário 2", "Cenário 3", "Cenário 4", "Cenário 5"]))
