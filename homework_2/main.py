def generate_Kaprekar(end):
    for i in range(end + 1):
        sqr = i ** 2
        digits = str(sqr)

        length = len(digits)
        split = int(length/2)

        while length > 1:
            left = int(digits[:split])
            right = int(digits[split:])
            if (left + right) == i:
                print("Number: " + str(i) + " Square: " + str(sqr))
            break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_Kaprekar(10000)

