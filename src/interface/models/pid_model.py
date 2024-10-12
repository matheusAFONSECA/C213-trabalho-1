import control as ctl  # type: ignore


def estimate_pid_values(tempo, degrau, saida_motor):
    # Determinar o valor final da resposta e amplitude do degrau
    amplitude_degrau = degrau[-1]
    valor_final = saida_motor[-1]

    # Estimar K, Tau, e Theta
    saida_ajustada = saida_motor - saida_motor[0]  # type: ignore  # noqa: F841
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


def CHR(k, tau, theta, amplitude_degrau, tempo):
    """
    Função para calcular a resposta do controlador CHR.
    """
    # Parâmetros do controlador CHR
    ti_chr = tau
    td_chr = theta / 2
    kp_chr = (0.6 * tau) / (k * theta)

    # print(f"Kp = {kp_chr}, Td = {ti_chr}, Ti = {td_chr}.")

    pid_chr = [kp_chr * td_chr, kp_chr, kp_chr / ti_chr]
    den_chr = [1, 0]
    controlador_chr = ctl.tf(pid_chr, den_chr)

    # Adicionando theta ao controlador CHR
    num_delay, den_delay = ctl.pade(theta, 20)
    controlador_chr_com_theta = ctl.series(
        ctl.tf(num_delay, den_delay), controlador_chr
    )
    sistema_com_theta = ctl.tf(k, [tau, 1])
    chr_completo = ctl.series(sistema_com_theta, controlador_chr_com_theta)

    sistema_chr_controlado = ctl.feedback(chr_completo, 1)
    tempo_chr, saida_chr = ctl.step_response(
        sistema_chr_controlado * amplitude_degrau, tempo
    )

    # Sobressinal do CHR
    informacoes_chr = ctl.step_info(sistema_chr_controlado)
    sobressinal_chr = informacoes_chr["Overshoot"]  # type: ignore  # noqa: F841
    # print(f'OVERSHOOT  com CHR: {sobressinal_chr:.4f}.')

    return (tempo_chr, saida_chr)


def ITAE(k, tau, theta, amplitude_degrau, tempo, tau_inicial=47.50):
    """
    Função para calcular a resposta do controlador ITAE.
    """
    a, b, c, d, e, f = 0.965, -0.85, 0.796, -0.147, 0.308, 0.929  # Parâmetros do ITAE

    kp_itae = (a / k) * ((theta / tau) ** b)
    ti_itae = tau / (c + (d * (theta / tau)))
    td_itae = tau * e * ((theta / tau) ** f)

    # print(f"Kp = {kp_itae}, Td = {td_itae}, Ti = {ti_itae}.")

    pid_itae = [kp_itae * td_itae, kp_itae, kp_itae / ti_itae]
    den_itae = [1, 0]
    controlador_itae = ctl.tf(pid_itae, den_itae)

    # Adicionando theta ao controlador ITAE
    num_delay, den_delay = ctl.pade(theta, 20)

    pid_itae_delay = ctl.series(ctl.tf(num_delay, den_delay), controlador_itae)

    sys_theta = ctl.tf(k, [tau_inicial, 1])
    itae = ctl.series(pid_itae_delay, sys_theta)
    sys_ctrl_itae = ctl.feedback(itae, 1)
    temp_ITAE, sinal_ITAE = ctl.step_response(sys_ctrl_itae * amplitude_degrau, tempo)

    ITAE_info = ctl.step_info(sys_ctrl_itae)
    overshoot_itae = ITAE_info["Overshoot"]  # type: ignore  # noqa: F841
    # print(f'OVERSHOOT por ITAE: {overshoot_itae:.4f}')

    return (temp_ITAE, sinal_ITAE)
