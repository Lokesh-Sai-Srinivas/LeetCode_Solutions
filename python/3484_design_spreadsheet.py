"""
Problem: 3484 - Design Spreadsheet  
Description: Implement a class Spreadsheet that supports setting a cell value, resetting a cell to zero, and evaluating formulas of the form "=A1+B2", where operands can be either integers or cell references.  
Date: 2025-09-19
"""

class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells[cell] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        x, y = formula.split('+')
        return self._get_opr_val(x) + self._get_opr_val(y)

    def _get_opr_val(self, oper:str) -> int:
        if oper.isdigit():
            return int(oper)
        return self.cells.get(oper, 0)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
