# Welcome platform
import sys
import pyfiglet 
from basic import arithmetic_eval
from powers import powers_eval


def main():
    problem = input("Enter your math problem: ")
    # answer = 


def function_selector():
    print("""
        Select a number from the following options:

        --- Core Mathematical Functions ---
        1. Basic Arithmetic: Standard operations including addition, subtraction, multiplication, division.
        2. Powers & Roots: Square, cube, and x-th power of y; square root, cube root, and x-th root.
        3. Logarithms: Common logarithms (log), natural logarithms (ln), and 10^x or e^x exponential functions.

        --- Advanced Mathematical Functions ---
        4. Trigonometry: Sine, cosine, tangent, their inverses, and hyperbolic functions.
        5. Probability: Permutations (nPr), combinations (nCr), factorials (n!), and random number generation (including dice, coin, and integer simulations).
        6. Statistics: Single and two-variable statistics, including mean, standard deviation, and regression models (linear, quadratic, exponential, logarithmic).
        7. N-Base Number Systems: Support for Binary, Pentals, Octal, Decimal, and Hexadecimal operations.
        """)
    selection = input("Choose a function to run: ")
    
    
    # if selection == '1':
    #     from basic import main as basic_main
    #     basic_main()
    # elif selection == '2':
    #     from powers import main as powers_main
    #     powers_main()




if __name__ == "__main__":
    function_selector()