import sys

def nex_to_phy(f_nex):

    f = open(f_nex, 'r')
    out = open(f_nex.replace(".nex", ".phylip").replace("data", "output/raxml_out"), 'w+')

    lines = f.readlines()
    num = 0
    mat = 10000
    
    for line in lines:

        if 'ntax' in line:
            for i in range(line.find('ntax')+5, len(line)):
                if (line[i] is ' ') or (line[i] is ';'):
                    break
                out.write(line[i])
            out.write(" ")
                
        if 'nchar' in line:
            for i in range(line.find('nchar')+6, len(line)):
                if (line[i] is ' ') or (line[i] is ';'):
                    break
                out.write(line[i])
            out.write('\n')

        if 'Matrix' in line:
            mat = num
            
        if (num > mat) and (num < len(lines) - 2) :
            out.write(line)
            
        num = num + 1
                
    
if len(sys.argv) > 1:

    nex_to_phy(sys.argv[1])
    
