import source.vvc_simulation as vs

vtm_dir = '/home/luispmendes/VVCSoftware_VTM/'
cfg_dir = '/home/luispmendes/VVCSoftware_VTM/cfg-files-test/'
out_dir = '/home/luispmendes/VVC_research/output-3/'

sim = vs.Simulation(n_frames=8, encoder=['RA'], qps=[22, 27, 32, 37], bg_exec=True, gprof=True)
sim.set_paths(out_dir, vtm_dir, cfg_dir)

sim.run_exec()

