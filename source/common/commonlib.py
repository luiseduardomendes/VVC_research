import os
import re
from os.path import isfile, isdir
from pathlib import Path
    
def file_subs(file_path, destiny_dir, rename_like) -> None:
    if isfile(file_path):
        source_path = f'{file_path}'
    else:   
        raise Exception("invalid file path!")
    
    if isdir(destiny_dir):
        destiny_path = f'{destiny_dir}'
    else:   
        raise Exception("Destiny is not a directory!")

    os.system(f"cp \"{source_path}\" \"{destiny_path}{rename_like}\"") 


def get_next_file(exec_buffer, erase = True):
    # reads the first line, then, if erase is on, erases the line read
    with open(exec_buffer, 'r') as f:
        file = f.readline()
        if file.endswith('\n'):
            file = file[:-1]
        if erase:
            with open(exec_buffer + 'temp', 'w') as out:
                for line in f:
                    out.write(line)
                out.close()
        f.close()
    
    if erase:
        os.remove(exec_buffer)
        os.system(f"mv {exec_buffer + 'temp'} {exec_buffer}")

    return file

def compile_VTM(vtm_path, repo_path):
    os.system(f'cmake {vtm_path} -DCMAKE_BUILD_TYPE=Release')
    os.system('make')
    os.system(f'cd {repo_path}')

def reset_exec_buffer(out_path, dir_path):
    files_list = [str(f) for f in Path(dir_path).rglob('*.cpp')]

    with open(out_path, 'w') as f:
        for line in files_list:
            f.write(line + '\n')
        f.close()

