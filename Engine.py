import chess
import chess.polyglot

reader = chess.polyglot.open_reader("komodo.bin")
book_moves = True

Checkmate_Score = 10000

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

def evaluate(board):
    
    eval = 0
    piece_values = {"P": 1, "N": 3, "B": 3, "R": 5, "Q": 9, "K": 0, "p": -1, "n": -3, "b": -3, "r": -5, "q": -9, "k": 0}
    for square in board.piece_map():
        piece = board.piece_at(square)
        if piece:
            eval += piece_values[piece.symbol()]

    if board.turn:
        return eval
    else:
        return -eval

def negamax(board, depth, alpha, beta):

    if board.is_game_over(claim_draw = True):
        if board.is_checkmate():
            return -Checkmate_Score - depth
        else:
            return 0

    if depth == 0:
        return evaluate(board)
    
    max_eval = float('-inf')
    
    for move in order_moves(board):
        board.push(move)
        eval = -negamax(board, depth - 1, -beta, -alpha)
        board.pop()
        
        max_eval = max(max_eval, eval)
        alpha = max(alpha, eval)
        
        if beta <= alpha:
            break
            
    return max_eval

def search(board, depth):

    global book_moves
    if book_moves:
        try:
            book_move = reader.weighted_choice(board)
            return book_move.move
        except:
            book_moves = False
            reader.close()

    best_move = None
    max_eval = float('-inf')
    alpha = float('-inf')
    beta = float('inf')

    for move in order_moves(board):
        board.push(move)
        eval = -negamax(board, depth - 1, -beta, -alpha)
        board.pop()

        if eval > max_eval:
            max_eval = eval
            best_move = move
        
        alpha = max(alpha, eval)

    return best_move
