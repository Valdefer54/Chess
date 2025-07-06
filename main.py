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

def run_chess_game(input_function=input, print_function=print):
    board = Board()
    board.set_pieces_board()
    current_player = "white"

    while True:
        board.boardPrinter()
        print_function(f"Turno del jugador: {current_player}")
        move_input = input_function(f"({current_player}) Introduce tu movimiento (ej. 'e2 e4') o escribe 'exit' para salir: ")

        if move_input.lower() == 'exit':
            print_function("Saliendo del juego.")
            break

        from_pos, to_pos = parse_move_input(move_input)

        if not from_pos or not to_pos:
            print_function("--- Movimiento inválido. Inténtalo de nuevo. ---")
            continue

        if board.move_piece(from_pos, to_pos, current_player):
            current_player = "black" if current_player == "white" else "white"
            print_function(f"Moved {board.startingBoard[to_pos[0]][to_pos[1]].name} from {from_pos} to {to_pos}")
        else:
            print_function("--- Movimiento inválido. Inténtalo de nuevo. ---")

        print_function("\n" + "="*40 + "\n")

if __name__ == "__main__":
    run_chess_game()