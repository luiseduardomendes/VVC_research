from vvc_performance import Simulation

vtm_dir = '/home/luispmendes/VVCSoftware_VTM/'
cfg_dir = '/home/luispmendes/VVCSoftware_VTM/cfg-files-test/'
out_dir = '/home/luispmendes/VVC_research/output030523/'

sim = Simulation(n_frames=32, encoder=['RA', 'AI'], bg_exec=True)
sim.set_paths(out_dir, vtm_dir, cfg_dir)
sim.set_version('RdCostModif')

sim.run_exec()

