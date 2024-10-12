import streamlit as st
from utils.plot_utils import plot_graph_1, plot_graph_2
from models.pid_model import calculate_pid

def main():
    # Título centralizado
    st.title("C213 - PROJETO DE SISTEMAS EMBARCADOS")

    # Divisão em duas colunas para os gráficos
    col1, col2 = st.columns(2)

    # Definição de valores padrão
    initial_radio_option = "dataset"  # Opção inicial do gráfico da esquerda
    initial_k, initial_t, initial_c = 1.0, 1.0, 0.0  # Valores iniciais para o gráfico da direita

    # ---- Gráfico da Esquerda ----
    with col1:
        st.subheader("Dataset - Malha aberta/fechada")

        # Inicializa o gráfico com a opção padrão do rádio
        fig_left = plot_graph_1(initial_radio_option)
        plot_left_placeholder = st.pyplot(fig_left)  # Placeholder para o gráfico da esquerda

        # Input do rádio para controle do gráfico da esquerda
        option = st.radio("Escolha o gráfico:", ("Dataset", "Malha aberta/fechada"), index=0)

        # Atualiza o gráfico da esquerda com base na seleção
        fig_left = plot_graph_1(option)
        plot_left_placeholder.pyplot(fig_left)

    # ---- Gráfico da Direita ----
    with col2:
        st.subheader("Gráfico PID - CHR / ITAE")

        # Inicializa o gráfico da direita com valores padrão
        fig_right = plot_graph_2((initial_k, initial_t, initial_c))
        plot_right_placeholder = st.pyplot(fig_right)  # Placeholder para o gráfico da direita

        # Input do rádio para controle do gráfico da esquerda
        option2 = st.radio("Escolha o tipo de PID:", ("CHR", "ITAE"), index=0)

        # Inputs para os parâmetros PID
        st.write("PARAMETROS PID")
        k = st.number_input("K", value=initial_k)
        t = st.number_input("T", value=initial_t)
        c = st.number_input("C", value=initial_c)

        # Botão para gerar o novo gráfico da direita
        if st.button("Gerar Gráfico"):
            pid_result = calculate_pid(k, t, c)  # Cálculo do modelo PID
            fig_right = plot_graph_2(pid_result)  # Geração do gráfico com os novos parâmetros
            plot_right_placeholder.pyplot(fig_right)  # Atualização do gráfico

if __name__ == "__main__":
    main()
