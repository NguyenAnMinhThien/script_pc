from subprocess import Popen, PIPE, STDOUT
import shlex
p = Popen(['grep', 'f'], stdout=PIPE, stdin=PIPE, stderr=STDOUT,shell= True)
grep_stdout = p.communicate(input=b'one\ntwo\nthree\nfour\nfive\nsix\n')[0]
print(grep_stdout.decode())
# -> four
# -> five
# ->

# p = Popen(['find', '.'], stdout=PIPE, stderr=STDOUT,shell= True)
cmd = "find . -name \"demo*\""
# args = shlex.split(cmd)
# print(args)
# p = Popen(['find', '.', '-name', '\"demo\*\"'], stdout=PIPE, stderr=STDOUT,shell= True)
p = Popen(cmd, stdout=PIPE, stderr=STDOUT,shell= True)
# p = Popen(args, stdout=PIPE, stderr=STDOUT,shell= True)
output = p.communicate()
print(output)
# print(output[0].decode().split("\n"))
Lines = output[0].decode().split("\n")
print(Lines)
print(type(output[0].decode()))
print(type("hehe"))
# -> four
# -> five
# ->

# import subprocess
#
# lsProcess = subprocess.Popen(["ls"], stdout=subprocess.PIPE, text=True,shell=True)
# grepProcess = subprocess.Popen(["grep", "demo"], stdin=lsProcess.stdout,stdout=subprocess.PIPE, text=True, shell = True)
# output, error = grepProcess.communicate()
#
# print(output)
# print(error)

# # dirname function
# import os
# import argparse
# parser = argparse.ArgumentParser(description="Register for MPG and MR flow verification")
# parser.add_argument("-d", help="This is option", required=False)
# parser.add_argument("-f", help="This is option", required=False)
# parser.add_argument("-e", help="This is option", required=False)
# parser.add_argument("-n", help="This is option", required=False)
# args = parser.parse_args()
#
# out = os.path.abspath(args.f)
# print(out)

# subprocess.run("touch findd_list_list_list", shell = True)
# subprocess.run("truncate -s 0 findd_list_list_list", shell = True)
# os.system("find %s > findd_list_list_list"%(mydir))
# print(f"{mydir}")
#
# subprocess.run("cat findd_list_list_list", shell = True)
# print("\nExcuting ...")
# dir1 = open('findd_list_list_list', 'r')
# Lines = dir1.readlines()
# dir1.close()

