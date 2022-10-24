import sys
import os

if len(sys.argv) <= 1:
    print('usage: generate.py <path>')
    exit()

path = sys.argv[1]
output = 'custom.qrc'

result = '<RCC>\n'
prefix_count = 0
file_count = 0

def std_dir(url:str):
    url = url.replace('\\','/')
    if url[:1] == '/':
        url = url[1:]
    if url[:1] == '/':
        return std_dir(url)
    return url

for now,dir_list,file_list in os.walk(path):
    now = now[len(path):]
    now = std_dir(now)
    result = result + '    <qresource prefix="/%s">\n' % now
    for fn in file_list:
        fn = std_dir(fn)
        p = now
        if p != '':
            p = p + '/'
        result = result + '        <file>%s%s</file>\n' % (p,fn)
        file_count += 1
    result = result + '    </qresource>\n'
    prefix_count += 1

result = result + '</RCC>'

with open(output,'w') as f:
    f.write(result)
    print('Completed, %s prefixes and %s files processed.' % (prefix_count,file_count))
