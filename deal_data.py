# load data to person txt 

file = open('ALl_chr22_small.vcf')  # data file 
lines = file.readlines()

# Loop the data and save each person into txt
# get snp for each person
# chr22 only has one alt in alt, other chr may need to change the code

# Lists of some person IDs that I want to save into txt
second_list = ['NA19625','NA20359','NA19657','NA19660','NA19664','NA19672','NA19726']
second_i_list = ['NA20414','NA20363','NA19753','NA19664','NA19672','NA19685','NA19738']
parent_list = ['NA19660','NA19661','NA19675','NA19675','HG00656','HG00657','NA19313','NA19381','NA19445','NA19469']
child_list = ['NA19685','NA19685','NA19678','NA19679','HG00702','HG00702','NA19331','NA19382','NA19453','NA19470']
ls = lines[29].split('\t')
data_index = []
# Which person's data I want to save into txt
use_info = second_list[:3] + second_i_list[:3] + parent_list[:3] + child_list[:3]
for info in use_info:
    data_index.append(ls.index(info))
print(data_index)

folder_path = 'chr22_person5/' 
name_line = lines[29].split('\t')
# two chromosomes of persons
f1 = ['']*(len(data_index))
f2 = ['']*(len(data_index))

for j in range(len(data_index)):
    i = data_index[j]
    f1[j] += name_line[i] + '\n'
    f2[j] += name_line[i] + '\n'

for line in lines[30:]:
    ls = line.split('\t')
    pos = ls[1]
    ref = ls[3]
    alt = ls[4].split(',')
    for j in range(len(data_index)):
        i = data_index[j]
        per = ls[i]
        pers = ls[i].split('|')
        p1 = int(pers[0][0])
        p2 = int(pers[1][0])
        if p1 != 0:
            snp = snp = '22/' + pos + '/' + ref + '/' + alt[p1-1] + '\n' 
            f1[j] += snp
        if p2 != 0:
            snp = snp = '22/' + pos + '/' + ref + '/' + alt[p2-1] + '\n' 
            f2[j] += snp

for j in range(len(data_index)):
    i = data_index[j]
    file1 = open(folder_path + 'chr22_' + name_line[i] + '_A.txt', 'w')
    file2 = open(folder_path + 'chr22_' + name_line[i] + '_B.txt', 'w')
    file1.write(f1[j])
    file2.write(f2[j])