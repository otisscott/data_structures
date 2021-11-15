from ArrayStack import ArrayStack


def helper():
    var_dict = {}
    inp = input('--> ')
    while inp != 'done()':
        if '=' in inp:
            split_inp = inp.split(' = ')
            result = solver(split_inp[1], var_dict)
            var_dict[split_inp[0]] = result
            print(split_inp[0])
            inp = input('--> ')
        elif len(inp.split()) == 1 and not inp.split()[0].isdigit():
            print(var_dict[inp])
            inp = input('--> ')
        else:
            result = solver(inp, var_dict)
            print(result)
            inp = input('--> ')


def solver(exp_str, var_dict):
    """
        :exp_str type: str
        :return type: int
        """
    exp_lst = exp_str.split()
    my_stack = ArrayStack()
    for i in range(len(exp_lst)):
        if exp_lst[i].isdigit():
            my_stack.push(int(exp_lst[i]))
        elif exp_lst[i] in var_dict:
            my_stack.push(var_dict[exp_lst[i]])
        else:
            num1 = my_stack.pop()
            num2 = my_stack.pop()
            if exp_lst[i] == '+':
                my_stack.push(num2 + num1)
            elif exp_lst[i] == '-':
                my_stack.push(num2 - num1)
            elif exp_lst[i] == '/':
                my_stack.push(num2 / num1)
            elif exp_lst[i] == '*':
                my_stack.push(num2 * num1)
    return my_stack.pop()


def main():
    helper()


main()
