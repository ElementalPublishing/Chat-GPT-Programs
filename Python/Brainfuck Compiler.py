import sys

TAPE_SIZE = 30000

def main():
  # Check if a BrainFuck program was provided as an argument
  if len(sys.argv) < 2:
    print("Error: no BrainFuck program provided")
    return

  # Read the BrainFuck program from the command line argument
  program = sys.argv[1]

  # Initialize the memory tape and pointer
  tape = [0] * TAPE_SIZE
  ptr = 0

  # Iterate through the program and execute the commands
  i = 0
  while i < len(program):
    c = program[i]
    if c == '>':
      ptr = (ptr + 1) % TAPE_SIZE
    elif c == '<':
      ptr = (ptr + TAPE_SIZE - 1) % TAPE_SIZE
    elif c == '+':
      tape[ptr] += 1
    elif c == '-':
      tape[ptr] -= 1
    elif c == '.':
      print(chr(tape[ptr]), end='')
    elif c == ',':
      tape[ptr] = ord(input())
    elif c == '[':
      if tape[ptr] == 0:
        brackets = 1
        while brackets > 0:
          i += 1
          if program[i] == '[':
            brackets += 1
          elif program[i] == ']':
            brackets -= 1
    elif c == ']':
      if tape[ptr] != 0:
        brackets = 1
        while brackets > 0:
          i -= 1
          if program[i] == '[':
            brackets -= 1
          elif program[i] == ']':
            brackets += 1
    i += 1

if __name__ == "__main__":
  main()