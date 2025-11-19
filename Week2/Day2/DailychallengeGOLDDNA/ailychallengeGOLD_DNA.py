import random

# --- DNA Components ---

class Gene:
    def __init__(self, value=None):
        if value is None:
            self.value = random.randint(0, 1)
        else:
            self.value = value

    def mutate(self):
        self.value = 1 - self.value

    def __repr__(self):
        return str(self.value)

class Chromosome:
    def __init__(self, genes=None):
        if genes is None:
            self.genes = [Gene() for _ in range(10)]
        else:
            self.genes = genes

    def mutate(self):
        for gene in self.genes:
            # High probability (0.8) to mutate the gene
            if random.random() < 0.8:
                gene.mutate()

    def get_values(self):
        return [gene.value for gene in self.genes]

    def __repr__(self):
        return "".join(str(gene.value) for gene in self.genes)

class DNA:
    def __init__(self, chromosomes=None):
        if chromosomes is None:
            self.chromosomes = [Chromosome() for _ in range(10)]
        else:
            self.chromosomes = chromosomes

    def mutate(self):
        for chromosome in self.chromosomes:
            # High probability (0.9) to mutate the chromosome
            if random.random() < 0.9:
                chromosome.mutate()

    def get_values(self):
        return [chromosome.get_values() for chromosome in self.chromosomes]

    def is_all_ones(self):
        for chromosome in self.chromosomes:
            for gene in chromosome.genes:
                if gene.value == 0:
                    return False
        return True

    def __repr__(self):
        return "\n".join(repr(c) for c in self.chromosomes)

# --- Organism ---

class Organism:
    def __init__(self, dna: DNA, environment_mutation_prob):
        self.dna = dna
        self.environment_mutation_prob = environment_mutation_prob
        self.generations = 0

    def reproduce_and_mutate(self):
        self.generations += 1
        # High probability (0.8) to trigger DNA mutation based on environment
        if random.random() < self.environment_mutation_prob:
            self.dna.mutate()

    def __repr__(self):
        return f"Organism (Gens: {self.generations}, Mut Rate: {self.environment_mutation_prob})"

# --- Simulation ---

def run_simulation(num_organisms, environment_prob, max_generations=50000):
    organisms = [Organism(DNA(), environment_prob) for _ in range(num_organisms)]
    generation = 0
    winner = None

    print("Starting simulation...")

    while True:
        generation += 1
        
        # Safety stop condition
        if generation > max_generations:
            print(f"\nStopped after reaching {max_generations} generations (Max Limit).")
            return None

        for organism in organisms:
            organism.reproduce_and_mutate()
            if organism.dna.is_all_ones():
                winner = organism
                break
        
        if winner:
            break
        
        if generation % 5000 == 0:
            print(f"Generation {generation} reached. Still mutating...")

    return winner

# --- Main Execution ---

if __name__ == "__main__":
    
    NUM_ORGANISMS = 10
    ENVIRONMENT_MUTATION_PROBABILITY = 0.8
    MAX_ITERATIONS = 150000

    winning_organism = run_simulation(NUM_ORGANISMS, ENVIRONMENT_MUTATION_PROBABILITY, MAX_ITERATIONS)

    if winning_organism:
        print("\n=============================================")
        print("BIOLOGY RESEARCH NOTEBOOK: Successful Evolution")
        print("=============================================")
        print(f"Goal Reached: DNA composed entirely of 1s.")
        print(f"Winning Organism: {winning_organism}")
        print(f"Total Generations (Iterations) Required: {winning_organism.generations}")
        print(f"Environment Mutation Probability: {ENVIRONMENT_MUTATION_PROBABILITY}")
        print("\nFinal DNA State:")
        print(winning_organism.dna)
        print("\nConclusion: Due to high mutation probabilities (0.8 environment, 0.8/0.9 internal), the organism successfully achieved the target state (all 1s) within a reasonable number of generations.")
        print("=============================================")
    else:
        print("\nSimulation stopped; target DNA was not reached.")