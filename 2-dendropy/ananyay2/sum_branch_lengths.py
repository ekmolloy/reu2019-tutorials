import dendropy
import sys
import re

# NOTE: THERE IS A HIGH PROBABLILITY THAT THIS WILL NOT WORK FOR ANYTHING OTHER THAN THE TWO TESTCASES I TRIED

def get_newick(filepath):
    with open(filepath) as f:
        return f.read()

# Idea: string manipulation
newick_in = get_newick(sys.argv[1])
in_arr = re.split(':|,', newick_in)

# basically a stack
branch_length = [0]

# the thing we'd like to return
out_string = ""

for i in range(len(in_arr)-1, -1, -1):
    curr = in_arr[i]

    curr_num = ""
    #split into numbers and non-numbers
    for j in range(len(curr)-1, -1, -1):
        c = curr[j]

        if(c == '\n' or c == ';'):
            # these are characters we'd like to ignore
            # do nothing but for some reason I can't just leave this blank
            None
        elif(not c.isdigit() or j == 0):
            # if it's not a number, just add it to the string
            # if it's the last character in this section, then we have to process the branch length that was in this section

            # add this character to the string or number, depending on what it is
            if (c.isdigit()):
                curr_num = c + curr_num
            else:
                out_string = c + out_string


            if (curr_num != ""):
                # deal with the numbers
                # formatting the output, put commas in their place
                if (out_string[0] != ')'):
                    out_string = ',' + out_string

                num = float(curr_num)
                

                if (in_arr[i-1][-1].isalpha() and i != 0):
                    out_string = ":" + str(num+branch_length[-1]) + out_string
                elif (in_arr[i-1][-1] == ")" and i != 0):
                    out_string = str(num+branch_length[-1]) + out_string
                    branch_length.append(num+branch_length[-1])
        elif (c == '('):    
            del branch_length[-1]
        else:
            #if it is a number then figure out what number we're reading
            curr_num = c + curr_num
            # the only reason this is complicated is because oftentimes numbers have more than one digit

print(out_string + ";")
