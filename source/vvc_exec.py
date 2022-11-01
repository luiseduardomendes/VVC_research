import os
import re

# cfg_encoder parameter must be only the name, without path
def exec(self, cfg_encoder: str, cfg_video: str, video_name: str, qp: int, satd_settings: str, gprof : bool=False):
    vtm_dir = "/home/luispmendes/VVCSoftware_VTM/"

    satd = satd_settings.replace('(', '').replace(')', '').replace('/', '-')
    cfg_dir = vtm_dir + "cfg/"    
    bin_dir = vtm_dir + "bin/" 
    out_dir = vtm_dir + "out/" + satd + '/'

    ts_status = ''
    if (cfg_encoder == 'encoder_intra_vtm.cfg'):
        ts_status = '-ts 1'

    encoder = self.encoder_used(cfg_encoder)

    print(f'encoding {video_name} with cfg {cfg_encoder}, {cfg_video} and qp {qp}')
    print(f'satd used: {satd_settings}')

    self.mkdir_directories(out_dir, encoder, video_name)
    
    if gprof:
        os.system(  f'\n\"{bin_dir}EncoderAppStatic\" ' +
                    f'-c \"{cfg_dir}{cfg_encoder}\" ' + # encoder 
                    f'-c \"{cfg_video}\" ' + # video parameters 
                    f'-b \"{out_dir}videos_bin/{video_name}.bin\" ' + # output binary video
                    f'-q {qp} -f 32 {ts_status} --SIMD=SCALAR ' +
                    f'>> \"{out_dir}{video_name}/{encoder}/exec_log/log_{video_name}_qp{qp}_{encoder}_{satd}_exec.gplog\" ' + 
                    f'&& gprof {bin_dir}EncoderAppStatic gmon.out' +
                    f'>> {out_dir}/{video_name}/{encoder}/gprof_log/log_{video_name}_qp{qp}_{encoder}_gprof.txt &'
        )

    else:
        os.system(  f'\n\"{bin_dir}EncoderAppStatic\" ' +
                    f'-c \"{cfg_dir}{cfg_encoder}\" ' + # encoder 
                    f'-c \"{cfg_video}\" ' + # video parameters 
                    f'-b \"{out_dir}videos_bin/{video_name}.bin\" ' + # output binary video
                    f'-q {qp} -f 32 {ts_status} --SIMD=SCALAR ' +
                    f'>> \"{out_dir}{video_name}/{encoder}/exec_log/log_{video_name}_qp{qp}_{encoder}_{satd}_exec.gplog\" &' 
        )



def encoder_used(self, cfg_encoder: str) -> str:
    return re.findall(r'^encoder_([\w]+)_vtm\.cfg$', cfg_encoder)[0]

def mkdir_directories(self, out_dir: str, encoder: str, video_name: str):
    
    directories = [
        f'{out_dir}',
        f'{out_dir}videos_bin/',
        f'{out_dir}{video_name}/',
        f'{out_dir}{video_name}/{encoder}/',
        f'{out_dir}{video_name}/{encoder}/exec_log/',
        f'{out_dir}{video_name}/{encoder}/gprof_log/'
    ]

    for d in directories:
        if not os.path.isdir(d):
            os.mkdir(d)
