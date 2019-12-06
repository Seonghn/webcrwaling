import os

ex = []
for (path, dir, files) in os.walk("C:/Users/csos/Desktop/official_api/hi"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.txt':
            ex.append(filename[:-4])

print(ex)