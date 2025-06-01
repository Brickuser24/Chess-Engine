import chess
import Engine

board = chess.Board()
depth = 4

while True:
    color = input("Will I play as White or Black?\n")
    if color == "White" or color == "Black":
        break
    print("Invalid Choice")
    print()

print()

if color == "White":
    while not board.is_game_over():

        #Engine's Move
        move = Engine.search(board,depth)
        print("I play", board.san(move))
        board.push(move)

        if board.is_game_over():
            break

        #Player's Move
        while True:
            move = input("Your move?\n")
            print()
            try:
                board.push_san(move)
                break
            except:
                print("Invalid Move Input") 
                print()

else:
    while not board.is_game_over():

        #Player's Move
        while True:
            move = input("Your move?\n")
            print()
            try:
                board.push_san(move)
                break
            except:
                print("Invalid Move Input") 
                print()
        
        if board.is_game_over():
            break
        
        #Engine's Move
        move = Engine.search(board,depth)
        print("I play", board.san(move))
        board.push(move)

print()
print(board.result())
print()
print("Good Game")
