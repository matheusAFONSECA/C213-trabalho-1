def calculate_pid(k, t, c):
    # Simulação de um cálculo PID simples
    return k, t, c

def estimate_pid_values(tempo, degrau, saida_motor):

    # Determinar o valor final da resposta e amplitude do degrau
    amplitude_degrau = degrau[-1]
    valor_final = saida_motor[-1]

    # Estimar K, Tau, e Theta
    saida_ajustada = saida_motor - saida_motor[0]
    valor_final = saida_motor[-1]
    K = valor_final / amplitude_degrau
    tempo_t1 = 0
    tempo_t2 = 0
    for i in range(len(saida_motor)):
        if saida_motor[i] >= 0.283 * valor_final and tempo_t1 == 0:
            tempo_t1 = tempo[i]
        if saida_motor[i] >= 0.6321 * valor_final:
            tempo_t2 = tempo[i]
            break

    tau_estimado = 1.5 * (tempo_t2 - tempo_t1)
    theta_estimado = tempo_t2 - tau_estimado

    return K, tau_estimado, theta_estimado
