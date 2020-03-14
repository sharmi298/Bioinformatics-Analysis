#Analysis of high-throughput sequences
import os
import re
#Read files from a given path
def readFiles(path):
    s = open(path).read()
    return s

#PART1
sequences = []
seq = ""

#Loop over the list of sequences
for filename in os.listdir("FileDirectory/"):
    print('The filenames in the choosen directoy are ' + filename) #Gives the filename of the files in the directory
    s1 = readFiles("./FileDirectory/" + filename)
    print('The number of sequences in each fasta files in the directory are ' + str(s1.count('>'))) #gives the count of sequences
    for f in s1:
        if not f.startswith('>'): 
            f = f.replace(" ", "")
            f = f.replace("\n", "")
            seq = seq + f
        else:
            sequences.append(seq)
            seq = ""
    sequences.append(seq)
    sequences = sequences[1:]
#To find the length of all the sequences in the list
    lengths = [len(i) for i in sequences]

#To obtain sequences with base pairs greater than 300 
temp1 = []      
for i in range(len(sequences)):
    element = sequences[i]
    if len(element) > 300:
        temp1.append(s1)

#Just to compare the number of sequences before and after filtering (>300bp)
print("Number of all the sequences including both fasta files in the directory: " + str(len(sequences)))        
print("Number of sequences with length greater than 300bp are: " + str(len(temp1)))


#function to return 10 longest and 10 shortest sequences 
def Longest10_Shortest10(file_contents):
    sequences2 = []
    seq2 = ""
    longest10seq = ""
    smallest10seq = ""
    for f2 in file_contents:
        if not f2.startswith('>'):
            f2 = f2.replace(" ","")
            f2 = f2.replace("\n","")
            seq2 = seq2 + f2    
        else:
            sequences2.append(seq2)
            seq2 = ""
    sequences2.append(seq2)
    sequences2.sort(key = len)
    longest10seq = sequences2[-10:]
    smallest10seq = sequences2[0:10]
    return [longest10seq, smallest10seq]

#for the first file and write the output as a .txt file to the current working directory
f = readFiles("./FASTAfile")
final = Longest10_Shortest10(f)


#function to determine the GC% in the sequences
def GC_Content(file_contents):
    sequence = ""
    lengths = []
    for line in file_contents:
        if line.startswith('>'):
            seq_id = line.rstrip()[0:]
            lengths.append(len(''.join(sequence)))
            sequence = []
        else:
            sequence += line.rstrip()
    
    #GC % formula
    GC_content = float((sequence.count('G') + sequence.count('C'))) / len(sequence) * 100

    return GC_content


#calculate the GC% and N50 for each fasta file and write as an output .txt file
f1 = readFiles("./FASTASeq")
with open('Part3_seq5.txt', 'w') as file_out:
    file_out.write("The GC%: " + str(GC_Content(f1)))

file_out.close()

