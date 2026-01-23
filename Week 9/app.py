from core.parser import tokenize, to_rpn
from core.evaluator import evaluate_rpn


from utils.errors import CalculatorError

def main():
    expr = input("Enter expression: ")
    try:
        tokens = tokenize(expr)
        rpn = to_rpn(tokens)
        result = evaluate_rpn(rpn)
        print(result)
    except CalculatorError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
