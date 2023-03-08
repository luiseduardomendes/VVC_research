import source.vvc_simulation as vs

s = vs.Simulation(n_frames=32, encoder=['RA', 'AI'], bg_exec=True)
s.set_vtm_dir('/home/luispmendes/VVCSoftware_VTM/')
s.set_cfg_dir('/home/luispmendes/VVCSoftware_VTM/cfg-files-test')
s.set_out_dir('/home/luispmendes/VVC_research/output07032023')

s.enable_bg_exec()
s.run_exec()

