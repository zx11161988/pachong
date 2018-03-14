#! /user/bin/env python
import openpyxl


class WriteData:
    number = 1
    path = "../building.xlsx"
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '2007测试表'

    def __init__(self):
        value = ["小区名称", "户型", "面积", "总价", "单价", "成交时间", "中介", "链接"]
        self.writedata(value)

    def writedata(self, value):
        for info in value:
            print(info)
        print("Append number = " + str(WriteData.number))
        for i in range(0, len(value)):
            WriteData.sheet.cell(WriteData.number, i+1, str(value[i]))
        WriteData.wb.save(WriteData.path)
        WriteData.number = WriteData.number + 1
        print("写入数据成功！")


if __name__ == '__main__':
    data = WriteData()
