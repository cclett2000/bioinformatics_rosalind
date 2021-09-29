# Charles Lett Jr.; Dr. Tilahun
# Bioinformatics
# September 8, 2021
# this script will calculate Hamming distance between two DNA sequences

blacklist = {'\n'}

with open('../bioinformatics_rosalind/data_files/rosalind_hamm.txt') as input_file:
    temp = []

    # works through file then appends to temp array
    for pos in input_file:
        # cleaner removes non-essential characters
        cleaner = ''.join(i for i in pos if i not in blacklist)
        temp.append(cleaner)

# calculates Hamming Distance (Number of changes needed to make both strings match)
ham_dist = 0
for j in range(len(temp[0])):
    if temp[0][j] != temp[1][j]:
        ham_dist += 1


print(ham_dist)