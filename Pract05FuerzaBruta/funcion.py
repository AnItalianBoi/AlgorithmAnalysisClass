import math
import tkinter as tk

import random
    
def fun(p1, p2):
    x=p2[0]-p1[0]
    y=p2[1]-p1[1]
    x=pow(x,2)
    y = pow(y, 2)
    return math.sqrt(x+y)

def calcular():
    p1 = (float(p1x.get()), float(p1y.get()))
    p2 = (float(p2x.get()), float(p2y.get()))
    p3 = (float(p3x.get()), float(p3y.get()))
    p4 = (float(p4x.get()), float(p4y.get()))
    p5 = (float(p5x.get()), float(p5y.get()))
    puntos = (p1, p2, p3, p4, p5)

    menor = None
    for i in range(5):
        for j in range(5):
            if i != j:
                resultado = fun(puntos[i], puntos[j])
                if menor is None or resultado < menor:
                    menor = resultado
                    PA = puntos[i]
                    PB = puntos[j]

    if menor is not None:
        res.config(text=f"El resultado es: {menor:.4f}, en los puntos {PA} y {PB}")
    else:
        res.config(text="El resultado es: N/A")
    return menor

def limpiar():
    for entry in [p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y]:
        entry.delete(0, tk.END)
    res.config(text="El resultado es: ")

def llenar_random():
    for entry in [p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y]:
        entry.delete(0, tk.END)
        entry.insert(0, str(random.randint(0, 10)))

root = tk.Tk()
root.title("Formula Euclidiana Clase")
root.geometry("360x250")

# P1
frame_p1 = tk.Frame(root)
frame_p1.pack(pady=5)
p1 = tk.Label(frame_p1, text="P1")
p1.pack(side=tk.LEFT, padx=5)
p1x = tk.Entry(frame_p1, width=7)
p1x.pack(side=tk.LEFT, padx=2)
p1y = tk.Entry(frame_p1, width=7)
p1y.pack(side=tk.LEFT, padx=2)

# P2
frame_p2 = tk.Frame(root)
frame_p2.pack(pady=5)
p2 = tk.Label(frame_p2, text="P2")
p2.pack(side=tk.LEFT, padx=5)
p2x = tk.Entry(frame_p2, width=7)
p2x.pack(side=tk.LEFT, padx=2)
p2y = tk.Entry(frame_p2, width=7)
p2y.pack(side=tk.LEFT, padx=2)

# P3
frame_p3 = tk.Frame(root)
frame_p3.pack(pady=5)
p3 = tk.Label(frame_p3, text="P3")
p3.pack(side=tk.LEFT, padx=5)
p3x = tk.Entry(frame_p3, width=7)
p3x.pack(side=tk.LEFT, padx=2)
p3y = tk.Entry(frame_p3, width=7)
p3y.pack(side=tk.LEFT, padx=2)

# P4
frame_p4 = tk.Frame(root)
frame_p4.pack(pady=5)
p4 = tk.Label(frame_p4, text="P4")
p4.pack(side=tk.LEFT, padx=5)
p4x = tk.Entry(frame_p4, width=7)
p4x.pack(side=tk.LEFT, padx=2)
p4y = tk.Entry(frame_p4, width=7)
p4y.pack(side=tk.LEFT, padx=2)

# P5
frame_p5 = tk.Frame(root)
frame_p5.pack(pady=5)
p5 = tk.Label(frame_p5, text="P5")
p5.pack(side=tk.LEFT, padx=5)
p5x = tk.Entry(frame_p5, width=7)
p5x.pack(side=tk.LEFT, padx=2)
p5y = tk.Entry(frame_p5, width=7)
p5y.pack(side=tk.LEFT, padx=2)


# Frame para los botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=5)
tk.Button(frame_botones, text="Calcular", command=calcular).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Llenar Random", command=llenar_random).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Limpiar", command=limpiar).pack(side=tk.LEFT, padx=5)

res = tk.Label(root, text="El resultado es: ")
res.pack(pady=5)



root.mainloop()