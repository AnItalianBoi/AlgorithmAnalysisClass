import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random as rd
import time

array = []
# Tiempos y pruebas para búsqueda lineal
avarageTimeL = [0, 0, 0, 0]
numberOfTriesL = [0, 0, 0, 0]
# Tiempos y pruebas para búsqueda binaria
avarageTimeB = [0, 0, 0, 0]
numberOfTriesB = [0, 0, 0, 0]

def generateRandInt():
    return rd.randint(0, 100000)

def generateArray(n):
    global array
    array = [generateRandInt() for _ in range(n)]
    lbl.config(text=f"Array Size: {len(array)}")
    array.sort()
    print(array, "Array generado y ordenado", len(array), "elementos")

def arraySize():
    if radioVar.get() == 1:
        return 100
    elif radioVar.get() == 2:
        return 1000
    elif radioVar.get() == 3:
        return 10000
    elif radioVar.get() == 4:
        return 100000
    else:
        return 0

def linealSearch(arr, target):
    start = time.perf_counter()
    index = -1
    for i in range(len(arr)):
        if arr[i] == target:
            index = i
            break
    end = time.perf_counter()
    elapsed_time = end - start

    idx = radioVar.get() - 1

    if index == -1:
        messagebox.showwarning("Advertencia", f"No se encontro el numero:{target}")
    else:
        messagebox.showinfo("Resultado", f"Numero encontrado en el indice: {index}")
        lblE.config(text=f"Entrada (Numero a buscar): \nNumero encontrado en el indice: {index}")
        numberOfTriesL[idx] += 1
        avarageTimeL[idx] += elapsed_time / numberOfTriesL[idx]
        updateResults()
        actualizarGrafica()

def binarySearch(arr, target):
    index = -1
    left = 0
    right = len(arr) - 1
    start = time.perf_counter()
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            index = mid
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    end = time.perf_counter()
    elapsed_time = end - start

    idx = radioVar.get() - 1
    

    if index == -1:
        messagebox.showwarning("Advertencia", f"No se encontro el numero:{target}")
    else:
        messagebox.showinfo("Resultado", f"Numero encontrado en el indice: {index}")
        lblE.config(text=f"Entrada (Numero a buscar): \nNumero encontrado en el indice: {index}")
        numberOfTriesB[idx] += 1
        avarageTimeB[idx] += elapsed_time / numberOfTriesB[idx]
        updateResults()
        actualizarGrafica()
    
def getInt():
    try:
        num = int(entrada.get())
        if num < 0:
            messagebox.showerror("Error", "Por favor ingresa un número entero positivo.")
            return None
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número entero positivo.")
        return None
    return num

def updateResults():
    # Lineal
    lblR100L.config(text=f"100: {avarageTimeL[0]*1000:.3f} ms, {numberOfTriesL[0]} pruebas")
    lblR1000L.config(text=f"1,000: {avarageTimeL[1]*1000:.3f} ms, {numberOfTriesL[1]} pruebas")
    lblR10000L.config(text=f"10,000: {avarageTimeL[2]*1000:.3f} ms, {numberOfTriesL[2]} pruebas")
    lblR100000L.config(text=f"100,000: {avarageTimeL[3]*1000:.3f} ms, {numberOfTriesL[3]} pruebas")
    # Binaria
    lblR100B.config(text=f"100: {avarageTimeB[0]*1000:.3f} ms, {numberOfTriesB[0]} pruebas")
    lblR1000B.config(text=f"1,000: {avarageTimeB[1]*1000:.3f} ms, {numberOfTriesB[1]} pruebas")
    lblR10000B.config(text=f"10,000: {avarageTimeB[2]*1000:.3f} ms, {numberOfTriesB[2]} pruebas")
    lblR100000B.config(text=f"100,000: {avarageTimeB[3]*1000:.3f} ms, {numberOfTriesB[3]} pruebas")

def actualizarGrafica():
    ax.clear()
    x = ["100", "1000", "10000", "100000"]
    # Multiplica los tiempos por 1000 para mostrar en ms
    ax.bar([i - 0.2 for i in range(4)], [t*1000 for t in avarageTimeL], width=0.4, label="Lineal", color='blue')
    ax.bar([i + 0.2 for i in range(4)], [t*1000 for t in avarageTimeB], width=0.4, label="Binaria", color='orange')
    ax.set_xticks(range(4))
    ax.set_xticklabels(x)
    ax.set_xlabel('Tamaño del Array')
    ax.set_ylabel('Tiempo Promedio (ms)')
    ax.set_title('Tiempo Promedio de Búsqueda')
    ax.legend()
    canvas.draw()

def checkEntry(*args):
    if entrada.get().isdigit():
        btnBL.config(state=tk.NORMAL)
        btnBB.config(state=tk.NORMAL)
    else:
        btnBL.config(state=tk.DISABLED)
        btnBB.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Practica 1 - Busqueda")
root.geometry("900x700")

frameTop = tk.Frame(root)
frameTop.pack(side=tk.TOP, fill=tk.X)

fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(["100", "1,000", "10,000", "100,000"], avarageTimeL, color='blue', label="Lineal")
ax.bar(["100", "1,000", "10,000", "100,000"], avarageTimeB, color='orange', label="Binaria")
ax.set_xlabel('Tamaño del Array')
ax.set_ylabel('Tiempo Promedio (s)')
ax.set_title('Tiempo Promedio de Búsqueda')
ax.legend()

canvas = FigureCanvasTkAgg(fig, master=frameTop)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

frameBottom = tk.Frame(root)
frameBottom.pack(side=tk.BOTTOM, fill=tk.X)

for i in range(5):
    frameBottom.grid_columnconfigure(i, minsize=50)
    frameBottom.grid_rowconfigure(i, minsize=50)

radioVar = tk.IntVar()
radioVar.set(1)
rb1 = tk.Radiobutton(frameBottom, text="100", variable=radioVar, value=1)
rb1.grid(row=0, column=1)
rb2 = tk.Radiobutton(frameBottom, text="1,000", variable=radioVar, value=2)
rb2.grid(row=1, column=1)
rb3 = tk.Radiobutton(frameBottom, text="10,000", variable=radioVar, value=3)
rb3.grid(row=2, column=1)
rb4 = tk.Radiobutton(frameBottom, text="100,000", variable=radioVar, value=4)
rb4.grid(row=3, column=1)

lbl = tk.Label(frameBottom, text="Array Size: ")
lbl.grid(row=0, column=2, padx=10, pady=10)

btn = tk.Button(frameBottom, text="Generar lista", command= lambda: generateArray(arraySize()))
btn.grid(row=1, column=2, padx=10, pady=10)

lblE = tk.Label(frameBottom, text="Entrada (Numero a buscar): ")
lblE.grid(row=0, column=3, padx=10, pady=10)

entrada = tk.Entry(frameBottom)
entrada.grid(row=1, column=3, padx=10, pady=10)
entrada.bind("<KeyRelease>", checkEntry)

btnBL = tk.Button(frameBottom, text="Busqueda Lineal", command=lambda: linealSearch(array, getInt()), state=tk.DISABLED)
btnBL.grid(row=2, column=3, padx=10, pady=10)

btnBB = tk.Button(frameBottom, text="Busqueda Binaria", command=lambda: binarySearch(array, getInt()), state=tk.DISABLED)
btnBB.grid(row=3, column=3, padx=10, pady=10)

# Labels para resultados de búsqueda lineal
lblZR_L = tk.Label(frameBottom, text="Resultados Lineal\n(Tiempo promedio)")
lblZR_L.grid(row=0, column=4, padx=10, pady=10)
lblR100L = tk.Label(frameBottom, text=f"100: {avarageTimeL[0]*1000:.3f} s, {numberOfTriesL[0]} pruebas")
lblR100L.grid(row=1, column=4, padx=10, pady=10)
lblR1000L = tk.Label(frameBottom, text=f"1,000: {avarageTimeL[1]*1000:.3f} s, {numberOfTriesL[1]} pruebas")
lblR1000L.grid(row=2, column=4, padx=10, pady=10)
lblR10000L = tk.Label(frameBottom, text=f"10,000: {avarageTimeL[2]*1000:.3f} s, {numberOfTriesL[2]} pruebas")
lblR10000L.grid(row=3, column=4, padx=10, pady=10)
lblR100000L = tk.Label(frameBottom, text=f"100,000: {avarageTimeL[3]*1000:.3f} s, {numberOfTriesL[3]} pruebas")
lblR100000L.grid(row=4, column=4, padx=10, pady=10)

# Labels para resultados de búsqueda binaria
lblZR_B = tk.Label(frameBottom, text="Resultados Binaria\n(Tiempo promedio)")
lblZR_B.grid(row=0, column=5, padx=10, pady=10)
lblR100B = tk.Label(frameBottom, text=f"100: {avarageTimeB[0]*1000:.3f} s, {numberOfTriesB[0]} pruebas")
lblR100B.grid(row=1, column=5, padx=10, pady=10)
lblR1000B = tk.Label(frameBottom, text=f"1,000: {avarageTimeB[1]*1000:.3f} s, {numberOfTriesB[1]} pruebas")
lblR1000B.grid(row=2, column=5, padx=10, pady=10)
lblR10000B = tk.Label(frameBottom, text=f"10,000: {avarageTimeB[2]*1000:.3f} s, {numberOfTriesB[2]} pruebas")
lblR10000B.grid(row=3, column=5, padx=10, pady=10)
lblR100000B = tk.Label(frameBottom, text=f"100,000: {avarageTimeB[3]*1000:.3f} s, {numberOfTriesB[3]} pruebas")
lblR100000B.grid(row=4, column=5, padx=10, pady=10)

root.mainloop()