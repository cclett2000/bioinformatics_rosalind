# Charles Lett Jr.; Dr. Tilahun
# Bioinformatics
# August 27 2021
# this script calculates GC richness from a .fasta file and then output the ID with the highest GC richness

from Bio import SeqIO
from Bio.SeqUtils import GC

def preprocessing():
    gc_data = []

    # calls file and runs BioPython on it to get id and GC content
    with open('../bioinformatics_rosalind/data_files/rosalind_gc.txt') as input_file:
        for record in SeqIO.parse(input_file, 'fasta'):
            gc_data.append([record.id, GC(record.seq)])

    # get highest GC content
    max_gc = max(gc_data)
    for i in range(len(max_gc)):
        print(max_gc[i])

preprocessing()