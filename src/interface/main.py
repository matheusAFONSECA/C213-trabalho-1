import streamlit as st
from layout.left_column import render_left_column
from layout.right_column import render_right_column

def main():
    # Título centralizado
    st.title("C213 - PROJETO DE SISTEMAS EMBARCADOS")

    # Definição de valores padrão
    initial_k, initial_t, initial_c = 1.0, 1.0, 0.0  # Valores iniciais para o gráfico da direita
    arquivo_mat = r'dataset/Dataset_Grupo6.mat'  # Caminho do dataset .MAT

    # Divisão em duas colunas para os gráficos
    col1, col2 = st.columns(2)

    # Renderizar a coluna da esquerda
    with col1:
        render_left_column(arquivo_mat)

    # Renderizar a coluna da direita
    with col2:
        render_right_column(initial_k, initial_t, initial_c)

if __name__ == "__main__":
    main()
