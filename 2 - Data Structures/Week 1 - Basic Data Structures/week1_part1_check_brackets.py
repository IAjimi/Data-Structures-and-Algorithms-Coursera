def checkBalance(string):
    stack = []
    stack_ix = []

    for n in range(len(string)):
        char = string[n]
        if char in ["(", "[", "{"]:
            stack.append(char)
            stack_ix.append(n)
        elif char in [")", "]", "}"]:
            if len(stack) == 0: 
                return False, n + 1
            top = stack.pop()
            stack_ix.pop()
            if (top == '[' and char != ']') or (top == '(' and char != ')') or (top == '{' and char != '}'):
                return False, n + 1
    return len(stack) == 0, stack_ix[-1] + 1 if stack_ix else 0


def main(text):
    mismatch, n = checkBalance(text)
    if mismatch == True:
        print("Success")
    else:
        print(n)


if __name__ == "__main__":
    text = input()
    main(text)
