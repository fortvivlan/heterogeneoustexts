import pickle
import os
from collections import defaultdict
import pandas as pd


def main():
    goldset = pickle.load(open('/home/al/PythonFiles/files/disser/readydata/annot500inds', 'rb'))
    p = '/home/al/PythonFiles/files/disser/experimentsthres1.5/'
    autosets = {name[12:]: os.path.join(p, name) for name in os.listdir(p) if name.startswith('breakpoints_')}
    texts = pickle.load(open('/home/al/PythonFiles/files/disser/readydata/lengthspartial', 'rb'))
    result = defaultdict(dict)
    result['Gold']['Total points'] = sum(map(len, goldset.values()))
    result['Gold']['Correct guesses'] = result['Gold']['Total points']
    result['Gold']['Precision'] = 1
    result['Gold']['Recall'] = 1
    result['Gold']['F-score'] = 1

    for name in autosets:
        autoset = pickle.load(open(autosets[name], 'rb'))
        totalauto = 0
        gets = 0
        falseneg = 0
        closecall = 0
        for key in goldset:
            if not autoset.get(key):
                autoset[key] = []
            totalauto += len(autoset[key])
            gets += len(set(autoset[key]) & set(goldset[key]))
            falses = set(autoset[key]) - set(goldset[key])
            falseneg += len(set(goldset[key]) - set(autoset[key]))
            closecallset = set()
            for autopoint in falses:
                for goldpoint in goldset[key]:
                    if abs(autopoint - goldpoint) <= 2:
                        closecallset.add(autopoint)
            closecall += len(closecallset)
        result[name]['Total points'] = totalauto
        result[name]['Correct guesses'] = gets
        result[name]['Precision'] = (gets + 0.5 * closecall) / totalauto
        result[name]['Recall'] = (gets + 0.5 * closecall) / (gets + falseneg)
        result[name]['F-score'] = 2 * result[name]['Precision'] * result[name]['Recall'] / (result[name]['Precision'] + result[name]['Recall'])
        result[name]['Precision'] = round(result[name]['Precision'], 3)
        result[name]['Recall'] = round(result[name]['Recall'], 3)
        result[name]['F-score'] = round(result[name]['F-score'], 3)
        result[name]['Close call'] = closecall

    df = pd.DataFrame.from_dict(result, orient='index')
    df.to_excel('breakpoints_total_thres1-5.xlsx')


if __name__ == '__main__':
    main()
