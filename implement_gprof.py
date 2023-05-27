import source.common.commonlib as c
import source.vvc_simulation as sim

old_file = "/home/luispmendes/VVCSoftware_VTM/src/Lib/CommonLib/"
new_file = "/home/luispmendes/VVC_research/RdCostModif.cpp"

c.file_subs(new_file, old_file, 'RdCost.cpp')
c.compile_VTM('/home/luispmendes/VVCSoftware_VTM')

