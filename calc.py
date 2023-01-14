from modules import calculator

print('To quit, enter \'quit\' or \'q!\' \n')
while True: 
  expression = input('Expression: ')
  if expression == 'q!' or expression == 'quit': break
  print(f'Result: {calculator.calc(expression)}')