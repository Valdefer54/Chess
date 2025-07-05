from board import Board

def algebraic_to_coords(notation):
    """
    Convierte la notación algebraica de ajedrez (ej. 'e4') a coordenadas del tablero (ej. (4, 4)).
    """
    try:
        file = notation[0].lower()
        rank = notation[1]
        if file not in 'abcdefgh' or not rank.isdigit() or not '1' <= rank <= '8':
            return None
        col = 'abcdefgh'.index(file)
        row = 8 - int(rank)
        return (row, col)
    except (IndexError, TypeError):
        return None

def parse_move_input(move_input):
    """
    Analiza la entrada del usuario (ej. "e2 e4") y la convierte en coordenadas de origen y destino.
    """
    try:
        parts = move_input.strip().split()
        if len(parts) != 2:
            return None, None
        from_notation, to_notation = parts
        from_pos = algebraic_to_coords(from_notation)
        to_pos = algebraic_to_coords(to_notation)
        return from_pos, to_pos
    except Exception:
        return None, None

if __name__ == "__main__":
    board = Board()
    board.set_pieces_board()
    current_player = "white"

    while True:
        board.boardPrinter()
        print(f"Turno del jugador: {current_player}")
        move_input = input(f"({current_player}) Introduce tu movimiento (ej. 'e2 e4') o escribe 'exit' para salir: ")

        if move_input.lower() == 'exit':
            print("Saliendo del juego.")
            break

        from_pos, to_pos = parse_move_input(move_input)

        if not from_pos or not to_pos:
            print("--- Formato de movimiento inválido. Usa notación algebraica (ej. 'e2 e4'). ---")
            continue

        # Validación 1: ¿Hay una pieza en la casilla de origen?
        piece = board.startingBoard[from_pos[0]][from_pos[1]]
        if not piece:
            print(f"--- No hay ninguna pieza en la casilla {move_input.split()[0]}. ---")
            continue

        # Validación 2: ¿La pieza pertenece al jugador actual?
        if piece.color != current_player:
            print(f"--- La pieza en {move_input.split()[0]} no es tuya. ---")
            continue

        # Validación 3 y movimiento: El método move_piece ya valida y ejecuta.
        if board.move_piece(from_pos, to_pos):
            # Si el movimiento fue exitoso, cambia de jugador.
            current_player = "black" if current_player == "white" else "white"
        else:
            # El método move_piece ya imprime el error específico.
            print("--- Inténtalo de nuevo. ---")

        print("\n" + "="*40 + "\n")