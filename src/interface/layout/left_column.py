import streamlit as st
import scipy.io
from utils.plot_utils import plot_dataset_graph, plot_graph_open_loop
from models.pid_model import estimate_pid_values
import control as ctl
import numpy as np

def render_left_column(arquivo_mat):
    """
    Função responsável por renderizar a coluna esquerda com o gráfico e os controles.
    """
    st.subheader("Dados do circuito")

    # Inicializa o gráfico com a opção padrão do rádio
    option = st.radio("Escolha o gráfico:", ("Dataset", "Malha Aberta/Fechada"), index=0)

    # Atualiza o título do gráfico da esquerda com base na opção selecionada
    st.subheader(f"{option}")

    # Carregar os dados do arquivo MAT e plotar o dataset
    dados_mat = scipy.io.loadmat(arquivo_mat)
    tempo = dados_mat['TARGET_DATA____ProjetoC213_Degrau'][0, :]  # Primeira linha como tempo
    degrau = dados_mat['TARGET_DATA____ProjetoC213_Degrau'][1, :]  # Segunda linha como valores do degrau
    saida_motor = dados_mat['TARGET_DATA____ProjetoC213_PotenciaMotor'][1, :]  # Segunda linha como saída do motor

    if option == "Dataset":

        fig_left = plot_dataset_graph(tempo, degrau, saida_motor, "Dataset")

    else:

        # Calcular e plotar a malha aberta
        K, tau_estimado, theta_estimado = estimate_pid_values(tempo, degrau, saida_motor)

        # Criar a função de transferência para a malha aberta
        malha_aberta = ctl.tf([K], [tau_estimado, 1])
        
        # Adicionando o theta
        num_delay, den_delay = ctl.pade(theta_estimado, 20)
        malha_aberta_com_theta = ctl.series(ctl.tf(num_delay, den_delay), malha_aberta)

        # Simular a resposta ao degrau
        tempo_aberta, saida_aberta = ctl.step_response(malha_aberta_com_theta, tempo)

        # Plotar a malha aberta/fechada
        fig_left = plot_graph_open_loop(tempo_aberta, saida_aberta, tempo, degrau, "Resposta em Malha Aberta/Fechada")

    # Placeholder para o gráfico da esquerda
    plot_left_placeholder = st.pyplot(fig_left)
