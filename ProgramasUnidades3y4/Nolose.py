class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_inorder_tree(expression):
    operand_stack = []
    operator_stack = []

    elements = expression.split()
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '(': 0}

    def handle_operator(element):
        while (operator_stack and operator_stack[-1] in precedence and
               precedence[element] <= precedence[operator_stack[-1]]):
            operator = operator_stack.pop()
            node = TreeNode(operator)
            node.right = operand_stack.pop()
            node.left = operand_stack.pop()
            operand_stack.append(node)

    for element in elements:
        if element == '(':
            operator_stack.append(element)
        elif element == ')':
            while operator_stack and operator_stack[-1] != '(':
                operator = operator_stack.pop()
                node = TreeNode(operator)
                node.right = operand_stack.pop()
                node.left = operand_stack.pop()
                operand_stack.append(node)
            operator_stack.pop()  # Remove the left parenthesis
        elif element in {'+', '-', '*', '/', '%'}:
            handle_operator(element)
            operator_stack.append(element)
        else:
            operand_stack.append(TreeNode(float(element)))

    while operator_stack:
        operator = operator_stack.pop()
        node = TreeNode(operator)
        node.right = operand_stack.pop()
        node.left = operand_stack.pop()
        operand_stack.append(node)

    return operand_stack[0]

def evaluate_tree(tree):
    if tree.value in {'+', '-', '*', '/', '%'}:
        left = evaluate_tree(tree.left)
        right = evaluate_tree(tree.right)
        if tree.value == '+':
            return left + right
        elif tree.value == '-':
            return left - right
        elif tree.value == '*':
            return left * right
        elif tree.value == '/':
            if right == 0:
                raise ValueError("Division by zero is not allowed")
            return left / right
        elif tree.value == '%':
            if right == 0:
                raise ValueError("Obtaining remainder of division by zero is not allowed")
            return left % right
    else:
        return tree.value

expression = input("Enter the infix expression: ")
try:
    tree = build_inorder_tree(expression)
    result = evaluate_tree(tree)
    print("Expression result:", result)
except ValueError as e:
    print("Invalid expression:", e)
