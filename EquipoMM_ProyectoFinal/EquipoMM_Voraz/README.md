# Proyecto final

Programa con finalidad de implementar si (si es posible) la mayoría de los algoritmos y métodos contemplados en clase, este caso se aplican los siguientes:

- Minimax
- Alpha-Beta Prunning (Divide y Vencerás)
- Codificación de Huffman (Algoritmos Voracez)
- Backtracking (por parte de minimax y Alpha-Beta Prunning)
- Ramificación (por parte de minimax y Alpha-Beta Prunning)
- Poda (por parte de Alpha-Beta Prunning) 

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

- Al ejecutar el programa visualizaremos el menú de selección de IA coloreadas por su dificultad y una para reproducir los replays:

![Ejecutar](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/ce184b51896d31c478e37a74b863973fb19064b1/EquipoMM_ProyectoFinal/EquipoMM_Voraz/img/1%20-%20Al%20inicializar%20el%20programa%20(selecci%C3%B3n%20de%20IA).png)

- Al seleccionar una dificultad la partida iniciará:

![Comienza el juego](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/5c135aed63ee882e7c86bf1aac9db503957df805/EquipoMM_ProyectoFinal/EquipoMM_Voraz/img/2%20-%20Inicia%20el%20juego.png)

-  En caso de elegir Minimax:
 el jugador siempre hará el primer movimiento a lo que la IA responderá con movimientos que considere adecuados:

![Primeros 5 movimientos | Minimax](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/5c135aed63ee882e7c86bf1aac9db503957df805/EquipoMM_ProyectoFinal/EquipoMM_Voraz/img/3MM%20-%20Primeros%205%20movimientos.png)

-  En caso de elegir Alpha-Beta:
 el jugador siempre hará el primer movimiento a lo que la IA responderá más rápido, con movimientos más difíciles de contrarestar:

![Primeros 5 movimientos | Alpha-Beta](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/5c135aed63ee882e7c86bf1aac9db503957df805/EquipoMM_ProyectoFinal/EquipoMM_Voraz/img/3AB%20-%20Primeros%205%20movimientos.png)

- Al finalizar la partida se esperan dos posibles resultados:
- - Al ganar:

![Victoria](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/5c135aed63ee882e7c86bf1aac9db503957df805/EquipoMM_ProyectoFinal/EquipoMM_Voraz/img/4MM%20-%20Final%20de%20la%20partida.png)

- - Al perder:

![Derrota](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/5c135aed63ee882e7c86bf1aac9db503957df805/EquipoMM_ProyectoFinal/EquipoMM_Voraz/img/4AB%20-%20Final%20de%20la%20partida.png)

- Al presionar el botón **"Ok"** se mostrará una gráfica con los tiempos de respuesta por turno de la IA, esto con fines comparativos:

- - Minimax:

![Grafica Minimax](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/5c135aed63ee882e7c86bf1aac9db503957df805/EquipoMM_ProyectoFinal/EquipoMM_Voraz/img/5MM%20-%20Tiempos%20de%20respuesta.jpg)

- - Alpha-Beta prunning:

![Grafica Alpha-Beta](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/5c135aed63ee882e7c86bf1aac9db503957df805/EquipoMM_ProyectoFinal/EquipoMM_Voraz/img/5AB%20-%20Tiempos%20de%20respuesta.jpg)

- En caso de precionar el botón "Reproducir", se abrirá el explorador de archivos permitiendo elegir entre guardados .txt y .bin, ambos cargaran la partida de igual forma, existen dos versiones para demostrar el funcionamiento de la compresión y descompresión de archivos por parte de la codifcación de huffman

![Selección de guardado](https://github.com/AnItalianBoi/AlgorithmAnalysisClass/blob/5c135aed63ee882e7c86bf1aac9db503957df805/EquipoMM_ProyectoFinal/EquipoMM_Voraz/img/5%20-%20Selecci%C3%B3n%20de%20replay.png)

Luego de selccionar el archivo de guardado, comenzará a reproducir la partida con los movimientos registrados del jugador como de la IA contenidos en el archivo .txt o .bin y al terminar serán devueltos al menú principal.

#Nota: El programa se cerrará automáticamente al presionar el botón **"Ok"** en caso de haber jugado

#Nota2: El programa se tendrá que cerrar manualmente con el botón **"X"** situado arriba a la derecha en caso de haber jugado un replay
