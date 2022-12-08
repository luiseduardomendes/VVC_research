import os
import re
import pandas as pd
import source.common.vvc_exec as vex
from auxiliar_files.server_paths import sv_paths as sv_path
from source.common.commonlib import file_subs, get_next_file, compile_VTM

file = get_next_file(sv_path['exec_buffer'])
file_subs(
    os.path.join('FilesForVVC/', file), 
    sv_path["commonlib"],
    'RdCost.cpp'
)

compile_VTM(sv_path["vtm"], sv_path["repo"])

cfg_videos_dir = sv_path['cfg_videos'] 
satd_src = sv_path['satd_src']
satd_dir = sv_path['commonlib']
out_videos_dir = sv_path['out_gprof']
vtm_dir = sv_path['vvc']

if not os.path.isdir(out_videos_dir):
    os.mkdir(out_videos_dir)

video_cfg = [
    f 
    for f in os.listdir(cfg_videos_dir) 
    if os.path.isfile(os.path.join(cfg_videos_dir, f)) and 
    f[-4:] == '.cfg'
]

quant_param = [
    22,
    27,
    32,
    37
]

enc_cfgs = [
    'encoder_intra_vtm.cfg',
    'encoder_lowdelay_vtm.cfg',
    'encoder_randomaccess_vtm.cfg'
]

setting_name = file
if file.endswith('.cpp'):
    setting_name = file[:-4]

for video in video_cfg:
    for qp in quant_param:
        for cfg in enc_cfgs:
            vex.exec(cfg, cfg_videos_dir+video, video[:-4], qp, setting_name, vtm_dir, gprof=True)
