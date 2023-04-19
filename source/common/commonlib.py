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
    if not(os.path.isdir(os.path.join(vtm_path, "build"))):
        os.mkdir(os.path.join(vtm_path, "build"))
    os.system(f'cd {os.path.join(vtm_path, "build")}')
    os.system(f'cmake {vtm_path} -DCMAKE_BUILD_TYPE=Release')
    turn_on_profiling_in_makefile(os.path.join(os.path.join(vtm_path, "build"),'CMakeCache.txt'))
    os.system('make')
    os.system(f'cd {repo_path}')

def create_exec_buffer(output_dir='.',output_name='.execution_buffer', dir_path='.', extension:str='.cpp'):
    files_list = [str(f) for f in Path(dir_path).rglob('*'+extension)]

    with open(os.path.join(output_dir, output_name), 'w') as f:
        for file in files_list:
            f.write(file + '\n')
        f.close()

def change_expression_in_file(file, expression, change_to):
    temp_file_name = ".swp_" + file
    while os.path.isfile(temp_file_name):
        temp_file_name = temp_file_name + '_'
    
    t = open (temp_file_name, 'w') 
    f = open(file, 'r')
    
    line = f.read()
    if len(re.findall(expression, line)) > 0:
        matches = re.finditer(expression, line, re.M)
        for match in matches:
            t.write(f'{line[:match.start()]}{change_to}{line[match.end():]}')
    else:
        t.write(line)                
    f.close()
    t.close()

    os.remove(file)
    os.rename(temp_file_name, file)


def turn_on_profiling_in_makefile(file):   
    if not os.path.isfile(file):
        raise Exception(f"File {file} does not exists")
    with open(file) as f:
        txt = f.read()
        f.close()

    check = re.findall('//Flags used by the CXX compiler during RELEASE builds.\nCMAKE_CXX_FLAGS_RELEASE:STRING=-O3 -DNDEBUG -pg', txt)
    if len(check) < 0:
        change_expression_in_file(
            file, 
            '//Flags used by the CXX compiler during RELEASE builds.\nCMAKE_CXX_FLAGS_RELEASE:STRING=-O3 -DNDEBUG'
            '//Flags used by the CXX compiler during RELEASE builds.\nCMAKE_CXX_FLAGS_RELEASE:STRING=-O3 -DNDEBUG -pg'
        )

    check = re.findall('//Flags used by the CXX compiler during RELWITHDEBINFO builds.\nCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING=-O2 -g -DNDEBUG -pg', txt)
    if len(check) < 0:
        change_expression_in_file(
            file,
            '//Flags used by the CXX compiler during RELWITHDEBINFO builds.\nCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING=-O2 -g -DNDEBUG',
            '//Flags used by the CXX compiler during RELWITHDEBINFO builds.\nCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING=-O2 -g -DNDEBUG -pg'
        )

def read_config_file(filename: str):
    with open(filename, 'r') as f:
        data = {
            "vtm_dir": f.readline().replace('\n', ''),
            "cfg_dir": f.readline().replace('\n', ''),
            "out_dir": f.readline().replace('\n', '')
        }
        f.close()
    print(data)
    
    if not os.path.isdir(data['vtm_dir']):
        raise Exception("vtm_dir is not a directory")
    elif not os.path.isdir(data['cfg_videos_dir']):
        raise Exception("cfg_videos_dir is not a directory")
    else:
        return data
    
