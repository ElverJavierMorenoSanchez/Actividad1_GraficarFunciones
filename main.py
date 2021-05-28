import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')

#Sistema lineal
x = np.linspace(-15,15,1000)

def f(x):
    return x**2 - x + 1

def g(x):
    return 2/(x-1)

def graficar():

    fig, ax = plt.subplots()
    ax.plot(x,f(x))
    ax.plot(x,g(x))

    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()

    ax.grid(True, linestyle = '-')

    ax.annotate("", xy = (xmax,0), xytext = (xmin,0),
            arrowprops=dict(color = 'gray', width = 1.5, headwidth = 8, headlength = 10))

    ax.annotate("", xy = (0,ymax), xytext = (0,ymin),
            arrowprops=dict(color = 'gray', width = 1.5, headwidth = 8, headlength = 10))

    plt.show()

#Mostrar Resultados

graficar()

