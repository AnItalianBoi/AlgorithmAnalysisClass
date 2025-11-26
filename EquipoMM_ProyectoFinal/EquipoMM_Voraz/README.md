# Implementación de Algoritmo Voraz Huffman

El objetivo de este programa es agregar algún algoritmo voraz al programa que se a estado llevando, el juego de damas, para esto se decidió implementar un manejo de archivos con compresión y descompresión mediante el algoritmo de **Huffman**.

# Instrucciones de Instalación

Se requiere de un intérprete de la siguiente versión para que el programa funcione correctamente:
- Python 3.13 (de preferencia)

**Instalación:**

- Clona el repositorio: 
``` python
git clone https://github.com/AnItalianBoi/AlgorithmAnalysisClass/tree/f4710a44420bf066ac07ae8f3ed5297e55c46a9c/EquipoMM_ProyectoFinal
```
- Navega al directorio del proyecto: ```cd EquipoMM_Voraz```
- Instala las dependencias: 
```pip install -r requirements.txt ```

## Ejecución

1. **Modo de ejecución:**
- Navega al directorio: ```cd EquipoMM_Voraz/src```
- Para ejecutar el script principal, usa el siguiente comando: `python main.py`

2. **Ejemplos de uso**

- Al ejecutar el programa visualizaremos el menú de selección de IA coloreadas por su dificultad:

![Ejecutar](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/7e319d7bd5bb2625053b916e1e387e7d2494808c/EquipoMM_DivideVenceras/img/1%20-%20Al%20inicializar%20el%20programa%20(selecci%C3%B3n%20de%20IA).png)

- Al seleccionar una dificultad la partida iniciará:

![Comienza el juego](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/f0681d4b0eab55439a4a68a286a980382349f101/EquipoMM_DivideVenceras/img/2%20-%20Inicia%20el%20juego.png)

-  En caso de elegir Minimax:
 el jugador siempre hará el primer movimiento a lo que la IA responderá con movimientos que considere adecuados:

![Primeros 5 movimientos | Minimax](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/f0681d4b0eab55439a4a68a286a980382349f101/EquipoMM_DivideVenceras/img/3MM%20-%20Primeros%205%20movimientos.png)

-  En caso de elegir Alpha-Beta:
 el jugador siempre hará el primer movimiento a lo que la IA responderá más rápido, con movimientos más difíciles de contrarestar:

![Primeros 5 movimientos | Alpha-Beta](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/f0681d4b0eab55439a4a68a286a980382349f101/EquipoMM_DivideVenceras/img/3AB%20-%20Primeros%205%20movimientos.png)

- Al finalizar la partida se esperan dos posibles resultados:
- - Al ganar:

![Victoria](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/f0681d4b0eab55439a4a68a286a980382349f101/EquipoMM_DivideVenceras/img/4MM%20-%20Final%20de%20la%20partida.png)

- - Al perder:

![Derrota](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/main/EquipoMM_DivideVenceras/img/4AB%20-%20Final%20de%20la%20partida.png)

- Al presionar el botón **"Ok"** se mostrará una gráfica con los tiempos de respuesta por turno de la IA, esto con fines comparativos:

- - Minimax:

![Grafica Minimax](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/6d3e448c0b6115aa1803dff486e2f3c79b00031c/EquipoMM_DivideVenceras/img/5MM%20-%20Tiempos%20de%20respuesta.jpg)

- - Alpha-Beta prunning:

![Grafica Minimax](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/5c103f5d5646901549911d62d66ccd68a70ca6c2/EquipoMM_DivideVenceras/img/5AB%20-%20Tiempos%20de%20respuesta.jpg)

#Nota: El programa se cerrará automáticamente al presionar el botón **"Ok"**
message.txt
4 KB
