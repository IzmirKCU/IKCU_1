# Some basic Shell commands
## Getting basic file information

### to get the current working directory

```
pwd
```

### to find the files in the current folder

```
ls
```

### to get detailed information about the files in the current folder

```
ls -l
```

### Searching for file patterns

to list all the `gff3` files in the current folder
```
ls -l *.gff3
```

### how many lines in a file/list of files

you can use the `wc -l` command
```
wc -l *.gff3
```

### searching across multiple folders for file patterns
`ls -l` will only let you search the current folder.  If you want to search subfolders as well, you can use the `find` command  

to find all `gff3` files in the current folder, and all subfolders

```
find ./ -name '*.gff3'
```

## Piping commands
you can use the `|` command to send the output from command to the next command

so, if you modify the command above to find gff3 files 
```
ls -l *.gff3
```

to 

```
ls -l *.gff3|wc -l
```

this will give you the total number of `gff3` files. 

How does this work? 
1. Because you are listing the file information in long format, each file is listed on one line.
2. Because you are 'piping' this output to the next command, `wc -l` sees this output as a file, and just prints the number of lines

## Getting more information about files
Another useful command is `xargs`
the syntax of the command is 

```
<filelist>|xargs <command>
```

What is tells the system to do is to execute the `<command>` command on the list of files

for example

```
find ./ -name '*.gff3'|xargs wc -l
```
 will print out the number of lines in each `gff3` file in the list returned by the `find ./ -name '*.gff3'` command


## Searching inside files

We can search inside files for patterns using commands such as `grep`, `awk` and `sed`, `grep`,  

### grep
we can search inside files using `grep`.  There are lots of things you can do, but some simple examples are as follows

1. find the number of lines that contain the string `chr1` 

```
grep -c 'chr1' rno.gff3
```

2. find the number of lines that don't contain the string `chr1` 

```
grep -cv 'chr1' rno.gff3
```

3. to find the number of lines that contain the string `chr1` at the **beginning** of the line we can use the `^` character  

```
grep -cv '^chr1' rno.gff3
```

4. to find the number of lines that contain the string `chr1` at the **end** of the line we can use the `$` character  

```
grep -cv 'chr1$' rno.gff3
```

5. using **Regular Expressions** with `grep`
All these searches will return any line that contains the string `chr1`, so this will include `chr1`, `chr10`, `chr11` .. `chr19`

How do we only get lines with `chr1` ?

We can use the fact that a gff3 file is tab delimited, this means that each line looks like this

```
chr1<tab>.<tab>miRNA_primary_transcript<tab>38238376<tab>8238456

```

if we search for lines that contain `chr1<tab>.` this will give us `chr1` but not `chr10` etc.

We tell the computer to look for the `<tab>` character using the string `\t` 

the `\t` string is called a **Regular Expression** and we use the `-P` flag to tell `grep` we want to use them

so

```
grep -cP 'chr1\t' rno.gff3 
```

### awk

This is another useful tool for searching inside files. 

For example, we often want to extract a single column from a tab delimited file.

to print only the first column, we can use the `cut` command

```
cut -f 1 rno.gff3
```

or, we can do the same thing using `awk`

```
awk '{print $1}' rno.gff3 |more
```

So, we can use this to get a summary of the number of `miRNA_primary_transcript` entries for each chromosome in the `rno.gff3` file

to get the lines containing miRNA primary transcript information
``` 
grep miRNA_primary_transcript rno.gff3 
``` 

To get the chromosome information from these lines
``` 
grep miRNA_primary_transcript rno.gff3 |awk '{print $1}' 
``` 
to get a list of all chromosomes we use the `uniq` command
``` 
grep miRNA_primary_transcript rno.gff3 |awk '{print $1}' |uniq
``` 
to count the number of miRNA primary transcripts for each chromosome, we add the `-c` flag to the `uniq` 
``` 
grep miRNA_primary_transcript rno.gff3 |awk '{print $1}' grep -v '#'|uniq -c
``` 

Finally, there is one line that is included that doesn't describe a chromosome

```
      1 #               <---- we don't want this line
     57 chr1
     38 chr10
     16 chr11

```
this is coming from one of the header lines 

```
# Hairpin precursor sequences have type "miRNA_primary_transcript". 
``` 

we can remove this using by adding the command `grep -v '#'` to the pipe
``` 
grep miRNA_primary_transcript rno.gff3 |awk '{print $1}'| grep -v '#'|uniq -c
``` 