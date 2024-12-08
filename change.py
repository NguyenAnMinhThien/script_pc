#!/common/appl/python/python-3.6.4/bin/python3
import warnings
import argparse
import openpyxl
import sys
import re

source = sys.argv[1]
template = sys.argv[2]
destination = sys.argv[3]
# How to replace a mask value with an explicit value, how to replace a variable naming with a value
# this include 3 file, main.s is the template, main_standby is the destination with multiple template creation, source is the where store all file will need to replaced.
# usagen: change.py source template destination : with source contain all element need to replaced, template contain x value, destination will be coppy out from template. No limit the number of mask value. 
print(source)
source = open(source, 'r')

print(source)
main_standby = ""
Lines = source.readlines()
for line in Lines:
  i = 0
  my_masks = str(line.strip()).split()
  f = open(template, "r")
  main = f.read()
  print(f"{my_masks}")
  while (i < len(my_masks)):
    print("hehe")
    print(my_masks[i])

    print(f"mask{i}")
    main = main.replace(f"mask{i}", my_masks[i])
    i = i + 1

  f.close()
  main_standby = main_standby + main +  "\n"

print(main_standby)
f = open(destination, "w")
f.write(main_standby)
f.close()

