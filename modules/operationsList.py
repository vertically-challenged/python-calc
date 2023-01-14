from .mathOperations import addition
from .mathOperations import division
from .mathOperations import exponentiation
from .mathOperations import multiplication
from .mathOperations import percent
from .mathOperations import subtraction

list = {
  '+': addition.calculate, 
  '-': subtraction.calculate, 
  '*': multiplication.calculate, 
  '/': division.calculate, 
  '^': exponentiation.calculate,
  '%': percent.calculate, 
}