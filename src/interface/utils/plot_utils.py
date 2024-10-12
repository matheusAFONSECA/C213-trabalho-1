import matplotlib.pyplot as plt
import numpy as np

def plot_graph_2(values, option2):
    k, t, c = values
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    
    if option2 == "CHR":
        y = k * np.exp(-t * x) + c  # Simulação para CHR
    else:
        y = k * np.sin(t * x) + c   # Simulação para ITAE
    
    ax.plot(x, y)
    ax.set_title(f"Gráfico PID - {option2}")
    return fig

def plot_dataset_graph(tempo, degrau, saida_motor, titulo):
    fig, ax = plt.subplots()
    
    ax.plot(tempo, degrau, label="Degrau")
    ax.plot(tempo, saida_motor, label="Saída do Motor")
    ax.set_xlabel('Tempo [s]')
    ax.set_ylabel('Amplitude')
    ax.set_title(titulo)
    ax.legend()
    
    return fig

def plot_graph_open_loop(tempo_aberta, saida_aberta, tempo, degrau, titulo):
    fig, ax = plt.subplots()
    ax.plot(tempo_aberta, saida_aberta, label="Saída em Malha Aberta")
    ax.plot(tempo, degrau, label="Degrau de Entrada")
    ax.set_xlabel('Tempo [s]')
    ax.set_ylabel('Amplitude')
    ax.set_title(titulo)
    ax.legend()
    
    return fig

def plot_graph_closed_loop(tempo_fechada, saida_fechada, tempo, degrau, titulo):
    fig, ax = plt.subplots()
    ax.plot(tempo_fechada, saida_fechada, label="Saída em Malha Fechada")
    ax.plot(tempo, degrau, label="Degrau de Entrada")
    ax.set_xlabel('Tempo [s]')
    ax.set_ylabel('Amplitude')
    ax.set_title(titulo)
    ax.legend()
    
    return fig
