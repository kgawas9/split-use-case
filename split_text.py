"""
Test use case to split the documents based on certain condition
"""
import re

test_string = '2-dimethylaminoethanol, 2-[(2-[2-(dimethylamino)ethoxy]ethyl)methylamino]ethanol'
test_string = 'METHANOL,KETHANOL, 1,2-DICHLOROBENZENE'
test_string = '1,3,5-TRIS(2-HYDROXYETHYL) HEXAHYDRO-S-TRIAZINE, 1,2-DICHLOROBENZENE,METHANOL,KETHANOL, 1,2-DICHLOROBENZENE'
test_string = 'Nickle Charoride (NiCl2), Hydrochloric acid'
test_string = 'D009, D008'
test_string = 'Light aromatic naphtha, 1,2,3-Trimmethylbenzene'
test_string = 'ACETON, PEROFLUORD-3,6,9-TrOXATRIDEANOIC ACID'
test_string = '1,3,5-Triazine-1,3,5(2H,H,6H)-triethanol, 1,2-Benzisothiazolin-3-one'

split_text = re.split(r"\b\w{3}[\W_]\w{1,2},", test_string)
print(split_text)

# splitted_list = test_string.split(',')
# chemical_lst = []
# str_chemical_val = ''


# for item in splitted_list:

#     if len(item) > 3:
#             if str_chemical_val:
#                  chemical_lst.append(str_chemical_val + "," + item.strip())
#                  str_chemical_val=''
#             else:
#                 if item[0] == ' ':
#                     if str_chemical_val:
#                         str_chemical_val = str_chemical_val + "," + item.strip()
#                     else:
#                         str_chemical_val = item.strip()
#                         if not len(splitted_list) > 2:
#                             chemical_lst.append(str_chemical_val)
#                             str_chemical_val=''
#                 else:
#                     chemical_lst.append(item.strip())
#     else:

#         if str_chemical_val:
#              str_chemical_val = str_chemical_val + "," + item.strip()
#         else:
#             str_chemical_val = item.strip()
#         # print('current value : ', item, ' | chemical string val : ', str_chemical_val)

# print(chemical_lst)


