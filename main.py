import os.path

from PySide6.QtCore import Qt, QByteArray, QBuffer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QFileDialog, QLabel, QWidget, QVBoxLayout, QLineEdit

from module.ExcelHandler import Excel
from ui.mainwindow import Ui_MainWindow

# 전역 변수
IS_SAVED = True         # 저장 여부 확인
BASE_DIR = os.path.dirname(os.path.abspath(__file__))           # 파일 위치 경로


class TableInnerWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(QVBoxLayout())
        self.lineEdit = QLineEdit()
        self.image = QLabel()

        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.layout().addWidget(self.lineEdit)
        self.layout().addWidget(self.image)

    def setText(self, text):
        self.lineEdit.setText(text)

    def setImage(self, img_data):
        # byte 자료형으로 이루어진 사진을 QLabel에 출력
        data = QByteArray(img_data)
        img = QPixmap()
        img.loadFromData(data)
        # 사진 크기를 칸에 맞게 수정
        img = img.scaled(window.tableWidget.cellWidget(0,0).width(), 190 + 10)
        self.image.setPixmap(img)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.excel = None

        # tableWidget 기본설정
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)               # 가로 길이 너비에 맞춤
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)                   # 세로길이는 220 고정
        self.tableWidget.setHorizontalHeaderLabels(['구간명/작업전 사진', '전주번호', '공정명/작업 후 사진'])     # 가로 탭은 항상 전, 번호, 후로 고정

        # 메뉴바 기본설정
        self.action_open.triggered.connect(self.open)
        self.action_save.triggered.connect(self.save)
        self.action_saveas.triggered.connect(self.saveas)

    def open(self):
        global IS_SAVED

        # 저장이 안 되었다면, 경고
        if not IS_SAVED:
            # TODO: 저장하라는 문구
            return

        file, _ = QFileDialog.getOpenFileName(self, '엑셀 파일 선택', BASE_DIR, "Excel file (*.xlsx)")
        # file = 'test.xlsx'  # For Test
        try:
            self.excel = Excel(file)
            print(self.excel)
        except Exception as e:
            print('[에러발생]', e)
        else:
            self.fillMainWindow(file)

    def fillMainWindow(self, file):
        # 파일 이름
        file = file.split('/')[-1]
        self.label_file.setText(file)

        # 공사정보
        self.lineEdit_date.setText(self.excel.sheet['Q2'].value)
        self.lineEdit_name.setText(self.excel.sheet['Q3'].value)
        self.lineEdit_company.setText(self.excel.sheet['B3'].value)
        self.lineEdit_project.setText(self.excel.sheet['B2'].value)

        # 공사사진
        # 시트에 맞게 row 칸 수를 조절
        self.tableWidget.setRowCount(self.excel.row)

        # 칸을 텍스트와 이미지를 표시하는 widget으로 설정
        for i in range(self.excel.row):
            for j in range(3):
                tableInnerWidget = TableInnerWidget()
                self.tableWidget.setCellWidget(i, j, tableInnerWidget)

        # 기존 시트에 삽입된 이미지를 불러와서 보여줌
        for cell in self.excel.images:
            col = 0 if cell[0] == 'A' else 2 if cell[0] == 'O' else 1
            row = (int(cell[1:]) - 6) // 22

            tableInnerWidget = self.tableWidget.cellWidget(row, col)
            img_data = self.excel.images[cell]._data()
            tableInnerWidget.setImage(img_data)

        for r in range(self.excel.row):
            row = 22 * r + 4

            # 구간명 설정
            구간명 = self.excel.sheet[f'B{row}'].value
            tableInnerWidget = self.tableWidget.cellWidget(r, 0)
            tableInnerWidget.setText(구간명)

            공정명 = self.excel.sheet[f'P{row}'].value
            tableInnerWidget = self.tableWidget.cellWidget(r, 2)
            tableInnerWidget.setText(공정명)


    def save(self):
        print("save function")

    def saveas(self):
        print("save as function")


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
