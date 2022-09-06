from distutils.log import Log
import re
from turtle import title
import pandas as pd
import matplotlib.pyplot as plt

# this object is used as return to the read_log function
# it is also used by the LogDF to append new data to a Log Data Frame
class LogDict:
    keys = ('bitrate','Y_PSNR','U_PSNR','V_PSNR','YUV_PSNR','fileName','qp','cfg','satd')
    def __init__(self, name : str, qp : int, cfg : str, satd : str, log_data : list = None):
        self.df = self.__mk_empty_df__()

        if log_data != None:
            for i, key in enumerate(list(self.keys)[:-4]):
                self.df[key].append(float(log_data[i]))
        else:
            for i, key in enumerate(list(self.keys)[:-4]):
                self.df[key].append(np.nan)

        self.df['fileName'].append(name)
        self.df['qp'].append(qp)
        self.df['cfg'].append(cfg)
        self.df['satd'].append(satd)

        self.df = pd.DataFrame(self.df)

    def getDf(self):
        return self.df

    def get(self, key : str):
        return self.df[key][0]

    def __mk_empty_df__(self) -> dict:
        df = {}
        for key in self.keys:
            df[key] = []
        return df

class LogDF:
    keys = ('bitrate','Y_PSNR','U_PSNR','V_PSNR','YUV_PSNR','fileName','qp','cfg','satd')

    def __init__(self) -> None:
        self.df = self.__mk_empty_df__()

    # appends a new LogDict (that is the return of read_log) to a LogDF (that storages more than one file data)
    def append(self, df : LogDict):
        self.df = pd.concat([self.df, df.getDf()], ignore_index=True)

    def getDataFrame(self) -> pd.DataFrame():
        return self.df

    def sort_by(self, key : str):
        self.df = self.df.sort_values(by=key).reset_index(drop=True)

    def get(self, key : str):
        return self.df[key][0]

    def __mk_empty_df__(self) -> pd.DataFrame:
        df = {}
        for key in self.keys:
            df[key] = []
        return pd.DataFrame(df)

    def plot(self, x : str = 'bitrate', y : str = 'YUV_PSNR', save : bool = False, output_name : str = None):
        if output_name == None:
            output_name = self.df['fileName'][0] + '_' + x + '_by_' + y

        ax = self.df.plot.line(x=x, y=y, title=output_name)
        if save:
            fig = ax.get_figure()
            fig.savefig(output_name + '.png')

        return ax

    def compare(self, cmp_with, x : str = 'bitrate', y : str = 'YUV_PSNR', save : bool = False, output_name : str = None):
        if output_name == None:
            output_name = self.df['fileName'][0] + '_' + cmp_with.get('fileName')[0] + '_' + x + '_by_' + y
        
        df2 = cmp_with.getDataFrame()

        fig, ax = plt.subplots()
        ax.plot(self.df[x], self.df[y])
        ax.plot(df2[x], df2[y])
        ax.set_xlabel(x)
        ax.set_ylabel(y)

        if save:
            fig = ax.get_figure()
            fig.savefig(output_name + '.png')

    def difference(self, cmp_with, x : str = 'bitrate', y : str = 'YUV_PSNR', save : bool = False, output_name : str = None):
        if output_name == None:
            output_name = self.df['fileName'][0] + '_' + cmp_with.get('fileName')[0] + '_' + x + '_by_' + y
        
        df2 = cmp_with.getDataFrame()

        fig, ax = plt.subplots()
        ax.plot(df2[x], df2[y] - self.df[y])

        ax.set_xlabel(x)
        ax.set_ylabel(y)

        if save:
            fig = ax.get_figure()
            fig.savefig(output_name + '.png')
        
        

# receives a file in the specified format "log_{VIDEONAME}_qp{QP}_{CONFIG}_.+RdCost{SATD}_exec"
# with the extension ".gplog", ".vvclog" or ".txt"
def read_log(file : str) -> LogDict:

    # Bitrate, Y-PSNR, U-PSNR, V-PSNR, YUV-PSNR
    ptrn = re.compile(r'^\s+\d+\s+a\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+$', re.M)  
    # Name, QP, config, satd
    file_name_ptrn = re.compile(r'log_(.+)_qp(\d{2})_(\w+)_.+RdCost(.+)_exec')

    if file.endswith('.txt') or file.endswith('.gplog') or file.endswith('.vvclog'):
        name, qp, cfg, satd = file_name_ptrn.findall(file)[0]
        with open(file) as f:
            log_text = f.read()
            check = ptrn.findall(log_text, re.M)
            if len(check) > 0:
                data_dict = LogDict(name, qp, cfg, satd, check[0])
            else:
                data_dict = LogDict(name, qp, cfg, satd, None)

            f.close()

    return data_dict   
    
def group_by_filename_1(data_set : list) -> LogDF:
    output = LogDF()
    for data in data_set:
        output.append(data)
        
    output.sort_by('qp')
    return output


# receives a list of LogDF and returns a dict of LogDF, grouped by qp

# split the data by each execution of VVC, i.e., the same video, coded with the same
# alteration on Software and the same configuration (AI, RA or LD)

# each key are composed by an APPROXIMATION on software, the NAME OF THE VIDEO encoded,
# and the CONFIGURATION USED (AI, RA, LD)

# output is a dict where each KEY are associated with it DATA_FRAME, that stores data
# from different QUANTIZATION PARAMETER (22, 27, 32, 37)


def split(data_set : list) -> dict:
    keys = []
    output = {}     

    for df in data_set:
        key = df.get('satd') + '_' + df.get('fileName') + '_' + df.get('cfg')
        if not key in keys:
            output[key] = LogDF()
            keys.append(key)
        
        output[key].append(df)
        
    for key in output.keys():
        output[key].sort_by('qp')

    return output
