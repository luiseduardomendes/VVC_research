import os
import re

# cfg_encoder parameter must be only the name, without path
def exec(cfg_encoder: str, cfg_video: str, video_name: str, qp: int, satd_settings: str, vtm_dir : str, n_frames:int=32, gprof : bool=False):

    satd = satd_settings.replace('(', '').replace(')', '').replace('/', '-')
    if satd.endswith('.cpp'):
        satd = satd[:-4]
    cfg_dir = vtm_dir + "cfg/"    
    bin_dir = vtm_dir + "bin/" 
    out_dir = vtm_dir + "_out_/"


    # ts status is only used when the cfg selected is the intra encoding
    ts_status = ''
    if (cfg_encoder == 'encoder_intra_vtm.cfg'):
        ts_status = '-ts 1'

    # finds out what is the cfg used
    encoder = __encoder_used__(cfg_encoder)

    print(f'encoding {video_name} with cfg {cfg_encoder}, {cfg_video} and qp {qp}')
    print(f'satd used: {satd_settings}')

    __mkdir__(out_dir, satd, encoder)
    
    if gprof:
        os.system(  
            f'\n\"{bin_dir}EncoderAppStatic\" ' +
            f'-c \"{cfg_dir}{cfg_encoder}\" ' + # encoder location
            f'-c \"{cfg_video}\" ' + # video parameters 
            f'-b \"{out_dir}videos_bin/{video_name}.bin\" ' + # output binary video
            f'-q {qp} -f {n_frames} {ts_status} --SIMD=SCALAR ' + # qp, number of frames, 
            f'>> \"{out_dir}vvc_log/{satd}/{encoder}/log_{video_name}_qp{qp}_{encoder}_{satd}.vvclog\" ' + 
            f'&& cd {bin_dir} && gprof {bin_dir}EncoderAppStatic gmon.out' +
            f'>> \"{out_dir}gprof_log/{satd}/{encoder}/log_{video_name}_qp{qp}_{encoder}_{satd}.gplog\" &'
        )

    else:
        os.system(  
            f'\n\"{bin_dir}EncoderAppStatic\" ' +
            f'-c \"{cfg_dir}{cfg_encoder}\" ' + # encoder 
            f'-c \"{cfg_video}\" ' + # video parameters 
            f'-b \"{out_dir}videos_bin/{video_name}.bin\" ' + # output binary video
            f'-q {qp} -f {n_frames} {ts_status} --SIMD=SCALAR ' +
            f'>> \"{out_dir}vvc_log/log_{video_name}_qp{qp}_{encoder}_{satd}.vvclog\" '
        )


def __mkdir__(out_dir, satd, encoder):
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)

    if not os.path.isdir(out_dir + 'vvclog/'):
        os.mkdir(out_dir + 'vvclog/')
    if not os.path.isdir(out_dir + 'gproflog/'):
        os.mkdir(out_dir + 'gproflog/')

    if not os.path.isdir(out_dir + 'vvclog/' + satd + '/'):
        os.mkdir(out_dir + 'vvclog/' + satd + '/')
    if not os.path.isdir(out_dir + 'gproflog/' + {satd} + '/'):
        os.mkdir(out_dir + 'gproflog/' + satd + '/')

    if not os.path.isdir(out_dir + 'vvclog/' + satd + '/' + encoder + '/'):
        os.mkdir(out_dir + 'vvclog/' + satd + '/' + encoder + '/')
    if not os.path.isdir(out_dir + 'gproflog/' + {satd} + '/' + encoder + '/'):
        os.mkdir(out_dir + 'gproflog/' + satd + '/' + encoder + '/')



def __encoder_used__(cfg_encoder: str) -> str:
    return re.findall(r'^encoder_([\w]+)_vtm\.cfg$', cfg_encoder)[0]

