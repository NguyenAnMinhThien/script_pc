#!/common/appl/python/python-3.6.4/bin/python3
import warnings
import argparse
import sys
import os
# usage: gitt file1 "comment.."
# usage: gitt "file1 file2" "comment for 2 files.."
file = sys.argv[1]
commit = sys.argv[2]
commit = '"' + commit + " at file " + file + '"'

print(f" {file} ")
print(f" {commit} ")
#os.system('echo %s %s'%(file, commit)) #this have worked
# the link to ref: the problem is dueto os.system only take the argument like a string
#  https://stackoverflow.com/questions/22101931/passing-more-than-one-variables-to-os-system-in-python

#os.system('csh '$file + "   " + $commit')
#os.system('csh '$file + "   " + $commit')
#
os.system('git add %s'%(file)) #this have worked
os.system('git commit -m %s'%(commit)) #this have worked
#f = open("./lib/template_standby_msys/main.s", "r")
#main = f.read()
#main_new = main.replace("<MASK_VALUE1>", mask1)
#main_new = main_new.replace("<SET_REG>", set_reg)
#main_new = main_new.replace("<MASK_VALUE2>", mask2)
#main_new = main_new.replace("<MASK_VALUE3>", mask3)
#main_new = main_new.replace("<STATUS_REG>", stat_reg)
#main_new = main_new.replace("<PROT_REG>", prot_reg)
#f.close()
#
#
#f = open("main_standby.s", "w")
#f.write(main_new)
#f.close()
#
#
## Create for test.s
#f = open("./lib/template_standby_msys/test.s", "r")
#test = f.read()
#test_new = test.replace("<BUS_MODULE>", myarray[0])
#f.close()
#
#f = open("test_standby.s", "w")
#f.write(test_new)
#f.close()
#
#set file = $argv[1]
#set commit = $argv[2]
#echo "$file $commit"
#echo "$commit"
