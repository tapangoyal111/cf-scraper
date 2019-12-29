import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def create_dick():
    df = pd.read_excel('sec.xlsx')
    col=list(df.columns)

    df=df.drop(columns=[col[0],col[1],col[3],col[6],col[8],col[9],col[10],col[11],col[12],col[13],col[14],col[15],col[16]])
    col=df.columns
    dick={}
    for i in df.index:
        dick[df[col[-1]][i]]=[df[col[0]][i],df[col[1]][i],df[col[2]][i]]

    df = pd.read_excel('fs.xlsx')
    col = list(df.columns)

    df = df.drop(
        columns=[col[0], col[1], col[3], col[6], col[8], col[9], col[10], col[11], col[12], col[13], col[14], col[15],
                 col[16]])
    col = df.columns
    dick1 = {}
    for i in df.index:
        dick1[df[col[-1]][i]] = [df[col[0]][i], df[col[1]][i], df[col[2]][i]]

    return (dick,dick1)
