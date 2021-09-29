# Charles Lett Jr.; Dr. Tilahun
# Bioinformatics
# August 25, 2021
# recurrence algorithm

import pandas as pd

# file handler / data collector
file_cont = pd.read_csv('../bioinformatics_rosalind/data_files/rosalind_fib.txt', sep=' ', header=None)

# convert pandas dataframe to list
data = file_cont.values.tolist()

n = data[0][0] # aka months
k = data[0][1] # aka rabbits per pair

adult_arr = [] # adult rabbits each month
baby_arr = [] # baby rabbits each month

for i in range(n):
    if i == 0 or i == 1 :
        # init data arrays
        adult_arr.append(1)
        baby_arr.append(k)
    else:
        a_temp = adult_arr[i - 1] + baby_arr[i - 1] # calc for adult_arr
        b_temp = adult_arr[i - 1] * k # calc for baby_arr

        # populate data arrays with remaining data
        adult_arr.append(a_temp)
        baby_arr.append(b_temp)

print('adult_arr', adult_arr)
print('baby_arr', baby_arr)