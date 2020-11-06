# Seeking for the longest word in a Dictionary

from collections import Counter
import time

words = open('filename').read().splitlines()

time_before = time.time()

k = Counter(words)

longest = max(k, key=len)
print('The longest word in Dictionary is:', longest, 'has' , len(longest), 'characters')

time_after = time.time()
time_taken = time_after - time_before
print ( 'Longest word found in: ' , time_taken)
print(".......................")




