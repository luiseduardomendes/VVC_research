import pandas as pd
import re
import os

class VVC_output(pd.DataFrame):
    __keys__ = ('frame','bitrate','Y_PSNR','U_PSNR','V_PSNR','YUV_PSNR','qp')
    def __init__(self, file_path = None, qps = None, frames = -1, data = None):        
        # 0         1           2           3           4           5
        # frames    bitrate     y_psnr      u_psnr      v_psrn      yuv_psnr
        pattern_frame = re.compile(r'^POC\s+(\d+)\s+LId:\s+\d+\s+TId:\s+\d+\s+\( \w+, \w-SLICE, QP \d+ \)\s+(\w+) bits \[Y (\d+\.\d+) dB\s+U (\d+\.\d+) dB\s+V (\d+\.\d+) dB', re.M)

        # 0           1           2           3           4
        # bitrate     y_psnr      u_psnr      v_psrn      yuv_psnr
        pattern_video = re.compile(r'^\s+\d+\s+a\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+$', re.M)

        if type(data) == pd.DataFrame:
            super().__init__(data)
            return

        super().__init__({
            'frame':    [],
            'bitrate':  [],
            'Y_PSNR':   [],
            'U_PSNR':   [],
            'V_PSNR':   [],
            'YUV_PSNR': [],
            'qp':       []
        })
        
        if file_path != None:    
            error_found = False      
            if frames != -1:
                for file_index, file in enumerate(file_path):
                    if os.path.isfile(file):
                        self.read_frames(file, qps[file_index], frames, pattern_frame, pattern_video)
                    else:
                        print(f'file \u001b[0;31m{file}\u001b[0m not found')
                        error_found = True
                        break
            else:
                for file_index, file in enumerate(file_path):
                    if os.path.isfile(file):
                        self.read_general(file, qps[file_index], pattern_video)
                    else:
                        print(f'file \u001b[0;31m{file}\u001b[0m not found')
                        error_found = True
                        break
            if error_found:
                super().__init__({
                    'frame':    [],
                    'bitrate':  [],
                    'Y_PSNR':   [],
                    'U_PSNR':   [],
                    'V_PSNR':   [],
                    'YUV_PSNR': [],
                    'qp':       []
                })
            else:   
                self.sort()        
          

    def sort(self):
        self = VVC_output(data=self.sort_values(by=['frame', 'qp']))

    def read_frames(self, file, qp, frames, pattern_frame, pattern_video):
        with open(file) as f:
            log = f.read()
            check = pattern_frame.findall(log)
            
            if len(check) == frames:
            
                for frame in check:
            
                    self.append_frame(frame, qp)

            

            check = pattern_video.findall(log)
            if len(check) > 0:
                frame = check[0]
                self.append_general(frame, qp)

    def read_general(self, file, qp, pattern_video):
        with open(file) as f:
            log = f.read()
            check = pattern_video.findall(log)
            if len(check) == 1:
                frame = check[0]
                self.append_general(frame, qp)

            f.close()

    def append_frame(self, frame, qp):

        frames, bitrate, y_psnr, u_psnr, v_psnr = frame
        
        self = self.__init__(data=pd.concat(
            [self, 
            pd.DataFrame({
                'frame':    [int(frames)],
                'bitrate':  [int(bitrate)],
                'Y_PSNR':   [float(y_psnr)],
                'U_PSNR':   [float(u_psnr)],
                'V_PSNR':   [float(v_psnr)],
                'YUV_PSNR': [float(y_psnr)],
                'qp':       [int(qp)]
            })],
            ignore_index=True
        ))

    def append_general(self, frame, qp):
        
        bitrate, y_psnr, u_psnr, v_psnr, yuv_psnr = frame
        
        self = self.__init__(data=pd.concat(
            [self, 
            pd.DataFrame({
                'frame':    [int(-1)],
                'bitrate':  [float(bitrate)],
                'Y_PSNR':   [float(y_psnr)],
                'U_PSNR':   [float(u_psnr)],
                'V_PSNR':   [float(v_psnr)],
                'YUV_PSNR': [float(yuv_psnr)],
                'qp':       [int(qp)]
            })]
        ))

