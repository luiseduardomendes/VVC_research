import pandas as pd
import re
import os

class VVC_output(pd.DataFrame):
    __keys__ = ('frame','bitrate','Y_PSNR','U_PSNR','V_PSNR','YUV_PSNR','qp')
    def __init__(self, file_path = None, qps = None, frames = -1):        
        # 0         1           2           3           4           5
        # frames    bitrate     y_psnr      u_psnr      v_psrn      yuv_psnr
        self.pattern_frame = re.compile(r'^POC\s+(\d+)\s+LId:\s+\d+\s+TId:\s+\d+\s+\( \w+, \w-SLICE, QP \d+ \)\s+(\w+) bits \[Y (\d+\.\d+) dB\s+U (\d+\.\d+) dB\s+V (\d+\.\d+) dB', re.M)

        # 0           1           2           3           4
        # bitrate     y_psnr      u_psnr      v_psrn      yuv_psnr
        self.pattern_video = re.compile(r'^\s+\d+\s+a\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+$', re.M)
        
        self.dt = {
            'frame':    [],
            'bitrate':  [],
            'Y_PSNR':   [],
            'U_PSNR':   [],
            'V_PSNR':   [],
            'YUV_PSNR': [],
            'qp':       []
        }
        self.qps = qps

        if file_path == None:
            self.create_empty_df()
        
        else:
            if frames != -1:
                for file_index, file in enumerate(file_path):
                    if os.path.isfile(file):
                        self.read_frames(file, file_index, frames)
                    else:
                        self.create_empty_df()
                        return
            else:
                for file_index, file in enumerate(file_path):
                    if os.path.isfile(file):
                        self.read_general(file, file_index)
                    else:
                        self.create_empty_df()
                        return

            super().__init__(self.dt)
            super().__init__((super().sort_values(by=['frame', 'qp'])))
        
    def create_empty_df(self):
        self.dt = {}
        for key in self.__keys__:
            self.dt[key] = []
        super().__init__(self.dt)

    def read_frames(self, file, file_index, frames):
        with open(file) as f:
            log = f.read()
            check = self.pattern_frame.findall(log)

            if len(check) == frames:
                for frame in check:
                    self.append_frame(frame, file_index)

            check = self.pattern_video.findall(log)
            if len(check) > 0:
                frame = check[0]
                self.append_general(frame, file_index)

    def read_general(self, file, file_index):
        with open(file) as f:
            log = f.read()
            check = self.pattern_video.findall(log)
            if len(check) == 1:
                frame = check[0]
                self.append_general(frame, file_index)

            f.close()

    def append_frame(self, frame, file_index):

        frames, bitrate, y_psnr, u_psnr, v_psnr = frame

        self.dt['frame'].append(int(frames))
        self.dt['bitrate'].append(int(bitrate))
        self.dt['Y_PSNR'].append(float(y_psnr))
        self.dt['U_PSNR'].append(float(u_psnr))
        self.dt['V_PSNR'].append(float(v_psnr))
        self.dt['YUV_PSNR'].append(self.calculate_YUV_PSNR(float(y_psnr), float(u_psnr), float(v_psnr)))
        self.dt['qp'].append(int(self.qps[file_index]))

    def append_general(self, frame, file_index):
        
        bitrate, y_psnr, u_psnr, v_psnr, yuv_psnr = frame

        self.dt['frame'].append(-1)
        self.dt['bitrate'].append(int(bitrate))
        self.dt['Y_PSNR'].append(float(y_psnr))
        self.dt['U_PSNR'].append(float(u_psnr))
        self.dt['V_PSNR'].append(float(v_psnr))
        self.dt['YUV_PSNR'].append(float(yuv_psnr))
        self.dt['qp'].append(int(self.qps[file_index]))

    def calculate_YUV_PSNR(self, Y_PSNR, U_PSNR, V_PSNR):
        return (float(Y_PSNR) + float(U_PSNR) + float(V_PSNR))/3

