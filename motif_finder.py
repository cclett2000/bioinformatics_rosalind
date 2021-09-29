# Charles Lett Jr.; Dr. Tilahun
# Bioinformatics
# September 27, 2021
# Script to identify motif positions within a sequence of DNA;

occur_loc = []
with open('../bioinformatics_rosalind/data_files/motif_samp.txt') as input_file:
    # '.readlines()' stores all lines in a list; neat
    data = input_file.readlines()
    seq = data[0]
    key = data[1]

# file handler
#  - store sequence/key(motif);

# seq analysis
#  - compare key to partitions of the sequence
#  - store pos-id in empty array;