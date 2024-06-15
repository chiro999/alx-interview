#!/usr/bin/python3
'''0x09. Island Perimeter'''

def island_perimeter(grid):
    '''returns the perimeter of the island described in grid'''
    counter = 0  # Initialize the perimeter counter
    grid_max = len(grid) - 1  # Index of the last row in the grid
    lst_max = len(grid[0]) - 1  # Index of the last column in the first row

    for lst_idx, lst in enumerate(grid):  # Iterate over each row in the grid
        for land_idx, land in enumerate(lst):  # Iterate over each cell in the row
            if land == 1:  # Check if the cell represents land (1)
                # Check left and right sides
                if land_idx == 0:  # If the land is on the left edge of the grid
                    counter += 1  # Add to perimeter for left edge
                    if lst[land_idx + 1] == 0:  # Check if the right neighbor is water
                        counter += 1  # Add to perimeter for right side
                elif land_idx == lst_max:  # If the land is on the right edge of the grid
                    if lst[land_idx - 1] == 0:  # Check if the left neighbor is water
                        counter += 1  # Add to perimeter for left side
                    counter += 1  # Add to perimeter for right edge
                else:  # If the land is not on an edge
                    if lst[land_idx - 1] == 0:  # Check if the left neighbor is water
                        counter += 1  # Add to perimeter for left side
                    if lst[land_idx + 1] == 0:  # Check if the right neighbor is water
                        counter += 1  # Add to perimeter for right side

                # Check top and bottom sides
                if lst_idx == 0:  # If the land is on the top edge of the grid
                    counter += 1  # Add to perimeter for top edge
                    if grid[lst_idx + 1][land_idx] == 0:  # Check if the bottom neighbor is water
                        counter += 1  # Add to perimeter for bottom side
                elif lst_idx == grid_max:  # If the land is on the bottom edge of the grid
                    if grid[lst_idx - 1][land_idx] == 0:  # Check if the top neighbor is water
                        counter += 1  # Add to perimeter for top side
                    counter += 1  # Add to perimeter for bottom edge
                else:  # If the land is not on an edge
                    if grid[lst_idx - 1][land_idx] == 0:  # Check if the top neighbor is water
                        counter += 1  # Add to perimeter for top side
                    if grid[lst_idx + 1][land_idx] == 0:  # Check if the bottom neighbor is water
                        counter += 1  # Add to perimeter for bottom side

    return counter  # Return the total perimeter
