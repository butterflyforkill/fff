class Calculator:
    def __init__(self) -> None:
        pass
    
    
    def add(self, num1, num2):
        return num1 + num2
    
    
    def subtract(self, num1, num2):
        return num2 - num1
    
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    
    def divide(self, num1, num2):
        if num2 == 0:
            return f"You can't divide by zero"
        else:
            return num1 / num2
        
    
calc = Calculator()
print(calc.add(56, 78))
print(calc.divide(12344, 456))
print(calc.multiply(56, 89))
print(calc.subtract(4, 0))
print(calc.subtract(7899, 45))