import itertools
import re

# The size of the board. Default tic-tac-toe is 3x3, but let's have it dynamic
BOARD_SIZE = 3

# We will make our moves similar to a chess game, this is a console app, no UI :(
BOARD_H = 'ABCDEFGH'
BOARD_V = '12345678'

# Pattern for valid moves
BOARD_PATTERN = '^[A-Z][0-9]$'

# This is the character that will be used for empty cell
BOARD_EMPTY_CELL='·'

# Players, default there is one X and one 0, but this should not be a limitation
PLAYERS = [ 'X', 'O']


# drawing the board, this is the closest thing to an UI
def draw(board):
  print(' ', end = '')
  for idx in range(len(board[0])): print(f' {BOARD_H[idx]}', end = '')
  print('')
  for idx, row in enumerate(board):
    print(f'{BOARD_V[idx]}', end = '')
    for item in row:
      print(f' {item}', end = '')
    print('')


# guard against invalid input
def validator(board, move):
  if not re.compile(BOARD_PATTERN).match(move):
    print(f'The move {move} does not follow the pattern {BOARD_PATTERN}')
    return False
  
  h_idx = BOARD_H.index(move[0])
  v_idx = BOARD_V.index(move[1])
  
  if h_idx > len(board[0]) - 1:
    print(f'The horizontal move {move[0]} is out of range. Maximum value is {BOARD_H[len(board[0]) - 1]}')
    return False
  if v_idx > len(board) - 1:
    print(f'The vertical move {move[1]} is out of range. Maximum value is {BOARD_V[len(board) - 1]}')
    return False
  
  if board[v_idx][h_idx] != BOARD_EMPTY_CELL:
    print(f'The move {move} was already played. Please select an empty cell.')
    return False

  return True


# this is where the moves are set into the board
def play(board, player, move):
  h_idx = BOARD_H.index(move[0])
  v_idx = BOARD_V.index(move[1])
  board[v_idx][h_idx] = player
  return board


# how the game is won
def winner(board):
  # horizontal win
  for row in board:
    if row.count(row[0]) == len(row) and row[0] != BOARD_EMPTY_CELL:
      return row[0]
  
  # vertical win
  for i in range(len(board)):
    col = []
    for row in board:
      col.append(row[i])
    if col.count(col[0]) == len(col) and col[0] != BOARD_EMPTY_CELL:
      return col[0]
  
  # diagonal win top-left -> bottom-right
  diag = []
  for idx in range(len(board)):
    diag.append(board[idx][idx])
  if diag.count(diag[0]) == len(diag) and diag[0] != BOARD_EMPTY_CELL:
      return diag[0]

  # diagonal win bottom-left -> top-right
  diag = []
  for col, row in enumerate(reversed(range(len(board)))):
    diag.append(board[row][col])
  if diag.count(diag[0]) == len(diag) and diag[0] != BOARD_EMPTY_CELL:
      return diag[0]
  
  return None


def main():
  # create the board in a dynamic way
  board = [ [ BOARD_EMPTY_CELL for x in range(BOARD_SIZE) ] for y in range(BOARD_SIZE) ]

  # iterator for players
  player_iterator = itertools.cycle(PLAYERS)

  current_winner = None
  current_turn = 0

  # we draw the initial board
  draw(board)

  # while there is no winner and there are empty cells left, do stuff
  while current_winner is None and current_turn < len(list(itertools.chain(*board))):
    current_turn += 1
    player = next(player_iterator)
    valid_move = False
    # we need to have a valid move to actually play it on the board
    while not valid_move:
      move = input(f'Player {player}, enter your move: ')
      valid_move = validator(board, move)
    board = play(board, player, move)
    draw(board)
    current_winner = winner(board)

  print(f'Winner: {current_winner}')

if __name__ == "__main__":
  main()
