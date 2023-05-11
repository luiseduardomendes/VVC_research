import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt    

class GprofDF(pd.DataFrame):
    def __init__(self, data = None) -> None:
        super().__init__(data)

    def read_file(self, file_name):           
        keys = ('time', 'cum_sec', 'self_sec', 'calls', 'self_s_call', 'tot_s_call', 'name', 'class')
        numeric_keys = ('time', 'cum_sec', 'self_sec', 'calls', 'self_s_call', 'tot_s_call')
        str_keys = ('name', 'class')


        pattern = re.compile(r'(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+|\s+)\s+(\d+|\s+)\s+(\d+\.\d+|\s+)\s+(\d+\.\d+|\s+)\s+(.+)()')

        pattern_class = re.compile(r'([^:( ]+)::([^<(]+).+')
        pattern_no_class = re.compile(r'([^ :(<>]+)[(<]')
            
        structBuffer = {}
        for key in keys:
            structBuffer[key] = []
        
        with open(file_name) as f:
            for line in f:
                check = pattern.findall(line)
                if len(check) != 0:
                    buffer = check[0][:]

                    match = pattern_class.findall(buffer[6])
                    if len(match) != 0:
                        match2 = pattern_class.findall(match[0][1])
                        #print(match2)
                        if len(match2) > 0:
                            class_name = match2[0][0]
                            funct_name = match2[0][1]
                        else:
                            class_name = match[0][0]
                            funct_name = match[0][1]

                    else:
                        match2 = pattern_no_class.findall(buffer[6])
                        if len(match2) > 0:
                            class_name = np.nan
                            funct_name = match2[0]
                        else:
                            class_name = np.nan
                            funct_name = np.nan
                    
                    for i, key in enumerate(numeric_keys):
                        if buffer[i] == '':
                            structBuffer[key].append(np.nan)
                        else:
                            try:
                                structBuffer[key].append(float(buffer[i]))
                            except:
                                structBuffer[key].append(np.nan)

                    structBuffer['class'].append(class_name)
                    structBuffer['name'].append(funct_name)

            f.close()
        
        self.__init__(structBuffer)
        return(self)
    
    def filter_function(self, function_name : str):
        return self[self['name'] == function_name]

    def filter_class(self, class_name: str):
        return self[self['class'] == class_name]

    def sort(self):
        return GprofDF(self.sort_values(by='time', ascending=False))
    
    def group_by_class(self):
        classes = []
        for i in self.index:
            c = self['class'][i]
            if not c in classes:
                classes.append(c)
        columns = ['time', 'cum_sec', 'self_sec', 'calls']

        dt2 = {}
        for col in columns:
            dt2[col] = {}
            for c in classes:
                tmp_dt = self[self['class'] == c]
                dt2[col][c] = tmp_dt.loc[:, col].sum(skipna=True)

        
        return GprofDF(dt2).sort()
    
    def gplot(self, column='time', head=10):
        x = list(self.index[:head])
        x.reverse()
        y = list(self.loc[:, column])[:head]
        y.reverse()

        plt.style.use('ggplot')
        plt.title(f'{column} - first {head} items')
        plt.barh(x, y)
        plt.show()