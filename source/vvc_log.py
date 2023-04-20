import pandas as pd
from pprint import pprint
from source.vvc_log_analysis.vvc_output import VVC_Output
from source.vvc_log_analysis.vvc_bd_rate import BD_Rate
import source.common.vvc_analyser_path as vvcpath

def vvc_frame_analysis(approximations, file_names, path, all_frames = True):

    qps = (22, 27, 32, 37)
    satds = approximations
    files = file_names
    cfgs = ('intra', 'lowdelay', 'randomaccess')

    _cfg_ = {
        'intra'         : 'AI',
        'lowdelay'      : 'LB',
        'randomaccess'  : 'RA'
    }

    df = BD_Rate()
    df.index.names=['version','video','cfg','frame']
    for satd in satds:
        for file in files:    
            for cfg in cfgs:
                path_logs = vvcpath.vvc_make_path(path, _cfg_[cfg], file, satd, qps)
                if len(path_logs) == 0:
                    continue
                
                path_refs = vvcpath.vvc_make_path(path, _cfg_[cfg], file, 'Precise', qps)
                if len(path_refs) == 0:
                    continue

                log = VVC_Output()
                log.read_multifile(path_logs, qps)
                log = (VVC_Output(data=log.sort_values(by=['frame', 'qp'])))
                
                ref = VVC_Output()
                ref.read_multifile(path_refs, qps)
                ref = (VVC_Output(data=ref.sort_values(by=['frame', 'qp'])))

                tmp_df = BD_Rate(satd=satd, video=file, cfg=cfg)
                tmp_df.calc_bdbr(log, ref)

                df.append_bd(tmp_df)
    return df
    
