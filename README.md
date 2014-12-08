#####These are some scripts to use freely, to process files in fasta or fastq format. Were used to genome assembly, comparative genomics.

###### fasta_file_random_trimming.py
From range of fasta records in paired end files randomly deletes defined number of records and puts left records into output file. All the fasta file content is loaded into memory so much depend on a file size. Dealing with whole libraries will be usually not manageable for regular PCs.

USAGE:
```
fasta_random_trimming.py paired_ends_1.fastq paired_ends_2.fastq output_1.fastq output_2.fastq <number of seq to delete=integer>
```

###### fasta_sequence_oneliner.py
Sometimes, mostly from web tools, you get fasta files where sequences in fasta records are fragmented by lines. This script makes them written in one line.

USAGE:
```
fasta_sequence_oneliner.py input.fasta output.fasta
```


