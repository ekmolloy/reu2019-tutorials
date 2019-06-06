import dendropy
import sys
import re

def get_newick(filepath):
    with open(filepath) as f:
        return f.read()

tree = dendropy.Tree.get(path=sys.argv[1], schema='newick')
newick_in = get_newick(sys.argv[1])

print(newick_in)

in_arr = re.split(':|,', newick_in)
print(in_arr)

branch_length = [0]
out_string = ""

for i in range(len(in_arr)-1, -1, -1):
    curr = in_arr[i]

    curr_num = ""
    #split into numbers and non-numbers
    for char in list(curr):
        print(list(curr))
        if(not char.isDigit()):
            out_string = char + out_string
            if (curr_num != ""):
                num = float(curr_num)
                if (in_arr[i-1][0].isAlpha() and i != 0):
                    out_string = str(num+branch_length[-1]) + ":" + out_string
                elif (in_arr[i-1][-1] == ")" and i != 0):
                    out_string = str(num+branch_length[-1]) + out_string
                    branch_length.append(num+branch_length[-1])
        elif (char == '('):            
            del branch_length[-1]
        else:
            curr_num = char + curr_num
            # the only reason this is complicated is because oftentimes numbers have more than one digit
            
