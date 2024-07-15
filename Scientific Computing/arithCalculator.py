def arithmetic_arranger(problems, show_answers=False):

    return problems



def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid problem format.'

        operand1, operator, operand2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not operand1.isdigit() or not operand2.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        result = None
        if operator == '+':
            result = str(int(operand1) + int(operand2))
        elif operator == '-':
            result = str(int(operand1) - int(operand2))

        width = max(len(operand1), len(operand2)) + 2
        first_line.append(operand1.rjust(width))
        second_line.append(operator + operand2.rjust(width - 1))
        dashes_line.append('-' * width)
        answers_line.append(result.rjust(width))

    arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dashes_line)
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers_line)

    return arranged_problems

# Test the function
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
