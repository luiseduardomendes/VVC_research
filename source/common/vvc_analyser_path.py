import os

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
