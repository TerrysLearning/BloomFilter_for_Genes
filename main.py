import helper_functions as hf

s = 100000 # define a bloom filter size 
bf1 = hf.generate_bloom('DNA_person/chr22_0_A.txt', s)
bf2 = hf.generate_bloom('DNA_person/chr22_0_B.txt', s)
bf3 = hf.generate_bloom('DNA_person/chr22_1_A.txt', s)
bf4 = hf.generate_bloom('DNA_person/chr22_1_B.txt', s)
inherit_result = hf.inherit_test(bf1, bf2, bf3, bf4) # get the inherit coefficient r
homo_num = hf.card_inter(bf1,bf2)
print(inherit_result/homo_num)
