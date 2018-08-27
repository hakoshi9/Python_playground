import os

path = ""
xibList = ""
splitXib = []

with open('./xibPath.txt', 'r') as xibPath:
    xibList = [s.strip() for s in xibPath.readlines()]



    

for xib in xibList:
    splitXib.append(xib.split('/'))
    

for xib in splitXib:
    make_path = ""
    for sx in xib:
        if '.xib' not in sx:
            make_path += sx + "\\"
            os.makedirs("{0}\\{1}".format(path, make_path), exist_ok=True)
        elif '.xib' in sx:
            full_path = make_path + sx.replace('.xib', '.txt')
            with open(path + "\\" + full_path, 'w') as xibFile:
                xibFile.write(make_path + sx)