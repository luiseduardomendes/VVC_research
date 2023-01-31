from source.vvc_execute_simulation import vvc_execute_simulation
from source.common.commonlib import read_config_file
from os import getcwd
from os.path import join

config_file = 'auxiliar_files/cfg_serv.txt'
data = read_config_file(config_file)

output_dir = data['out_videos_dir']
cfg_vid_dir = data['cfg_videos_dir']
vtm_path = data['vtm_dir']

vvc_execute_simulation(
    cfg_vid_dir=cfg_vid_dir, 
    output_dir=output_dir, 
    vtm_path=vtm_path, 
    num_frames=32, 
)