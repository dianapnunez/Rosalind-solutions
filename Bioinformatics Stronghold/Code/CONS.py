"""
Rosalind Problem ID: CONS
Title: Consensus and Profile
URL: https://rosalind.info/problems/cons/
Description: Given a collection of DNA strings in FASTA format, return a profile matrix and a corresponding consensus string.
"""

import os

"""
  Parses a raw FASTA file and collects all DNA sequences into a flat list, skipping header rows starting with '>'. current_seq  manages a temporary scratchpad while reading the file, and the final result gets stored in sequences.
  """
def parse_fasta(file_path):
    sequences = []
    current_seq = []

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Missing dataset at target location: {file_path}")

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_seq:
                    sequences.append("".join(current_seq))
                    current_seq = []
            else:
                current_seq.append(line)
        if current_seq:
            sequences.append("".join(current_seq))

    return sequences


#Constructs the 4xn counting profile matrix dictionary and derives the final high-frequency consensus sequence array.
def build_profile_and_consensus(sequences):
    seq_len = len(sequences[0])

    # Step 1: Initialize profile matrix dictionary arrays with zeros
    profile = {
        'A': [0] * seq_len,
        'C': [0] * seq_len,
        'G': [0] * seq_len,
        'T': [0] * seq_len
    }

    # Step 2: Populate nucleotide frequency arrays column by column
    for seq in sequences:
        for index, nucleotide in enumerate(seq):
            profile[nucleotide][index] += 1

    # Step 3: Compute the top consensus character for each index slice
    consensus_list = []
    for i in range(seq_len):
        max_count = -1
        best_nucleotide = ''

        # Check alphabetical order 'A', 'C', 'G', 'T' to naturally resolve any ties
        for base in ['A', 'C', 'G', 'T']:
            if profile[base][i] > max_count:
                max_count = profile[base][i]
                best_nucleotide = base

        consensus_list.append(best_nucleotide)

    consensus_string = "".join(consensus_list)
    return consensus_string, profile


def main():
    # Relative path pointing directly into your nested repository data directory
    data_file_path = os.path.join("..", "Data", "rosalind_cons.txt")

    try:
        # Load and parse sequences
        dna_sequences = parse_fasta(data_file_path)

        # Calculate matrix models
        consensus, profile_matrix = build_profile_and_consensus(dna_sequences)

        # Print outputs exactly matching Rosalind's target verification format
        print(consensus)
        for base in ['A', 'C', 'G', 'T']:
            counts_str = " ".join(map(str, profile_matrix[base]))
            print(f"{base}: {counts_str}")

    except FileNotFoundError as e:
        print(e)
        print("💡 Tip: Ensure your dataset file is named 'rosalind_cons.txt' inside the Data folder.")

# Script entry point: executes the pipeline only when run directly
if __name__ == "__main__":
    main()
