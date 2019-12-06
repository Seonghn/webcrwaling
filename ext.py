path = 'C:/Users/csos/Desktop/official_api/'
with open(path + 'output.txt', 'r', encoding='utf-8') as f:
    line = f.readlines()
line = ''.join(line).split('Class Index\nPackage Index\n')
print(line)