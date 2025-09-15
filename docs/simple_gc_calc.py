
sequence = "ACGTGCAGTAGTCA"
        
gcCount = 0.0;
ntCount = 0.0;
n = 0
while n < len(sequence):
    nt = sequence[n]


    if nt == 'G' or nt == 'C':
        gcCount += 1
        ntCount += 1


    if nt == 'A' or nt == 'T':
        ntCount +=1


    n += 1


gcPercent = gcCount/ntCount


print(f"GC % is {gcPercent:.2f}")