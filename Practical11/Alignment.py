# the findings: 1.the alignment score for human and cat:3717.0, the percentage:0.8521739130434782
#               2.the alignment score for human and mouse:3579.0.0, the percentage:8211180124223603%
#               3.the alignment score for cat and mouse：3592.0， the percentage:0.817391304347826%
# the sequences of human and cat are most closely related
# We can make biological or evolutionary interpretation from these data that human has a closer genetic relationship with cat than mouse.

# use the blosum package to access blosum62 matrix
# use itertools to combine three sequences
import blosum as bl
matrix = bl.BLOSUM(62)
# create a dictionary
dic = dict()
#open the three files.
# extract the sequence line
with open('ACE2_human.fa', 'r') as f:
    n = 0
    for line in f:
        n += 1
        if n == 2:
            dic['human'] = line[: -1]
with open('ACE2_mouse.fa', 'r') as f:
    n = 0
    for line in f:
        n += 1
        if n == 2:
            dic['mouse'] = line[: -1]
with open('ACE2_cat.fa', 'r') as f:
    n = 0
    for line in f:
        n += 1
        if n == 2:
            dic['cat'] = line[: -1]


# define a function use blosum62 matrix to get score for each letter and calculate the total score
# return the score and percentage
def alignment(seq1, seq2):
    score = 0
    edit_distance = 0
    for i in range(len(seq1)):
        score += matrix[seq1[i]][seq2[i]]
        if seq1[i] == seq2[i]:
            edit_distance += 1
    percentage = edit_distance / len(seq1)
    return score, percentage
# calculation of human and mouse:
print(alignment(dic['human'],dic['mouse']))
# human and cat:
print(alignment(dic['human'],dic['cat']))
# mouse and cat:
print(alignment(dic['mouse'],dic['cat']))

# output:
# alignment score for human and cat:3717.0, the percentage:0.8521739130434782
# alignment score for human and mouse:3579.0.0, the percentage:8211180124223603%
# alignment score for cat and mouse：3592.0， the percentage:0.817391304347826%

