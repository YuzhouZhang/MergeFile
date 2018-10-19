import os
import zipfile

import pandas as pd
import rarfile

os.chdir('/home/zhangyuzhou/PycharmProjects/MergeFile')

for root, folders, files in os.walk(os.getcwd()):
    for folder in folders:
        if 'input' in folder:
            print(folder)
            os.chdir(folder)


def extract_file():
    for root, folders, files in os.walk(os.getcwd()):
        for file in files:
            if os.path.isfile(file) and os.path.splitext(file)[-1] == '.zip':
                zip_file = zipfile.ZipFile(file)
                zip_file.extractall()
                zip_file.close()
                os.remove(file)
                extract_file()
            elif os.path.isfile(file) and os.path.splitext(file)[-1] == '.rar':
                rar_file = rarfile.RarFile(file)
                rar_file.extractall()
                rar_file.close()
                os.remove(file)
                extract_file()


for root, folders, files in os.walk(os.getcwd()):
    for file in files:
        if os.path.isfile(file) and os.path.splitext(file)[-1] == '.xlsx':
            xlsx_file = pd.ExcelFile(file)
            for sheet_name in xlsx_file.sheet_names:
                print(sheet_name)
                print(os.path.splitext(file)[0])
                df = pd.read_excel(file, sheet_name=sheet_name).to_excel("%s+%s.xlsx" % (os.path.splitext(file)[0], sheet_name), sheet_name=sheet_name)
            os.remove(file)
