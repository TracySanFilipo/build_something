import random


def create_grid(row, col):
    grid_dict = {}
    grid = []
    for x in range(0, row):
        for y in range(0, col):
            grid.append(str((x, y)))
    for string in grid:
        grid_dict[string] = 0
    return grid_dict


def seed_letter(grid, letter, cell_row, cell_col, grid_rows, grid_col):
    new_grid = grid
    seed_cell_chances = [0, letter]
    seed_answer = random.choice(seed_cell_chances)
    new_grid[(str((cell_row, cell_col)))] = seed_answer
    if (cell_row + 1) <= grid_rows:
        seed_cell_right1 = [0, 0, letter]
        seed_cell_right1_answer = random.choice(seed_cell_right1)
        new_grid[(str(((cell_row + 1), cell_col)))] = seed_cell_right1_answer
    if (cell_row - 1) >= 0:
        seed_cell_left1 = [0, 0, letter]
        seed_cell_left1_answer = random.choice(seed_cell_left1)
        new_grid[(str(((cell_row + 1), cell_col)))] = seed_cell_left1_answer
    if (cell_col + 1) <= grid_col:
        seed_cell_up1 = [0, 0, letter]
        seed_cell_up1_answer = random.choice(seed_cell_up1)
        new_grid[(str((cell_row, (cell_col + 1))))] = seed_cell_up1_answer
    if (cell_col - 1) >= 0:
        seed_cell_down1 = [0, 0, letter]
        seed_cell_down1_answer = random.choice(seed_cell_down1)
        new_grid[(str((cell_row, (cell_col - 1))))] = seed_cell_down1_answer
    print(new_grid)
    return new_grid


def playwithgrid():
    while True:
        try:
            user_row = int(input("Please choose a number of rows: "))
            user_col = int(input("Please choose a number of columns: "))
        except ValueError:
            print("Enter whole numbers for row and column")
        else:
            grid = create_grid(user_row, user_col)
            while True:
                user_seed = input("Please choose a letter: ")
                if user_seed.isalpha() and len(user_seed) == 1:
                    while True:
                        try:
                            row = int(input("Please choose a x-coordinate: "))
                            col = int(input("Please choose a y-coordinate: "))
                        except ValueError:
                            print("Enter whole numbers for cell location")
                        else:
                            if row in range(0, user_row) and col in range(0, user_col):
                                grid = seed_letter(grid, user_seed, row, col, user_row, user_col)
                                break
                elif user_seed.lower() == 'quit':
                    quit()


def main():
    while True:
        user_input = input("Please choose to create a grid[g] or quit[q]: ")
        if user_input.lower() in ['grid', 'g']:
            playwithgrid()
        elif user_input.lower() in ['quit', 'q']:
            print("Good bye")
            quit()
        else:
            continue


main()
