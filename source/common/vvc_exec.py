import os
import re
from auxiliar_files.server_paths import sv_paths

# cfg_encoder parameter must be only the name, without path
def exec(
        # --------------- vtm parameters --------------- #
        vtm_dir : str,                  # path to VTM
        encoder_name: str,              # name of encoder used = ('AI', 'LB', 'RA')
        cfg_video: str,                 # path to the '.cfg' file
        qp: int,                        # quantization parameter used
        
        # ------------- optional parameters ------------ #
        out_dir: str = '_out_',         # output to the logs and binaries files
        video_name: str='any',          # output video name
        VTM_version: str='precise',     # name of the version of vtm executed
        n_frames='',                    # number of frames that must be 
        background_exec:bool=True,      # execute the encoder in background
        gprof : bool=False,             # flag to execute using profiler or not
        display_data:bool=True          # print the configurations used
    ):

    # standard path to the config and binaries
    cfg_dir = os.path.join(vtm_dir, 'cfg')
    bin_dir = os.path.join(vtm_dir, 'bin')

    # standard path to the encoders
    cfg_dict = {
        'AI': 'encoder_intra_vtm.cfg',
        'LB': 'encoder_lowdelay_vtm.cfg',
        'RA': 'encoder_randomaccess_vtm.cfg',
    }
    cfg_encoder = os.path.join(cfg_dir, cfg_dict[encoder_name])

    # ts status is only used when the cfg selected is the intra encoding
    ts_status = ''
    if (cfg_encoder == 'encoder_intra_vtm.cfg'):
        ts_status = '-ts 1'

    if display_data:
        __display_info__(video_name, encoder_name, cfg_video, qp, VTM_version)
    
    if background_exec:
        background_status = '&'
    else:
        background_status = ''

    video_identifier        = f'{video_name}_qp{qp}_{cfg_encoder}_{VTM_version}'
    binary_encoder_path     = os.path.join(bin_dir, 'EncoderAppStatic')
    encoder_cfg_path        = os.path.join(cfg_dir, cfg_encoder)

    binary_videos_dir       = os.path.join(out_dir, 'videos_bin')
    make_path_bin(binary_videos_dir)

    binary_videos_path      = os.path.join(binary_videos_dir, f'{video_identifier}.bin')

    vvc_log_name            = f'log_{video_identifier}.vvclog'
    gprof_log_name          = f'log_{video_identifier}.gplog'
    
    output_log_path_vvc     = os.path.join(out_dir, 'vvc_log', VTM_version, cfg_encoder, vvc_log_name)
    make_path_log_vvc(out_dir, VTM_version, cfg_encoder)
    
    output_log_path_gprof   = os.path.join(out_dir, 'gprof_log', VTM_version, cfg_encoder, gprof_log_name)
    make_path_log_gprof(out_dir, VTM_version, cfg_encoder)
    
    command = \
        f'\n\"{binary_encoder_path}\" ' + \
        f'-c \"{encoder_cfg_path}\" ' + \
        f'-c \"{cfg_video}\" ' + \
        f'-b \"{binary_videos_path}\"' + \
        f'-q {qp} -f {n_frames} + {ts_status} --SIMD=SCALAR' + \
        f'>> \"{output_log_path_vvc}\" {background_status}'

    if gprof:
        command = command + \
            f'&& cd {bin_dir} && gprof {binary_encoder_path} gmon.out' + \
            f'>> \"{output_log_path_gprof}\" {background_status}'


def __display_info__(
        video_name, 
        encoder_name,
        cfg_video,
        qp,
        VTM_version
    ):
    print()
    print(f'Encoding:...........{video_name}')
    print()
    print(f'Encoder:............{encoder_name}')
    print(f'Video codif:........{cfg_video}')
    print(f'QP:.................{qp}')
    print(f'VTM version used:...{VTM_version}')
    print()
    
def make_path_log_vvc(out_dir, VTM_version, cfg_encoder):
    if not os.path.isdir(os.path.join(out_dir, 'vvc_log')):
        os.mkdir(os.path.join(out_dir, 'vvc_log'))
    if not os.path.isdir(os.path.join(out_dir, 'vvc_log', VTM_version)):
        os.mkdir(os.path.join(out_dir, 'vvc_log', VTM_version))
    if not os.path.isdir(os.path.join(out_dir, 'vvc_log', VTM_version, cfg_encoder)):
        os.mkdir(os.path.join(out_dir, 'vvc_log', VTM_version, cfg_encoder))

def make_path_log_gprof(out_dir, VTM_version, cfg_encoder):
    if not os.path.isdir(os.path.join(out_dir, 'gprof_log')):
        os.mkdir(os.path.join(out_dir, 'gprof_log'))
    if not os.path.isdir(os.path.join(out_dir, 'gprof_log', VTM_version)):
        os.mkdir(os.path.join(out_dir, 'gprof_log', VTM_version))
    if not os.path.isdir(os.path.join(out_dir, 'gprof_log', VTM_version, cfg_encoder)):
        os.mkdir(os.path.join(out_dir, 'gprof_log', VTM_version, cfg_encoder))

def make_path_bin(binary_videos_dir):
    if not os.path.isdir(binary_videos_dir):
        os.mkdir(binary_videos_dir)