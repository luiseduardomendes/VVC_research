import vvc_log as vl
import os
qps = (22, 27, 32, 37)
satds = os.listdir('../out/')
file = 'BQMall'
cfg = 'intra'

dfs = []
for satd in satds:
    for qp in qps:
        dfs.append(vl.read_log(f'../out/{satd}/{file}/{cfg}/exec_log/log_{file}_qp{qp}_{cfg}_{satd}_exec.gplog'))

dfs = vl.split(dfs)
for key in dfs.keys():
    dfs[key].plot(y='bitrate', x='qp', save=False)

keys = list(dfs.keys())
dfs[keys[0]].compare(dfs[keys[1]], x='qp', y='bitrate')

dfs[keys[0]].difference(dfs[keys[1]], x='qp', y='bitrate')