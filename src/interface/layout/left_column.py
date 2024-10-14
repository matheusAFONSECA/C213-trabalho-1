import streamlit as st
import control as ctl  # type: ignore
from models.pid_model import estimate_pid_values
from utils.plot_utils import (
    plot_dataset_graph,
    plot_graph_open_loop,
    plot_graph_closed_loop,
)


def render_left_column(tempo, degrau, saida_motor):
    """
    Renders the left column with the graph and controls.

    Parameters:
    tempo (array-like): Time data for the system.
    degrau (array-like): Step input data for the system.
    saida_motor (array-like): Motor output data for the system.
    """
    st.subheader("Dados do circuito")

    with st.container(height=350):
        plot_title_graph = st.empty()  # Placeholder for the graph title
        plot_left_placeholder = st.empty()  # Placeholder for the graph

    # Initialize the graph with the default radio option
    option = st.radio(
        "Escolha o gráfico:", ("Dataset", "Malha aberta", "Malha fechada"), index=0
    )

    plot_title_graph.subheader(f"{option}")

    # Calculate and plot the open loop
    K, tau_estimado, theta_estimado = estimate_pid_values(tempo, degrau, saida_motor)

    if option == "Dataset":
        fig_left = plot_dataset_graph(tempo, degrau, saida_motor, "Dataset")

    elif option == "Malha aberta":
        # Create the transfer function for the open loop
        open_loop = ctl.tf([K], [tau_estimado, 1])

        # Adding the delay
        num_delay, den_delay = ctl.pade(theta_estimado, 20)
        open_loop_with_theta = ctl.series(ctl.tf(num_delay, den_delay), open_loop)

        # Simulate the step response
        tempo_open, saida_open = ctl.step_response(open_loop_with_theta, tempo)

        # Create plot for the open loop
        fig_left = plot_graph_open_loop(
            tempo_open, saida_open, tempo, degrau, "Resposta em Malha Aberta"
        )

    else:

        # Adding the delay
        num_delay, den_delay = ctl.pade(theta_estimado, 20)
        
        # Create the transfer function for the open loop
        open_loop = ctl.tf([K], [tau_estimado, 1])
        open_loop_with_theta = ctl.series(ctl.tf(num_delay, den_delay), open_loop)

        # Create the transfer function for the closed loop
        closed_loop = ctl.feedback(open_loop_with_theta, 1)

        # closed_loop_with_theta = ctl.series(ctl.tf(num_delay, den_delay), closed_loop)

        # Simulate the step response
        tempo_closed, saida_closed = ctl.step_response(closed_loop, tempo)

        # Create plot for the closed loop
        fig_left = plot_graph_closed_loop(
            tempo_closed, saida_closed, tempo, degrau, "Resposta em Malha Fechada"
        )

    # Display the graph in the placeholder
    plot_left_placeholder.pyplot(fig_left)
