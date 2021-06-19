import sys
import math

def main(argv):
    n = int(argv[0])
    m = int(argv[1])
    if 2**n > math.factorial(m):
        print("Exponential")
    else:
        print("Factorial")

if __name__ == '__main__':
    main(sys.argv[1:])
