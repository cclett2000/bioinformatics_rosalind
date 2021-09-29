# Charles Lett Jr.; Dr. Tilahun
# Bioinformatics
# September 8, 2021
# This script will calculate the probability of two organisms creating
# an organism that has dominant alleles

from random import choices

# 0 = homozygous dominant (YY)
# 1 = 0 heterozygous (Yy)
# 2 = 0 homozygous recessive (yy)
# holds number for each phenotype

# number of times to run probability
# - higher numbers produce better accuracy at a higher runtime;
i = 35000

# file handler
with open('../data_files/sample.txt') as input_file:
    data = input_file.read()
    data = data.split(' ')

    # phenotype/weight storage
    # weight is the number of each organism type; used for probability calculation
    dom, rec = 0, 0
    organism = ['hom_dom', 'het_dom', 'hom_rec']
    weights = [int(data[0]),int(data[1]), int(data[2])]

    for j in range(i):
        test = choices(organism, weights=weights, k=2)

        # increment respective var
        if 'hom_dom' and 'het_dom' not in test:
            rec += 1
        elif 'hom_dom' or 'het_dom' in test:
            dom += 1

        # print(test)

    # calculation: dominant probability
    calc = round(dom / i, 5)
    print(dom,  rec)
    print(calc)

