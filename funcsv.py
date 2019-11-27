# demo very basic file IO
infile_name = 'mark.txt'
outfile_name = 'markout.txt'

with open ('markin.txt', 'r') as infile, open (outfile_name, 'w') as outfile:
    for line in infile:
        outfile.write(line)
        print (line, end=" ")
        

    