# Exercise 3: Double Dice Simulation
import random

def throw_dice():
    """
    Simulates the rolling of a single six-sided die.
    
    :return: An integer between 1 and 6.
    """
    return random.randint(1, 6)

def throw_until_doubles():
    """
    Keeps throwing two dice until both land on the same number (doubles).
    
    :return: The total number of throws required to reach doubles (integer).
    """
    throws_count = 0
    while True:
        # Throw the two dice
        die1 = throw_dice()
        die2 = throw_dice()
        throws_count += 1
        
        # Check for doubles
        if die1 == die2:
            return throws_count

def main():
    """
    Runs the double dice simulation 100 times, collects the results, 
    and prints the total and average throws.
    """
    NUM_TRIALS = 100
    
    # Use a list to store the number of throws required for each of the 100 trials
    results = [] 
    
    # Throw doubles 100 times
    for _ in range(NUM_TRIALS):
        throws = throw_until_doubles()
        results.append(throws)
        
    # Calculate statistics
    total_throws = sum(results)
    average_throws = total_throws / NUM_TRIALS
    
    # Print results
    print(f"--- Double Dice Simulation ({NUM_TRIALS} Trials) ---")
    print(f"Total throws: {total_throws}")
    
    # Round the average to 2 decimal places
    print(f"Average throws to reach doubles: {average_throws:.2f}")

# Start the simulation
if __name__ == "__main__":
    main()