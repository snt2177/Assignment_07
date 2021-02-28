#------------------------------------------#
# Title: loading_file.py
# Desc: Creates a starter binary CDInventory.dat file for CDInventory.py
# Change Log: (Who, When, What)
# STimchenko, 2021-Feb-27, Created File
#------------------------------------------#



lstTbl = [
    {'ID': 1, 'Title': 'Bad', 'Artist': 'Michael Jackson'},
    {'ID': 2, 'Title': 'The Big Wheel', 'Artist': 'Rurig'}
    ]
    
strFileName = 'CDInventory.dat'

def save_data(data, file_name):
    with open (file_name, 'wb') as fileObj:
        pickle.dump(data, fileObj)

import pickle
save_data(lstTbl, strFileName) 
