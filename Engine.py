import chess

fen = input("Enter a fen: ")
#fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

#depth = int(input("Depth to search: "))
depth = 4

board = chess.Board(fen)

def evaluate(board,depth):

    if board.turn == chess.BLACK and board.is_checkmate():
        return 10000 + depth
    if board.turn == chess.WHITE and board.is_checkmate():
        return -10000 - depth
    if board.is_game_over() and not board.is_checkmate():
        return 0

    eval = 0
    piece_values = {"P": 1, "N": 3, "B": 3, "R": 5, "Q": 9, "K": 0, "p": -1, "n": -3, "b": -3, "r": -5, "q": -9, "k": 0}
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            eval += piece_values[piece.symbol()]
          
    return eval

def minimax(board,depth):

    if depth == 0 or board.is_game_over():
        return evaluate(board, depth)
    
    if board.turn:
        best = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board,depth-1)
            board.pop()
            best = max(eval,best)
    
    else:
        best = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board,depth-1)
            board.pop()
            best = min(eval,best)
    
    return best

def search(board,depth):

    best_move = None

    if board.turn:
        best = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board,depth-1)
            board.pop()
            if eval > best:
                best = eval
                best_move = move

    else:
        best = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board,depth-1)
            board.pop()
            if eval < best:
                best = eval   
                best_move = move
    
    return best_move

result = search(board,depth)
print(result)
