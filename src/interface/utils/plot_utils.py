import matplotlib.pyplot as plt
import numpy as np

def plot_graph_1(option):
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    if option == "dataset":
        y = np.sin(x)
    else:
        y = np.cos(x)
    ax.plot(x, y)
    return fig

def plot_graph_2(values):
    k, t, c = values
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    y = k * np.exp(-t * x) + c
    ax.plot(x, y)
    return fig
