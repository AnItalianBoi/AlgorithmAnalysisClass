import tkinter as tk
from tkinter import messagebox

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def quick_sort(arr):
    if len(arr)<=1:
        return arr

    pivot = arr[len(arr)//2]

    left = [x for x in arr if x<pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print(f"Left: {left} Middle: {middle} Right: {right}")
    return quick_sort(left)+middle+quick_sort(right)

# --- Función que se llama al presionar el botón ---

def mostrar_grafico(original, ordenado):
    fig = Figure(figsize=(6, 3), dpi=100)

    # Subgráficos: antes y después
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    # Gráfico de barras original
    ax1.bar(range(len(original)), original, color='skyblue')
    ax1.set_title("Antes")
    ax1.set_xticks([])

    # Gráfico de barras ordenado
    ax2.bar(range(len(ordenado)), ordenado, color='lightgreen')
    ax2.set_title("Después")
    ax2.set_xticks([])

    # Dibujar en el canvas de tkinter
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

def ordenar():
    entrada = entrada_txt.get()
    try:
        # Convertimos la entrada en una lista de enteros
        numeros = list(map(int, entrada.split(',')))
        ordenado = quick_sort(numeros)
        resultado_lbl.config(text="Arreglo ordenado: " + str(ordenado))
        mostrar_grafico(numeros, ordenado)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números separados por comas.")

# --- Interfaz gráfica ---
ventana = tk.Tk()
ventana.title("Quick Sort con Gráfica")
ventana.geometry("700x500")

instruccion_lbl = tk.Label(ventana, text="Ingresa números separados por comas:")
instruccion_lbl.pack(pady=5)

entrada_txt = tk.Entry(ventana, width=50)
entrada_txt.pack(pady=5)

ordenar_btn = tk.Button(ventana, text="Ordenar", command=ordenar)
ordenar_btn.pack(pady=10)

resultado_lbl = tk.Label(ventana, text="")
resultado_lbl.pack(pady=5)

ventana.mainloop()