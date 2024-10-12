import streamlit as st
from utils.plot_utils import plot_graph_2
from models.pid_model import calculate_pid

def render_right_column(initial_k, initial_t, initial_c):
    """
    Função responsável por renderizar a coluna direita com o gráfico PID e os controles.
    """
    st.subheader("Gráfico PID")

    # Inicializa o gráfico da direita com valores padrão
    option2 = st.radio("Escolha o tipo de PID:", ("CHR", "ITAE"), index=0)
    
    # Atualiza o título do gráfico da direita com base na opção selecionada
    st.subheader(f"Gráfico PID - {option2}")

    # Inicializa o gráfico da direita com os valores padrão
    fig_right = plot_graph_2((initial_k, initial_t, initial_c), option2)
    plot_right_placeholder = st.pyplot(fig_right)  # Placeholder para o gráfico da direita

    # Inputs para os parâmetros PID
    st.write("PARAMETROS PID")
    k = st.number_input("K", value=initial_k)
    t = st.number_input("T", value=initial_t)
    c = st.number_input("C", value=initial_c)

    # Botão para gerar o novo gráfico da direita
    if st.button("Gerar Gráfico"):
        pid_result = calculate_pid(k, t, c)  # Cálculo do modelo PID
        fig_right = plot_graph_2(pid_result, option2)  # Geração do gráfico com os novos parâmetros
        plot_right_placeholder.pyplot(fig_right)  # Atualização do gráfico
