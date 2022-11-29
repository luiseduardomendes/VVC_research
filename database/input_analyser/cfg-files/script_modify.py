from os import path, listdir
import re
from os import rename, remove

dir = '.'

files = [f for f in listdir(dir) if path.isfile(path.join(dir, f)) and f[-4:] == '.cfg']

#files = ['Campfire.cfg']

print(files)

pattern = re.compile(r'(InputFile                     : /home/video)(.+)')

for file_ in files:
    data = open(file_, 'r')
    new_data = open(file_[:-4]+'_copy.cfg','w')
    for line in data:
        check = pattern.findall(line)
        if len(check) > 0:
            new_data.write('InputFile                     : /'+check[0][1]+'\n')
        else:
            new_data.write(line)
    data.close()
    new_data.close()
    remove(file_)
    rename(file_[:-4]+'_copy.cfg', file_)
