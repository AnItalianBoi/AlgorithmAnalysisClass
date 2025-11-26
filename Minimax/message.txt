import tkinter as tk
import math

# ---------------------------
# Lógica del juego
# ---------------------------

board = [" " for _ in range(9)]  # tablero lineal
buttons = []  # referencia a botones para actualizarlos

def winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columnas
        [0, 4, 8], [2, 4, 6]              # diagonales
    ]
    for combo in win_conditions:
        if all(board[i] == player for i in combo):
            return True
    return False

def empty_squares(board):
    return " " in board

def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == " "]

def minimax(board, depth, is_maximizing):
    if winner(board, "O"):
        return 1
    elif winner(board, "X"):
        return -1
    elif not empty_squares(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = "O"
            score = minimax(board, depth + 1, False)
            board[move] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = "X"
            score = minimax(board, depth + 1, True)
            board[move] = " "
            best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in available_moves(board):
        board[i] = "O"
        score = minimax(board, 0, False)
        board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    return move

# ---------------------------
# Interfaz gráfica
# ---------------------------

def handle_click(index):
    if board[index] == " " and not winner(board, "X") and not winner(board, "O"):
        board[index] = "X"
        buttons[index].config(text="X", state="disabled")

        if winner(board, "X"):
            status_label.config(text="¡Ganaste! 🎉")
            disable_all()
            return
        elif not empty_squares(board):
            status_label.config(text="Empate 🤝")
            disable_all()
            return

        # turno computadora
        move = best_move(board)
        board[move] = "O"
        buttons[move].config(text="O", state="disabled")

        if winner(board, "O"):
            status_label.config(text="La computadora gana 😎")
            disable_all()
        elif not empty_squares(board):
            status_label.config(text="Empate 🤝")
            disable_all()

def disable_all():
    for b in buttons:
        b.config(state="disabled")

def reset_game():
    global board
    board = [" " for _ in range(9)]
    for b in buttons:
        b.config(text=" ", state="normal")
    status_label.config(text="Tu turno (X)")

# ---------------------------
# Construcción de la ventana
# ---------------------------

root = tk.Tk()
root.title("Tic-Tac-Toe con Minimax")

frame = tk.Frame(root)
frame.pack()

for i in range(9):
    b = tk.Button(frame, text=" ", font=("Arial", 24), width=5, height=2,
                  command=lambda i=i: handle_click(i))
    b.grid(row=i//3, column=i%3)
    buttons.append(b)

status_label = tk.Label(root, text="Tu turno (X)", font=("Arial", 14))
status_label.pack(pady=10)

reset_button = tk.Button(root, text="Reiniciar", command=reset_game, font=("Arial", 12))
reset_button.pack()

root.mainloop()