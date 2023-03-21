#include <iostream>
#include <cstdio>

#define TAPE_SIZE 30000

int main(int argc, char** argv) {
  // Check if a BrainFuck program was provided as an argument
  if (argc < 2) {
    std::cout << "Error: no BrainFuck program provided" << std::endl;
    return 1;
  }

  // Read the BrainFuck program from the command line argument
  char* program = argv[1];

  // Initialize the memory tape and pointer
  unsigned char tape[TAPE_SIZE] = {0};
  unsigned char* ptr = tape;

  // Iterate through the program and execute the commands
  for (int i = 0; program[i] != '\0'; i++) {
    switch (program[i]) {
      case '>':
        ptr++;
        break;
      case '<':
        ptr--;
        break;
      case '+':
        (*ptr)++;
        break;
      case '-':
        (*ptr)--;
        break;
      case '.':
        std::putchar(*ptr);
        break;
      case ',':
        *ptr = std::getchar();
        break;
      case '[':
        if (*ptr == 0) {
          int brackets = 1;
          while (brackets > 0) {
            i++;
            if (program[i] == '[') brackets++;
            if (program[i] == ']') brackets--;
          }
        }
        break;
      case ']':
        if (*ptr != 0) {
          int brackets = 1;
          while (brackets > 0) {
            i--;
            if (program[i] == '[') brackets--;
            if (program[i] == ']') brackets++;
          }
        }
        break;
    }
  }

  return 0;
}
