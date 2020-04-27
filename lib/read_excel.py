import os
import sys
import xlrd

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
from conf.settings import DATA_PATH

file_path = DATA_PATH + r'\test_case.xlsx'


#  print(file_path)

def read_excel(sheet_name='Sheet01', excel_path=file_path):
    workbook = xlrd.open_workbook(excel_path)  # 打开文件
    sheets = workbook.sheet_names()#  获取所有sheet
    #  print(sheets) #  ['Sheet01','Sheet02','Sheet03']

    #  根据sheet名称获取sheet内容(也可以根据格局索引从0开始)
    sheet = workbook.sheet_by_name(sheet_name)

    #  获取第二行作为key
    first_row = sheet.row_values(1)

    #  获取行数
    rows_lenth = sheet.nrows
    all_rows = []
    rows_dict = []
    for i in range(rows_lenth):
        if i < 2:
            continue
        all_rows.append(sheet.row_values(i))
    for row in all_rows:
        lis = dict(zip(first_row,row))
        rows_dict.append(lis)
        return rows_dict


if __name__ == '__main__':
    res = read_excel()
    print(res)



