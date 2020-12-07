from test_framework import generic_test

# Explaination: For each bit, must multiply itself by that bit's place value
# ex. 0b1 = x1 0b10 = x2,  0b100 = x4  0b1000 = x8
# so  0b1011 = (x)*(x*x)*(x*x*x*x*x*x*x*x)
# Time: O(n) where n is # of bits
# Implement without ** operator
def power(x: float, y: int) -> float:
    result, power = 1.0, y
    if y < 0:
        power, x = -y, 1.0 / x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result

if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
