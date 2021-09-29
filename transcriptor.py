# Charles Lett Jr.; Dr. Tilahun
# Bioinformatics
# August 23, 2021
# test script to transcribe DNA to RNA

path = '../bioinformatics_rosalind/data_files/rosalind_rna.txt'

# open file
with open (path, 'r') as file:
    file_content = file.read()

file_content = file_content.replace('T', 'U')

print(file_content)



