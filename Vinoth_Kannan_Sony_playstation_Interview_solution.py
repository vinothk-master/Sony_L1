"""
I have used stack method to arrive at the solution.

This solution has

Time complexity of O(N)
Space compelxity of O(N) -> in worst case whereas in the best case it can be solved in O(1)
"""

from typing import Optional


def evaluate(expression: str) -> Optional[int]:
    cur = 0  # for storing the current number
    op = "+"
    stack = []  # This solution is based on the stack operation
    parentheses_stack = []  # To check valid parenthesis in a given string
    for s in expression:
        if s == "(":
            parentheses_stack.append(s)
        elif s == ")":
            if not parentheses_stack:  # if the stack is empty which means there is no corresponding open bracket and
                # it is considered as invalid
                return 0
            parentheses_stack.pop()
    if parentheses_stack:
        return 0

    def helper(
        op, cur
    ):  # This helper function is used to perform the calculation based on the operation in the string
        if op == "+":
            stack.append(cur)
        elif op == "-":
            stack.append(-cur)
        elif op == "*":
            stack.append(
                stack.pop() * cur
            )  # According to the 'BODMAS' rule * has the higher priority than "+-", so the * is performed with the top value int the stack
        elif op == "/":
            stack[-1] = int(
                float(stack[-1]) / cur
            )  # According to the 'BODMAS' rule / has the higher priority than "*+-" so the / is performed with the top value in the stack and appended

    for char in range(len(expression)):
        if expression[char].isdigit():
            cur = (
                cur * 10 + int(expression[char])
            )  # The digit can be of multiple digit places, inorder to validate as a single number we use this
        elif (
            expression[char] == "("
        ):  # if we see this in the string, we shall append to my stack along with the operation to perform
            stack.append(op)
            cur = 0
            op = "+"
        elif expression[char] in ["+", "-", "*", "/", ")"]:
            helper(op, cur)
            if (
                expression[char] == ")"
            ):  # if we see in the string which means, we need to perform the calculation within the ()
                cur = 0
                while isinstance(stack[-1], int):
                    cur += stack.pop()
                op = stack.pop()
                helper(op, cur)
            cur = 0
            op = expression[char]
    helper(op, cur)
    return sum(stack)  # Will return the sum of all the values in the string


# Below are the cases I have validated which includes the positive and negative scenarios

testcases = {
    "TC1": "1+3",  # Positive
    "TC2": "(1+3)*2",  # Positive
    "TC3": "(4/2)+6",  # Positive
    "TC4": "4 + (12 / (1 * 2))",  # Positive
    "TC5": "(1 + (12 * 2)",  # Negative
    "TC6": "(1 + (12 * 2)))",  # Negative
    "TC7": "(((1 + (12 * 2))",  # Negative
    "TC8": "(1 + (12 * 2))(",  # Negative
    "TC9": ")(1 + (12 * 2))",  # Negative
    "TC10": "1+3(",  # Negative
    "TC11": "(1 + 10)",  # Positive
    "TC12": "(10/10)",  # Positive
    "TC13": "(10 /(5+5))",  # Positive
    "TC14": "(1 + ()",  # Negative
    "TC15": "(1 + (0))",  # Positive
}

for key in testcases:
    print(key, " -> ", evaluate(testcases[key]))
