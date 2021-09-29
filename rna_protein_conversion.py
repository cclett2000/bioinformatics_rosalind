# Charles Lett Jr.; Dr. Tilahun
# Bioinformatics
# September 24, 2021
# This script will take an RNA string and translate it into a protein

# codon chart the program will use to check which protein codon should be generated
codon_ref = {'UUU': 'F',      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
             'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
             'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
             'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
             'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
             'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
             'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
             'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
             'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
             'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
             'UAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
             'UAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
             'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
             'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
             'UGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
             'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G' }

# file handler
with open('../bioinformatics_rosalind/data_files/rosalind_prot.txt') as input_file:
    data = input_file.read()
    protein = [] # empty list for codon storage

    i = 0
    while i < len(data):
        temp_key = data[i: i+3] # stores the 3 letter key for codon retrieval
        if codon_ref.get(temp_key) == 'Stop':
            break
        else:
            # print(temp_key) # debug; shows temp key each iteration
            protein.append(codon_ref.get((temp_key)))

        i += 3

    print(''.join(protein))

