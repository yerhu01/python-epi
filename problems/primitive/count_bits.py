from test_framework import generic_test

# Count the number of bits set to 1

# O(n) where n is number of bits to represent x
def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

def main():
    print(count_bits(0b10110))
    print(count_bits(0x12A))
        #0001 0010 1010
    print(count_bits(100))
        #100 = 0b1100100

if __name__ == '__main__':
    main()
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
