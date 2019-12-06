ext = []
cls_ext = []
api = ['android', 'androidx constraint', 'androidx test', 'androidx', 'automotive', 'billing', 'components', 'constraint', 'databinding', 'install referrer', 'material', 'play core', 'support', 'test support', 'things', 'wearable']
sibal = 16
print(api[sibal], len(api))
with open('C:/Users/csos/Desktop/official_api/hi/' + api[sibal] + '.txt','r') as ff:
    ext = ff.readlines()

pak_name = []
reg = ''
for i in ext:
    if i == 'Overview\n':
        pak_name.append(reg)
    reg = i

for i in range(0, len(ext)):
    check = 0
    for j in pak_name:
        if ext[i] == j:
            check = 1
    if check == 0:
        cls_ext.append(ext[i])

# print(cls_ext)

del_list = []
for i in range(1,len(cls_ext)):
    if cls_ext[i] == '\n':
        if cls_ext[i-1] == '\n':
            if cls_ext[i+1] != 'Overview\n':
                del_list.append(cls_ext[i+1])
del_list = list(set(del_list))
print(del_list)

only_cls = []
for i in range(0, len(cls_ext)):
    check = 0
    for j in del_list:
        if cls_ext[i] == j:
            check = 1
    if check == 0:
        only_cls.append(cls_ext[i])
# print(only_cls)

str_cls = ''.join(only_cls).replace('\n\nOverview\n\n', '**********************')
# print(str_cls)

re_cls = (str_cls.replace('\n', ' ')).split('**********************')
# print(re_cls)
re_cls[0] = re_cls[0].split('   ')[1]
print(re_cls)

re_pak = []
for i in pak_name:
    re_pak.append(i.replace('\n', ''))
# print(re_pak)

final = []
c = 0
for j in re_cls:
    reg = j.split(' ')
    for i in reg:
        if i != '':
            final.append(''.join(re_pak[c]) + '.' + ''.join(i) + '\n')
    c += 1
print(final)

with open('C:/Users/csos/Desktop/official_api/final/'+api[sibal]+'.txt', 'w') as f:
    for i in final:
        f.writelines(i)
# re_cls_name_sp = []
# re_pak_name = []
# for i in only_cls:
#     re_cls_name_sp.append(i.replace('\n', ' '))
# for i in pak_name:
#     re_pak_name.append(i.replace('\n', ''))
# print(re_cls_name_sp)
# print(re_pak_name)
#
# re_cls_name = ''.join(re_cls_name_sp)
# print(re_cls_name.split('   '))

# for i in re_pak_name:
#     for j in range(0, len(re_cls_name)):
#         if re_cls_name[j] ==



# for i in pak_name:
#