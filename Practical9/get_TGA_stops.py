import re
# successfully read the file
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
inp = xfile.read()
print (inp)
# create a new file TGA_genes.fa with sequences	of	genes that	end	with the stop codon	‘TGA’.
# simplify the gene name
output = open(r'TGA_genes.fa', 'w')
with open(r'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as b:
    a = ''
    for i in b:
        if i.startswith('>'):
            if a.endswith('TGA\n'):
                output.write(name + '\n' + a)
            a = ''
            name = i.split()[0]
            continue
        a += i
output.close()
