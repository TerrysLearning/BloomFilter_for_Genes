import helper_functions as hf

s = 100000 # define a bloom filter size 
bf1 = hf.generate_bloom('DNA_person/chr22_0_A.txt', s)
bf2 = hf.generate_bloom('DNA_person/chr22_0_B.txt', s)
bf3 = hf.generate_bloom('DNA_person/chr22_1_A.txt', s)
bf4 = hf.generate_bloom('DNA_person/chr22_1_B.txt', s)
inherit_result = hf.inherit_test(bf1, bf2, bf3, bf4) # get the inherit coefficient r
homo_num = hf.card_inter(bf1,bf2)
print(inherit_result/homo_num)


# One example of testing multiple parent relationship
# import random 
# import pandas as pd
# c_indexs = [127, 128, 129, 130, 131, 132, 133, 148, 149, 150, 151, 160]
# f_indexs = [134, 135, 136, 137, 138, 139, 140, 152, 153, 154, 155, 166]
# m_indexs = [141, 142, 143, 144, 145, 146, 147, 156, 157, 158, 159, 'x']
# d = {'ID':[], 'Kin_Result':[], 'Stranger_Result':[]}
# df = pd.DataFrame(d)
# s = 200000
# chr_index = '1'
# file = open('data.vcf')
# lines = file.readlines()
# ls_22 = lines[22].split('\t')
# for i in range(len(c_indexs)):
#     f_name = 'chr'+chr_index +'_person/chr'+ chr_index + '_' + str(f_indexs[i]-9)
#     c_name = 'chr'+chr_index +'_person/chr'+ chr_index + '_' + str(c_indexs[i]-9)
#     st_index = random.choice(range(9, 100))  # stranger
#     st_name = 'chr'+chr_index +'_person/chr'+ chr_index + '_' + str(st_index)
    
#     bfc1 = hf.generate_bloom( c_name + '_A.txt', s)
#     bfc2 = hf.generate_bloom( c_name + '_B.txt', s)
#     bff1 = hf.generate_bloom( f_name + '_A.txt', s)
#     bff2 = hf.generate_bloom( f_name + '_B.txt', s)
#     bfs1 = hf.generate_bloom( st_name + '_A.txt', s)
#     bfs2 = hf.generate_bloom( st_name + '_B.txt', s)
    
#     # Test father with child
#     homo_num = hf.card_inter(bff1,bff2)
#     print(homo_num, '*****')
#     print(hf.actual_insec(f_name + '_A.txt', f_name + '_B.txt')[0])
    
#     kin_result = hf.inherit_test(bff1, bff2, bfc1, bfc2)
#     print(kin_result)
#     rs1 = round(kin_result/homo_num, 4)
    
#     # Test father with stranger
#     stra_result = hf.inherit_test(bff1, bff2, bfs1, bfs2)
#     rs2 = round(stra_result/homo_num, 4)
    
#     # Add into csv
#     ids = ls_22[f_indexs[i]] + ' / ' + ls_22[c_indexs[i]]
#     df.loc[len(df.index)] = [ids, rs1, rs2] 
