# Charles Lett Jr.; Dr. Tilahun
# Bioinformatics
# August 23, 2021
# test script to count the number of each nucleotide in a given file

# var
A = 0
G = 0
T = 0
C = 0

# file
path = '/rosalind_dna.txt'
file = open(path)
file = file.read()

# counter
for i in file:
    if i == 'A':
        A += 1
    elif i == 'G':
        G += 1
    elif i == 'C':
        C += 1
    elif i == 'T':
        T += 1

# output
print(A, C, G, T)
