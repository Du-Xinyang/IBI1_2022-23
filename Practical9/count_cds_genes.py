# 	Ask the	user to input one of the three stop codons(TAA,TAG or TGA)
stop_codons = input("input one of the three stop codons(TAA,TAG or TGA)")
# open the files
genes = open('%s_stop_gene.fa' % stop_codons, 'w')
with open(r'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as a:
    s = ''
    name = ''
    for i in a:
        if i.startswith('>'):
            if s.endswith(stop_codons + '\n'):
                L = s.split()
                s = ''.join(L)
                start_codons = [j.start() for j in re.finditer('ATG', s)]
                end_codons = [j.start() for j in re.finditer(stop_codons, s)]
                count = 0
# using two for-loops to count the numbers of coding sequences
                for start in start_codons:
                    for end in end_codons:
                        if end > start:
                            count += 1
                genes.write(name + ' number of coding sequences: %s ' % count + '\n' + s + '\n')
            s = ''
            name = i.split()[0]
            continue
        s += i
genes.close()
