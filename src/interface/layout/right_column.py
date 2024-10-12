import streamlit as st
from utils.plot_utils import plot_graph_2, plot_graph_pid
from models.pid_model import calculate_pid, CHR, estimate_pid_values, ITAE
import control as ctl

def render_right_column(initial_k, initial_theta, initial_tau, tempo, degrau, amplitude_degrau, saida_motor):
    """
    Função responsável por renderizar a coluna direita com o gráfico PID e os controles.
    """
    st.subheader("Gráfico PID")

    # Inicializa o gráfico da direita com valores padrão
    option2 = st.radio("Escolha o tipo de PID:", ("CHR", "ITAE"), index=0)
    
    # Atualiza o título do gráfico da direita com base na opção selecionada
    st.subheader(f"Gráfico PID - {option2}")

    # Inputs para os parâmetros PID
    st.write("PARAMETROS PID")
    k = st.number_input("K", value=initial_k)
    theta = st.number_input("Theta", value=initial_theta)
    tau = st.number_input("Tau", value=initial_tau)

    if option2 == "CHR":

        tempo_chr, saida_chr = CHR(k, tau, theta, amplitude_degrau, tempo)

        fig_right = plot_graph_pid(tempo_chr, saida_chr, tempo, option2, degrau, amplitude_degrau)  # Gráfico com CHR

    elif option2 == "ITAE":

        tempo_itae, saida_itae = ITAE(k, tau, theta, amplitude_degrau, tempo)  # Controlador ITAE

        fig_right = plot_graph_pid(tempo_itae, saida_itae, tempo, option2, degrau, amplitude_degrau)  # Gráfico com CHR


    # Botão para gerar o novo gráfico da direita
    if st.button("Gerar Gráfico"):
        if option2 == "CHR":

            tempo_chr, saida_chr = CHR(k, tau, theta, amplitude_degrau, tempo)

            fig_right = plot_graph_pid(tempo_chr, saida_chr, tempo, option2, degrau, amplitude_degrau)  # Gráfico com CHR

        elif option2 == "ITAE":

            tempo_itae, saida_itae = ITAE(k, tau, theta, amplitude_degrau, tempo)  # Controlador ITAE

            fig_right = plot_graph_pid(tempo_itae, saida_itae, tempo, option2, degrau, amplitude_degrau)  # Gráfico com CHR

    plot_right_placeholder = st.pyplot(fig_right)  # Placeholder para o gráfico da direita
