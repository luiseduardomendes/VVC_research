from source.common.vvc_exec import exec
import os

cfg_dir = 'database/cfg-files'
vtm_dir = '/home/luispmendes/VVCSoftware_VTM/'
out_dir = 'out'

exec(
    vtm_dir,
    'RA',
    os.path.join(cfg_dir, 'BasketballDrive.cfg'), 
    37,
    out_dir,
    'BasketballDrive',
    'precise',
    8,
    False, 
)
