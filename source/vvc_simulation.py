import os 
import re
from source.common.commonlib import file_subs, compile_VTM
import source.common.vvc_exec_refact as vvc_exec
from pathlib import Path

class Simulation:
    cfg_dir = None
    vtm_dir = None
    out_dir = None

    version = 'Precise'
    qps = [22, 27, 32, 37]
    encoder = ['AI', 'RA', 'LD']

    n_frames = 32
    bg_exec = False
    gprof = False

    videos = []

    def __init__(self, n_frames = 32, version = 'Precise', qps = [22, 27, 32, 37], encoder = ['AI', 'RA', 'LD'], bg_exec = False, gprof = False):
        self.set_n_frames(n_frames)
        self.set_version(version)
        self.set_qps(qps)
        self.set_encoder(encoder)
        if gprof:
            self.enable_gprof() 
        else:
            self.disable_gprof()
        if bg_exec:
            self.enable_bg_exec()
        else:
            self.disable_bg_exec()

    def run_exec(self):
        print('Execution running')
        self.get_exec_info()

        _exec = vvc_exec.vvc_executer(
            vtm_path    =   self.vtm_dir,
            version     =   self.version,
            n_frames    =   self.n_frames
        )
        _exec.bg_exec = self.bg_exec
        _exec.enable_display()
        _exec.set_output_path(self.out_dir)

        for video in self.videos:
            _exec.set_video_cfg(os.path.join(self.cfg_dir, video), video[:-4])
            for cfg in self.encoder:
                _exec.set_cfg(cfg)
                for qp in self.qps:
                    _exec.set_qp(qp)
                    _exec.run_exec()
        print('Simulation done')

    def get_exec_info(self):
        info = \
            f'---------------------------------------------- \n' + \
            f'\n' + \
            f'version :         {self.version} \n' + \
            f'qps :             {self.qps} \n' + \
            f'encoder :         {self.encoder} \n' + \
            f'n_frames :        {self.n_frames} \n' + \
            f'background exec : {self.bg_exec} \n' + \
            f'gprof :           {self.gprof} \n' + \
            f'videos :          [ \n'
        for i, video in enumerate(self.videos):
            info += \
            f'                      {i:2}. {video}\n'
        info += f'                  ] \n' + \
                f'---------------------------------------------- \n'

        info += f'Total execution {len(self.videos)} x {len(self.qps)} x {len(self.encoder)} = {len(self.videos) * len(self.qps) * len(self.encoder)} simulations\n---------------------------------------------- \n'
        
        print(info)
        return info

    def remove_video_from_buffer(self, file_index):
        try:
            indexes = list(file_index)
            indexes.sort(reverse=True)
            for index in indexes:
                del self.videos[index]
        except AttributeError:
            try:
                del self.videos[file_index]
            except:
                raise Exception("invalid index type")
        except :
            raise Exception("invalid index type")
       


    def replace_file(self, new_file, old_file):
        file_subs(new_file, old_file, Path(old_file).stem)
        compile_VTM(self.vtm_dir, os.getcwd())

    def set_n_frames(self, n_frames):
        self.n_frames = n_frames
    
    def set_out_dir(self, out_dir):
        self.out_dir = self.__create_output_dir__(out_dir)

    def set_vtm_dir(self, vtm_dir):
        self.vtm_dir = vtm_dir

    def set_cfg_dir(self, cfg_dir):
        self.cfg_dir = cfg_dir
        self.videos = self.__config_files_in_dir__(cfg_dir)

    def set_version(self, version):
        self.version = version

    def set_qps(self, qps):
        self.qps = qps
    
    def set_encoder(self, encoder):
        self.encoder = encoder

    def enable_gprof(self):
        self.gprof = True
    
    def disable_gprof(self):
        self.gprof = False

    def enable_bg_exec(self):
        self.bg_exec = True
    
    def disable_bg_exec(self):
        self.bg_exec = False

    def __create_output_dir__(self, output_dir):
        if not os.path.isdir(output_dir):
            os.mkdir(output_dir)
        else:
            while(os.path.isdir(output_dir)):
                output_dir = self.__rename_dir__(output_dir)
            os.mkdir(output_dir)
        return output_dir

    def __config_files_in_dir__(self, cfg_vid_dir):
        if not os.path.isdir(cfg_vid_dir):
            raise Exception("Video config directory not exists")
        
        return [
            f 
            for f in os.listdir(cfg_vid_dir) 
            if os.path.isfile(os.path.join(cfg_vid_dir, f)) and 
            f[-4:] == '.cfg'
        ]
    def __rename_dir__(self, d : str ):
        matches = re.findall(r'(\d+)$', d)
        if len(matches) > 0:
            n = int(matches[-1])
            n = n + 1
            d = d[:-1] + str(n)
        else:
            d = d + '1'
        return d
