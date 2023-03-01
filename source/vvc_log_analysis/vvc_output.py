import pandas as pd
import re
import os

class VVC_Output(pd.DataFrame):
    __keys__ = ('frame','bitrate','Y_PSNR','U_PSNR','V_PSNR','YUV_PSNR','qp')
    __full_vid_pattern__ = re.compile(r'^\s+\d+\s+a\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+$', re.M)
    __frame_pattern__ = re.compile(r'^POC\s+(\d+)\s+LId:\s+\d+\s+TId:\s+\d+\s+\( \w+, \w-SLICE, QP \d+ \)\s+(\w+) bits \[Y (\d+\.\d+) dB\s+U (\d+\.\d+) dB\s+V (\d+\.\d+) dB', re.M)

    def __init__(self, data=None) -> None:
        super().__init__(data)

    def read_multifile(self, filenames : str, qps : int):
        for file, qp in zip(filenames, qps):
            self.read_file(file, qp)
        return self

    def read_file(self, filename : str, qp : int):
        if not os.path.isfile(filename):
            raise FileNotFoundError()
        
        self.read_all_frames(filename, qp)
        self.read_full_execution(filename, qp)
        return self

    def read_full_execution(self, filename : str, qp : int):
        if not os.path.isfile(filename):
            raise FileNotFoundError()

        with open(filename) as f:
            log = f.read()
            check = self.__full_vid_pattern__.findall(log)
            if len(check) == 1:
                self.__full_execution_decoder__(check[0], qp)
            f.close()

    def read_all_frames(self, filename : str, qp : int):
        if not os.path.isfile(filename):
            raise FileNotFoundError()
        
        with open(filename) as f:
            log = f.read()
            check = self.__frame_pattern__.findall(log)
            if len(check) >= 1:
                for frame in check:
                    self.__each_frame_decoder__(frame, qp)
            f.close()

            
    def __full_execution_decoder__(self, data, qp):
        bitrate, y_psnr, u_psnr, v_psnr, yuv_psnr = data
        data = pd.DataFrame({
            'frame':    [int(-1)],
            'bitrate':  [float(bitrate)],
            'Y_PSNR':   [float(y_psnr)],
            'U_PSNR':   [float(u_psnr)],
            'V_PSNR':   [float(v_psnr)],
            'YUV_PSNR': [float(yuv_psnr)],
            'qp':       [int(qp)]
        })
        self.append(data)
            

    def __each_frame_decoder__(self, data, qp):
        frames, bitrate, y_psnr, u_psnr, v_psnr = data
        data = pd.DataFrame({
            'frame':    [int(frames)],
            'bitrate':  [int(bitrate)],
            'Y_PSNR':   [float(y_psnr)],
            'U_PSNR':   [float(u_psnr)],
            'V_PSNR':   [float(v_psnr)],
            'YUV_PSNR': [float(y_psnr)],
            'qp':       [int(qp)]
        })

        self.append(data)
    
    def append(self, data):
        self.__init__(data=pd.concat([self, data]))


        

