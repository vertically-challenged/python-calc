from . import isNumeric

def create(string = ''):
  token = []
  currentNumber = ''
  split = list(string)

  for i in split: 
    if isNumeric.check(i) or i == '.': currentNumber += i
    elif (i == '-' and currentNumber == '') and (len(token) == 0 or token[len(token)-1] == '('):
      token.append('0')
      token.append(i)
    else: 
      if i != '(' and currentNumber != '': token.append(currentNumber)
      token.append(i)
      currentNumber = ''
  
  if currentNumber != '': token.append(currentNumber)

  return token

