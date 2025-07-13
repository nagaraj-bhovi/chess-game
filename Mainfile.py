#Chess Game implemetation using Python:
import pygame
import os
pygame.init()
WIDTH = 900
HEIGHT = 700
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two Player pygame Chess')
font = pygame.font.Font('freesansbold.ttf', 10)
#font = pygame.font.Font('None', 20)
big_font = pygame.font.Font('freesansbold.ttf', 20)
timer = pygame.time.Clock()
fps = 60 

#Game variables ad Images:
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_location = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                  (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_location = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                  (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]

captured_pieces_white = []
captured_pieces_black = []
# 0 - white turn no selection: 1- white tunr piece selection: 2 - black turn no slection, 3 - black turn piece selected
turn_step = 0
selection = 100 
valid_moves = []

small_piece = 50
Bigg_piece = 60

#load in game piece images(queen, king, rook, bishop, knight, pawn)
black_queen = pygame.image.load ('D:/Nagaraj_Python_codes/Chess_Implemetation/Images/black_queen.png')
black_queen = pygame.transform.scale(black_queen, (60, 60))
black_queen_small = pygame.transform.scale(black_queen, (small_piece, small_piece))
black_king = pygame.image.load ('D:/Nagaraj_Python_codes/Chess_Implemetation/Images/black_king.png')
black_king = pygame.transform.scale(black_king, (30, 30))
black_king_small = pygame.transform.scale(black_king, (small_piece, small_piece))
black_rook = pygame.image.load ('D:/Nagaraj_Python_codes/Chess_Implemetation/Images/black_rook.png')
black_rook = pygame.transform.scale(black_rook, (60, 60))
black_rook_small = pygame.transform.scale(black_rook, (small_piece, small_piece))
black_bishop = pygame.image.load ('D:/Nagaraj_Python_codes/Chess_Implemetation/Images/black_bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (60, 60))
black_bishop_small = pygame.transform.scale(black_bishop, (small_piece, small_piece))
black_knight = pygame.image.load ('D:/Nagaraj_Python_codes/Chess_Implemetation/Images/black_knight.png')
black_knight = pygame.transform.scale(black_knight, (60, 60))
black_knight_small = pygame.transform.scale(black_knight, (small_piece, small_piece))
black_pawn = pygame.image.load ('D:/Nagaraj_Python_codes/Chess_Implemetation/Images/black_pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (55, 55))
black_pawn_small = pygame.transform.scale(black_pawn, (25, 25))

white_queen = pygame.image.load ('D:/Nagaraj_Python_codes/Chess_Implemetation/Images/white_queen.png')
white_queen = pygame.transform.scale(white_queen, (60, 60))
white_queen_small = pygame.transform.scale(white_queen, (small_piece, small_piece))
white_king = pygame.image.load ('D:/Nagaraj_Python_codes/Chess_Implemetation/Images/white_king.png')
white_king = pygame.transform.scale(white_king, (60, 60))
white_king_small = pygame.transform.scale(white_king, (small_piece, small_piece))
white_rook = pygame.image.load ('D:/Nagaraj_Python_codes/Chess_Implemetation/Images/white_rook.png')
white_rook = pygame.transform.scale(white_rook, (60, 60))
white_rook_small = pygame.transform.scale(white_rook, (small_piece, small_piece))
white_bishop = pygame.image.load ('D:/Nagaraj_Python_codes/Chess_Implemetation/Images/white_bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (60, 60))
white_bishop_small = pygame.transform.scale(white_bishop, (small_piece, small_piece))
white_knight = pygame.image.load ('D:/Nagaraj_Python_codes/Chess_Implemetation/Images/white_knight.png')
white_knight = pygame.transform.scale(white_knight, (60, 60))
white_knight_small = pygame.transform.scale(white_knight, (small_piece, small_piece))
white_pawn = pygame.image.load ('D:/Nagaraj_Python_codes/Chess_Implemetation/Images/white_pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (55, 55))
white_pawn_small = pygame.transform.scale(white_pawn, (25, 25))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

#check variable /flashing counter
def draw_board():
    tile_size = 75  # changed from 100
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [column * tile_size * 2, row * tile_size, tile_size, tile_size])
        else:
            pygame.draw.rect(screen, 'light gray', [tile_size + column * tile_size * 2, row * tile_size, tile_size, tile_size])

    for i in range(9):
        pygame.draw.line(screen, 'black', (0, tile_size * i), (600, tile_size * i), 2)
        pygame.draw.line(screen, 'black', (tile_size * i, 0), (tile_size * i, 600), 2)

    pygame.draw.rect(screen, 'gray', [0, 600, WIDTH, 100], 3)
    pygame.draw.rect(screen, 'gold', [0, 600, WIDTH, 100], 3)
    pygame.draw.rect(screen, 'gold', [600, 0, 300, HEIGHT], 3)

    status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                   'Black: Select a Piece to Move!', 'Black: Select a Destination!']
    screen.blit(big_font.render(status_text[turn_step], True, 'black'), (10, 620))


#function to check all piecec valid options on board
def check_option():
    pass

#draw pieces onto board.
def draw_pieces():
    for i in range(len(white_pieces)):
        piece = white_pieces[i]
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_location[i][0]*75+10, white_location[i][1]*75+10))
        else:
            screen.blit(white_images[index], (white_location[i][0]*75+10, white_location[i][1]*75+10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_location[i][0]*75+1, white_location[i][1]*75+1,75,75], 2)

    for i in range(len(black_pieces)):
        piece = black_pieces[i]
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_location[i][0]*75+10, black_location[i][1]*75+10))
        else:
            screen.blit(black_images[index], (black_location[i][0]*75+10, black_location[i][1]*75+10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_location[i][0]*75+1, black_location[i][1]*75+1,75,75], 2)
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', (black_location[i][0] *75+1, black_location[i][1] * 75+1, 75, 75), 2)

def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

# check valid pawn moves, this function is working fine 
def check_pawn(position, color):
    moves_list = []
    x, y = position

    if color == 'white':
        friends = white_location
        enemies = black_location
        direction = 1
        start_row = 1
        end_limit = 7
    else:
        friends = black_location
        enemies = white_location
        direction = -1
        start_row = 6
        end_limit = 0

    # Forward 1 square
    one_ahead = (x, y + direction)
    if one_ahead not in white_location and one_ahead not in black_location and 0 <= one_ahead[1] <= 7:
        moves_list.append(one_ahead)

        # Forward 2 squares (only if pawn is at start position and 1-ahead is empty)
        two_ahead = (x, y + 2 * direction)
        if y == start_row and two_ahead not in white_location and two_ahead not in black_location:
            if one_ahead not in white_location and one_ahead not in black_location:
                moves_list.append(two_ahead)

    # Diagonal captures
    for dx in [-1, 1]:
        diag = (x + dx, y + direction)
        if 0 <= diag[0] <= 7 and 0 <= diag[1] <= 7 and diag in enemies:
            moves_list.append(diag)

    return moves_list

#check rook moves, this function is working fine 
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_location
        friends_list = white_location
    else:
        friends_list = black_location
        enemies_list = white_location
    for i in range(4): #down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain*x), position[1] + (chain * y)) not in friends_list and\
                0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
                
            else:
                path = False
    return moves_list

#check valid knight moves
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_location
        friends_list = white_location
    else:
        friends_list = black_location
        enemies_list = white_location
    # 8 sqares to check knights, they can go 2 squares in one direction and one in another.
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target_pos = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target_pos not in friends_list and 0 <= target_pos[0] <= 7 and 0 <= target_pos[1] <= 7:
            moves_list.append(target_pos)


    return moves_list

#check bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_location
        friends_list = white_location
    else:
        friends_list = black_location
        enemies_list = white_location
    for i in range(4): #up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain*x), position[1] + (chain * y)) not in friends_list and\
                0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
                
            else:
                path = False
    return moves_list
    
#check queen moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.extend(second_list)# Add rook moves to bishop moves
    return moves_list

#check king moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_location
        friends_list = white_location
    else:
        friends_list = black_location
        enemies_list = white_location
    # 8 sqares to check king, they can go 1 squares in any direction.
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (-0, -1)]
    for i in range(8):
        target_pos = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target_pos not in friends_list and 0 <= target_pos[0] <= 7 and 0 <= target_pos[1] <= 7:
            moves_list.append(target_pos)


    return moves_list

# check for valid moves for just piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

#draw valid moves on screen 
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 75 + 38, moves[i][1] * 75 + 40), 5)

#draw captured pieces on side of screen
def draw_captured():

    # White captured (black pieces) – draw on top
    for i, captured_piece in enumerate(captured_pieces_white):
        if captured_piece in piece_list:
            index = piece_list.index(captured_piece)
            screen.blit(small_black_images[index], (600, 5 + 50 * i))

    # Black captured (white pieces) – draw below white's
    for i, captured_piece in enumerate(captured_pieces_black):
        if captured_piece in piece_list:
            index = piece_list.index(captured_piece)
            screen.blit(small_white_images[index], (800, 15 + 50 * i))
#main Game loop:
black_options = check_options(black_pieces, black_location, 'black')
white_options = check_options(white_pieces, white_location, 'white')
run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    draw_captured()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type ==  pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coored = event.pos[0]//75
            y_coored = event.pos[1]//75
            click_coords = (x_coored, y_coored)
            if turn_step <= 1:
                if click_coords in white_location:
                    selection = white_location.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_location[selection] = click_coords
                    if click_coords in black_location:
                        black_piece = black_location.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_location.pop(black_piece)
                    black_options = check_options(black_pieces, black_location, 'black')
                    white_options = check_options(white_pieces, white_location, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords in black_location:
                    selection = black_location.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_location[selection] = click_coords
                    if click_coords in white_location:
                        white_piece = white_location.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_location.pop(white_piece)
                    black_options = check_options(black_pieces, black_location, 'black')
                    white_options = check_options(white_pieces, white_location, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []




    pygame.display.update()   # <<< MISSING: this is crucial
pygame.quit()