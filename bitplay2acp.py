def reversebits(n, bit_size=32):
    result = 0
    for i in range(bit_size):
        bit = (n >> i) & 1
        result |= (bit << (bit_size - 1 - i))
    return result
g = int(input("Enter a number to reverse its bits: "))
rev = reversebits(g, 3)

print("The number with its bits reversed is:", bin(rev)[2:])
# The above code reverses the bits of a given number.5
