import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt    

class GprofDF(pd.DataFrame):
    def __init__(self, data = None) -> None:
        super().__init__(data)

    def read_file(self, file_name):   
        keys = ('time','cum_sec','self_sec','calls','self_s_call','tot_s_call','namespace','class','function','definition')
        num_keys = ('time','cum_sec','self_sec','calls','self_s_call','tot_s_call')

        ptrn0 = re.compile(r'^\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+|\s+)\s+(\d+|\s+)\s+(\d+\.\d+|\s+)\s+(\d+\.\d+|\s+)\s+(.+)')
        ptrn1 = re.compile(r'(\w+)(?:<.+>)?::(\w+)(?:<.+>)?::(\w+)(?:<.+>)?\(')
        ptrn2 = re.compile(r'(\w+)(?:<.+>)?::(\w+)(?:<.+>)?\(')
        ptrn3 = re.compile(r'(\w+)(?:<.+>)?\(')
        
        df = {
            'time':[],
            'cum_sec':[],
            'self_sec':[],
            'calls':[],
            'self_s_call':[],
            'tot_s_call':[],
            'namespace':[],
            'class':[],
            'function':[],
            'definition':[]
        }

        with open(file_name) as f:
            for line in f:
                match = ptrn0.findall(line)
                if len(match) == 0:
                    if line == ' %         the percentage of the total running time of the':
                        break
                    continue

                for i, key in enumerate(num_keys):
                    buffer = match[0]
                    if buffer[i] == '':
                        df[key].append(np.nan)
                    else:
                        try:
                            df[key].append(float(buffer[i]))
                        except:
                            df[key].append(np.nan)
                df['definition']=match[0][6] 

                match = ptrn1.findall(line)
                if len(match) > 0:
                    df['namespace'].append(match[0][0])
                    df['class'].append(match[0][1])
                    df['function'].append(match[0][2])
                    continue
                match = ptrn2.findall(line)
                if len(match) > 0:
                    df['namespace'].append(np.nan)
                    df['class'].append(match[0][0])
                    df['function'].append(match[0][1])
                    continue
                match = ptrn3.findall(line)
                if len(match) > 0:
                    df['namespace'].append(np.nan)
                    df['class'].append(np.nan)
                    df['function'].append(match[0])
                    continue
                df['namespace'].append(np.nan)
                df['class'].append(np.nan)
                df['function'].append(np.nan)    
            f.close()

        self.__init__(df)
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

        dt2 = GprofDF(dt2).sort()
        return GprofClasses(dt2)
    
    def gplot(self, column='time', head=10):
        x = list(self.loc[:, 'function'])[:head]
        x.reverse()
        y = list(self.loc[:, column])[:head]
        y.reverse()

        plt.style.use('ggplot')
        plt.title(f'{column} - first {head} functions')
        plt.barh(x, y)
        plt.show()
    
class GprofClasses(pd.DataFrame):
    def __init__(self, data = None) -> None:
        super().__init__(data)

    def read_file(self, file_name):
        df = GprofDF().read_file(file_name)
        return df.group_by_class()
    
    def gplot(self, column='time', head=10):
        x = list(self.index[:head])
        x.reverse()
        y = list(self.loc[:, column])[:head]
        y.reverse()

        plt.style.use('ggplot')
        plt.title(f'{column} - first {head} classes')
        plt.barh(x, y)
        plt.show()