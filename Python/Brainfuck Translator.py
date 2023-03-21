import sys
import ctypes
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit

# Use a memory-mapped file to store the BrainFuck interpreter's dynamic library.
lib = ctypes.CDLL('brainFuck.dll', mode=ctypes.RTLD_MEMORY)

# Define the function prototype for the interpreter's main function.
lib.brainFuck.argtypes = [ctypes.c_char_p]
lib.brainFuck.restype = ctypes.c_char_p

def execute_brainFuck(program):
    # Call the BrainFuck interpreter's main function and return the output as a string.
    output = lib.brainFuck(program.encode())
    return output.decode()

def encode_input(input_str):
    # Use a lookup table to convert ASCII values to BrainFuck code.
    lookup_table = ['+' * i for i in range(256)]

    # Encode the input string as BrainFuck code using the lookup table.
    output = ''.join(lookup_table[ord(c)] for c in input_str)
    return output

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_widget = QTextEdit(self)
        self.input_widget = QLineEdit(self)
        self.input_widget.returnPressed.connect(self.run_brainFuck)
        self.setCentralWidget(self.text_widget)

    def run_brainFuck(self):
        # Get the input string from the input widget.
        input_str = self.input_widget.text()

        # Encode the input string as BrainFuck code and execute it.
        program = encode_input(input_str)
        output = execute_brainFuck(program)

        # Display the output in the text widget.
        self.text_widget.setPlainText(output)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())