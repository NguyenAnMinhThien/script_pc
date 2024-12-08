# extract the content in a block,
# create an array contain [tag, some lines here, endpoint]
# reach the content (here is the tag and some line)
# create the endpont in a series of lines
import argparse
parser = argparse.ArgumentParser(description="Register for MPG and MR flow verification")
parser.add_argument("-tag", help="This is option", required=False)
parser.add_argument("-input", help="This is option", required=False)
parser.add_argument("-header", help="This is option", required=False)
args = parser.parse_args()

tag = args.tag
input = args.input
header = args.header

# tag = 'python'
# input = 'input.txt'
# header = 'header.txt'
# my_array = ['tag', 'line1', 'line2', 'endpoint'];
#
# for i in my_array:
#     if i != 'endpoint':
#         print(i)
#     else:
#         #do nothing
#         print("")


# if (line == tag || line not contained in header.txt) ignore
#     else meand it is on the endpoint (new tag) so break the for loop
toggle = 0
f = open(input, 'r', encoding='utf-8')
g = open(header, 'r', encoding='utf-8')
header_lines = g.readlines()
header_lines_strip = list()
for x in header_lines:
    header_lines_strip.append(x.strip())
#     print(("^" + tag.lower().strip() + "$") in header_lines_strip)
# print("heree")
for line in f.readlines():
    # print(line.lower().strip())
    if line.lower().strip() == tag:
        print(line.lower().strip())
        toggle = 1

    elif toggle == 1 and ("^" + line.lower().strip() + "$") in header_lines_strip:
        break
    elif toggle == 1:
        print(line.lower().strip())
        # solve for the first case when the tag still not appear
        # only jump to break after toggle == 1 and reach a tag in header_lines
    else:
        continue
    # the diagram of this code like a square pulse that it only process if the pulse toggle to 1 , the other case it will ignore and continue
# or line.lower().strip() not in header_lines
f.close()
g.close()
# allow the excuted mode for a script in git bash (the scope is in the window)

#demo converage
# if toggle == 0:
#     print ('')
# else:
#     print('haha')
# checkpoint :
# + dont case sensitve with the tag in input.txt ok
# + with the tag at begining and at the end will be miss, but this case is not happen after running sorting.
# + multiple tags adjency will be ok, and can printout.
# + pre requist: this script only run after we sort it and after runnign main.py and output