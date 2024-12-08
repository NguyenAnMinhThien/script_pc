hereeee
demo.py
#!/common/appl/python/python-3.6.4/bin/python3
import warnings
import argparse
import openpyxl
import sys
import re

#open and read the file after the appending:
#f = open("final", "r")
#mydata = f.read()
#print(mydata)
#f.close
mydata = sys.argv[1]
myarray = mydata.split()
#if (myarray[0] == "axad" or myarray[0] == "axmm2_mm" or  myarray[0] == ) :
#  myarray[4] = "10"
# with many cases the bit_position have two number, we use -1 like counting from the last.
bit_position = re.split(r':', myarray[4])
num2 = str(bit_position[1])
print(num2[0:-1])

position = num2[0:-1]
myarray[4] = str(position)

#myarray[4] is the bit position for shifting, if the the number is 2 bit, we can not cal 
run_stat = 0x3
mstp_stat = 0x2
rst_stat = 0x1
stop_stat = 0x00

or_stop_stat = 0xfffffffc
or_rst_stat = 0xfffffffd
or_mstp_stat = 0xfffffffe


set_reg = "MDLC" + myarray[2] + "MSRES" + myarray[3]
stat_reg = "MDLC" + myarray[2] + "MSRESS" + myarray[3]
prot_reg = "MDLC" + myarray[2] + "PKCPROT1"


#heree create for standby

mask1 = run_stat << int(myarray[4])
mask2 = ~(~or_stop_stat << int(myarray[4]))
mask3 = stop_stat << int(myarray[4])

mask4 = rst_stat << int(myarray[4])

mask1 = str(hex(mask1))
mask2 = "0x" + (str(hex(mask2))[-8:-1] + str(hex(mask2))[-1])
mask3 = str(hex(mask3))

mask4 = str(hex(mask4))


f = open("./lib/template_standby/main.s", "r")
main = f.read()
main_new = main.replace("<MASK_VALUE1>", mask1)
main_new = main_new.replace("<SET_REG>", set_reg)
main_new = main_new.replace("<MASK_VALUE2>", mask2)
main_new = main_new.replace("<MASK_VALUE3>", mask3)
main_new = main_new.replace("<MASK_VALUE4>", mask4)
main_new = main_new.replace("<STATUS_REG>", stat_reg)
main_new = main_new.replace("<PROT_REG>", prot_reg)
f.close()


f = open("main_standby.s", "w")
f.write(main_new)
f.close()


# Create for test.s
f = open("./lib/template_standby/test.s", "r")
test = f.read()
test_new = test.replace("<BUS_MODULE>", myarray[0])
f.close()

f = open("test_standby.s", "w")
f.write(test_new)
f.close()

# Create for usr_sim.tcl

f = open("./lib/template_standby/tcl_vcs/usr_sim.tcl", "r")
usr_sim = f.read()
usr_sim_new = usr_sim.replace("<MSTP_N>", sys.argv[2])
f.close()

f = open("usr_sim_standby.tcl", "w")
f.write(usr_sim_new)
f.close()
#heree create for sfrst


mask1 = run_stat << int(myarray[4])
mask2 = ~(~or_rst_stat << int(myarray[4]))
mask3 = rst_stat << int(myarray[4])

mask1 = str(hex(mask1))
mask2 = "0x" + (str(hex(mask2))[-8:-1] + str(hex(mask2))[-1])
mask3 = str(hex(mask3))

print(f"sfrst is    '{mask2}'");

mask4 = ~(~or_stop_stat << int(myarray[4]))
mask4 = "0x" + (str(hex(mask4))[-8:-1] + str(hex(mask4))[-1])

mask5 = ~(~or_mstp_stat << int(myarray[4]))
mask5 = "0x" + (str(hex(mask5))[-8:-1] + str(hex(mask5))[-1])

mask6 = mstp_stat << int(myarray[4])
mask6 = str(hex(mask6))

mask7 = stop_stat << int(myarray[4])
mask7 = str(hex(mask7))

f = open("./lib/template_sfrst/main.s", "r")
main = f.read()
main_new = main.replace("<MASK_VALUE1>", mask1)
main_new = main_new.replace("<SET_REG>", set_reg)
main_new = main_new.replace("<MASK_VALUE2>", mask2)
main_new = main_new.replace("<MASK_VALUE3>", mask3)
main_new = main_new.replace("<MASK_VALUE4>", mask4)
main_new = main_new.replace("<MASK_VALUE5>", mask5)
main_new = main_new.replace("<MASK_VALUE6>", mask6)
main_new = main_new.replace("<MASK_VALUE7>", mask7)
main_new = main_new.replace("<STATUS_REG>", stat_reg)
main_new = main_new.replace("<PROT_REG>", prot_reg)
f.close()

# mask_value3 : if the before is sfrst, used in checkstate
# mask_value1 : 11 to mask, or check if before it is run state.
# mask\_value5: set for current state is mstp
# mask_value4: set for current state is standby
# mask_value2: set for current state is sfrst
f = open("main_sfrst.s", "w")
#f.write(set_reg + " " + stat_reg + " " +  prot_reg + "\n")
#f.write(str(mask1) + " " + str(mask2) + " " + str(mask3) + "\n\n")
f.write(main_new)
f.close()


# Create for test.s
f = open("./lib/template_sfrst/test.s", "r")
test = f.read()
test_new = test.replace("<BUS_MODULE>", myarray[0])
f.close()

f = open("test_sfrst.s", "w")
f.write(test_new)
f.close()

# Create for usr_sim.tcl

f = open("./lib/template_sfrst/tcl_vcs/usr_sim.tcl", "r")
usr_sim = f.read()
usr_sim_new = usr_sim.replace("<MSTP_N>", sys.argv[2])
f.close()

f = open("usr_sim_sfrst.tcl", "w")
f.write(usr_sim_new)
f.close()
#heree create for mstp

mask1 = run_stat << int(myarray[4])
mask2 = ~(~or_mstp_stat << int(myarray[4]))
mask3 = mstp_stat << int(myarray[4])

mask1 = str(hex(mask1))
mask2 = "0x" + (str(hex(mask2))[-8:-1] + str(hex(mask2))[-1])
mask3 = str(hex(mask3))

# Create for main.s
f = open("./lib/template_mstp/main.s", "r")
main = f.read()
main_new = main.replace("<MASK_VALUE1>", mask1)
main_new = main_new.replace("<SET_REG>", set_reg)
main_new = main_new.replace("<MASK_VALUE2>", mask2)
main_new = main_new.replace("<MASK_VALUE3>", mask3)
main_new = main_new.replace("<STATUS_REG>", stat_reg)
main_new = main_new.replace("<PROT_REG>", prot_reg)
f.close()


f = open("main_mstp.s", "w")
f.write(main_new)
f.close()


# Create for test.s
f = open("./lib/template_mstp/test.s", "r")
test = f.read()
test_new = test.replace("<BUS_MODULE>", myarray[0])
f.close()

f = open("test_mstp.s", "w")
f.write(test_new)
f.close()


# Create for usr_sim.tcl

f = open("./lib/template_mstp/tcl_vcs/usr_sim.tcl", "r")
usr_sim = f.read()
usr_sim_new = usr_sim.replace("<MSTP_N>", sys.argv[2])
f.close()

f = open("usr_sim_mstp.tcl", "w")
f.write(usr_sim_new)
f.close()

##ref
#f.write(set_reg + " " + stat_reg + " " +  prot_reg + "\n")
#f.write(str(mask1) + " " + str(mask2) + " " + str(mask3) + "\n\n")
hereeee

