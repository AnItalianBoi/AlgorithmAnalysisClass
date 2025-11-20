# Visualizador de Tecnica Voraz

El objetivo de esta actividad, es programar los algoritmos voraces de Prim y Kruskal en python, para poder observar y entender de mejor manera su funcionamiento, utilizando un grafo ya definido obtenido de la primer pagina de: https://es.scribd.com/document/403078422/Algoritmo-PRIM.

![Grafo](https://estrucuturas2unincca.wordpress.com/wp-content/uploads/2018/11/imagen8.png?w=556&h=232)

# Instrucciones de Instalación

Se requiere de un intérprete de la siguiente versión para que el programa funcione correctamente:

**Instalación:**

- Clona el repositorio: 
``` python
git clone https://github.com/NicodobleG/25B-An-lisis-de-Algoritmos---D01---L_Mi-7-9am/tree/9c111004e9363f10c6a1028de764b46bafb47991/EquipoMM_C%C3%B3digo%20Huffman
```
- Navega al directorio del proyecto: ```cd EquipoMM_Código Huffman```
- Instala las dependencias: 
```pip install -r requirements.txt ```

## Ejecución

1. **Modo de ejecución:**
- Navega al directorio: ```cd EquipoMM_Código Huffman/src```
- Para ejecutar el script principal, usa el siguiente comando: `python main.py`

2. **Instrucciones de uso**

- Al ejecutar el programa visualizaremos una ventana que contiene el grafo a tratar, dos botones y un campos:

![Ejecutar](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/827e1214db10da3c988ed487292607b016b21daa/EquipoMM_PrimKruskal/EquipoMM_PrimKruskal1.png)

- Para ejecutar el algoritmo de Prim, se deberá seleccionar un nodo inicial válido, siendo este alguno de los mostrados en el grafo, después el botón verde claro dice "Ejecutar":

![Prim usado](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/827e1214db10da3c988ed487292607b016b21daa/EquipoMM_PrimKruskal/EquipoMM_PrimKruskal2.png)

-  Para ejecutar el algoritmo de Kruskal, solo deberá presionar el botón azil claro que dice "Ejecutar":

![Kruska](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/827e1214db10da3c988ed487292607b016b21daa/EquipoMM_PrimKruskal/EquipoMM_PrimKruskal3.png)

Como podemos observar, al menos del lado de Prim usado el nodo inicial "0", los resultadoos son prácticamente los mismos, diferentes metodologías fueron usadas, obervamos que obtiene un árbol de expansión mínima igual, esto cambia si se elige otro nodo inicial, pero el peso total no se altera, al menos en este caso.

- Una vez se termine de usar el program, se puede finalizar presionando el botón "X" situado en la parte superior derecha de la ventana.
