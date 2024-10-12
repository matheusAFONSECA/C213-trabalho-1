import streamlit as st
from utils.plot_utils import plot_graph_pid
from models.pid_model import CHR, ITAE


def render_right_column(
    initial_k, initial_theta, initial_tau, tempo, degrau, amplitude_degrau, saida_motor
):
    """
    Função responsável por renderizar a coluna direita com o gráfico PID e os controles.
    """
    st.subheader("Gráfico PID")

    with st.container(height=350):
        plot_title_graph = st.empty()  # Cria um espaço reservado para o título do gráfico
        # Placeholder para o gráfico
        plot_right_placeholder = st.empty()  # Cria um espaço reservado para o gráfico

    # Inicializa o gráfico da direita com valores padrão
    option2 = st.radio("Escolha o tipo de PID:", ("CHR", "ITAE"), index=0)

    plot_title_graph.subheader(f"{option2}")

    # Inputs para os parâmetros PID
    st.write("PARAMETROS PID")
    k = st.number_input("K", value=initial_k)
    theta = st.number_input("Theta", value=initial_theta)
    tau = st.number_input("Tau", value=initial_tau)

    # Atualiza o gráfico com base na opção selecionada
    if option2 == "CHR":
        tempo_chr, saida_chr = CHR(k, tau, theta, amplitude_degrau, tempo)
        fig_right = plot_graph_pid(
            tempo_chr, saida_chr, tempo, option2, degrau, amplitude_degrau
        )  # Gráfico com CHR

    elif option2 == "ITAE":
        tempo_itae, saida_itae = ITAE(
            k, tau, theta, amplitude_degrau, tempo
        )  # Controlador ITAE
        fig_right = plot_graph_pid(
            tempo_itae, saida_itae, tempo, option2, degrau, amplitude_degrau
        )  # Gráfico com ITAE

    # Atualiza o gráfico no placeholder
    plot_right_placeholder.pyplot(fig_right)  # Placeholder para o gráfico da direita
