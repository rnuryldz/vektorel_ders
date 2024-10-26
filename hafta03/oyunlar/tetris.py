import random
import os
import time

# Oyun tahtası boyutları
ROW, COLUMN = 20, 10

# Tetris tahtası
board = [[' ' for _ in range(COLUMN)] for _ in range(ROW)]

# Şekil listesi
tetrominoes = [
[['1', '1', '1', '1']],
[['1', '1', '1'], ['0', '1', '0']],
[['1', '1', '1'], ['1', '0', '0']],
[['1', '1', '1'], ['0', '0', '1']],
[['1', '1'], ['1', '1']],
[['1', '1', '0'], ['0', '1', '1']],
[['0', '1', '1'], ['1', '1', '0']]
]

# Rastgele bir tetromino seçme
def get_random_tetromino():
return random.choice(tetrominoes)

# Tahtayı temizleme
def clear_board():
for i in range(ROW):
for j in range(COLUMN):
board[i][j] = ' '

# Şekli tahtaya ekleme
def place_tetromino(tetromino, row, col):
for i in range(len(tetromino)):
for j in range(len(tetromino[i])):
if tetromino[i][j] == '1':
board[row + i][col + j] = '1'

# Şekli tahtadan kaldırma
def remove_tetromino(tetromino, row, col):
for i in range(len(tetromino)):
for j in range(len(tetromino[i])):
if tetromino[i][j] == '1':
board[row + i][col + j] = ' '

# Tahtayı ekrana yazdırma
def print_board():
os.system('cls' if os.name == 'nt' else 'clear')
for row in board:
print('|' + '|'.join(row) + '|')
print('-' * (2 * COLUMN + 1))

# Tetrominoyu tahtada hareket ettirme
def move_tetromino(tetromino, row, col, move):
remove_tetromino(tetromino, row, col)
if move == 'down':
row += 1
elif move == 'left':
col -= 1
elif move == 'right':
col += 1
place_tetromino(tetromino, row, col)
return row, col

# Tetrominoyu tahtada döndürme
def rotate_tetromino(tetromino):
return list(zip(*reversed(tetromino)))

# Tahtada bir satırı kontrol etme ve temizleme
def check_and_clear_row():
global board
for i in range(ROW - 1, -1, -1):
if ' ' not in board[i]:
del board[i]
board.insert(0, [' ' for _ in range(COLUMN)])

# Oyun döngüsü
def run_game():
clear_board()
current_tetromino = get_random_tetromino()
current_row, current_col = 0, COLUMN // 2 - len(current_tetromino[0]) // 2

while True:
print_board()
user_input = input("Left (L), Right (R), Rotate (U), Down (D): ").lower()

if user_input == 'l':
current_row, current_col = move_tetromino(current_tetromino, current_row, current_col, 'left')
elif user_input == 'r':
current_row, current_col = move_tetromino(current_tetromino, current_row, current_col, 'right')
elif user_input == 'u':
current_tetromino = rotate_tetromino(current_tetromino)
elif user_input == 'd':
current_row, current_col = move_tetromino(current_tetromino, current_row, current_col, 'down')

# Tahtada bir satır kontrol et ve temizle
check_and_clear_row()

# Yeni bir tetromino getir
if current_row + len(current_tetromino) > ROW:
current_tetromino = get_random_tetromino()
current_row, current_col = 0, COLUMN // 2 - len(current_tetromino[0]) // 2
else:
current_row, current_col = move_tetromino(current_tetromino, current_row, current_col, 'down')

# Oyunu başlat
if __name__ == "__main__":
run_game()