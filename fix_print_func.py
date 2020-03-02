import re, os

file_list = os.listdir()
for file_name in file_list:
    if '.py' in file_name:

        fp = open(file_name, 'r')
        file_content = fp.read()
        fp.close()

        file_content = re.sub(r'print\s([\sa-zA-Z0-9._()%\'",]+)$', r'print(\2)', file_content)
        fp = open(file_name.split('.')[0]+'_1.py', 'w')
        fp.write(file_content)
        fp.close()
