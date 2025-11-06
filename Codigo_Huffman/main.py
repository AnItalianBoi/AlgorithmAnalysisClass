import tkinter as tk
from tkinter import filedialog, messagebox
from bitarray import bitarray
import os, pickle, struct
from collections import Counter
import heapq
class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol(frecuencias):
    heap = [NodoHuffman(c, f) for c, f in frecuencias.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        combinado = NodoHuffman(None, n1.frecuencia + n2.frecuencia)
        combinado.izquierda = n1
        combinado.derecha = n2
        heapq.heappush(heap, combinado)
    return heap[0]

def generar_codigos(nodo, codigo=None, codigos=None):
    if codigos is None:
        codigos = {}
    if codigo is None:
        codigo = bitarray()
    if nodo.caracter is not None:
        codigos[nodo.caracter] = codigo.copy()
    else:
        generar_codigos(nodo.izquierda, codigo + bitarray('0'), codigos)
        generar_codigos(nodo.derecha, codigo + bitarray('1'), codigos)
    return codigos

def codificar(texto, codigos):
    resultado = bitarray()
    for c in texto:
        resultado.extend(codigos[c])
    return resultado

def decodificar(codigo_binario, arbol):
    resultado = []
    nodo = arbol
    for bit in codigo_binario:
        nodo = nodo.izquierda if not bit else nodo.derecha
        if nodo.caracter is not None:
            resultado.append(nodo.caracter)
            nodo = arbol
    return ''.join(resultado)


# Guardar archivo único
def guardar_comprimido(ruta, arbol, bits):
    arbol_serializado = pickle.dumps(arbol)
    with open(ruta, 'wb') as f:
        f.write(struct.pack('I', len(arbol_serializado)))
        f.write(arbol_serializado)
        bits.tofile(f)

def cargar_comprimido(ruta):
    with open(ruta, 'rb') as f:
        tam_arbol = struct.unpack('I', f.read(4))[0]
        arbol = pickle.loads(f.read(tam_arbol))
        bits = bitarray()
        bits.fromfile(f)
    return arbol, bits

# GUI
class HuffmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Compresor Huffman")
        self.archivo = ""
        self.texto = ""

        # Botones
        tk.Button(root, text="📂 Elegir archivo", command=self.elegir_archivo).pack()
        tk.Button(root, text="🗜️ Comprimir", command=self.comprimir).pack()
        tk.Button(root, text="🔁 Descomprimir", command=self.descomprimir).pack()

        # Vista de contenido
        self.vista = tk.Text(root, height=15, width=60)
        self.vista.pack()

        # Vista de tamano
        self.tamano = tk.Label(root, text="Tamaño: ")
        self.tamano.pack()

    def elegir_archivo(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if ruta:
            self.archivo = ruta
            with open(ruta, 'r', encoding='utf-8') as f:
                self.texto = f.read()
            self.vista.delete(1.0, tk.END)
            self.vista.insert(tk.END, self.texto)
            self.tamano.config(text=f"Tamaño original: {os.path.getsize(ruta)} bytes")

    def comprimir(self):
        if not self.texto:
            messagebox.showerror("Error", "No hay texto cargado.")
            return
        frecuencias = Counter(self.texto)
        arbol = construir_arbol(frecuencias)
        codigos = generar_codigos(arbol)
        bits = codificar(self.texto, codigos)
        guardar_comprimido("archivo.huff", arbol, bits)
        self.tamano.config(text=f"Comprimido: {os.path.getsize('archivo.huff')} bytes")
        messagebox.showinfo("Listo", "Archivo comprimido como 'archivo.huff'.")

    def descomprimir(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivo Huffman", "*.huff")])
        if ruta:
            arbol, bits = cargar_comprimido(ruta)
            texto = decodificar(bits, arbol)
            self.vista.delete(1.0, tk.END)
            self.vista.insert(tk.END, texto)
            self.tamano.config(text=f"Descomprimido: {len(texto.encode('utf-8'))} bytes")

#Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    app = HuffmanGUI(root)
    root.mainloop()
