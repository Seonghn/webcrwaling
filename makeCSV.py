import csv, os, subprocess
import time, datetime

line = []
pathLine = []
dirName = []
jja = []


def arr_reset():
    line = []
    pathLine = []
    dirName = []
    return line, pathLine, dirName

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.txt':
                    line.append(filename)
                    dirName.append(dirname)
                    if dirname[-1] == '/':
                        pathLine.append(full_filename)
                    else:
                        pathLine.append(dirname + '/' + filename)
    except PermissionError:
        pass


def permission_extract(p_list, save_path, st_time):
    print('- search 함수 실행 -')
    search('Z:/0.Dataset/AndroZoo/permission(.txt)')
    print('- search 함수 완료 -')
    print(time.time() - st_time)
    for i in range(0, len(line)):
        getRow = [0] * len(p_list)
        getRow[0] = line[i]
        try:
            with open(pathLine[i], 'r', encoding='utf-8') as f:
                p_read = f.readlines()
            for j in p_read:
                cnt = 0
                for k in p_list[1:]:
                    if cnt > len(getRow):
                        break
                    if j.find(k[:-1]) != -1:
                        getRow[cnt+1] = 1
                    cnt += 1
            if pathLine[i].find('benign') != -1:
                with open(save_path + 'ben_permission.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(getRow)
            else:
                with open(save_path + 'mal_permission.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(getRow)
        except UnicodeDecodeError:
            jja.append(pathLine[i])
            pass
        print(i)
    return jja


def main():
    st_time = time.time()
    arr_reset()
    pl_path = 'Z:/0.Dataset/AndroZoo/'
    save_path = 'Z:/0.Dataset/AndroZoo/permission(.txt)/'
    with open(pl_path + 'permission_list.txt', 'r', encoding='utf-8') as pl:
        p_list = ['apk_name'] + pl.readlines()

    with open(save_path + 'ben_permission.csv', 'w+', encoding='utf-8', newline='') as perm:
        writer = csv.DictWriter(perm, fieldnames=p_list)
        writer.writeheader()

    with open(save_path + 'mal_permission.csv', 'w+', encoding='utf-8', newline='') as perm:
        writer = csv.DictWriter(perm, fieldnames=p_list)
        writer.writeheader()
        # writer = csv.writer(perm)
    print('- 기준 csv 생성 -')
    permission_extract(p_list, save_path, st_time)
    print('- 퍼미션 추출 완료 -')
    print(time.time() - st_time)
    print('- 에러뜬 파일 -')
    print(jja)


if __name__ == '__main__':
    main()
