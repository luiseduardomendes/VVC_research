import os

def make_path_ref(path, cfg, file, qps):
    f = []
    for qp in qps:
        temp_file = os.path.join(
            path, 
            'Preciso', 
            cfg, 
            f'{file}_QP{qp}.txt'
        ) 
        if os.path.isfile(temp_file):
            f.append(temp_file)
        else:
            print(f"file {temp_file} not found")
            return []
    return f

def make_path_log(path, cfg, file, satd, qps):
    f = []
    for qp in qps:
        temp_file = os.path.join(
            path, 
            satd, 
            file, 
            cfg, 
            'exec_log',
            f'log_{file}_qp{qp}_{cfg}_{satd}_exec.gplog'
        )
        if os.path.isfile(temp_file):
            f.append(temp_file)
        else:
            print(f"file {temp_file} not found")
            return []
    return f
