import pandas as pd
from pprint import pprint
from source.vvc_output import VVC_Output
from source.vvc_bd_rate import BD_Rate
import source.common.log_path as log_path

def vvc_frame_analysis(versions, file_names, path, all_frames = True):

    qps = (22, 27, 32, 37)
    files = file_names
    cfgs = ('AI', 'LB', 'RA')

    df = BD_Rate()
    df.index.names=['version','video','cfg','frame']
    for version in versions:
        for file in files:    
            for cfg in cfgs:
                path_logs = log_path.vvc_log_path(path, cfg, file, version, qps)
                if len(path_logs) == 0:
                    continue
                
                path_refs = log_path.vvc_log_path(path, cfg, file, 'Precise', qps)
                if len(path_refs) == 0:
                    continue

                log = VVC_Output()
                log.read_multifile(path_logs, qps, all_frames)
                log = (VVC_Output(data=log.sort_values(by=['frame', 'qp'])))
                
                ref = VVC_Output()
                ref.read_multifile(path_refs, qps, all_frames)
                ref = (VVC_Output(data=ref.sort_values(by=['frame', 'qp'])))

                tmp_df = BD_Rate(version=version, video=file, cfg=cfg)
                tmp_df.calc_bdbr(log, ref)

                df.append_bd(tmp_df)
    return df
    
