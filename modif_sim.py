import source.vvc_simulation as vs

vtm_dir = '/home/luispmendes/VVCSoftware_VTM/'
cfg_dir = '/home/luispmendes/VVCSoftware_VTM/cfg-files-test/'
out_dir = '/home/luispmendes/VVC_research/output030523/'

sim = vs.Simulation(n_frames=32, encoder=['RA', 'AI'], bg_exec=True)
sim.set_paths(out_dir, vtm_dir, cfg_dir)
sim.set_version('RdCostModif')

sim.run_exec()

