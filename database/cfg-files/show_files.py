from os import listdir, path

files = [f for f in listdir('.') if path.isfile(path.join('.', f)) and f[-4:] == '.cfg']

print(files)

    
