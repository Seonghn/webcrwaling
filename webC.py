from urllib.request import urlopen
from bs4 import BeautifulSoup

path = 'C:/Users/csos/Desktop/official_api/'
# r = requests.get('https://developer.android.com/reference/packages.html')
# html = r.text

with open(path + 'html.txt', 'r') as f:
    hl = f.readlines()
hll = []
for i in hl:
    hll.append(i.split('\n')[0])
# print(hll)

for i in hll:
    html = urlopen(i)
    line = BeautifulSoup(html, 'html.parser')
    print(i)
    # with open(path + 'api.txt', 'a+', encoding='utf-8') as f:
    for j in line.find_all(string=True):
        print(j)



# for link in line.find_all('a'):
#     print(link.text.strip(), link.get('href'))

# with open('C:/Users/csos/Desktop/official_api/api.txt','w',encoding='utf-8') as f:
#     for i in line:
#         f.writelines(i)
