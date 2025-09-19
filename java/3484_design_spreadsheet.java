"""
Problem: 3484 - Design Spreadsheet  
Description: Implement a class Spreadsheet that supports setting a cell value, resetting a cell to zero, and evaluating formulas of the form "=A1+B2", where operands can be either integers or cell references.  
Date: 2025-09-19
"""

class Spreadsheet {
    private Map<String ,Integer> cells;

    public Spreadsheet(int rows) {
        cells = new HashMap<>();
    }
    
    public void setCell(String cell, int value) {
        cells.put(cell, value);
    }
    
    public void resetCell(String cell) {
        cells.put(cell, 0);
    }
    
    public int getValue(String formula) {
        formula = formula.substring(1);
        String[] parts = formula.split("\\+");
        return getOperandValue(parts[0]) + getOperandValue(parts[1]);
    }

    private int getOperandValue(String operand) {
        if(Character.isDigit(operand.charAt(0))) 
            return Integer.parseInt(operand);
        return cells.getOrDefault(operand, 0);
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = new Spreadsheet(rows);
 * obj.setCell(cell,value);
 * obj.resetCell(cell);
 * int param_3 = obj.getValue(formula);
 */
