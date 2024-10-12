import matplotlib.pyplot as plt # type: ignore

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

def plot_graph_pid(tempo_res, sinal_res, tempo, Titulo, degrau, amplitude_degrau):
    fig, ax = plt.subplots()

    ax.plot(tempo_res, sinal_res * amplitude_degrau, label= Titulo)
    ax.plot(tempo_res, degrau, label='Degrau de Entrada')
    ax.set_xlabel('Tempo (segundos)')
    ax.set_xlim([0, len(tempo) * 0.1])
    ax.set_ylabel('Saída')
    ax.set_title(Titulo)
    ax.legend(loc='lower right')

    return fig  
