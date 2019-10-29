import xlrd
workbook = xlrd.open_workbook("test.xlsx")
sheet_names = workbook.sheet_names()

for sheet_name in sheet_names: # sheet表
    sheet2 = workbook.sheet_by_name(sheet_name)
    print(sheet_name,">>>")

    rows = sheet2.row_values(3) # 获取第四行
    cols = sheet2.col_values(1) # 获取第二列

    print(rows)
    print(cols)
    print("\n")