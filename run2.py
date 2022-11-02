import os
import re
import sys
import pandas as pd
import source.vvc_exec as vex

def file_subs(file_path, destiny_dir) -> None:

    if __verify_path__(file_path):
        source_path = f'{file_path}'
    else:   
        raise Exception("invalid file path!")
    
    if __verify_dir__(destiny_dir):
        destiny_path = f'{destiny_dir}'
    else:   
        raise Exception("Destiny is not a directory!")

    os.system(f"cp \"{source_path}\" \"{destiny_path}RdCost.cpp\"") 

def __verify_path__(path:str) -> bool:
    if os.path.isfile(path):
        return True
    return False

def __verify_dir__(dir1 : str) -> bool:
    if os.path.isdir(dir1):
        return True
    return False
    
# create a pandas series to generalize the paths used
temp = pd.read_csv('source/server_paths.csv')
sv_path = temp['path']
sv_path = sv_path.set_axis(temp['dir'])

pattern = re.compile(r'^FilesForVVC/(.+)$')

file = sys.argv[1]

file_subs('FilesForVVC/'+file, sv_path["commonlib"])

os.system(f'cmake {sv_path["vtm"]} -DCMAKE_BUILD_TYPE=Release')
os.system('make')
os.system(f'cd {sv_path["repo"]}')

temp =  pd.read_csv('source/server_paths.csv')
sv_path = temp['path']
sv_path = sv_path.set_axis(temp['dir'])

cfg_videos_dir = sv_path['vtm'] + '/cfg-files/'
satd_src = sv_path['repo'] + '/FilesForVVC/'
satd_dir = sv_path['commonlib']
out_videos_dir = sv_path['out']

video_cfg = [f for f in os.listdir(cfg_videos_dir) if os.path.isfile(os.path.join(cfg_videos_dir, f)) and f[-4:] == '.cfg']

quant_param = [
        22,
        27,
        32,
        37]
enc_cfgs = [
    'encoder_intra_vtm.cfg',
    'encoder_lowdelay_vtm.cfg',
    'encoder_randomaccess_vtm.cfg'
]

setting_name = file

for video in video_cfg[:1]:
    for qp in quant_param[:1]:
        for cfg in enc_cfgs[:1]:
            vex.exec(cfg, cfg_videos_dir+video, video[:-4], qp, setting_name)
