# create a function that determines	whether	a	given DNA sequence	is	likely	to	be	protein-coding	or	not.
import re
def g(x):
    x = DNAseq
# Here we consider the start codon and stop codon are both included in the sequence portion.
    y = re.findall(r'(ATG\S+TGA)',x)
    e = str(y)
    z = len (e)
    a = len(x)
    b = z/a
    if b > 0.5:
        print('protein-coding')
    elif b <0.1:
        print('non-coding')
    else:
        print('unclear')
# assume the input sequence contains both upper and lower case is:
DNAseq = 'aTCTTtAATGCCTTatAACGGAATTGACaGg'
DNAseq = DNAseq.upper()
# show how the function works
g(DNAseq)
