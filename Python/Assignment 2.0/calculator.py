def calculate(a, b, formula):
  if formula == '+':
    return a + b
  elif formula == '-':
    return a - b
  elif formula == '*':
    return a * b
  elif formula == '/':
    return a / b
  else:
    print('Please only input from the above mentioned operators.')
    return 'Closing program...'

print('Choose a number')
a = float(input())
print('Choose a second number')
b = float(input())
print('Do you want to * / - or + ?')
formula = input()
answer = calculate(a, b, formula)
print(answer)
