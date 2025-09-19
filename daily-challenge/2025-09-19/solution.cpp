"""
Problem: 3484 - Design Spreadsheet  
Description: Implement a class Spreadsheet that supports setting a cell value, resetting a cell to zero, and evaluating formulas of the form "=A1+B2", where operands can be either integers or cell references.  
Date: 2025-09-19
"""

using namespace std;

class Spreadsheet {
    unordered_map<string, int> cells;

public:
    Spreadsheet(int rows) {
        
    }
    
    void setCell(string cell, int value) {
        cells[cell] = value;
    }
    
    void resetCell(string cell) {
        cells[cell] = 0;
    }
    
    int getValue(string formula) {
        formula = formula.substr(1);
        size_t plusPos = formula.find('+');
        string x = formula.substr(0, plusPos);
        string y = formula.substr(plusPos + 1);
        return getOperandValue(x) + getOperandValue(y);
    }

private:
    int getOperandValue(const string& operand) {
        if(isdigit(operand[0])){
            return stoi(operand);
        }
        return cells.count(operand) ? cells[operand] : 0;
    }
};

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet* obj = new Spreadsheet(rows);
 * obj->setCell(cell,value);
 * obj->resetCell(cell);
 * int param_3 = obj->getValue(formula);
 */
