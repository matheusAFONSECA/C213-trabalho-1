import streamlit as st
import control as ctl       # type: ignore
from models.pid_model import estimate_pid_values
from utils.plot_utils import (
    plot_dataset_graph,
    plot_graph_open_loop,
    plot_graph_closed_loop,
)


def render_left_column(tempo, degrau, saida_motor):
    """
    Função responsável por renderizar a coluna esquerda com o gráfico e os controles.
    """
    st.subheader("Dados do circuito")

    with st.container(height=350):
        plot_title_graph = st.empty()  # Cria um espaço reservado para o título do gráfico
        # Placeholder para o gráfico
        plot_left_placeholder = st.empty()  # Cria um espaço reservado para o gráfico


    # Inicializa o gráfico com a opção padrão do rádio
    option = st.radio(
        "Escolha o gráfico:", ("Dataset", "Malha Aberta", "Malha Fechada"), index=0
    )

    plot_title_graph.subheader(f"{option}")

    # Calcular e plotar a malha aberta
    K, tau_estimado, theta_estimado = estimate_pid_values(tempo, degrau, saida_motor)

    if option == "Dataset":
        fig_left = plot_dataset_graph(tempo, degrau, saida_motor, "Dataset")

    elif option == "Malha Aberta":
        # Criar a função de transferência para a malha aberta
        malha_aberta = ctl.tf([K], [tau_estimado, 1])

        # Adicionando o theta
        num_delay, den_delay = ctl.pade(theta_estimado, 20)
        malha_aberta_com_theta = ctl.series(ctl.tf(num_delay, den_delay), malha_aberta)

        # Simular a resposta ao degrau
        tempo_aberta, saida_aberta = ctl.step_response(malha_aberta_com_theta, tempo)

        # Criar plot da malha aberta
        fig_left = plot_graph_open_loop(
            tempo_aberta, saida_aberta, tempo, degrau, "Resposta em Malha Aberta"
        )

    else:
        # Criar a função de transferência para a malha aberta
        malha_fechada = ctl.tf([K], [tau_estimado * theta_estimado, tau_estimado, 1])

        # Adicionando o theta
        num_delay, den_delay = ctl.pade(theta_estimado, 20)
        malha_fechada_com_theta = ctl.series(
            ctl.tf(num_delay, den_delay), malha_fechada
        )

        # Simular a resposta ao degrau
        tempo_fechada, saida_fechada = ctl.step_response(malha_fechada_com_theta, tempo)

        # Criar plot da malha fechada
        fig_left = plot_graph_closed_loop(
            tempo_fechada, saida_fechada, tempo, degrau, "Resposta em Malha Fechada"
        )

    # Placeholder para o gráfico da esquerda
    plot_left_placeholder.pyplot(fig_left)  # Placeholder para o gráfico da esquerda
