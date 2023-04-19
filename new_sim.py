import source.vvc_simulation as vs

vtm_dir = '/home/luispmendes/VVCSoftware_VTM/'
cfg_dir = '/home/luispmendes/VVCSoftware_VTM/cfg-files-test'
out_dir = '/home/luispmendes/VVC_research/output09_03_23'

sim = vs.Simulation(n_frames=32, encoder=['RA', 'AI', 'LB'], bg_exec=True)
sim.set_paths(out_dir, vtm_dir, out_dir)

sim.run_exec()

