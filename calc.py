class Calculator:
    def user_input(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("This is an invalid input.")
    
    def user_interface(self):
        print(
            """
            1. Add
            2. Substract
            3. Multiply
            4. Divide
            5. Exit
            """
        )
    
    def add(self, a, b):
        return a + b
    
    def substract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            print("Math error")
        else:
            return a / b
    
    def run(self):
        while True:
            self.user_interface()

            choice = int(input("Enter any number between 1-5: "))
            if choice not in [1, 2, 3, 4, 5]:
                print("You choose an invalid option.")
                continue
            elif choice == 5:
                print("You exit from the calculator.")
                break

            num1 = self.user_input("Enter the first number: ")
            num2 = self.user_input("Enter the second number: ")

            if choice == 1:
                print(f"{num1} + {num2} = {self.add(num1, num2)}")
            elif choice == 2:
                print(f"{num1} - {num2} = {self.substract(num1, num2)}")
            elif choice == 3:
                print(f"{num1} * {num2} = {self.multiply(num1, num2)}")
            elif choice == 4:
                print(f"{num1} / {num2} = {self.divide(num1, num2)}")

c1 = Calculator()
c1.run()