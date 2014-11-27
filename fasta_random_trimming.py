# -*- coding: utf-8 -*-
# python3
import sys
import random
#from range of sequences from file randomly deletes defined number of sequences
#and puts it into output file
#python3 frepe.py <input1.fastq> <input2.fastq> <output1.fastq> \
# <output2.fastq> <number of seq to delete>
input_file = sys.argv[1]
input_file_sec = sys.argv[2]

output_file = sys.argv[3]
output_fasta = open(output_file, 'w')
output_fasta.close()

output_file_sec = sys.argv[4]
output_fasta_sec = open(output_file_sec, "w")
output_fasta_sec.close()

# no of sequences to erase
number_to_delete = sys.argv[5]

# indexes of fasta definitions from input file
indexes_of_fastq_start = []


def random_number_generator(fastq_list, number):
    number_of_int = int(number)
    max_for_int = len(fastq_list)
    no_list = random.sample(range(max_for_int), number_of_int)  # gives unique set of random numbers
    return no_list


#def erase_random_elements(elements_list, iterable_random_numbers):
#    s = set(iterable_random_numbers)  # set() gives unordered unique no's
#    elements_list = [x for i, x in enumerate(elements_list) if i not in s]
#    return elements_list

def erase_random_elements(elements_list, iterable_random_numbers):
    for i in iterable_random_numbers:
        elements_list[i] = None
    elements_list = filter(None, elements_list)
    return elements_list


def grouped(list_of_elements, n):  # groups list elements into n-groups
    return zip(*[iter(list_of_elements)] * n)


with open(input_file, 'r') as input_content1:
    with open(input_file_sec, 'r') as input_content2:
        print("1. Creating a list of first file fasta sequences...")
        fasq_seqs = list(grouped(input_content1, 2))
        length1 = len(fasq_seqs)
        print("Finished! You've got " + str(len(fasq_seqs)) +
        " sequences in first file. You should have the same number in paired fasta file\n")
        print("Generating list of random indexes...")
        random_numbers = random_number_generator(fasq_seqs, number_to_delete)
        print("Finished! " + number_to_delete +
        " sequences will be deleted in both files.\n")
        print("Starting deletion in first file...")
        fasq_seqs = erase_random_elements(fasq_seqs, random_numbers)
        print("Deletion finished! Proceed to writing first output file...")
        output = open(output_file, 'a')
        for seq in fasq_seqs:
            for line in seq:
                output.write(line)
        output.close()
        fasq_seqs = []
        print("Writing finished\n")
        print("2. Creating a list of second file fasta sequences...")
        fasq_seqs = list(grouped(input_content2, 2))
        print("Finished! You've got " + str(len(fasq_seqs)) +
        " sequences in second file.\n")
        if len(fasq_seqs) == length1:
            print("Starting deletion in second file...")
            fasq_seqs = erase_random_elements(fasq_seqs, random_numbers)
            print("Deletion finished! Proceed to writing second output file...")
            output = open(output_file_sec, 'a')
            for seq in fasq_seqs:
                for line in seq:
                    output.write(line)
            output.close()
            print("Writing finished")
        else:
            print("ERROR!. Different number of sequneces in input files.")