// Basic calculation string
let calculation = '';

function addToCalculation(symbol) {
    calculation += String(symbol);
    document.getElementById('text_result').value = calculation;
}

function evaluateCalculation() {
    try {
        calculation = String(eval(calculation));
        document.getElementById('text_result').value = calculation;
    } catch {
        clearField();
        document.getElementById('text_result').value = 'Error';
    }
}

function clearField() {
    calculation = '';
    document.getElementById('text_result').value = '';
}
