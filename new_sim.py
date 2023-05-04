import source.vvc_simulation as vs

vtm_dir = '/home/luispmendes/VVCSoftware_VTM/'
cfg_dir = '/home/luispmendes/VVCSoftware_VTM/cfg-files-test/'
out_dir = '/home/luispmendes/VVC_research/output040523-1/'

sim = vs.Simulation(n_frames=32, encoder=['RA', 'AI'], qps=[37], bg_exec=True, gprof=True)
sim.set_paths(out_dir, vtm_dir, cfg_dir)

sim.run_exec()

