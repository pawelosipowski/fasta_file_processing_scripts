My scripts to process files in fasta or fastq format. Were used to genome assembly, comparative genomics.

##### fasta_file_random_trimming.py

From range of sequences in a file randomly deletes defined number of sequences and puts it into output file.
All the fasta file content is loaded into memory so much depend on a file size. Dealing with whole libraries will be usually not manageable for regular PCs.


USAGE:
```
fasta_random_trimming.py <paired_ends_1> <paired_ends_2> <output_1> <output_2> <number of seq to delete>
```
