#!/common/appl/python/python-3.6.4/bin/python3
import warnings
import sys
import os
import subprocess
import argparse
# ref: https://stackoverflow.com/questions/89228/how-do-i-execute-a-program-or-call-a-system-command
# ref: https://stackoverflow.com/questions/14622314/python-inserting-variable-string-as-file-name
# we use subprocess to excute a specific command, but if we want to pass a variable to shell from a var of py, do it by os.system
# In this code, you can learn: pass a file variable to an open function, excute any command in csh via python, use if else, transfero a argument via py script

#usage: kill.py /shsv/ipw1/BUS/users/thiennguyen/temp//killme_0316 killl

#these command cannot excute the ps x command
#cmd = 'ps x \| egrep \"xterm.*axrt1\" > ! kill_list_list_list '
#cmd = 'csh ps x | egrep "xterm.*axrt1" > ! kill_list_list_list'
#cmd = 'ps x | egrep "xterm.*axrt1" > ! kill_list_list_list'
#print(f"{cmd}")
#cmd = 'ps x \| egrep \"xterm.*axrt1\" > ! kill_list_list_list '
#os.system('%s'%(cmd))
#os.system("ps x | egrep \"xterm.*axrt1\" > ! kill_list_list_list")
#os.system("ps x | egrep xterm > ! kill_list_list_list")
#os.system("ps x  >! kill_list_list_list")

parser = argparse.ArgumentParser(description="Register for MPG and MR flow verification")
parser.add_argument("-file", help="This is option", required=False)
parser.add_argument("-kill", help="This is option", required=False)
args = parser.parse_args()
print(f"{args.kill}")
print(f"{args.file}")

#A comment : not use !, the name of file with . for hiden file in python. Use ' ' to make the " " inside that command, 
subprocess.run("touch kill_list_list_list", shell = True)
subprocess.run("truncate -s 0 kill_list_list_list", shell = True)
if args.kill=="kill -9":
  subprocess.run('ps x | egrep "xterm.*" > kill_list_list_list', shell = True)
elif args.kill=="bkill":
  subprocess.run('bjobs | egrep x5h_frun > kill_list_list_list', shell = True)
#print(f"{len(sys.argv)}")  We will not use this argv without parser, because with the arg sometime need and sometime no need, the good way is to use parser
myfile= str(args.file).strip()
# args.file : This is nonetype object, so if u want to use, must transfer to string first
print(f"{myfile}")
#if len(sys.argv)>1:
#  print(f"{sys.argv[1]}")
#  myfile = sys.argv[1]
if myfile=="None":
  subprocess.run("cat kill_list_list_list", shell = True)
  #
  # Using readlines()
  file1 = open('kill_list_list_list', 'r')
  Lines = file1.readlines()
else:
  os.system("cat %s"%(myfile))
  #
  # Using readlines()
  file1 = open('%s'% myfile, 'r')
  Lines = file1.readlines()
 
# Strips the newline character
for line in Lines:
  myid = line.split()
  id = myid[0]
  #print(f"{myid[0]}")
  #subprocess.run("echo %s"%(myid[0])) This is not work
  # subprocess.run("echo $id", shell = True)
  #subprocess.run("kill -9 %s"%myid[0])
  #subprocess.run("echo $line", shell = True)
  os.system('echo %s'%(myid[0])) 

subprocess.run('rm -f kill_list_list_list', shell = True)
print("Please add killl option to kill them")

if args.kill=="kill -9":
  for line in Lines:
    myid = line.split()
    os.system('kill -9 %s'%(myid[0])) 
    print("Have killed them")
elif args.kill=="bkill":
  for line in Lines:
    myid = line.split()
    os.system('bkill %s'%(myid[0])) 
    print("Have bkill them")
#
#if len(sys.argv)>1:
#  if sys.argv[1]=="killl":
#    for line in Lines:
#      myid = line.split()
#      os.system('kill -9 %s'%(myid[0])) 
#      print("Have killed them")

## Using readlines()
#file1 = open('kill_list_list_list', 'r')
#Lines = file1.readlines()
# 
#count = 0
## Strips the newline character
#for line in Lines:
#    count += 1
#    print("Line{}: {}".format(count, line.strip()))



#set kill_list_list_list = `cat .kill_list_list_list`
#echo "$kill_list_list_list"
#foreach line (`cat .kill_list_list_list`)
#  echo "$line"
##  set kill = `echo $line | awk -F' ' 'print $1'`
##  echo "$kill"
#end
