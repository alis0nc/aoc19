import sys

def fuel_required(mass):
    return mass // 3 - 2

if __name__ == '__main__':
    result = 0
    with open(sys.argv[1] ,'rt') as f:
        for line in f:
            result += fuel_required(int(line))
    print(result)