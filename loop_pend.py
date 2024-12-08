#!/common/appl/python/python-3.6.4/bin/python3
import warnings
import sys
import os
import subprocess
import argparse
import time

parser = argparse.ArgumentParser(description="Register for MPG and MR flow verification")
parser.add_argument("-file", help="This is option", required=False)
parser.add_argument("-pend", help="This is option", required=False)
parser.add_argument("-server", help="This is option", required=False)
parser.add_argument("-find", help="This is option", required=False)

args = parser.parse_args()
print(f"{args.pend}")
print(f"{args.file}")
print(f"{args.server}")
if args.server=="regression server":
  servers = ["rvc-srv0305", "rvc-srv0306", "rvc-srv0307"]
else:
  #servers = ["rvc-srv0300", "rvc-srv0301", "rvc-srv0302", "rvc-srv0303", "rvc-srv0304", "rvc-srv0305", "rvc-srv0306", "rvc-srv0307", "rvc-srv0308", "rvc-srv0309"]
  servers = ["rvc-srv0305", "rvc-srv0306", "rvc-srv0307"]
print(len(servers))
print(f"{args.server}")
print(servers[0])
subprocess.run("touch pend_pend_pend", shell = True)
subprocess.run("truncate -s 0 pend_pend_pend", shell = True)
#bjobs_found = subprocess.run('bjobs | egrep "PEND.*x5h_frun"', shell = True)
#print(str(bjobs_found))
#if (bjobs_found == "No unfinished job found") :
#  print(f"hehehe {bjobs_found}")
if args.find=="frun":
    print("huhu")
    subprocess.run('bjobs | egrep "PEND.*x5h_frun" > pend_pend_pend', shell = True)
elif args.find=="fsim":
  print("hehe")
  subprocess.run('bjobs | egrep "PEND.*x5h_fsim" > pend_pend_pend', shell = True)
elif args.find=="make":
  subprocess.run('bjobs | egrep "PEND.*make" > pend_pend_pend', shell = True)
elif args.find=="MAKE":
  subprocess.run('bjobs | egrep "PEND.*MAKE" > pend_pend_pend', shell = True)
else:
  print("Please input the arguments for find")

myfile = "pend_pend_pend"
file_stats = os.stat(myfile)
print(file_stats.st_size)
#loop the servers for any bjobs need to run
i = 0
#condition to finish
while file_stats.st_size!=0:
  #condition for finish hope

  if args.find=="frun":
    print("huhu")
    subprocess.run('bjobs | egrep "PEND.*x5h_frun" > pend_pend_pend', shell = True)
  elif args.find=="fsim":
    print("hehe")
    subprocess.run('bjobs | egrep "PEND.*x5h_fsim" > pend_pend_pend', shell = True)
  elif args.find=="make":
    subprocess.run('bjobs | egrep "PEND.*make" > pend_pend_pend', shell = True)
  elif args.find=="MAKE":
    subprocess.run('bjobs | egrep "PEND.*MAKE" > pend_pend_pend', shell = True)
  else:
    print("Please input the arguments for find")

#  elif args.find=="fsim":
#    subprocess.run('bjobs | egrep "PEND.*x5h_fsim" > pend_pend_pend', shell = True)
#  elif args.find=="make":
#    subprocess.run('bjobs | egrep "PEND.*make" > pend_pend_pend', shell = True)
#  elif args.find=="MAKE":
#    subprocess.run('bjobs | egrep "PEND.*MAKE" > pend_pend_pend', shell = True)
#  else:
#    print("Please input the arguments for find")

  myfile = "pend_pend_pend"
  file_stats = os.stat(myfile)
  
  #file has the id 
  myfile= str(args.file).strip()
  print(f"{myfile}")
  if myfile=="None":
    subprocess.run("cat pend_pend_pend", shell = True)
    file1 = open('pend_pend_pend', 'r')
    Lines = file1.readlines()
  else:
    os.system("cat %s"%(myfile))
    file1 = open('%s'% myfile, 'r')
    Lines = file1.readlines()
  # extract the id number only   
  for line in Lines:
    myid = line.split()
    id = myid[0]
    os.system('echo %s'%(myid[0])) 

  subprocess.run('rm -f pend_pend_pend', shell = True)
  print("Please add pend option to pend them")

  if args.pend=="pend":
    for line in Lines:
      myid = line.split()
      os.system('bmod -m %s %s'%(servers[i],myid[0])) 
      print("Have pended them")

  #if the first server is busy, try the second, the third ..
  if i<(len(servers) -1):
    i = i+1
  else:
    i = 0
  time.sleep(120)


