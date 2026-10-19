#  Accept two numbers and display remainder of their division
def division_remainder(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    remainder = num1 % num2
    return f"The remainder of {num1} divided by {num2} is {remainder}."