import pandas as pd
from source.vvc_log_analysis.vvc_output import VVC_output
import numpy as np
from scipy import interpolate, integrate
import math


class BD_Rate(pd.Series):
    __indexes__ = ['satd','video','cfg','frame']
    def __init__(self, cmp_df : VVC_output = None, ref_df : VVC_output = None, satd = None, video = None, cfg = None, qps=4):

        if cmp_df == None:
            bdr = []
            index = self.__mk_empty_index__()

        else:
            bdr = [
                self.bdbr(cmp_df.iloc[i:i+qps], ref_df.iloc[i:i+qps]) 
                for i in range(0, len(cmp_df['frame']), qps)
            ]
            index = self.__mk_index__()


        super().__init__(
            bdr, 
            index=index
        )

    def __mk_empty_index__(self) -> pd.MultiIndex:
        return pd.MultiIndex.from_arrays(
            [[], [], [], [],], names=self.__indexes__
        )

    def __mk_index__(self, satd, video, cfg, cmp_df, qps) -> pd.MultiIndex:
        
        index = pd.MultiIndex.from_arrays(
            [
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
            ],
            names = self.__indexes__
        )

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
