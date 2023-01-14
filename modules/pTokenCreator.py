from . import isNumeric
from . import operationPriorities

def create(token):
  pToken = []
  stack = []
  countBracket = 0

  for i in token:
    if isNumeric.check(i): pToken.append(i)
    elif i == '(': 
      stack.append(i)
      countBracket += 1
    elif i == ')':
      while len(stack) > 0 and stack[len(stack)-1] != '(':
        pToken.append(stack.pop())
      if len(stack) > 0: stack.pop()
    else:  
      while len(stack) > 0 and stack[len(stack)-1] != '(' and (operationPriorities.priorities[stack[len(stack)-1]] >= operationPriorities.priorities[i]):
        pToken.append(stack.pop())
      stack.append(i)
  
  while len(stack) > 0: 
    pToken.append(stack.pop())

  return pToken