import curses # For terminal handling
from curses import wrapper # To wrap the main function for proper initialization and cleanup of curses
import queue # For implementing the breadth-first search (BFS) algorithm to find the shortest path in the maze
# FIX: removed `import color` - no such module exists (ModuleNotFoundError).
# Colours already come from curses itself (curses.color_pair in print_maze).
import time # For adding a delay to visualize the pathfinding process in the maze

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
] # Define the maze as a 2D list, where '#' represents walls, 'O' is the starting point, and 'X' is the endpoint


def print_maze(maze, stdscr, path=[]): # Function to print the maze in the terminal, with an optional path parameter to visualize the path found in the maze
    BLUE = curses.color_pair(1) # Initialize color pair for the maze walls and paths, blue is text and black is the background color of the terminal, so the maze will be displayed in blue on a black background
    RED = curses.color_pair(2) # Initialize color pair for the path found in the maze, red is text and black is the background color of the terminal, so the path will be displayed in red on a black background

    for i, row in enumerate(maze): # Iterate through each row of the maze, with the index i representing the row number and row representing the actual row data (index & value) row is the list.
        for j, value in enumerate(row): # Iterate through each value in the row, with the index j representing the column number and value representing the actual value at that position in the maze
            if (i, j) in path: # Check if the current position (i, j) is part of the path found in the maze
                stdscr.addstr(i, j*2, "X", RED) # If it is part of the path, print "X" in red color at the corresponding position in the terminal, 2 spaces on the column
                # j*2 is used to add spacing between the columns for better visualization
            else:
                stdscr.addstr(i, j*2, value, BLUE) # If it is not part of the path, print the original value from the maze in blue color at the corresponding position in the terminal


def find_start(maze, start): # Function to find the starting position in the maze, which is represented by "O" in the maze, and return its coordinates (row, column)
    for i, row in enumerate(maze): # Iterate through each row of the maze, with the index i representing the row number and row representing the actual row data (index & value) row is the list.
        for j, value in enumerate(row): # Iterate through each value in the row, with the index j representing the column number and value representing the actual value at that position in the maze
            if value == start: # Check if the current value is equal to the starting point "O"
                return i, j # If it is, return the coordinates (row, column) of the starting point in the maze

    return None # If the starting point is not found in the maze, return None


def find_path(maze, stdscr): # Function to find the shortest path in the maze using breadth-first search (BFS) algorithm and visualize it in the terminal
    start = "O" # Define the starting point in the maze, which is represented by "O" in the maze
    end = "X" # Define the endpoint in the maze, which is represented by "X" in the maze
    start_pos = find_start(maze, start) # Find the starting position in the maze using the find_start function, which returns the coordinates (row, column) of the starting point "O" in the maze

    q = queue.Queue() # Create a queue to implement the breadth-first search (BFS) algorithm, which will be used to explore the maze level by level and find the shortest path from the starting point to the endpoint
    q.put((start_pos, [start_pos])) # Add the starting position and the initial path (which contains only the starting position) to the queue as a tuple,
    # where start_pos is the coordinates of the starting point and [start_pos] is a list representing the path taken so far (initially containing only the starting position)

    visited = set() # Create a set to keep track of visited positions in the maze, which will help to avoid cycles and redundant exploration during the BFS algorithm

    while not q.empty(): # Continue the BFS algorithm until the queue is empty, which means that all possible paths have been explored
        current_pos, path = q.get() # Get the current position and the path taken to reach that position from the queue,
        #where current_pos is the coordinates of the current position being explored and path is a list representing the path taken to reach that position
        row, col = current_pos # Unpack the current position into row and column coordinates for easier access

        stdscr.clear() # Clear the terminal screen before printing the maze with the current path visualization
        print_maze(maze, stdscr, path) # Call the print_maze function to print the maze in the terminal, passing the maze, the standard screen object (stdscr), and the current path to visualize the path found in the maze
        time.sleep(0.2) # Add a delay of 0.2 seconds to visualize the pathfinding process in the maze, allowing the user to see the exploration of the maze step by step
        stdscr.refresh() #  Refresh the terminal to show the changes made by printing the maze with the current path visualization

        if maze[row][col] == end: # Check if the current position in the maze is the endpoint "X", which means that a path from the starting point to the endpoint has been found
            return path # If the endpoint is found, return the path taken to reach it, which is a list of coordinates representing the path from the starting point to the endpoint in the maze

        neighbors = find_neighbors(maze, row, col) # To find obstruction
        # Call the find_neighbors function to get the neighboring positions (up, down, left, right) of the current position in the maze,
        # which will be explored in the BFS algorithm

        for neighbor in neighbors: # Iterate through each neighboring position to explore it in the BFS algorithm
            if neighbor in visited: # Check if the neighboring position has already been visited, which means that it has already been explored in the BFS algorithm,
                #so we skip it to avoid redundant exploration and cycles in the maze
                continue # Check if the neighboring position has already been visited, which means that it has already been explored in the BFS algorithm, so we skip it to avoid redundant exploration and cycles in the maze

            r, c = neighbor # Unpack the neighboring position into row and column coordinates for easier access
            if maze[r][c] == "#": # Check if the neighboring position is a wall ("#") in the maze, which means that it is an obstruction and cannot be traversed,
                # so we skip it and do not add it to the queue for further exploration
                continue # Check if the neighboring position is a wall ("#") in the maze, which means that it is an obstruction and cannot be traversed, so we skip it and do not add it to the queue for further exploration 

            new_path = path + [neighbor] # Create a new path by adding the neighboring position to the current path, which represents the path taken to reach that neighboring position in the maze
            q.put((neighbor, new_path)) # add it to the queue as a tuple, where neighbor is the coordinates of the neighboring position and
            # new_path is a list representing the path taken to reach that neighboring position (which is the current path plus the neighboring position)
            visited.add(neighbor) # Add the neighboring position to the visited set to mark it as visited, preventing redundant exploration of the same position in future iterations of the BFS algorithm


def find_neighbors(maze, row, col): # Function to find the neighboring positions (up, down, left, right) of a given position in the maze, which will be explored in the BFS algorithm
    # bsf stands for? Breadth-First Search, which is a graph traversal algorithm that explores all the neighbors of a node before moving on to the next level of neighbors.
    # In the context of the maze, it means that the algorithm will explore all the neighboring positions (up, down, left, right) of the current position
    # before moving on to explore the neighbors of those neighboring positions, effectively exploring the maze level by level to find the shortest path from the starting point to the endpoint. 
    neighbors = [] # Create an empty list to store the neighboring positions that will be explored in the BFS algorithm

    if row > 0:  # UP - Check if the current row is greater than 0 to ensure that we are not going out of bounds when checking the upward neighbor
        neighbors.append((row - 1, col)) # why append neighbour? Because we want to add the neighboring position (row - 1, col) to the list of neighbors that will be explored in the BFS algorithm, allowing us to explore the maze in all four directions (up, down, left, right) from the current position.
    if row + 1 < len(maze):  # DOWN - Check if the current row is less than the length of the maze to ensure that we are not going out of bounds when checking the downward neighbor
        neighbors.append((row + 1, col)) 
    if col > 0:  # LEFT - Check if the current column is greater than 0 to ensure that we are not going out of bounds when checking the left neighbor       
        neighbors.append((row, col - 1)) 
    if col + 1 < len(maze[0]):  # RIGHT - Check if the current column is less than the length of the maze row to ensure that we are not going out of bounds when checking the right neighbor
        neighbors.append((row, col + 1))

    return neighbors # Return the list of neighboring positions that will be explored in the BFS algorithm, which includes the valid neighboring positions (up, down, left, right)
# that are within the bounds of the maze.

def main(stdscr): # screen object passed by the wrapper function to handle terminal display
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK) # Initialize color pair for the maze walls and paths
    # blue is text and black is the background color of the terminal, so the maze will be displayed in blue on a black background
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) # Initialize color pair for the path found in the maze

    find_path(maze, stdscr) # Find the shortest path in the maze and visualize it
    stdscr.getch() # Wait for a key press before exiting the program


wrapper(main) # Wrap the main function to ensure proper initialization and cleanup of curses