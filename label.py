import pandas as pd 
import numpy as np
import os
import sys
  

def data_awal():
    D1 = pd.read_csv(' kelas1.csv')
    D1=pd.DataFrame(D1.values, columns = ["label1", "ch1", "ch2", "ch3", 
                                          "ch4","ch5","ch6","ch7","ch8" ])
    D1.loc[D1['label1'] >-1, 'label1'] = '1'
    D1.to_csv('1.csv')
    print(D1)

def data_kedua():
    D2 = pd.read_csv(' kelas2.csv')
    D2=pd.DataFrame(D2.values, columns = [ "ch1", "ch2", "ch3", 
                                          "ch4","ch5","ch6","ch7","ch8" ])
    D2.loc[D2['label2'] >-1, 'label2'] = '2'
    print (D2)
    D2.to_csv('2.csv')

def total_data() :
    data_1 =pd.read_csv('1.csv')
    data_2 =pd.read_csv('2.csv')
    tot= pd.concat([data_1,data_2])
    tot.to_csv(' dataku.csv',header=None)
    print(tot)


for i in range (3):
        data_awal()
        data_kedua()
        total_data()




