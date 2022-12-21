from art import logo
# ADD
def add(n1,n2):
    return n1+n2

# substract
def substract(n1,n2):
    return n1-n2

#MULTIPLY
def multiply(n1,n2):
    return n1*n2

#Divide
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide
}

def calculator():
    print(logo)
    should_continue=True
    num1=float(input("what is the first number? :"))

    while should_continue:
        for symbol in operations:
            print(symbol)
        operations_symbol=input("pick an operation from the line above: ")
        num2=float(input("what the second number? :"))
        calculation_function=operations[operations_symbol]
        answer=calculation_function(num1,num2)
        print(f"{num1}{operations_symbol}{num2}={answer}")
        if input(f"Type 'y' to continue calculating with {answer}:")=="y":
            num1=answer
        else:
            should_continue=False
            calculator()

calculator()