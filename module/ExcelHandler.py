import string

import openpyxl

from module.MyException import NoCorrectExcelFile, ExcelNotFoundError


class Excel:
    def __init__(self, file):
        self.wb = None
        self.sheet = None
        self.images = {}
        self.row = 0

        # 엑셀 파일을 불러옴
        try:
            self.wb = openpyxl.load_workbook(file)
        except FileNotFoundError:
            raise ExcelNotFoundError
        else:
            if '공정별사진대장' not in self.wb.sheetnames:
                raise NoCorrectExcelFile
            # '공정별사진대장' 시트 선택
            self.sheet = self.wb['공정별사진대장']

            # 세로 칸수를 셈
            self.row = (self.sheet.max_row - 3) // 22

            # {위치: 이미지}
            for image in self.sheet._images:
                r = image.anchor._from.row + 1
                c = string.ascii_uppercase[image.anchor._from.col]
                cell = f'{c}{r}'

                self.images[cell] = image

    def save_info(self, date, name, company, project):
        self.sheet['Q2'] = date
        self.sheet['Q3'] = name
        self.sheet['B3'] = company
        self.sheet['B2'] = project

    def save_image(self):
        pass

    def __str__(self):
        return f'row: {self.row}, images: {self.images}'