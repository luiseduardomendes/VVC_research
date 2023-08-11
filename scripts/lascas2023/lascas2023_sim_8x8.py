from vvcpy import sim
from vvcpy import common as cm
from os.path import join

setup_file = 'setup_lascas.yaml'
Sim = sim.Simulation()
Sim.read_yaml(setup_file)

vtm = cm.commonlib.yaml_reader(setup_file)['vtm']

new_file = 'RdCostFiles/RdCost-8x8-SAD.cpp'
old_file = join(vtm, 'source', 'Lib', 'CommonLib', 'RdCost')
version = 'RdCost-8x8-SAD'

Sim.change_version(version, old_file, new_file)

Sim.run_exec()

