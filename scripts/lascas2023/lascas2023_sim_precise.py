from vvcpy import sim
from vvcpy import common as cm
from os.path import join

setup_file = 'setup_lascas.yaml'
Sim = sim.Simulation()
Sim.read_yaml(setup_file)

Sim.run_exec()

