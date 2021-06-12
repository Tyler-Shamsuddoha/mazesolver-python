# import random
# from collections import deque
import queue
import time
from colorama import init, Fore

init()
directions = ("R", "L", "U", "D")
fr_directions = frozenset(directions)


def hardcoded_maze():
    hardcoded = []
    hardcoded.append(["█", "█", "█", "█", "█", "█", "█", "█", "█"])
    hardcoded.append(["█", " ", " ", " ", " ", " ", " ", " ", "█"])
    hardcoded.append(["█", " ", "█", " ", "█", " ", "█", " ", "█"])
    hardcoded.append(["█", "█", "█", " ", "█", " ", "█", " ", "█"])
    hardcoded.append(["F", " ", "█", " ", "█", " ", "█", " ", "S"])
    hardcoded.append(["█", " ", " ", " ", " ", " ", "█", " ", "█"])
    hardcoded.append(["█", " ", "█", " ", "█", " ", "█", " ", "█"])
    hardcoded.append(["█", " ", " ", " ", " ", " ", "█", " ", "█"])
    hardcoded.append(["█", "█", "█", "█", "█", "█", "█", "█", "█"])

    return hardcoded


def init_maze(maze_height, maze_width):
    """Create the maze.

    :param int maze_height: The height of the intended maze
    :param int maze_width: The width of the intended maze
    :returns [] maze: The maze populated by unvisited blocks
    """
    maze = []
    for i in range(0, maze_height):
        line = []
        for j in range(0, maze_width):
            line.append(" ")
        maze.append(line)

    return maze


def print_maze(maze, finished_path):
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if maze[i][j] == "S":
                # We have found the starting cell
                x_pos = i
                y_pos = j
    path_list = []
    for move in finished_path:
        if move == "R":
            x_pos += 1
        elif move == "L":
            x_pos -= 1
        elif move == "U":
            y_pos -= 1
        elif move == "D":
            y_pos += 1

        path_list.append((x_pos, y_pos))

    for row in range(0, len(maze)):
        for col in range(0, len(maze[0])):
            if (row, col) in path_list:
                print("+ ", end="")
            else:
                print(maze[row][col] + " ", end="")
        print()


def print_unsolved_maze(maze):
    """Prints the maze out using colorama
    :param [] maze: The populated maze
    """
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == " ":
                print(Fore.WHITE, f'{maze[i][j]}', end="")
            elif maze[i][j] == "F":
                print(Fore.GREEN, f'{maze[i][j]}', end="")
            elif maze[i][j] == 'S':
                print(Fore.RED, f'{maze[i][j]}', end="")
            elif maze[i][j] == "█":
                print(Fore.BLACK, f'{maze[i][j]}', end="")
            else:
                print(maze[i][j], end="")
        print()


def find_exit_point(maze, path):
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if maze[i][j] == "S":
                # We have found the starting cell
                x_pos = i
                y_pos = j
    for move in path:
        if move == "R":
            x_pos += 1
        elif move == "L":
            x_pos -= 1
        elif move == "U":
            y_pos -= 1
        elif move == "D":
            y_pos += 1

    if maze[x_pos][y_pos] == "F":
        print("--- %s seconds ---" % (time.time() - start_time))
        print("Maze completed!")
        print_maze(maze, path)
        return True

    return False


def check_index(index_x, index_y, maze):
    if not 0 <= index_x < len(maze[0]):
        return False
    elif not 0 <= index_y < len(maze):
        return False
    return True


def valid(maze, moves):
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if maze[i][j] == "S":
                # We have found the starting cell
                x_pos = i
                y_pos = j
    for move in moves:
        if move == "L":
            x_pos -= 1

        elif move == "R":
            x_pos += 1

        elif move == "U":
            y_pos -= 1

        elif move == "D":
            y_pos += 1

        if not check_index(x_pos, y_pos, maze):
            return False
        if maze[x_pos][y_pos] == "█":
            return False
    return True


def do_breadth_first():
    global start_time
    print("Attempting breadth first search...")
    start_time = time.time()
    maze = hardcoded_maze()
    nums = queue.Queue()
    nums.put("")
    add = ""

    while not find_exit_point(maze, add):
        add = nums.get()
        for i in fr_directions:
            put = add + i
            if valid(maze, put):
                nums.put(put)


def do_depth_first():
    pass


def print_menu():
    print("Press 1 to solve using breadth first search")
    print("Press 2 to solve using depth first search")
    print("Press 3 to solve using A* search")
    print("Press 4 to generate a new maze")
    print("Press 0 to quit")


if __name__ == '__main__':
    quit = False
    print_menu()
    while not quit:
        # print("\nEnter an option: (1 to print available options)")
        action = int(input("\nEnter an option: (1 to print available options)\n"))
        if action == 1:
            do_breadth_first()
            break
        elif action == 2:
            print("2 was selected")
            # do_depth_first()
            break
        elif action == 3:
            # do_astar()
            break
        elif action == 4:
            # Create new maze
            break
        elif action == 0:
            quit = True
            print("Quitting...")
            break
        else:
            print("Please choose an option from the list")
