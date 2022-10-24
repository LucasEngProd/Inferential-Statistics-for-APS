import back_end_aps

# n = tamanho da amostra
# z = valor para determinação do nível de confiança
# p_start = delimitação inicial para tempo de processamento
# p_end = delimitação final para tempo de processamento
# d_start = delimitação inicial para data de entrega
# d_end = delimitação final para data de entrega
# j_size = quantidade de tarefas
# m_size = quantidade de máquinas

n = 1000
z = 1.96
p_start = 10
p_end = 50
d_start = 100
d_end = 150
j_size = 10
m_size = 10

back_end_aps.rules_results(p_start, p_end, d_start, d_end, j_size, n, z)
back_end_aps.johnson_results(p_start, p_end, j_size, n, z)
back_end_aps.neh_results(p_start, p_end, j_size, m_size, n, z)
