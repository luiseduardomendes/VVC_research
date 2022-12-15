import pandas as pd
from pprint import pprint
from source.vvc_log_analysis.vvc_output import VVC_output
from source.vvc_log_analysis.vvc_bd_rate import BD_Rate
from source.common.sv_make_path import *

def vvc_frame_analysis(approximations, file_names, path, all_frames = True):

    qps = (22, 27, 32, 37)
    satds = approximations
    files = file_names
    cfgs = ('intra', 'lowdelay', 'randomaccess')

    _conv_cfg_ = {
        'intra'         : 'AI',
        'lowdelay'      : 'LB',
        'randomaccess'  : 'RA'
    }

    if all_frames:
        frames = 32
    else:
        frames = -1

    df = BD_Rate()
    for satd in satds:
        for file in files:    
            for cfg in cfgs:
                path_logs = make_path_log(path, cfg, file, satd, qps)
                if len(path_logs) == 0:
                    continue
                
                path_refs = make_path_ref(path, _conv_cfg_[cfg], file, qps)
                if len(path_refs) == 0:
                    continue

                log = VVC_output(path_logs, qps, frames)
                log = (VVC_output(data=log.sort_values(by=['frame', 'qp'])))
                
                ref = VVC_output(path_refs, qps, frames)
                ref = (VVC_output(data=ref.sort_values(by=['frame', 'qp'])))


                df = pd.concat([df, BD_Rate(log, ref, satd, file, cfg)])
    return df
    
