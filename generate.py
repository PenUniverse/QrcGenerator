import sys
import xml
import os

path = sys.argv[1]
output = 'custom.qrc'

result = '<RCC>\n'
prefix_count = 0
file_count = 0

for now,dir_list,file_list in os.walk(path):
    now = now[len(path):]
    if now == '':
        now = '/'
    now = now.replace('\\','/')
    result = result + '    <qresource prefix="%s">\n' % now
    for n in file_list:
        result = result + '        <file>%s%s</file>\n' % (now[1:],n)
        file_count += 1
    result = result + '    </qresource>\n'
    prefix_count += 1

result = result + '</RCC>'

with open(output,'w') as f:
    f.write(result)
    print('Completed, %s prefixes and %s files processed.' % (prefix_count,file_count))
