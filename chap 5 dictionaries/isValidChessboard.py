# check for exactly 1 white king and 1 black king (finished)
# check for <= 16 pieces (finished)
# check for <= 8 pawns (finished)
# check for valid squares (1a to 8h) (done)
# check for valid piece names ('w' or 'b' + piece name {bishop, pawn, knight, queen, king, rook}) (done)

# return true if board meets criteria

# set of valid pieces
validPieces = {'wking', 'wqueen', 'wpawn', 'wrook', 'wbishop', 'wknight',
                'bking', 'bqueen', 'bpawn', 'brook', 'bbishop', 'bknight'}

letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}

def isValidChessBoard(board):
    wTotal = 0
    bTotal = 0

    #empty dictionary where we will count individual pieces
    pieceCount = {}

    for square, piece in board.items():

        #check if piece is valid
        if piece not in validPieces:
            return False

        #check if square is valid
        if int(square[0]) > 8 or int(square[0]) < 0:
            return False
        if square[1] not in letters:
            return False
    
        #insert new value in pieceCount with value of zero and increment by 1
        pieceCount.setdefault(piece, 0)
        pieceCount[piece] += 1

        #abort early if there are more than 16 pieces on either side
        if piece[0] == 'b':
            bTotal += 1
            if bTotal > 16:
                return False
        elif piece[0] == 'w':
            wTotal += 1
            if bTotal > 16:
                return False
    
    #check that each side doesn't have more than 8 pawns
    if 'bpawn' in pieceCount or 'wpawn' in pieceCount:
        if pieceCount['bpawn'] > 8 or pieceCount['wpawn'] > 8:
            return False
    
    #check that each side has exactly 1 king
    if 'bking' not in pieceCount or 'wking' not in pieceCount:
        return False

    if pieceCount['bking'] > 1 or pieceCount['wking'] > 1:
            return False
    
    #debugging purposes
    print(bTotal, wTotal, pieceCount)

    return True

##chessBoard = {'6c': 'bking', '8h': 'wqueen', '2g': 'bbishop', '8e': 'bqueen', '8f': 'wking'}

chessBoard = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
'5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
'5b': 'bpawn','6b': 'bpawn','7b': 'bpawn',
'1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
'5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
'5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn', '8h': 'wpawn'}

print(isValidChessBoard(chessBoard))