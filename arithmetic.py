def arithmetic_arranger(expression, result=False):
    # Check if there are more than 5 expressions, which is not allowed.
    if len(expression) > 5:
        return "Error: Too many problems."

    # Initialize variables to store lines of the arranged expressions.
    line1 = ""   # The first line containing the first operand
    line2 = ""   # The second line containing the operator and second operand
    line3 = ""   # The third line for underlining
    line4 = ""   # The fourth line containing the results (if result=True)

    # Loop through each expression in the list.
    for exp in expression:
        exp = exp.replace(" ", "")  # Remove all whitespace from the expression.

        # Check for the supported operators ('+' and '-' only).
        if "+" in exp:
            exp = exp.split("+")
            operator = "+"
        elif "-" in exp:
            exp = exp.split("-")
            operator = "-"
        else:
            return "Error: Operator must be '+' or '-'."

        # Check if both operands are composed of digits only.
        if not (exp[0].isdigit() and exp[1].isdigit()):
            return "Error: Numbers must only contain digits."

        # Check if operands have more than 4 digits.
        if len(exp[0]) > 4 or len(exp[1]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the width needed for formatting.
        align = max([len(exp[0]), len(exp[1])]) + 2

        # If the 'result' argument is True, calculate and format the result.
        if result:
            res = str(eval(exp[0] + operator + exp[1]))
            line4 += res.rjust(align) + "    "

        # Format and build lines 1, 2, and 3 for the current expression.
        line1 += exp[0].rjust(align) + "    "
        line2 += operator + exp[1].rjust(align - 1) + "    "
        line3 += "-" * (align) + "    "

    # Remove trailing whitespace from each line.
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()

    # Combine the lines to create the arranged string.
    arranged_string = "\n".join([line1, line2, line3])

    # If 'result' is True, add the fourth line with results.
    if result:
        line4 = line4.rstrip()
        arranged_string += "\n" + line4 + "\n" + line3

    return arranged_string

# Example usage with result=True
print(arithmetic_arranger(["32 + 8", "1 - 38015", "9999 + 9999", "523 - 49"], True))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
