import re

# test_string = '2-dimethylaminoethanol, 2-[(2-[2-(dimethylamino)ethoxy]ethyl)methylamino]ethanol'
# test_string = 'METHANOL,KETHANOL, 1,2-DICHLOROBENZENE'
test_string = '1,3,5-TRIS(2-HYDROXYETHYL) HEXAHYDRO-S-TRIAZINE, 1,2-DICHLOROBENZENE,METHANOL,KETHANOL, 1,2-DICHLOROBENZENE'

splitted_list = test_string.split(',')
chemical_lst = []

tmp_lst = []
counter = 1
for item in splitted_list:
    if counter == 1:
        tmp_lst.append(item)
        chemical_lst.append(item)
        counter += 1
        continue
    
    # print('last item ', tmp_lst[-1:][0])
    # print('last item two char ', tmp_lst[-1:][0][-2:])
    # print('is char, ', isinstance(tmp_lst[-1:][0][-2:], str))
    # print('is char, ', re.search("\d", tmp_lst[-1:][0][-2:]))
    # tmp_lst.append(item)

    # print('============')
    # if tmp_lst[-1:][0][0] == ' ':
    #     print('blank found')
    # tmp = ''

    
    if re.search("\d", tmp_lst[-1:][0][-2:]):
        print('in if - char is : ',tmp_lst[-1:][0][0])
        if tmp_lst[-1:][0][0] == ' ':
            print('inside')
            chemical_lst.pop()
            tmp = ''.join(map(str, tmp_lst[-1:][0]))
            current_val = item
            # print(tmp.strip() + ","+ current_val)
            chemical_lst.append(tmp.strip() + "," + str(current_val))
            tmp_lst.append(item)
            # tmp.append(item)
            # st = ','.join(tmp)
            # print('string : ',st)
            # print('break point found')
        else:
            tmp_lst.append(item)
            chemical_lst.pop()
            chemical_lst.append(','.join(tmp_lst))
            # print(chemical_lst)
            # print(tmp.strip() + ","+ current_val)

    else:
        # break
        tmp_lst.append(item)
        chemical_lst.append(item)
       

        # print('in else ', tmp_lst)
    print('chemical list: ',chemical_lst)

