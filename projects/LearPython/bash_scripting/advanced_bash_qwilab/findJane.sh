# Prerequisites
# For this lab, you should have a sound knowledge of these Linux commands:

# cat
# grep
# cut
# cat:

# The cat command allows us to create single or multiple files, view the contents of a file, concatenate files, and redirect output in terminal or other files.

# Syntax:

# cat [file]
# grep:

# The grep command, which stands for "global regular expression print", processes text line-by-line and prints any lines that match a specified pattern.

# Syntax:

# grep [pattern] [file-directory]
# Here, [file-directory] is the path to the directory/folder where you want to perform a search operation. The grep command is also used to search text and match a string or pattern within a file.

# Syntax:

# grep [pattern] [file-location]
# cut:

# The cut command extracts a given number of characters or columns from a file. A delimiter is a character or set of characters that separate text strings.

# Syntax:

# cut [options] [file]
# For delimiter separated fields, the - d option is used. The -f option specifies the field, a set of fields, or a range of fields to be extracted.

# Syntax:

# cut -d [delimiter] -f [field number]
# Linux I/O Redirection
# Redirection is defined as switching standard streams of data from either a user-specified source or user-specified destination. Here are the following streams used in I/O redirection:

# Redirection into a file using >

# Append using >>

# Redirection into a file
# Each stream uses redirection commands. A single greater than sign (>) or a double greater than sign (>>) can be used to redirect standard output. If the target file doesn't exist, a new file with the same name will be created.

# Commands with a single greater than sign (>) overwrite existing file content.

# cat > [file]
# Commands with a double greater than sign (>>) do not overwrite the existing file content, but it will append to it.

# cat >> [file]
# So, rather than creating a file, the >> command is used to append a word or string to the existing file.

# find 
# -------
# grep 'jane' ../data/list.txt

# grep " jane " ../data/list.txt | cut -d ' ' -f 1-3


# testing
# ----------

# if test -e ~/data/jane_profile_07272018.doc; then echo "File exists"; else echo "File doesn't exist"; fi

# for loop
# ---------
# for i in 1 2 3; do echo $i; done



# exercise 

#!/bin/bash

> oldFiles.txt

files=$(grep  " jane " ../data/list.txt | cut -d ' ' -f 3)

for i in $files;do
     if test -e $HOME$i; then
        echo $HOME$i>> oldFiles.txt
    else
        echo "File doesn't exist";fi 
done



#!/usr/bin/env python3

import sys
import subprocess

file = open(sys.argv[1],"r")
path='/home/<username>'
for line in file.readlines():
#  print(line)
  old_name = line.strip()
  new_name = old_name.replace("jane","jdoe")
  subprocess.run(["mv", old_name, new_name])
file.close()
