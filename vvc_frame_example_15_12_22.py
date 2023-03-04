from source.vvc_log import vvc_frame_analysis

approximations = ['4x4-1-RdCost4x4-1-8x8-1']
file_names = ['BQMall']
path = '/home/luismendes/Documentos/GitHub/VVC_research/database/input_analyser/out/'

df = vvc_frame_analysis(
    approximations,
    file_names,
    path
)

print(df.to_string())