import sys
import vvcpy
import os

path = os.path.join(os.getcwd(), sys.argv[1])
vtm_path = os.path.join(path, 'VVCSoftware_VTM')
cmake_file = os.path.join(vtm_path, 'build', 'CMakeCache.txt')
vvcpy.common.commonlib.turn_on_profiling_in_makefile(cmake_file)
vvcpy.common.commonlib.compile_VTM(vtm_path)
#print(cmake_file)
#print(vtm_path)
