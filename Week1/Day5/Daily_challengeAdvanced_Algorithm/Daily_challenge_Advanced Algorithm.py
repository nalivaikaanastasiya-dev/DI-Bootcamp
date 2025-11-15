import random

# Starter Code: Generates a list of 20000 random numbers and sets the target
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728

# Set to store the found pairs to prevent duplicates (e.g., (1000, 2728) and (2728, 1000))
# The pairs will be stored as sorted tuples (e.g., (1000, 2728))
found_pairs = set()

# Set to store numbers seen so far, for O(1) lookup efficiency
seen_numbers = set()

def find_target_sum_pairs(numbers, target):
    """
    Finds all unique pairs in the list that sum up to the target number.
    Uses a single loop and a set for O(n) efficiency.
    """
    
    # Loops: Iterate through the list of numbers once
    for number in numbers:
        # Conditionals: Determine the complement needed
        complement = target - number
        
        # Conditionals: Check if the complement has been seen before
        if complement in seen_numbers:
            # Pair found! Sort the pair to ensure uniqueness in the found_pairs set
            pair = tuple(sorted((number, complement)))
            found_pairs.add(pair)
            
        # Add the current number to the set of seen numbers
        seen_numbers.add(number)

    # Functions: Return the final set of unique pairs
    return found_pairs

# Execute the function and store the result
result_pairs = find_target_sum_pairs(list_of_numbers, target_number)

## --- Output ---
print(f"Target Number: {target_number}")
print(f"Total pairs found: {len(result_pairs)}\n")

if result_pairs:
    print("Example Pairs Found:")
    # Loops: Print a sample of the found pairs
    for pair in list(result_pairs)[:5]: 
        print(f"  {pair[0]} and {pair[1]} sums to the target_number {target_number}")
else:
    print("No pairs found that sum to the target number.")