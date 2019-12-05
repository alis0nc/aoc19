import sys

def fuel_required(mass):
    return mass // 3 - 2

if __name__ == '__main__':
    result = 0
    with open(sys.argv[1] ,'rt') as f:
        for line in f:
            fuel = fuel_required(int(line))
            result += fuel
            while fuel > 0:
                fuel = fuel_required(fuel)
                if fuel >= 0: # ignore negative fuel requirements
                    result += fuel
    print(result)