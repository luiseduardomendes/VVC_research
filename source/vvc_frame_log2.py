from scipy import interpolate, integrate
import pandas as pd
import numpy as np
import math
import re
import os

from pprint import pprint

class VVC_output(pd.DataFrame):
    __keys__ = ('frame','bitrate','Y_PSNR','U_PSNR','V_PSNR','YUV_PSNR','qp')
    def __init__(self, file_path, qps, frames):
        
        # 0         1           2           3           4           5
        # frames    bitrate     y_psnr      u_psnr      v_psrn      yuv_psnr

        pattern_frame = re.compile(r'^POC\s+(\d+)\s+LId:\s+\d+\s+TId:\s+\d+\s+\( \w+, \w-SLICE, QP \d+ \)\s+(\w+) bits \[Y (\d+\.\d+) dB\s+U (\d+\.\d+) dB\s+V (\d+\.\d+) dB', re.M)

        # 0           1           2           3           4
        # bitrate     y_psnr      u_psnr      v_psrn      yuv_psnr

        pattern_video = re.compile(r'^\s+\d+\s+a\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+$', re.M)
        
        dt = {}
        for key in self.__keys__:
            dt[key] = []
        for index, file in enumerate(file_path):
            if os.path.isfile(file):
                with open(file) as f:
                    log = f.read()
                    check = pattern_frame.findall(log)
                    if len(check) == frames:
                        for i in check:
                            dt['frame'].append(int(i[0]))
                            dt['bitrate'].append(int(i[1]))
                            dt['Y_PSNR'].append(float(i[2]))
                            dt['U_PSNR'].append(float(i[3]))
                            dt['V_PSNR'].append(float(i[4]))
                            dt['YUV_PSNR'].append((float(i[2]) + float(i[3]) + float(i[4]))/3)
                            dt['qp'].append(int(qps[index]))
                    check = pattern_video.findall(log)
                    if len(check) > 0:
                        i = check[0]
                        dt['frame'].append(-1)
                        dt['bitrate'].append(float(i[0]))
                        dt['Y_PSNR'].append(float(i[1]))
                        dt['U_PSNR'].append(float(i[2]))
                        dt['V_PSNR'].append(float(i[3]))
                        dt['YUV_PSNR'].append(float(i[4]))
                        dt['qp'].append(qps[index])
            else:
                dt = {}
                for key in self.__keys__:
                    dt[key] = []
                super().__init__(dt)
                return
        super().__init__(dt)
        super().__init__((super().sort_values(by=['frame', 'qp'])))
        
    
    def print(self):
        print(self)

class BD_Rate(pd.Series):
    __indexes__ = ('satd','video','cfg','frame')
    def __init__(self, cmp_df : VVC_output, ref_df : VVC_output, satd, video, cfg, qps=4):
        
        bdr = [
            self.bdbr(cmp_df.iloc[i:i+qps], ref_df.iloc[i:i+qps]) 
            for i in range(0, len(cmp_df['frame']), qps)
        ]
        index = [
            [
                satd
                for i in range(0, len(cmp_df['frame']), qps)
            ],
            [
                video
                for i in range(0, len(cmp_df['frame']), qps)
            ],
            [
                cfg
                for i in range(0, len(cmp_df['frame']), qps)
            ], 
            [
                cmp_df['frame'][i]
                for i in range(0, len(cmp_df['frame']), qps)
            ],
        ]

        super().__init__(
            bdr, 
            index=index
        )
        
    
    def print(self):
        print(self)

    def bdbr(self, cmp, ref):
        if not (len(cmp['bitrate']) == len(ref['bitrate']) and len(cmp['bitrate'] == 4)):

            return None

        VVC     = np.asarray(cmp.loc[:,'bitrate':'YUV_PSNR'])
        HEVC    = np.asarray(ref.loc[:,'bitrate':'YUV_PSNR'])
        
        HEVC = HEVC[HEVC[:,0].argsort()]
        VVC = VVC[VVC[:,0].argsort()]

        xa, ya = np.log10(HEVC[:,0]), HEVC[:,4]
        xb, yb = np.log10(VVC[:,0]), VVC[:,4]
        
        max_i = len(ya)
        i = 1
        while(i < max_i):
            if ya[i] < ya[i-1] or yb[i] <  yb[i-1]:
                ya = np.delete( ya,i)
                yb = np.delete( yb,i)
                xa = np.delete( xa,i)
                xb = np.delete( xb,i)
                max_i = len(ya)
            else:
                i += 1

        x_interp = [max(min(xa), min(xb)), min(max(xa),max(xb))]
        y_interp = [max(min(ya), min(yb)), min(max(ya),max(yb))]

        interp_br_a = interpolate.PchipInterpolator(ya,xa)
        interp_br_b = interpolate.PchipInterpolator(yb,xb)

        bdbr_a = integrate.quad(interp_br_a, y_interp[0], y_interp[1])[0]
        bdbr_b = integrate.quad(interp_br_b, y_interp[0], y_interp[1])[0]

        bdbr = (bdbr_b - bdbr_a) / (y_interp[1] - y_interp[0])
        bdbr = (math.pow(10., bdbr)-1)*100

        return bdbr

