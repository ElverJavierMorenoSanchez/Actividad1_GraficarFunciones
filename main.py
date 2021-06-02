#Importamos las librerias
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')

#Sistema lineal
x = np.linspace(-15,15,1000) #Se crea el espacio que tendra el sistema lineal

#Primera Función
def f(x):
    return x**2 - x + 1
#Segunda función
def g(x):
    return 2/(x-1)

#Funcion que grafica las funciones
def graficar():

    #Codigo principal
    fig, ax = plt.subplots() #Se encarga de graficar el plano
    ax.plot(x,f(x))
    ax.plot(x,g(x))

    #### Codigo que ayuda a la estetica de la grafica final ####
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()

    ax.grid(True, linestyle = '-')

    ax.annotate("", xy = (xmax,0), xytext = (xmin,0),
            arrowprops=dict(color = 'gray', width = 1.5, headwidth = 8, headlength = 10))

    ax.annotate("", xy = (0,ymax), xytext = (0,ymin),
            arrowprops=dict(color = 'gray', width = 1.5, headwidth = 8, headlength = 10))
    ################### Fin Codigo #########################

    plt.show() #Muestra las graficas

#Mostrar Resultados
graficar()

