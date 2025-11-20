import random, time

# Array

public_grid = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]
private_grid = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]

grid_size = len(private_grid)

def reset_grid():
    global public_grid, private_grid
    public_grid = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    ]
    private_grid = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    ]

def display_grid(x):
    rows = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    columns = "    0    1    2    3    4    5    6    7    8    9"
    print(columns)
    for row in range(grid_size):
        index = row
        content = x[row]
        print(f'{rows[index]} {content}')
    print("\n----------------------------------------------------\n")

def grid_num():
    return random.randint(0,9)

def generate_mines():
    global private_grid
    while True:
        try:
            print("How many mines do you want on your grid?")
            mines = int(input())
            if mines <= 90 and mines >= 1:
                break
            print("Please enter a number between 1 and 90")
        except ValueError:
            print("Please enter a number")
    for i in range(mines):
        x = grid_num()
        y = grid_num()
        if private_grid[x][y] == "X":
            while private_grid[x][y] == "X":
                x = grid_num()
                y = grid_num()
        private_grid[x][y] = "X"

def get_private_grid():
    global private_grid
    generate_mines()
    for row in range(grid_size):
        for col in range(grid_size):
            
            # Check if the current cell is a mine or not, if so skip
            if private_grid[row][col] == "X":
                continue

            # Set count of neighbouring mines to 0
            count = 0

            # USED AI TO GUIDE ME (LINE 97 TO 108)
            for neighbour_row in range(row - 1, row + 2):
                for neighbour_col in range(col - 1, col + 2):

                    if neighbour_row < 0 or neighbour_row >= grid_size:
                        continue
                    if neighbour_col < 0 or neighbour_col >= grid_size:
                        continue

                    if private_grid[neighbour_row][neighbour_col] == "X":
                        count = count + 1

            private_grid[row][col] = str(count)


def reveal_cell(row, col):
    public_grid[row][col] = private_grid[row][col]

def place_flag(row, col):
    if public_grid[row][col] == ".":
        public_grid[row][col] = "F"
    elif public_grid[row][col] == "F":
        print("This cell is already a flag")
    else:
        print("This cell has already been revealed")

def remove_flag(row, col):
    if public_grid[row][col] == ".":
        print("This cell has no flag")
    elif public_grid[row][col] == "F":
        public_grid[row][col] = "."
    else:
        print("This cell has already been revealed")

def player_move():
    while True:
        print("What would you like to do:\n[R] - Reveal \n[F] - Flag \n[U] - Unflag")
        action = str(input()).upper().strip()
        if action in ("R", "F", "U"):
            break
        print("Invalid action, try again.\n")

    while True:
        try:
            print("Choose your row (0-9)")
            row = int(input())
            if row >= 0 and row <= 9:
                break
            print("Row must be between 0 and 9\n")
        except ValueError:
            print("Please enter a number.\n")

    while True:
        try:
            print("Choose your column (0-9)")
            col = int(input())
            if col >= 0 and col <= 9:
                break
            print("Column must be between 0 and 9.\n")
        except ValueError:
            print("Please enter a number.\n")
    return action, row, col

def check_win():
    for row in range(grid_size):
        for col in range(grid_size):

            if private_grid[row][col] != "X": # Checks if cell is not a mine

                if public_grid[row][col] == ".": # Checks whether the user has revealed the cell
                    return False

    return True # Returns True if all cells which are not mines are revealed

def game():
    get_private_grid() # Generates all the mines and numbers

    while True:
        display_grid(public_grid) # Displays the grid
        time.sleep(0.3)

        action, row, col = player_move()

        # Flag
        if action == "F":
            place_flag(row, col)
            time.sleep(0.2)
            continue

        # Remove Flag
        if action == "U":
            remove_flag(row,col)
            time.sleep(0.2)
            continue

        # Reveal Cell
        if action == "R":

            # Check whether the row is flagged
            if public_grid[row][col] == "F":
                print("You must remove the flag before you reveal this cell")
                time.sleep(1)
                continue

            # Check whether the cell contains a mine
            if private_grid[row][col] == "X":
                print("BOOM! You hit a mine!")
                time.sleep(1.5)
                print("This is the actual grid")
                print("\n----------------------------------------------------\n")
                display_grid(private_grid)
                break

            reveal_cell(row,col)
            time.sleep(0.2)

            if check_win() == True:
                print("You win! ALL safe cells revealed!")
                time.sleep(1.5)
                print("\n----------------------------------------------------\n")
                display_grid(private_grid)
                break


play = True

while play:
    game()
    print("Would you like to play again?\n[Y] - Yes\n[N] - No\n--------------")
    user_input = str(input()).upper()
    if user_input == "Y":
        play = True
        time.sleep(1.5)
        reset_grid()
    elif user_input == "N":
        print("Shutting Down...")
        time.sleep(1)
        play = False
        break
    else:
        print("Error occured, restart game")
        play = False
        time.sleep(0.4)
        break

