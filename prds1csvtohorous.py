# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 05:58:18 2024

@author: Gayatri kulkarni
"""
import pandas as pd
sInputFileName='C:/VKHCG/05-DS/9999-Data/Country_Code.csv'
InputData=pd.read_csv(sInputFileName,encoding="Latin-1")
print('Input Data Values ===============================================')
print(InputData)
print('============================================================================')

#Processing Rules ================================================================
ProcessData=InputData
# Remove columns 150-2 Code and 150-3-CODE
ProcessData.drop('ISO-2-CODE', axis=1,inplace=True)
ProcessData.drop('ISO-3-Code', axis=1,inplace=True)
print(ProcessData)

# Rename Country and Iso-MA9
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-MA9': 'CountryNumber'}, inplace=True)
print(ProcessData)

# Set new Index
#ProcessData.set_index('CountryNumber', inplace=True)
# Sort data by CountryNumber
ProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True)
print('Process Data  Values ===============================================')
print(ProcessData)
print('============================================================================')

#OutputData Agreement
OutputData=ProcessData
sOutputFileName='C:/VKHCG/05-DS/9999-Data/HORUS-CSV-Country.csv'
OutputData.to_csv(sOutputFileName, index=False)
print('CSV to Hours - Done')
#Utility done ====================================================
print('Gayatri Kulkarni -53004230002')