# QuantumComputingMatrixOperationCLI

🧮 QuantumComputingMatrix  
**Overview**  

QuantumComputingMatrix is a modular Python-based command-line interface (CLI) application designed for performing matrix operations — including addition, subtraction, multiplication, and division — with a focus on extendability for quantum and AI-based matrix computation in future versions.

It includes:  
- A Mini CLI shell for interactive matrix entry and operations  
- Matrix parsing and validation system  
- Custom matrix display for visual representation  
- Support for keyboard input detection (Up/Down navigation)  
- Modular design following software engineering best practices

🚀 Features
- ✅ Matrix input using intuitive string format [r11,r12:r21,r22:...]  
- ✅ CLI that supports command history and variable referencing (var1, var2, …)  
- ✅ Add, subtract, multiply, and divide matrices easily  
- ✅ Detect UP/DOWN arrow keys for history navigation (Windows compatible)  
- ✅ Modular, scalable design ready for future quantum computing integration

🧰 Example Usage

Run the CLI:
```bash

>>> [1,2:3,4]         # Create a matrix (stored as var1)
>>> [5,6:7,8]         # Create another (stored as var2)
>>> var1 + var2       # Add the two matrices
>>> var1 * var2       # Multiply matrices
>>> data              # Show all stored matrices
>>> his               # View command history
>>> exit              # Quit the CLI
Matrix Input Format

Matrix should be entered as:
[row1_elements:row2_elements:row3_elements...]
[1,2,3:4,5,6:7,8,9]
1 2 3
4 5 6
7 8 9
Key Components

MatrixCli → Handles CLI input and command execution

MatrixOperation → Performs all matrix arithmetic

KeyListener → Detects arrow key presses

Matrix_Display → Prints matrix in formatted style

🪄 Future Enhancements

Integrate quantum matrix operations for Qubit simulation

Add complex number support

Implement matrix determinant, inverse, and eigenvalue computation

Enable file I/O for matrix storage and retrieval

💻 Requirements

Python 3.10+

Works on Windows, Linux, and macOS

No external libraries (pure Python implementation)

🧑‍💻 Author
Ghanashyam Dhakal
📧 gdhakal@lakeheadu.ca

🌐 GitHub Profile
python Lib/MatrixMultiplication.py

