#!/common/appl/python/python-3.6.4/bin/python3
import warnings
import sys
import os
import subprocess
import argparse
# Created on 03/20/2024
#usage: findd -dir . -findd <the name need to find> -exec "vimx -p"
#usage: findd -findd <the name need to find> -exec "vimx -p"   in this case it will use the current dir, if -exec none it will excute the vimx -o command.
#usage: use -f "*_address.equ" to find more file 

# continuue: the file searce if use *, need to input *_axad, cannot use *axad ? why
# how to pass 2 variable into a command in pythong in os command Solved
parser = argparse.ArgumentParser(description="Register for MPG and MR flow verification")
parser.add_argument("-d", help="This is option", required=False)
parser.add_argument("-f", help="This is option", required=False)
parser.add_argument("-e", help="This is option", required=False)
parser.add_argument("-n", help="This is option", required=False)
args = parser.parse_args()
where_I_find = str(args.d)
if str(args.d) == "None":
  where_I_find = "."
mydir = where_I_find + ' -name ' +  "'" +str(args.f) + "'"
print(mydir)
subprocess.run("touch findd_list_list_list", shell = True)
subprocess.run("truncate -s 0 findd_list_list_list", shell = True)
os.system("find %s > findd_list_list_list"%(mydir))
print(f"{mydir}")

subprocess.run("cat findd_list_list_list", shell = True)
print("\nExcuting ...")
dir1 = open('findd_list_list_list', 'r')
Lines = dir1.readlines()
dir1.close()


# if str(args.n) == "None":

mylines = ""
for line in Lines:
  mylines = str(line.strip())
  cmd = str(args.e)
  if cmd == "None":
    cmd = "echo "
    os.system('%s  %s'%(cmd,mylines))
  else:
      cmd = cmd.replace("xx", mylines)
      for sub_cmd in cmd.split(";"):
        os.system('%s'%(sub_cmd))

# else:
#
#   mylines = ""
#   for line in Lines:
#     mylines = str(line.strip())
#     cmd = str(args.e)
#     if cmd == "None":
#       cmd = "echo "
#     os.system('echo %s'%(mylines))
#     os.system('%s  %s'%(cmd,mylines))

subprocess.run('rm -f findd_list_list_list', shell = True)



