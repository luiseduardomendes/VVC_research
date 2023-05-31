import numpy as np
import os
import re

def get_info_from_path(path):
    pattern = re.compile(r'log_([^_]+)_qp([^_]+)_([^_]+)_([^_]+)\..+')
    match = pattern.findall(path)
    if len(match) > 0:
        return {
            'video':match[0][0],
            'qp':match[0][1], 
            'cfg':match[0][2],
            'version':match[0][3],
            'log_type':match[0][4]
        }
    else:
        return {
            'video':np.nan,
            'qp':np.nan, 
            'cfg':np.nan,
            'version':np.nan,
            'log_type':np.nan
        }

def gprof_make_path(path, cfg, file, version, qps):
    return ext_make_path(path, cfg, file, version, qps, 'gprof')

def vvc_make_path(path, cfg, file, version, qps):
    return ext_make_path(path, cfg, file, version, qps, 'vvc')

def ext_make_path(path, cfg, file, version, qps, log_type):
    f = []
    decod_log_type = {
        'gprof': {'ext': '.gplog', 'folder': 'gprof_log'},
        'vvc': {'ext': '.vvclog', 'folder': 'vvc_log'}
    }
    for qp in qps:
        temp_file = os.path.join(
            path, 
            f'{decod_log_type[log_type]["folder"]}',
            version, 
            file, 
            cfg, 
            f'log_{file}_qp{qp}_{cfg}_{version}{decod_log_type[log_type]["ext"]}'
        )
        if os.path.isfile(temp_file):
            f.append(temp_file)
        else:
            return []
            raise Exception(f"error on make_path_log: file {temp_file} not found")
    return f
