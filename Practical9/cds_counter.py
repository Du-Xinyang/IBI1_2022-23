import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
sub_seq = str(re.findall(r'^ATG.+', seq))
num_1 =re.findall(r'TAG|TGA|TAA',sub_seq)
num = len(num_1)
print(num)
