import os

class vvc_executer:
    def __init__(self, vtm_path=None, video=None, video_cfg=None, cfg='AI', qp=22, version='Precise', n_frames=32):
        self.ts_status = ''
        
        self.set_cfg(cfg)
        self.set_qp(qp)
        self.set_version(version)
        
        if video_cfg != None and video != None:
            self.set_video_cfg(video_cfg, video)
        if vtm_path != None:
            self.set_vtm_path(vtm_path)

        self.n_frames = n_frames
        self.display = True
        self.bg_exec = False

    def run_exec(self):
        self.bin_encoder_path = os.path.join(self.bin_dir, 'EncoderAppStatic')
        self.cfg_encoder_path = os.path.join(self.cfg_dir, self.cfg_enc)
        self.bin_videos_path  = os.path.join(self.output_path, 'videos_bin')

        self.update_config()
        self.update_paths()

        os.system(self.__create_command__())

        if self.display:
            self.__display_info__()

    def set_video_params(self, video, cfg, qp, version):
        self.__set_video_identifier__(video, cfg, qp, version)
        self.video = video
        self.set_cfg(cfg)
        self.qp = qp
        self.version = version

    def set_vtm_path(self, vtm_path:str):
        self.vtm_path = vtm_path
        self.cfg_dir = os.path.join(vtm_path, 'cfg')
        self.bin_dir = os.path.join(vtm_path, 'bin')
    
    def set_version(self, version:str):
        self.version = version

    def set_output_path(self, output_path:str):
        self.output_path = output_path
        
    def __enable_output_in_ext_file__(self):
        vvc_log_name            = f'log_{self.video_identifier}.vvclog'
        try:
            self.__make_path_log_vvc__(self.output_path, self.version, self.cfg)
            self.output_vvc_log_path = os.path.join(self.output_path, 'vvc_log',        self.version, self.cfg, vvc_log_name)
        except AttributeError:
            raise Exception("Output path not defined")        

    def set_video_cfg(self, video_cfg:str, video_name:str):
        self.video_cfg = video_cfg
        self.video = video_name

    def set_cfg(self, cfg):
        cfg_dict = {
            'AI': 'encoder_intra_vtm.cfg',
            'LB': 'encoder_lowdelay_vtm.cfg',
            'RA': 'encoder_randomaccess_vtm.cfg',
        }
        self.cfg = cfg
        self.cfg_enc = cfg_dict[cfg]
        if cfg == 'AI':
            self.ts_status = '-ts 1'

    def set_qp(self, qp):
        self.qp = qp

    def update_config(self):
        self.__set_video_identifier__(self.video, self.cfg, self.qp, self.version)
    
    def update_paths(self):
        self.__enable_output_in_ext_file__()

    def enable_display(self):
        self.display = True

    def disable_display(self):
        self.display = False

    def enable_bg_exec(self):
        self.bg_exec = True

    def disable_bg_exec(self):
        self.bg_exec = False
    
    def __create_command__(self):
        command = self.__main_command__()
        if self.bg_exec:
            command += f'>> \"{self.output_vvc_log_path}\" & '
        return command
    
    def __main_command__(self):
        return f'/\"{self.bin_encoder_path}\" ' + \
        f'-c \"{self.cfg_encoder_path}\" ' + \
        f'-c \"{self.video_cfg}\" ' + \
        f'-b \"{self.bin_videos_path}\" ' + \
        f'-q {self.qp} -f {self.n_frames} {self.ts_status} --SIMD=SCALAR ' 

    def __set_video_identifier__(self, video, cfg, qp, version):
        self.video_identifier = f'{video}_qp{qp}_{cfg}_{version}'

    def __make_path_log_vvc__(self, out_dir, VTM_version, video_name, encoder_name):
        if not os.path.isdir(out_dir):
            os.mkdir(out_dir)
        if not os.path.isdir(os.path.join(out_dir, 'vvc_log')):
            os.mkdir(os.path.join(out_dir, 'vvc_log'))
        if not os.path.isdir(os.path.join(out_dir, 'vvc_log', VTM_version)):
            os.mkdir(os.path.join(out_dir, 'vvc_log', VTM_version))
        if not os.path.isdir(os.path.join(out_dir, 'vvc_log', VTM_version, video_name)):
            os.mkdir(os.path.join(out_dir, 'vvc_log', VTM_version, video_name))
        if not os.path.isdir(os.path.join(out_dir, 'vvc_log', VTM_version, video_name, encoder_name)):
            os.mkdir(os.path.join(out_dir, 'vvc_log', VTM_version, video_name, encoder_name))

    def __display_info__(
        self,
    ):
        print()
        print(f'Encoding: ........... {self.video}')
        print()
        print(f'Video identifier: ... {self.video_identifier}')
        print(f'Video config: ....... {self.video_cfg}')
        print(f'Encoder: ............ {self.cfg}')
        print(f'QP: ................. {self.qp}')
        print(f'VTM version used: ... {self.version}')
        print(f'frames encoded: ..... {self.n_frames}')
        print()

