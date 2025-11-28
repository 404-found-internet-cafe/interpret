BOARD = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]

def place_symbol(sym, posx, posy):
    cell_is_populated = BOARD[posy][posx] != ""

    if cell_is_populated:
        raise BaseException("Cell already has a symbol in it")
    else:
        BOARD[posy][posx] = sym

