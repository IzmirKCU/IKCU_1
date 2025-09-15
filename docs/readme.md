This folder contains two java files CalcGC.jar and GCCalc.jar
They both calculate average GC content for an input file of fasta sequences
We can find out how to run the program by typing
```
$ java -jar day1/GCCalculation/software/GCcalc.jar -h

GCCalc
initializing
parse arguments
    =======================================================================\
    | GCCalc  :                                                            \
    |    Java code to calculate GC percentage in a FastA file              \
    =======================================================================\
usage: command line options
 -f,--sequence file <arg>   sequence file in FASTA format
 -h,--help                  view help


```
So, we just need to specify a fasta file.  Let’s start with the file day1/GCCalculation/data/GCtest.fa 
(This corresponds to an alignment of sequences for the 3’UTR of the *Lysine Methyltransferase 5B* gene)

First test with `GCCalc.jar`
```
$ java -jar day1/GCCalculation/software/GCCalc.jar 
-f day1/GCCalculation/data/GCtest.fa

GCCalc
initializing
parse arguments
fasta input file is <day1/GCCalculation/data/ENSG00000110066___ENST00000441488___2___KMT5B__uniq_aln.fa>
read <16> sequences from file
average GC value of all sequences is <43.35%>
```

And repeat using `CalcGC.jar`
```
$ java -jar day1/GCCalculation/software/CalcGC.jar 
-f day1/GCCalculation/data/GCtest.fa
```
