# python-challenge
## RU03-python

This directory contains PyBank and PyPoll subdirectories. Each contains a program (main.py) designed to analyze data kept in .csv files within resource subdirectories. Each also contains a file to show respective program results (results.txt).

### PyBank
This program puts output into one string variable rather than output or write information to the file incrementally. Formatting functions were used with the final table dollar values. There is also a variable initialized with a value of "None" to catch the first time the variable is updated with real data within the loop.

### PyPoll
I tried to keep track of unique voter IDs in a list to guard against repeat votes, but soon found my screen frozen as the program tried to check each row against the list. So proceeded without the check, guessing there were no repeat voter IDs, but was curious how to more efficiently look for duplicate values in a large data set.
