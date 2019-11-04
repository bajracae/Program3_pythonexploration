####################################################################################################
# Author: Aeijan Bajracharya
# Title: Program 3 - pythonexploration
# Description: The program creates 3 files, writes ten random characters into each file, and takes 
# two random numbers and finds the product of the two. All of these are printed onto the terminal
# interface.
# Date: 11/4/19
####################################################################################################

import string
import random
import sys

f = open("cabagge.txt", "w");
g = open("eggplant.txt", "w");
h = open("potato.txt", "w");

####################################################################################################
# Source: stackoverflow
# Post: Generate a random letter in Python
# Author: Mark Rushakoff, John R Perry
# Code version: N/A 
# Availability: https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
####################################################################################################
for i in range(10):
    f.write(random.choice(string.ascii_lowercase));
    g.write(random.choice(string.ascii_lowercase));
    h.write(random.choice(string.ascii_lowercase));
    if(i == 9):
        f.write('\n');
        g.write('\n');
        h.write('\n');

f.close();
g.close();
h.close();
    
####################################################################################################
# Source: stackoverflow
# Post: The difference between sys.stdout.write and print?
# Author: dogbane, AkshayNevrekar
# Code version: N/A 
# Availability: https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print
####################################################################################################
a = open('cabagge.txt');
r = a.read();
sys.stdout.write(r);

b = open('eggplant.txt');
r = b.read();
sys.stdout.write(r);

c = open('potato.txt');
r = c.read();
sys.stdout.write(r);

####################################################################################################
# Source: Python Central
# Post: How to Generate a Random Number in Python
# Author: Jackson Cooper
# Code version: N/A 
# Availability: https://www.pythoncentral.io/how-to-generate-a-random-number-in-python/
####################################################################################################
num1 = random.randint(1, 42);
num2 = random.randint(1, 42);
print(num1);
print(num2);
print(num1 * num2);
