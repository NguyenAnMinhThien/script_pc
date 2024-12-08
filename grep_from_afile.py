#!/common/appl/python/python-3.6.4/bin/python3
import warnings
import argparse
import sys
import re
file1 = sys.argv[1] #need to grep from other files.
file2 = sys.argv[2] 


#pattern =  re.compile(r'axrt$')
#text_file = open("./probe.tcl", "r")
text_file = open(file1, "r")
for line in text_file:
  linee = line.strip()
  text_file2 = open(file2, "r")
  for line2 in text_file2:
    if re.search(linee,line2):
      linee2 = line2.strip()
      print(linee2)

