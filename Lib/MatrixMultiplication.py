#want to know which cli is being used


from Utility.Matrix_Display import display_matrix
from Function.MatrixOperationFile import MatrixOperations
class MatrixCli:

    def __init__(self):
        self.command=""
        self.userInputData = {}
        self.counter = 1
        self.history = []
        self.history_index = None

    def mini_cli(self):
        print("Welcome to Mini CLI! Type 'help' for commands, 'exit','quit or 'q' to quit.\n")
        upDownPressCounter = 0
        while True:
            try:
                self.command = input(">>> ").strip()  # remove spaces if there is any

                # if empty input continue with cli again
                if self.command == "":
                    continue
                #Check for variable name
                if self.userInputData.keys().__contains__(self.command):
                   if self.userInputData[self.command]:
                       display_matrix(self.userInputData[self.command])
                   continue
                # Exit commands
                if self.command.lower() in ["exit", "quit", "q"]:
                    print("Have a good day! Exiting CLI...")
                    break

                # Available help command
                if self.command.lower() == "help":
                    print(
                        "Available commands:\n  help - show this message\n  exit/quit/q - exit CLI\n  data-shows data in stored more updates will be posted here \n history-his \n")
                    self.history.append(command.lower())#storing command
                    continue

                if self.command.lower()=="data":
                    print(self.userInputData)
                    self.history.append(self.command.lower())
                    continue


                #Matrix operations conditions check
                if any(op in self.command for op in ["+", "-", "*", "/"]):
                    # parse operator
                    for op in ["+", "-", "*", "/"]:
                        if op in self.command:
                            left, right = map(str.strip, self.command.split(op))
                            break

                    if left not in self.userInputData or right not in self.userInputData:
                        print("One or both variables not found.")
                        continue

                    A = self.userInputData[left]
                    B = self.userInputData[right]

                    try:
                        if op == "+":
                            result = MatrixOperations.add(A, B)
                        elif op == "-":
                            result = MatrixOperations.subtract(A, B)
                        elif op == "*":
                            result = MatrixOperations.multiply(A, B)
                        elif op == "/":
                            result = MatrixOperations.divide(A, B)
                        else:
                            print("Unknown operator")
                            continue

                        # store result in a new variable
                        var_name = f"var{self.counter}"
                        self.userInputData[var_name] = result
                        self.counter += 1
                        print(f"{var_name} =")
                        display_matrix(result)
                        self.history.append(self.command)

                    except Exception as e:
                        print("Error:", e)
                    continue

                #matrix operation complete here


                if self.command.lower()=="his":
                    print(self.history)
                    continue
                # Process other input
                variableName=f"var{self.counter}"
                self.userInputData[variableName]=self.parse_matrix(self.command)
                self.history.append(self.command)
                print(f"{variableName}={self.userInputData[variableName]}")
                self.counter +=1  # increase counter every time to make it unique
            except KeyboardInterrupt:
                print("\nExiting CLI...")
                break

            except EOFError:
                print("\nExiting CLI...")
                break

    def parse_matrix(self, data):

        ##Parse matrix string in format [r11,r12:r21,r22:...]
        ##Rejects invalid special characters except [ ] , :
        ###Returns 2D list if valid, else False

        # Allowed characters: digits, colon, comma, brackets, minus (for negative numbers)
        allowed_chars = "0123456789[],:-"

        # Check for invalid characters
        for c in data:
            if c not in allowed_chars:
                print("Invalid Input! Please enter matrix like [1,2:2,1]")
                return False

        # Remove brackets
        stripped = data.strip("[]")
        if not stripped:
            print("Empty matrix not allowed!")
            return False

        # Split into rows
        rows = stripped.split(":")
        matrix = []
        for row in rows:
            elements = row.split(",")
            try:
                # Convert to integers
                int_row = [int(el.strip()) for el in elements]
                matrix.append(int_row)
            except ValueError:
                print("Invalid number in matrix! Only integers allowed.")
                return False

        return matrix

# Run the CLI
if __name__ == "__main__":
    cli=MatrixCli()
    cli.mini_cli()



