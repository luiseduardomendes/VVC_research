from source.vvc_simulation import Simulation
import os


vtm = '/mnt/c/Users/dudup/OneDrive/Área de Trabalho/VVCSoftware_VTM/'
cfg = '/mnt/c/Users/dudup/OneDrive/Área de Trabalho/New folder/VVC/VVC_research/database/input_analyser/cfg-files-t/'
out = '/mnt/c/Users/dudup/OneDrive/Área de Trabalho/New folder/VVC/VVC_research/out1406_1/'
rep = '/mnt/c/Users/dudup/OneDrive/Área de Trabalho/New folder/VVC/VVC_research/'
old = '/mnt/c/Users/dudup/OneDrive/Área de Trabalho/VVCSoftware_VTM/source/Lib/CommonLib/RdCost.cpp'
new = '/mnt/c/Users/dudup/OneDrive/Área de Trabalho/New folder/VVC/VVC_research/RdCost-vert.cpp'
ver = 'RdCost-2'
enc = ['RA']
qps = [37]
frs = 8

sim = Simulation(n_frames=frs, qps=qps, encoder=enc, version=ver, bg_exec=True)
sim.set_paths(out, vtm, cfg)
#sim.change_version(ver, old, new)

sim.run_exec()
