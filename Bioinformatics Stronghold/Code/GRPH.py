"""
Rosalind Problem ID: GRPH
Title: Overlap Graphs
URL: https://rosalind.info/problems/grph/
Description: Given a collection of DNA strings in FASTA format, return the
             adjacency list corresponding to its overlap graph for a
             threshold value of k=3.
"""

import sys


def parse_fasta(file_path):
    """Parses a FASTA file and returns a dictionary of {ID: DNA_string}."""
    sequences = {}
    current_id = None
    current_seq = []

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                if current_id:
                    sequences[current_id] = "".join(current_seq)
                current_id = line[1:]  # Strip the '>' character
                current_seq = []
            else:
                current_seq.append(line)
        if current_id:
            sequences[current_id] = "".join(current_seq)

    return sequences


def find_overlap_graph(sequences, k=3):
    """Finds all directed edges where the suffix of s matches the prefix of t."""
    edges = []

    # Compare every sequence with every other sequence
    for id_s, seq_s in sequences.items():
        for id_t, seq_t in sequences.items():
            if id_s == id_t:
                continue  # Skip comparing a sequence to itself

            # Get the suffix of length k from sequence s
            suffix = seq_s[-k:]
            # Get the prefix of length k from sequence t
            prefix = seq_t[:k]

            if suffix == prefix:
                edges.append((id_s, id_t))

    return edges


def main():
    # Update this path to match your local file name inside your Data folder
    file_path = "../Data/rosalind_grph.txt"

    try:
        sequences = parse_fasta(file_path)
        overlap_edges = find_overlap_graph(sequences, k=3)

        # Print the adjacency list in the exact format Rosalind expects
        for id_s, id_t in overlap_edges:
            print(f"{id_s} {id_t}")

    except FileNotFoundError:
        print(f"Error: Could not find the file at {file_path}. Please check your path.")


if __name__ == "__main__":
    main()
