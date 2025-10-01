import tkinter as tk
import random
import time

LISTA = []
VAL_MIN = 1
VAL_MAX = 10000
TAMLISTA = 0

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i, j = 0, 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado += izquierda[i:]
    resultado += derecha[j:]
    return resultado

def generar():
    global LISTA, TAMLISTA
    try:
        TAMLISTA = int(entrada.get())
    except ValueError:
        TAMLISTA = 10  # valor por defecto
    random.seed(time.time())
    LISTA = [random.randint(VAL_MIN, VAL_MAX) for _ in range(TAMLISTA)]
    lblInfo.config(text=f"Lista creada con {TAMLISTA} elementos")
    txtSalida.delete("1.0", tk.END)
    txtSalida.insert(tk.END, f"Lista generada:\n{LISTA}\n")

def ordenar():
    global LISTA
    LISTA = merge_sort(LISTA)
    lblInfo.config(text="Lista ordenada con MergeSort")
    txtSalida.insert(tk.END, f"\nLista ordenada:\n{LISTA}\n")

# GUI
root = tk.Tk()
root.title("Visualizador sencillo - MergeSort")

panel = tk.Frame(root)
panel.pack(pady=6)

tk.Label(panel, text="Tamaño de la lista").pack(padx=5, side="left")
entrada = tk.Entry(panel, bg="light goldenrod")
entrada.pack(padx=5, side="left")
lblInfo = tk.Label(panel, text="")
lblInfo.pack(padx=5, side="left")

tk.Button(panel, text="Crear lista", command=generar).pack(side="left", padx=5)
tk.Button(panel, text="Ordenar (MergeSort)", command=ordenar).pack(side="left", padx=5)

# Cuadro de salida de texto
txtSalida = tk.Text(root, width=120, height=20, bg="white")
txtSalida.pack(padx=10, pady=10)

root.mainloop()