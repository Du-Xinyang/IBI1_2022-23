import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
# find the start codon
sub_seq = str(re.findall(r'^ATG.+', seq))
# find all stop codons
num_1 =re.findall(r'TAG|TGA|TAA',sub_seq)
# since we only consider one start codon at the beginning of the provided sequence, we only need to count the number of the stop codons.
num = len(num_1)
print(num)
