# create a function that	determines	whether	a	given	DNA	 sequence	is	likely	to	be	protein-coding	or	not.
import re
def g(x):
    x = DNAseq
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
DNAseq = 'ATCTTTAATGCCTTATAACGGAATTGACAGG'
g(DNAseq)
