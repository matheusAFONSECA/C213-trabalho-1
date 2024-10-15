import streamlit as st
from models.pid_model import CHR, ITAE
from utils.plot_utils import plot_graph_pid


def render_right_column(
    initial_k, initial_theta, initial_tau, tempo, degrau, amplitude_degrau, saida_motor
):
    """
    Function responsible for rendering the right column with the PID graph and controls.

    Parameters:
    initial_k (float): Initial value for the K parameter.
    initial_theta (float): Initial value for the Theta parameter.
    initial_tau (float): Initial value for the Tau parameter.
    tempo (list): List of time values for the simulation.
    degrau (float): Step input value.
    amplitude_degrau (float): Amplitude of the step input.
    saida_motor (list): Motor output values.
    """
    st.subheader("Gráfico do controlador PID")

    # Container for the graph with a fixed height
    with st.container(height=350):
        plot_title_graph = st.empty()  # Placeholder for the graph title
        plot_right_placeholder = st.empty()  # Placeholder for the graph

    # Radio button to select the type of PID
    option2 = st.radio("Escolha o tipo de PID:", ("CHR", "ITAE"), index=0)
    plot_title_graph.subheader(f"{option2}")

    # Inputs for PID parameters
    st.write("Parâmetros do PID")

    k_vazio = st.empty()
    theta_vazio = st.empty()
    tau_vazio = st.empty()

    if option2 == "CHR":
        # Update the PID parameters based on the input values
        initial_k = 0.09
        initial_theta = 5.17
        initial_tau = 47.25

    elif option2 == "ITAE":
        # Update the PID parameters based on the input values
        initial_k = 0.12
        initial_theta = 3.55
        initial_tau = 61.86

    k = k_vazio.number_input("Kp", value=initial_k)
    theta = theta_vazio.number_input("Td", value=initial_theta)
    tau = tau_vazio.number_input("Ti", value=initial_tau)

    # Update the graph based on the selected option
    if option2 == "CHR":

        tempo_chr, saida_chr = CHR(k, tau, theta, amplitude_degrau, tempo)
        fig_right = plot_graph_pid(
            tempo_chr, saida_chr, tempo, option2, degrau, amplitude_degrau
        )

    elif option2 == "ITAE":

        tempo_itae, saida_itae = ITAE(k, tau, theta, amplitude_degrau, tempo)
        fig_right = plot_graph_pid(
            tempo_itae, saida_itae, tempo, option2, degrau, amplitude_degrau
        )

    # Update the graph in the placeholder
    plot_right_placeholder.pyplot(fig_right)
