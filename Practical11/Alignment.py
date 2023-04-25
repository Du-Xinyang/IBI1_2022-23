# the findings: 1.the alignment score for human and cat:119, the percentage:14.76%
#               2.the alignment score for human and mouse:144, the percentage:17.87%
#               3.the alignment score for cat and mouse：147， the percentage:18.24%
# the sequences of cat and mouse are most closely related
# We can make biological or evolutionary interpretation from these data that cat and mouse have closer genetic relationship though cat is the natural enemy of mouse. And human has closer genetic relationship with mouse that cat.


# compare the sequence between human and cat
# extract the sequence line
file_human = open('ACE2_human.fa')
file_cat = open('ACE2_cat.fa')
output1 = open('human_gene','w')
for line in file_human:
    if not line.startswith('>'):
        output1.write(line)
        output1.close()
file1 = open('human_gene')
seq1 = file1.read()
output2 = open('cat_gene','w')
for line in file_cat:
    if not line.startswith('>'):
        output2.write(line)
        output2.close()
file2 = open('cat_gene')
seq2 = file2.read()
# compare the sequence
edit_distance1 = 0
for i in range(len(seq1)):
    if seq1[i]!=seq2[i]:
       edit_distance1 += 1
print(edit_distance1)
# calculate the	percentage	of identical amino acids for each of the three	comparisons
percentage1 = edit_distance1/len(seq1)*100
print("%.2f%%" % percentage1)

# compare the sequence between human and mouse
file_mouse = open('ACE2_mouse.fa')
output3 = open('mouse_gene','w')
for line in file_mouse:
    if not line.startswith('>'):
        output3.write(line)
        output3.close()
file3 = open('mouse_gene')
seq3 = file3.read()
# compare the sequence between human and mouse
edit_distance2 = 0
for i in range(len(seq1)):
    if seq1[i]!=seq3[i]:
       edit_distance2 += 1
print(edit_distance2)
# calculate the	percentage	of identical amino acids for each of the three	comparisons
percentage2 = edit_distance2/len(seq1)*100
print("%.2f%%" % percentage2)

# compare the sequence between cat and mouse
edit_distance3 = 0
for i in range(len(seq2)):
    if seq2[i] != seq3[i]:
        edit_distance3 += 1
print(edit_distance3)
# calculate the	percentage	of identical amino acids for each of the three	comparisons
percentage3 = edit_distance3 / len(seq2) * 100
print("%.2f%%" % percentage3)
