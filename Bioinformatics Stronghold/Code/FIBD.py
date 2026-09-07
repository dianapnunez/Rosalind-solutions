"""
Rosalind Problem ID: FIBD
Title: Mortal Fibonacci Rabbits
URL: https://rosalind.info
Description: Given positive integers n and m, return the total number of pairs
             of rabbits that remain after the n-th month if all rabbits live
             for exactly m months.
"""

import os

"""
   Computes the remaining rabbit population using a tracking array where
   index i represents the number of rabbit pairs that are i months old.
   """
def solve_mortal_rabbits(n, m):
    # Initialize an age-cohort list of size m with zeros
    # index 0 = 0 months old (newborns), index m-1 = oldest possible living group
    age_cohorts = [0] * m

    # Month 1 setup: exactly 1 newborn pair of rabbits
    age_cohorts[0] = 1

    # Simulate months from Month 2 up to Month n
    for month in range(1, n):
        # 1. Calculate newborns: every adult (age >= 1) produces 1 newborn pair
        newborns = sum(age_cohorts[1:])

        # 2. Shift generations: shift older populations right by 1 month aging step
        # We walk backwards through the array to avoid overwriting values
        for age in range(m - 1, 0, -1):
            age_cohorts[age] = age_cohorts[age - 1]

        # 3. Insert the newly generated babies into the age 0 slot
        # (The rabbits that were previously at index m-1 naturally drop off and die)
        age_cohorts[0] = newborns

    # The total surviving population is the sum of all remaining age cohorts
    return sum(age_cohorts)


def main():
    # Relative path pointing into your repository data directory
    data_file_path = os.path.join("..", "Data", "rosalind_fibd.txt")

    try:
        if not os.path.exists(data_file_path):
            raise FileNotFoundError(f"Missing dataset at target location: {data_file_path}")

        with open(data_file_path, 'r') as f:
            line = f.read().strip()
            if not line:
                return
            # Parse the two input integers (n = target months, m = lifespan)
            n, m = map(int, line.split())

        # Compute the structural population model
        total_rabbits = solve_mortal_rabbits(n, m)
        print(total_rabbits)

    except FileNotFoundError as e:
        print(e)
        print("💡 Tip: Ensure your dataset file is named 'rosalind_fibd.txt' inside your Data folder.")


# Script entry point: executes the pipeline only when run directly
if __name__ == "__main__":
    main()
