from decimal import *
from . import tokenCreator
from . import pTokenCreator
from . import isNumeric
from . import operationsList

def calc(mathExpString = ''): 
  numbers = []
  operations = []
  token = tokenCreator.create(mathExpString)
  pToken = pTokenCreator.create(token)
  print(f'pToken: {pToken}')

  for i in pToken:
    if isNumeric.check(i): numbers.append(i)
    else:
      operations.append(i)
      while len(numbers) >= 2 and len(operations) >= 1:
        numbers.append(operationsList.list[operations.pop()](Decimal(numbers.pop()), Decimal(numbers.pop())))

  return numbers[0]
