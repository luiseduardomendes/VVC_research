from pathlib import Path

out_path = '.execution_buffer.txt'
dir_path = 'FilesForVVC/'

files_list = [str(f) for f in Path(dir_path).rglob('*.cpp')]

with open(out_path, 'w') as f:
    for line in files_list:
        f.write(line + '\n')
    f.close()


