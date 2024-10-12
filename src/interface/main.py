import streamlit as st
from layout.left_column import render_left_column
from layout.right_column import render_right_column
import scipy.io  # type: ignore


def main():
    # Título centralizado
    st.title("C213 - PROJETO DE SISTEMAS EMBARCADOS")

    # Definição de valores padrão
    initial_k, initial_theta, initial_tau = (
        29.056,
        10.10,
        47.50,
    )  # Valores iniciais para o gráfico da direita
    arquivo_mat = r"dataset/Dataset_Grupo6.mat"  # Caminho do dataset .MAT

    # Carregar os dados do arquivo MAT e plotar o dataset
    dados_mat = scipy.io.loadmat(arquivo_mat)
    tempo = dados_mat["TARGET_DATA____ProjetoC213_Degrau"][
        0, :
    ]  # Primeira linha como tempo
    degrau = dados_mat["TARGET_DATA____ProjetoC213_Degrau"][
        1, :
    ]  # Segunda linha como valores do degrau
    saida_motor = dados_mat["TARGET_DATA____ProjetoC213_PotenciaMotor"][
        1, :
    ]  # Segunda linha como saída do motor

    amplitude_degrau = degrau[-1]

    # Divisão em duas colunas para os gráficos
    col1, col2 = st.columns(2)

    # Renderizar a coluna da esquerda
    with col1:
        render_left_column(tempo, degrau, saida_motor)

    # Renderizar a coluna da direita
    with col2:
        render_right_column(
            initial_k,
            initial_theta,
            initial_tau,
            tempo,
            degrau,
            amplitude_degrau,
            saida_motor,
        )


if __name__ == "__main__":
    main()
