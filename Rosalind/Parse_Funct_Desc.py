__author__ = 'ravi'

import re

in_file = open("/Users/ravi/Desktop/TAIR9_functional_descriptions.txt",'rU')

for line in in_file:
    line_elements = line.split('\t') # split each line by tab into an array
    Model_name = line_elements[0]
    Type = line_elements[1]
    Short_description = line_elements[2]
    Curator_summary = line_elements[3]
    Computational_description = line_elements[4] # this is the array element we want to parse out

    print Model_name + "\t" + Type + "\t" + Short_description + "\t" + Curator_summary + "\t", # print out the first three columns of each row which don't need to be messed with

    keywords = ['FUNCTIONS IN','LOCATED IN', 'EXPRESSED IN', 'INVOLVED IN', 'EXPRESSED DURING', 'CONTAINS InterPro DOMAIN/s','BEST Arabidopsis thaliana protein match is'] # these are the keywords which we will use to split column 4 by
    for keyword in keywords:
        regex = re.escape(keyword) + ':.+?;' # construct a regular expression, which will look for the keyword followed by :<bunch_of_text_with_spaces><ending in ;> The <bunch of text with spaces> is represented in regex as .+ the ?; makes is so you only search till the first ; and not be greedy
        keyword_match = re.search(regex,Computational_description)
        if keyword_match: print keyword_match.group() + "\t", # if keyword regular exp is found print it out followed by a tab and go to the next keyword
        else: print "\t",# if not found then print an empty tab, this lines up your keywords across all entries.
    print "\n"

in_file.close()
