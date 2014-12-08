### this script sources fasta file with sequences formated to more than one line (having "\n")
### and outputs fasta file where each fasta record have one line of sequence
### usage: $python sequence_one_liner_for_fasta.py <input.fasta> <output.fasta>

import sys

def write_fasta_seqs_in_one_line(source, destination):
    output = open(destination, "a")
    one_fasta_record = ""
    seq_line_count = 0                 # way to write last sequence because...
    fasta_record_count = 0
    for line in open(source):
        if line.startswith('>'):
            fasta_record_count = fasta_record_count + 1
            output.write(one_fasta_record)    # will not write it under this condition
            # new fasta record
            if fasta_record_count == 1:
                one_fasta_record = line
            else:
                one_fasta_record = "\n" + line
                seq_line_count = 0
        else:
            sequence = line.rstrip("\n")
            seq_line_count = seq_line_count + 1
            one_fasta_record = one_fasta_record + sequence
    if seq_line_count > 0:                    # but will under this one
        output.write(one_fasta_record)
    output.close()
    print("\n" + str(fasta_record_count) + " fasta sequences were converted to one line. Thank you.")





#input_file_content = open(input_file, 'r')
#input_fasta = input_file_content.readlines()
#input_file_content.close()

#param_input = sys.argv[1]
input_file = sys.argv[1]
#if param_input != "-i" or sys.argv[2] is None:
#    print("wrong imput")

#param_output = sys.argv[3]
output_file = sys.argv[2]

write_fasta_seqs_in_one_line(input_file, output_file)





#inpust_fasta = open(output_file, 'w')
#output_fasta.close()
