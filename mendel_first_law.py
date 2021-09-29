# Charles Lett Jr.; Dr. Tilahun
# Bioinformatics
# September 20, 2021 (HBDGM!)
# Second attempt at solving Mendel's first law problem from Rosalind
# ***not finished yet***

with open('../bioinformatics_rosalind/data_files/sample.txt') as input_file:
    count_dat = input_file.read()
    count_dat = count_dat.split(' ')
    count_dat = [int(i) for i in count_dat] # convert str to int

    dat_lst = [['hom_dom', count_dat[0]], # 0
               ['het_dom', count_dat[1]], # 1
               ['hom_rec', count_dat[2]], # 2
               sum(count_dat)]            # -1 - total
    print(dat_lst)