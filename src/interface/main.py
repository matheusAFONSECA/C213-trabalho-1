import streamlit as st
import scipy.io  # type: ignore
from layout.left_column import render_left_column
from layout.right_column import render_right_column


def main():
    # Centralized title
    st.title("C213 - PROJETO DE SISTEMAS EMBARCADOS")

    # Default values for the right column graph
    initial_k, initial_theta, initial_tau = 29.056, 10.10, 47.50
    arquivo_mat = r"dataset/Dataset_Grupo6.mat"  # Path to the .MAT dataset

    # Load data from the MAT file
    dados_mat = scipy.io.loadmat(arquivo_mat)
    tempo = dados_mat["TARGET_DATA____ProjetoC213_Degrau"][0, :]  # First row as time
    degrau = dados_mat["TARGET_DATA____ProjetoC213_Degrau"][
        1, :
    ]  # Second row as step values
    saida_motor = dados_mat["TARGET_DATA____ProjetoC213_PotenciaMotor"][
        1, :
    ]  # Second row as motor output

    amplitude_degrau = degrau[-1]  # Step amplitude

    # Split into two columns for the graphs
    col1, col2 = st.columns(2)

    # Render the left column
    with col1:
        render_left_column(tempo, degrau, saida_motor)

    # Render the right column
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
