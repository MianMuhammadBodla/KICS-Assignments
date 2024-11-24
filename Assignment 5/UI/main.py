import add
import sub
import divid
import mult

def get_input():
    a = float(input("Please Enter First Number: "))
    b = float(input("Please Enter Second Number: "))
    return a, b

def main():
    while True:
        a, b = get_input()
        operation = input("Please choose an operator (+, -, /, x): ")

        if operation == "+":
            print(f"Your answer is = {add.add(a, b)}")
        elif operation == "-":
            print(f"Your answer is = {sub.sub(a, b)}")
        elif operation == "/":
            print(f"Your answer is = {divid.divide(a, b)}")
        elif operation == "x":
            print(f"Your answer is = {mult.multi(a, b)}")
        else:
            print("Please choose a correct operation.")

        if input("Do you want to quit the calculator (Y for quit, N for not)? ").upper() == "Y":
            break

if __name__ == "__main__":
    main()







