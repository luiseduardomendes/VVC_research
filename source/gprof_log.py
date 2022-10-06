import re
import pandas as pd
import numpy as np

def read_gprof_out(file, max_n = 15):           

    keys = ('time', 'cum_sec', ' self_sec', 'calls', 'self_s_call', 'tot_s_call', 'name', 'class')

    pattern = re.compile(r'(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+|\s+)\s+(\d+|\s+)\s+(\d+\.\d+|\s+)\s+(\d+\.\d+|\s+)\s+(.+)()')
        
    structBuffer = {}
    for key in keys:
        structBuffer[key] = []
    
    with open(file) as f:
        for line in f:
            check = pattern.findall(line)
            if len(check) != 0:
                buffer = check[0][:]
                for i, key in enumerate(keys):
                    if buffer[i] == '':
                        structBuffer[key].append(np.nan)
                    else:
                        try:
                            structBuffer[key].append(float(buffer[i]))
                        except:
                            structBuffer[key].append((buffer[i]))
                if '::' in buffer[6]:
                    class_name = buffer[6].split(sep='::')[0]
                else:
                    class_name = np.nan

                funct_name = buffer[6].split(sep='(')[0]
                funct_name = funct_name.split(sep='::')[-1]
                structBuffer['class'][-1] = class_name
                structBuffer['name'][-1] = funct_name

            if len(structBuffer['class']) >= max_n:
                break
        f.close()
    return pd.DataFrame(structBuffer)
    