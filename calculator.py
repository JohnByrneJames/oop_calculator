class Calculator:  # Define calculator

    @staticmethod  # These can be accessed through instances but also can be accessed without too
    def addition(num1, num2):
        return num1 + num2

    @staticmethod  
    def subtraction(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplication(num1, num2):
        return num1 * num2

    @staticmethod
    def division(num1, num2):
        return num1 / num2

    @staticmethod
    def modulo(num1, num2):
        return num1 % num2

    @staticmethod
    def quotient(num1, num2):
        return num1 // num2

    @staticmethod
    def exponentiation(num1, num2):
        return num1 ** num2


