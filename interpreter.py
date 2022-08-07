from parser import Parser
from run import Run

vars = []

print("Welcome to the DylanScript interpreter (v0.0.1)")

while True:
  line_of_code = input(" -> ")
  tokens = Parser(line_of_code).tokens
  print(tokens)
  #Run(tokens)