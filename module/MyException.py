class NoCorrectExcelFile(Exception):
    def __init__(self):
        super().__init__('올바른 엑셀 파일이 아닙니다.')


class ExcelNotFoundError(Exception):
    def __init__(self):
        super().__init__('엑셀 파일을 찾을 수 없습니다.')