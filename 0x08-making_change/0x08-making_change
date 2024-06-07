#!/usr/bin/python3
"""Change making module.
"""

def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    
    Args:
    coins (list): List of the values of the coins available.
    total (int): The total amount of money to make with the coins.
    
    Returns:
    int: The fewest number of coins needed to make the total amount.
         If it's not possible to make the total amount with the given coins, returns -1.
    """
    
    # If the total amount is less than or equal to 0, no coins are needed.
    if total <= 0:
        return 0

    # Remaining amount to be made.
    rem = total
    
    # Counter for the number of coins used.
    coins_count = 0
    
    # Index for iterating through the sorted coins list.
    coin_idx = 0
    
    # Sort the coins in descending order to use the largest denominations first.
    sorted_coins = sorted(coins, reverse=True)
    
    # Number of different coin denominations available.
    n = len(coins)
    
    # While there is still some amount remaining to be made:
    while rem > 0:
        # If we have gone through all coin denominations and still have some amount left, return -1.
        if coin_idx >= n:
            return -1
        
        # If the current coin can be used (it doesn't make the remaining amount negative):
        if rem - sorted_coins[coin_idx] >= 0:
            # Use the coin by subtracting its value from the remaining amount.
            rem -= sorted_coins[coin_idx]
            # Increment the coin count.
            coins_count += 1
        else:
            # Move to the next smaller coin denomination.
            coin_idx += 1
    
    # Return the total number of coins used.
    return coins_count
