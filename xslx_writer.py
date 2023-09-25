from typing import Dict, List

import openpyxl as xlsx

from course import Course


class XlsxWriter:

    TEMPLATE_FILENAME: str = "template.xlsx"

    TITLE_ROW: int = 0
    SWS_ROW: int = 1
    TYPE_ROW: int = 2
    LANGUAGE_ROW: int = 3
    CATEGORY_ROWS: Dict[str, int] = {
        category: 5 + i
        for i, category in enumerate(Course.CATEGORIES)
    }
    START_COLUMN: str = 3

    _courses: List[Course]
    _workbook: xlsx.Workbook
    _worksheet: xlsx.worksheet

    def __init__(self, courses: List[Course]):
        self._courses = courses
        self._workbook = xlsx.load_workbook(self.TEMPLATE_FILENAME)
        self._worksheet = self._workbook['Sheet1']

    def _write_cell(self, row: int, column: int, value: str):
        self._worksheet.cell(row=row + 1, column=column + 1).value = value

    def write(self, filename: str):
        for column, course in enumerate(
            self._courses, start=self.START_COLUMN
        ):
            self._write_cell(self.TITLE_ROW, column, course.title)
            self._write_cell(self.SWS_ROW, column, course.sws)
            self._write_cell(self.TYPE_ROW, column, course.type_)
            self._write_cell(self.LANGUAGE_ROW, column, course.language)
            for category in course.categories:
                row = self.CATEGORY_ROWS[category]
                self._write_cell(row, column, course.ects)

        self._workbook.save(filename)
