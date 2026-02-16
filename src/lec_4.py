# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:15:22 2025

@author: pathouli
"""

from utils import *

the_path = "C:/Users/pathouli/Box Sync/myStuff/academia/torhea/fall_2025/data/"

the_data = file_walker(the_path)

#get summary statistics for a specific column
print (the_data["label"].value_counts())

#concatenate an entire column of strings in a pd
all_text = the_data["body"].str.cat(sep=" ")
#what is count of ALL tokens?
print ("total tokens:", len(all_text.split()))

#what is count of unique token
print ("total tokens:", len(set(all_text.split())))


#https://docs.python.org/3/library/os.html
import collections 
the_dictionary=dict()
the_dictionary["all"]=collections.Counter(all_text.split())






"""
Create pandas dataframe, which will have 2 columns
1. Body that will contain tmp
2. Label that contain the directory name: fishing, hiking, machinelearning
mathematics
"""


#test_tmp = file_reader(full_path)

# ex = j("the cat jumped over the bed", 
#        "the dog chased the cat")
#print (ex)

"""create a function called word_fun that outputs a dictionary where every 
key is a unique token and the value is the number of times that token shows up
in the input corpus"""

"""red red blue purple --> {'red': 2, 'blue': 1, 'purple': 1}
"""

#test = word_fun("the cat and the dog chased the cat")
#
#https://docs.python.org/3/library/re.html
#lower case everything and replace any non letter with a " "
#https://www.asciitable.com/

#test = clean_txt(str_in)
#str_t = "The! cat and the dog123_ chased[] the cat!!"
#test_wf = word_fun(str_t)
#print (test_wf)

# f = open(full_path, "r")
# text = f.readlines()
# f.close()

#f = open(full_path, "r")
#text = f.readline()
#print (text)
#f.close()

#good for VERY large files
# with open(full_path, "r") as file:
#     while True:
#         line = file.readline()
#         print (line)
#         if not line:
#             break




