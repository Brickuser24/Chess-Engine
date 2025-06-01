import chess

fen = input("Enter a fen: ")
#fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

#depth = int(input("Depth to search: "))
depth = 4

board = chess.Board(fen)

def order_moves(board):
    promotions = []
    captures = []
    checks = []
    regular = []

    for move in board.legal_moves:
        if move.promotion:
            promotions.append(move)
        elif board.is_capture(move):
            captures.append(move)
        elif board.gives_check(move):
            checks.append(move)
        else:
            regular.append(move)

    return promotions + captures + checks + regular

def evaluate(board,depth):

    if board.turn == chess.BLACK and board.is_checkmate():
        return 10000 + depth
    if board.turn == chess.WHITE and board.is_checkmate():
        return -10000 - depth
    if board.is_game_over() and not board.is_checkmate():
        return 0

    eval = 0
    piece_values = {"P": 1, "N": 3, "B": 3, "R": 5, "Q": 9, "K": 0, "p": -1, "n": -3, "b": -3, "r": -5, "q": -9, "k": 0}
    for square in board.piece_map():
        piece = board.piece_at(square)
        if piece:
            eval += piece_values[piece.symbol()]
    return eval

def minimax(board,depth,alpha,beta):

    if depth == 0 or board.is_game_over():
        return evaluate(board, depth)
    
    if board.turn:
        best = float('-inf')
        for move in order_moves(board):
            board.push(move)
            eval = minimax(board,depth-1,alpha,beta)
            board.pop()
            best = max(eval,best)
            alpha = max(alpha,eval)
            if beta <= alpha:
                break
    
    else:
        best = float('inf')
        for move in order_moves(board):
            board.push(move)
            eval = minimax(board,depth-1,alpha,beta)
            board.pop()
            best = min(eval,best)
            beta = min(beta, eval)
            if beta <= alpha:
                break
    
    return best

def search(board,depth):

    best_move = None
    alpha = float('-inf')
    beta = float('inf')

    if board.turn:
        best = float('-inf')
        for move in order_moves(board):
            board.push(move)
            eval = minimax(board,depth-1,alpha,beta)
            board.pop()
            if eval > best:
                best = eval
                best_move = move
            alpha = max(alpha, eval)

    else:
        best = float('inf')
        for move in order_moves(board):
            board.push(move)
            eval = minimax(board,depth-1,alpha,beta)
            board.pop()
            if eval < best:
                best = eval   
                best_move = move
            beta = min(beta, eval)
    
    return best_move

result = search(board,depth)
print(result)
