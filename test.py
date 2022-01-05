# -*- coding: utf8 -*-
import os
os.chdir('/Users/naco/Desktop/regex_name')
a_file = open("blacklist.txt", "r")

list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(line_list)
a_file.close()
unique = []
for name in list_of_lists:         # 1st loop
   if name not in unique:   # 2nd loop
      unique.append(name)
print(unique)
textfile = open("a_file.txt", "w", encoding='utf-8')
for element in unique:
    textfile.write(element + "\n")
textfile.close()
