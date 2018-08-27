import os

path_list = []
xib_list = []
txt_list = []
path1 = ""
path2 = ""

def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

for file in find_all_files(path1):
    path_list.append(file)


print('--------------------------------')
print('--------------------------------')
print('--------------------------------')

with open(path2, "w") as xibPath:
    for xib in path_list:
        if ".xib" in xib:
            replaced_xib = xib.replace(path1, '')
            xibPath.write(replaced_xib + "\n")
            xib_list.append(replaced_xib)

    for xib in xib_list:
        print(xib)


print(len(xib_list))