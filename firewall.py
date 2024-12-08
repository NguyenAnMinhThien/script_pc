firewall.py

heree
#!/common/appl/python/python-3.6.4/bin/python3

import argparse
import math
import warnings
import array
import re
import os

#hehe = math.log2(4)
#bigger = math.log2(6)
#sub = bigger - hehe
#print(sub)
#print(bin(6))
##this only works for integer value, the modulor
#print(6%2)
#
#print(6 >> 1)
#
#print((6>>1)%2)


#The first column : address of the begining of that range
#The second column : address of ending of that range
#The final column : size data of that range 

#an array of integer values
#my_array = array.array('i',[])
#my_array.append(4)
#my_array.append(6)
#
#print(my_array[1])


#decompress the input number into many bits 1 and its positions.
def count_bits(number):
  #my_array = array.array('i',[])
  my_array = []
  counter = 0
  while number:
    counter = counter + 1
    if (number & 1):
      #both two these ways are corrected, but how we can apply alternative ?
      #my_array.insert(len(my_array),counter + 10)
  # To avoid the overbit, we need to proceed the big bit first then we process the MSB later.
      my_array.insert(0,counter + 10)
    number >>= 1

  return my_array

#Args: The number of bit 1, the shift position
def create_mask(value, shift):
 mask = pow(2,value) -1
 mask = mask << shift
 return mask


# ADDreg = _num & _mask ; _num is the number after + the size of sub range
# ending: is the end address of a sub range
def firewall_mapping(total, sub, begining):
  count_total = count_bits(total)
  count_sub = count_bits(sub)
  mapping_array = []

  begining = begining.replace("H'","0x")
  begining = begining.replace("_","")
  begining = int(begining,16)

  

  if (len(count_total) == 1):
    for root in count_total:
      i = 0
      for element in count_sub:
        #find mask
        result = root - element
        mask_final = create_mask(result, element -1)
        #find addreg
        #heree begining value may be uncorrected.
        begining_test = begining
        ending = begining + pow(2,element -1) -1
        #update the value of beginning to for creating a continuos region
        begining = ending + 1
        addreg = mask_final & ending 
        addreg_test = mask_final & begining_test
        if (addreg == addreg_test):
          #create 2-D array
          mapping_array.insert(i,[mask_final,addreg,"true"])
          i = i + 1
          print(hex(begining_test))
          print("mask     ->", hex(mask_final))
          print("addreg   ->", hex(addreg))
          print(hex(ending))
          print("")
        else:
          i = i+1
          mapping_array.insert(i,[mask_final,addreg,"fail"])
  else:
    print("The total size range of all regions are not the power of 2, please split it")
  return mapping_array



if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="firewall config")
  parser.add_argument("-input", help="Path to firewall info", required=True)
  args = parser.parse_args()

# In the main flow, we get the region number
# In the sub flow, we get the return value from the region_ex function 

  file1 = open(str(args.input), 'r')
  Lines = file1.readlines()
  counting_region = 0
  counting_region_ex = 0

#calculate the total size, update the value of dictionary [key-value]
  dict = {}
  for line in Lines:
    myid = line.split()
    if (len(line) > 1 and re.search("^(?!The_end).*", line)):
        if (re.search("mod_name",myid[0])):
          mod_name = myid[1]
          dict[mod_name] = 0
        else:
          dict[mod_name] = dict[mod_name] + int(myid[-1])
      


#Input the args into the mapping, the total size and the sub range of the region you want.

  overlap = {}
  for line in Lines:
    myid = line.split()
    if (len(line) > 1 and re.search("^(?!The_end).*", line)):
        if (re.search("mod_name",myid[0])):
         print("mod_name    " + myid[1] + "\n")
         counting_region_ex = 0
         counting_region = 0
         mod_name_miror = myid[1]
         #initial overlap
         overlap[mod_name_miror] = [counting_region]
         overlap[mod_name_miror] += [counting_region_ex]

         f = open(myid[1],"w")
         f.write("mod_name" + "\t\t" + myid[1] + "\n\n" ) 
        else :
         output = firewall_mapping(dict[mod_name_miror], int(myid[-1]), myid[0])
         for output_element in output:
            if (output_element[2]== "true"):
               addmsk = "ADDmsk_" + str(counting_region_ex) + "\t\t" + str(hex(output_element[0])) + "\n"
#               if (hex(output_element) & hex(int(myid[0])) == hex(output_element) & hex(int(myid[1]))):
               addreg = "ADDreg_" + str(counting_region_ex) + "\t\t" + str(hex(output_element[1])) + "\n"
               addreg_id = "ADDreg_id_" + str(counting_region_ex) + "\t\t" + str(counting_region) + "\n" + "\n"
               f.write(addmsk)
               f.write(addreg)
               f.write(addreg_id)
               counting_region_ex += 1
            else:
                print("You should have submitting again for this case")
#               else:
#                 addreg = "ADDreg_" + str(counting_region_ex) + "\t\t" + "undefined, there are something wrong, should do by manualy" + "\n"
                 
         counting_region += 1
         overlap[mod_name_miror] = [counting_region]
         overlap[mod_name_miror] += [counting_region_ex]
  ##os.system('sed -i "2inumber_of_region \t\t hehe " axdsp_apb_ardsp_fw.cfg')
  #os.system('echo %s  %s'%(counting_region,mod_name_miror))
  #os.system('sed -i 2inumber_of_region  %s'%(mod_name_miror))
    else:
      f.close()
      

#This is a way to insert a line into a file
# sed -i '1icolumn1, column2, column3' testfile.csv
# Finally, addingo the total region counting into the first lines of the output file.

# use dic to store the key value of each file, include the total size of a instance.
#later, when we see again the instance, we will input the firewall_mapping the value of total size.

# why these codes not work ?when add them into the code, it will gen the empty file ! but when use the independent file, it gives the correct result.
#print(counting_region,mod_name_miror)
##os.system('sed -i "2inumber_of_region \t\t hehe " axdsp_apb_ardsp_fw.cfg')
#os.system('echo %s  %s'%(counting_region,mod_name_miror))
#os.system('sed -i 2inumber_of_region  %s'%(mod_name_miror))
#print("hehe")
#os.system('echo %s  %s'%(counting_region,mod_name_miror))
#os.system('sed -i "2inumber_of_region %s"  %s'%(counting_region,mod_name_miror))

for file in overlap:
  os.system('sed -i "2inumber_of_region %s"  %s'%(overlap[file][0],file))
  os.system('sed -i "3inumber_of_region_ex %s"  %s'%(overlap[file][1],file))
  os.system('sed -i "4iaddr_bitwidth %s"  %s'%("hehe",file))


#convert the string format of the input address into the correspondence format of hex value
#convert that string into integer first, base 16 (default it is 10), then convert the integer value into hex later.
#The AND excution must do on integer. The result later convert to hex.
#Each region has the sub regions, each sub has its own range size. Need to get the begin and ending of each sub to sure the ADDreg correctly.
#A function has inputs args: The start, end of that region, and the array after mapping. This will output another array has the same size but with other meaning - each element is the ADDreg of the sub region.


heree
mod_name  axdsp_apb_ardsp_fw.cfg
H'0_CBF0_0000		H'0_CBF0_0FFF	BUSreg (DSP) Region 0		4
H'0_CBF0_1000		H'0_CBF0_1FFF	BUSreg (DSP) Region 1		4
H'0_CBF0_2000		H'0_CBF0_2FFF	BUSreg (DSP) Region 2		4
H'0_CBF0_3000		H'0_CBF0_3FFF	BUSreg (DSP) Region 3		4
H'0_CBF0_4000		H'0_CBF0_4FFF	BUSreg (DSP) Region 4		4
H'0_CBF0_5000		H'0_CBF0_5FFF	BUSreg (DSP) Region 5		4
H'0_CBF0_6000		H'0_CBF0_6FFF	BUSreg (DSP) Region 6		4
H'0_CBF0_7000		H'0_CBF0_7FFF	BUSreg (DSP) Region 7		4

mod_name  axdsp_apb_ardsp_fw_demo.cfg
H'0_CBF0_0000		H'0_CBF0_1FFF	BUSreg (DSP) Region 0		8
H'0_CBF0_2000		H'0_CBF0_2FFF	BUSreg (DSP) Region 2		4
H'0_CBF0_3000		H'0_CBF0_3FFF	BUSreg (DSP) Region 3		4
H'0_CBF0_4000		H'0_CBF0_4FFF	BUSreg (DSP) Region 4		4
H'0_CBF0_5000		H'0_CBF0_5FFF	BUSreg (DSP) Region 5		4
H'0_CBF0_6000		H'0_CBF0_6FFF	BUSreg (DSP) Region 6		4
H'0_CBF0_7000		H'0_CBF0_7FFF	BUSreg (DSP) Region 7		4

mod_name  axdsp_apb_ardsp_fw_demo2.cfg
H'0_CBF0_0000		H'0_CBF0_0FFF	BUSreg (DSP) Region 0		4
H'0_CBF0_1000		H'0_CBF0_2FFF	BUSreg (DSP) Region 1		8
H'0_CBF0_3000		H'0_CBF0_3FFF	BUSreg (DSP) Region 3		4
H'0_CBF0_4000		H'0_CBF0_4FFF	BUSreg (DSP) Region 4		4
H'0_CBF0_5000		H'0_CBF0_5FFF	BUSreg (DSP) Region 5		4
H'0_CBF0_6000		H'0_CBF0_6FFF	BUSreg (DSP) Region 6		4
H'0_CBF0_7000		H'0_CBF0_7FFF	BUSreg (DSP) Region 7		4

mod_name                 axdsp_axi_dsparcsyns_fw
H'0_CF00_0000		H'0_CF00_0FFF	DSP ars syn Region 0		4
H'0_CF00_1000		H'0_CF00_3FFF	DSP ars syn Region 1		12
H'0_CF00_4000		H'0_CF00_7FFF	DSP ars syn Region 2		16
H'0_CF00_8000		H'0_CF00_9FFF	DSP ars syn Region 2		8
H'0_CF00_A000		H'0_CF00_AFFF	DSP ars syn Region 2		4
H'0_CF00_B000		H'0_CF00_BFFF	DSP ars syn Region 3		4
H'0_CF00_C000		H'0_CF3F_FFFF	DSP ars syn Region 4		4048
The_end

heree
A solving for the coleaguage to solve the mask address of the input
ï?¨	Solution:
+ the first address of that region
+ the size of that region
+ the size of the total number of all regions in that slave.
Output: the value of mask

Solution:
+ the total number of bits for the size of that range (a) , is calculated by logÂ¬2(that range)
+ the total number of bits for the size of the total range. (t)  , is calculated by log2(total size)
(because the value will increase from the MSB positions, so from a size data bytes, it will be mask to 0 from the MSB position also -> surely we have removed correct from the end)
+ the total bits change will be  (t â?" a) and the position it begins starting is  (a+1) 
+ if that size is 12KB = (8 + 4) -> external is 2 regions , generally for a number, we divided to total number of external regions base on the number of bit 1 in that appearance : e.x : 28 = 11100 -> 3 regions external. If the old user define to 4 external regions, it is also true, 28 = 16 + 4 + 4 +4

heree

