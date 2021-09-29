# Charles Lett Jr.; Dr. Tilahun
# Bioinformatics
# August 25, 2021
# Test script to create a complimentary DNA sequence

path = "../bioinformatics_rosalind/data_files/rosalind_rna.txt"
dna_ref = {'A', 'G', 'T', 'C'}
temp = []

# open file
with open (path, 'r') as file:
    content = file.read()

# reverse data
for line in reversed(content):
    temp.append(line)

# replace data
for pos in range(len(temp)):
    if temp[pos] not in dna_ref:
        temp[pos] = ''

    elif temp[pos] == 'A':
        temp[pos] = 'T'

    elif temp[pos] == 'G':
        temp[pos] = 'C'

    elif temp[pos] == 'T':
        temp[pos] = 'A'

    elif temp[pos] == 'C':
        temp[pos] = 'G'

# convert list to string
temp = ''.join(temp)

# output
print(temp)