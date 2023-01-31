from source.common.commonlib import file_subs, compile_VTM
from source.common.vvc_exec import exec
import os
import re

def vvc_execute_simulation(
    cfg_vid_dir:str,
    output_dir:str,
    vtm_path:str,

    qps : list = [22, 27, 32, 37],
    enc_cfgs : list = ['AI','LB','RA'],
    version : str = 'Precise',

    num_frames : int = 32,
    enable_gprof : bool = True,
    enable_background_execution : bool = False,

    src_modify_file: str = None,
    dst_modify_file: str = None,
    rename_file: str = None
):
    __create_output_dir__(output_dir)
    
    video_cfg = __config_files_in_dir__(cfg_vid_dir)
    
    if src_modify_file != None and dst_modify_file != None:
        file_subs(src_modify_file, dst_modify_file, rename_file)
        compile_VTM(vtm_path, os.getcwd())


    for video in video_cfg:
        for cfg in enc_cfgs:
            for qp in qps:
                exec(
                    vtm_dir         = vtm_path, 
                    encoder_name    = cfg, 
                    cfg_video       = os.path.join(cfg_vid_dir, video), 
                    qp              = qp,
                    out_dir         = output_dir,
                    video_name      = video[:-4], 
                    VTM_version     = version, 
                    n_frames        = str(num_frames),
                    gprof           = enable_gprof,
                    background_exec = enable_background_execution
                )

def __create_output_dir__(output_dir):
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    else:
        while(os.path.isdir(output_dir)):
            output_dir = __rename_dir__(output_dir)
        os.mkdir(output_dir)

def __config_files_in_dir__(cfg_vid_dir):
    if os.path.isdir(cfg_vid_dir):
        raise Exception("Video config directory not exists")
    return [
        f 
        for f in os.listdir(cfg_vid_dir) 
        if os.path.isfile(os.path.join(cfg_vid_dir, f)) and 
        f[-4:] == '.cfg'
    ]

def __rename_dir__(d : str ):
    matches = re.findall(r'(\d+)$', d)
    if len(matches) > 0:
        n = int(matches[-1])
        n = n + 1
        d = d[:-1] + str(n)
    else:
        d = d + '1'
    return d