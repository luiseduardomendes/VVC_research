import os

def gprof_make_path(path, cfg, file, version, qps):
    ext_make_path(path, cfg, file, version, qps, 'gprof')

def vvc_make_path(path, cfg, file, version, qps):
    ext_make_path(path, cfg, file, version, qps, 'vvc')

def ext_make_path(path, cfg, file, version, qps, log_type):
    f = []
    decod_log_type = {
        'gprof': {'ext': '.gplog', 'folder': 'gprof_log'},
        'vvc': {'ext': '.vvclog', 'folder': 'vvc_log'}
    }
    decod_folder = {
        'AI': 'intra',
        'LD': 'lowdelay',
        'RA': 'randomaccess'
    }
    for qp in qps:
        temp_file = os.path.join(
            path, 
            version, 
            file, 
            decod_folder[cfg], 
            f'{decod_log_type[log_type]["folder"]}',
            f'log_{file}_qp{qp}_{cfg}_{version}_{decod_log_type[log_type]["ext"]}'
        )
        if os.path.isfile(temp_file):
            f.append(temp_file)
        else:
            raise Exception(f"error on make_path_log: file {temp_file} not found")
            return []
    return f
