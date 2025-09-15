from Bio import SeqIO
import pandas as pd

newfile = open("new.txt", "w")
records = list(SeqIO.parse("/Users/simonray/uio_dropbox_sr/myTeaching/IKCU2/data/hairpin.fa", "fasta"))

seqLens = []
i=0
while i < len(records):
    seqLens.append(len(records[i].seq))
    i = i + 1
dfseqLens = pd.DataFrame(seqLens, columns=['lengths'])

from matplotlib import pyplot as plt
import seaborn as sns
sns.histplot(data=dfseqLens, x="lengths", binwidth=1)
