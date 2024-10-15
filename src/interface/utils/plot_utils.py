import matplotlib.pyplot as plt # type: ignore

def plot_dataset_graph(tempo, degrau, saida_motor, titulo):
    """
    Plots a graph for the dataset.

    Parameters:
    tempo (list or array): Time data points.
    degrau (list or array): Step input data points.
    saida_motor (list or array): Motor output data points.
    titulo (str): Title of the graph.

    Returns:
    fig: The matplotlib figure object.
    """
    fig, ax = plt.subplots()
    
    ax.plot(tempo, degrau, label="Degrau")
    ax.plot(tempo, saida_motor, label="Saída do Motor")
    ax.set_xlabel('Tempo [s]')
    ax.set_ylabel('Amplitude')
    ax.set_title(titulo)
    ax.legend()
    
    return fig

def plot_graph_open_loop(tempo_aberta, saida_aberta, tempo, degrau, titulo):
    """
    Plots a graph for the open loop response.

    Parameters:
    tempo_aberta (list or array): Time data points for open loop.
    saida_aberta (list or array): Open loop output data points.
    tempo (list or array): Time data points for step input.
    degrau (list or array): Step input data points.
    titulo (str): Title of the graph.

    Returns:
    fig: The matplotlib figure object.
    """
    fig, ax = plt.subplots()
    ax.plot(tempo_aberta, saida_aberta, label="Saída em Malha Aberta")
    ax.plot(tempo, degrau, label="Degrau de Entrada")
    ax.set_xlabel('Tempo [s]')
    ax.set_ylabel('Amplitude')
    ax.set_title(titulo)
    ax.legend()
    
    return fig

def plot_graph_closed_loop(tempo_fechada, saida_fechada, tempo, degrau, titulo):
    """
    Plots a graph for the closed loop response.

    Parameters:
    tempo_fechada (list or array): Time data points for closed loop.
    saida_fechada (list or array): Closed loop output data points.
    tempo (list or array): Time data points for step input.
    degrau (list or array): Step input data points.
    titulo (str): Title of the graph.

    Returns:
    fig: The matplotlib figure object.
    """
    fig, ax = plt.subplots()
    ax.plot(tempo_fechada, saida_fechada, label="Saída em Malha Fechada")
    ax.plot(tempo, degrau, label="Degrau de Entrada")
    ax.set_xlabel('Tempo [s]')
    ax.set_ylabel('Amplitude')
    ax.set_ylim(-1, 800)
    ax.set_title(titulo)
    ax.legend()
    
    return fig

def plot_graph_pid(tempo_res, sinal_res, tempo, Titulo, degrau):
    """
    Plots a graph for the PID controller response.

    Parameters:
    tempo_res (list or array): Time data points for PID response.
    sinal_res (list or array): PID response signal data points.
    tempo (list or array): Time data points for step input.
    Titulo (str): Title of the graph.
    degrau (list or array): Step input data points.
    amplitude_degrau (float): Amplitude of the step input.

    Returns:
    fig: The matplotlib figure object.
    """
    fig, ax = plt.subplots()

    ax.plot(tempo_res, sinal_res, label= Titulo)
    ax.plot(tempo_res, degrau, label='Degrau de Entrada')
    ax.set_xlabel('Tempo (segundos)')
    ax.set_xlim([0, len(tempo) * 0.1])
    ax.set_ylabel('Saída')
    ax.set_title(Titulo)
    ax.legend(loc='lower right')

    return fig  
