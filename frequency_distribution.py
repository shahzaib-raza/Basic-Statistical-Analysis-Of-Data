# imports required

import numpy as np
import string
import math
import pandas as pd
import statistics

# generating random 60 values for testing program

li = np.random.randint(1, 100, 60)

# calculating and measuring basic info of data and print them on screen

minimum = li.min()
maximum = li.max()
list_range = maximum - minimum
no_of_classes = round(1+(3.3*(math.log(60, 10))))
class_width = round(int(list_range/no_of_classes))
print('\nMinimum value of data: ', minimum)
print('\nMaximum value of data: ', maximum)
print('\nrange of data: ', list_range)
print('\nno. of classes : ', no_of_classes)
print('\nwidth of classes: ', class_width, '\n')

# making empty lists for frequency distribution columns

class_intervals = []
fr = []
mp = []
cf = []

# performs a while loop for inserting row values of frequency distribution columns

n = li.min()
while n <= maximum:
    # lower_class_limit
    lower_class = n
    # upper_class_limit
    upper_class = n + class_width
    # converting class limits into string to represent them in an arranged manner
    lc = str(lower_class)
    uc = str(upper_class)
    iClass = str(lc+'---'+uc)
    class_intervals.append(iClass)
    # performs a for loop for calculating frequency of class(just like telly marks)
    freq = 0
    for val in li:
        if val in range(lower_class, (upper_class+1)):
            freq += 1
    fr.append(freq)
    # calculating mid points
    mid = (lower_class+upper_class)/2
    mp.append(mid)
    n += (class_width + 1)

# calculating cumulative frequencies
f = 0
for freq in fr:
    f += freq
    cf.append(f)

# creating a numPy arrays of columns of frequency distribution
frequencies = np.array(fr)
mid_points = np.array(mp)
cum_frequencies = np.array(cf)

freq_mid = frequencies * mid_points

# creating header for data frame
headings = ['  Class Intervals', '  Frequencies(f)', '  Mid Points(x)', '  Cum.Freq.(C.F)', '  (f.x)']

# creating table for PanDAs data_frame
tab = [freq_mid, cum_frequencies, mid_points, frequencies, class_intervals]
table = np.vstack(np.flip(np.rot90(tab)))

# creating frequency ditribution table in PanDAs data_frame
data = pd.DataFrame(data=table, columns=headings)
print(data)

# calculating mean, mode & median
mean = statistics.mean(li)
med = statistics.median(li)
mode = statistics.mode(li)
print('\nMean of data is: ', mean)
print('\nMedian of data is: ', med)
print('\nMode of data is: ', mode)


# comments with respect to results
if mode < med < mean:
    print('\nGiven data set is skewed to left side.')
elif mode > med > mean:
    print('\nGiven data set is skewed to right side.')
elif mode == med == mean:
    print('\nThe given data set is normally distributed.')
