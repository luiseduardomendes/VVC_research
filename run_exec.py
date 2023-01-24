import os
import sys
import source.common.vvc_exec as vex
from source.common.commonlib import read_config_file

if not os.path.isfile(sys.argv[1]):
    raise Exception("Insert a valid input argument")
config_file = sys.argv[1]
data = read_config_file(config_file)

out_videos_dir = data['out_videos_dir']
cfg_videos_dir = data['cfg_videos_dir']
vtm_dir = data['vtm_dir']


if not os.path.isdir(out_videos_dir):
    os.mkdir(out_videos_dir)

video_cfg = [
    f 
    for f in os.listdir(cfg_videos_dir) 
    if os.path.isfile(os.path.join(cfg_videos_dir, f)) and 
    f[-4:] == '.cfg'
]

quant_param = [22,27,32,37]

enc_cfgs = ['AI','LB','RA']

setting_name = 'precise'


for video in video_cfg:
    for qp in quant_param:
        for cfg in enc_cfgs:
            vex.exec(
                vtm_dir         = vtm_dir, 
                encoder_name    = cfg, 
                cfg_video       = os.path.join(cfg_videos_dir, video), 
                qp              = qp,
                out_dir         = out_videos_dir,
                video_name      = video[:-4], 
                VTM_version     = setting_name, 
                n_frames        = '32',
                gprof           = True,
                background_exec = True
            )

