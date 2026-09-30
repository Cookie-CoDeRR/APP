def knapsack(max_capacity, weights, values, n):
    # Step 1: Create a 2D table filled with 0s
    # It has (n + 1) rows and (max_capacity + 1) columns
    dp = [[0 for _ in range(max_capacity + 1)] for _ in range(n + 1)]
    
    # Step 2: Loop through items (i) and capacities (w)
    for i in range(1, n + 1):
        for w in range(1, max_capacity + 1):
            
            current_weight = weights[i-1]
            current_value = values[i-1]
            
            # If the item fits in our current capacity w
            if current_weight <= w:
                # Max of (Taking it) vs (Leaving it)
                take_it = current_value + dp[i-1][w - current_weight]
                leave_it = dp[i-1][w]
                
                dp[i][w] = max(take_it, leave_it)
                
            # If the item is too heavy, we must leave it
            else:
                dp[i][w] = dp[i-1][w]
                
    # The bottom-right cell contains our final maximum value
    return dp[n][max_capacity]

# --- Test it out ---
values = [60, 100, 120]
weights = [10, 20, 30]
max_capacity = 50
n = len(values)

print(f"Maximum value: {knapsack(max_capacity, weights, values, n)}") 
# Output: Maximum value: 220 (Takes items 2 and 3)
