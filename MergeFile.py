import os

import pandas as pd

os.getcwd()

os.chdir('/home/zhangyuzhou/PycharmProjects/MergeFile')

for root, folders, files in os.walk(os.getcwd()):
    for folder in folders:
        if 'input' in folder:
            print(folder)
            os.chdir(folder)

for root, folders, files in os.walk(os.getcwd()):
    for folder in folders:
        os.chdir(os.path.join(root, folder))
        print(os.getcwd())
        df_total = pd.DataFrame()
        for file in os.listdir(os.getcwd()):
            if os.path.isfile(file):
                print(file)
                print(os.path.splitext(file))
                if os.path.splitext(file)[-1] == '.xlsx':
                    df = pd.read_excel(file)
                    print(df.shape)
                    df_total = pd.concat((df, df_total), sort=False)
                elif os.path.splitext(file)[-1] == '.csv':
                    df = pd.read_csv(file, engine='python', encoding='gbk')
                    print(df.shape)
                    df_total = pd.concat((df, df_total), sort=False)
        df_total.to_csv("/home/zhangyuzhou/PycharmProjects/MergeFile/output/%s.csv" % folder, encoding='utf-8')
