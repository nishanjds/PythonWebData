# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 18:20:38 2017

@author: Nishanthan Kamaleson

Assignment : Finding Numbers in a Haystack
Description : Read through and parse a file with text and numbers. Later, extract all the numbers in the file and compute the sum of the numbers.
"""

# Import Regex Library
import re

# Define the path for the given files
path_1 = 'Data/regex_sum_42.txt'
path_2 = 'Data/regex_sum_41927.txt'

# Initialise the total as zero
total = 0

# Open the file
with open(path_2) as file :
    
    # Read the lines
    for line in file :
        # Pattern match for numbers
        snumbers = re.findall('[0-9]+', line)
        # Convert the snumbers to floats
        numbers = list(map(int, snumbers))
        # Add the numbers to total 
        total += sum(numbers)
        
# Print the total
print(total)        
        

# Compact code
print(sum([int(num) for num in re.findall('[0-9]+', open(path_2).read())]))