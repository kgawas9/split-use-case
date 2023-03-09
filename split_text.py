import re

# test_string = '2-dimethylaminoethanol, 2-[(2-[2-(dimethylamino)ethoxy]ethyl)methylamino]ethanol'
# test_string = 'METHANOL,KETHANOL, 1,2-DICHLOROBENZENE'
# test_string = '1,3,5-TRIS(2-HYDROXYETHYL) HEXAHYDRO-S-TRIAZINE, 1,2-DICHLOROBENZENE,METHANOL,KETHANOL, 1,2-DICHLOROBENZENE'
# test_string = 'Nickle Charoride (NiCl2), Hydrochloric acid'
# test_string = 'D009, D008'
test_string = 'Light aromatic naphtha, 1,2,3-Trimmethylbenzene'

splitted_list = test_string.split(',')

chemical_lst = []
tmp_lst = []

str_chemical_val = ''
temp_val = False

for item in splitted_list:
    # print('current item : ', item , ' | previous item : ', tmp_lst[-1])
    
    if len(item) > 3:
            if str_chemical_val:
                 chemical_lst.append(str_chemical_val + "," + item.strip())
                 str_chemical_val=''
            else:
                chemical_lst.append(item.strip())
    else:
        if str_chemical_val:
             str_chemical_val = str_chemical_val + "," + item.strip()
        else:
            str_chemical_val = item.strip()
        # print('current value : ', item, ' | chemical string val : ', str_chemical_val)

    tmp_lst.append(item)

print(chemical_lst)


















#     try:
#         if tmp_lst[-1][-3]:
#             # print('in try - if')
#             if str_chemical_val:
#                 print('in str_chemical value')
#                 chemical_lst.append(str_chemical_val)
#                 str_chemical_val = ''
#             chemical_lst.append(item)
#     except:
#         print('in except')
#         str_chemical_val =  str_chemical_val + "," + item
#         print('previous value ', [tmp_lst[-1]], ' | current value : ', item, ' | chemical string val : ', str_chemical_val)

#     tmp_lst.append(item)

# print(chemical_lst)