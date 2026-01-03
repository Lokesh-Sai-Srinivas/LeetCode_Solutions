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