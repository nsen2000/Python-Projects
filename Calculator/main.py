logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1/n2

print(logo)

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
             }

def calculator():
  num1 = float(input("What is the first number? "))
  check = True
  while (check == True):
    for operation in operations:
      print(operation)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What is the next number? "))
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")
    check_input = input(f"Do you want to continue calculating with {first_answer}? Type 'y' for yes or 'n' to start a new calculation or 'x' to exit: ")
    num1 = first_answer
    if check_input == "n":
      check = False
      calculator()
    elif check_input == "y":
      check = True
    elif check_input == "x":
      check = False
      print("Goodbye")

calculator()