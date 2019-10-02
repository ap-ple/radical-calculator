while True:
  from math import sqrt
  from os import system
  from stuff import *
  system('cls')
  def findnum():
    x = input("Enter number: √")
    if x.isdigit():
      x = int(x)
      return x
    return "Error: not a valid number"
  print("Square Root Calculator")
  x = findnum()
  if type(x) == str:
    input(x)
  elif sqrt(x) != int(sqrt(x)):
    print("Simplest Radical Form:")
    print(radical(x))
    print("Decimal:")
    input(f"~{sqrt(x)}")
  else:
    input(f"Square Root: {int(sqrt(x))}")