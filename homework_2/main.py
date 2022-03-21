def generate_Kaprekar(end):
    # iterate
    for i in range(end - 1):
        # get the square
        sqr = i ** 2
        digits = str(sqr) 

        # and get the num of its digits
        length = len(digits)
        split = int(length/2)

        while length > 1:
            # split the squares into two halves
            left = int(digits[:split])
            right = int(digits[split:])

            # add the two halves to see if their sum is equal to the original number
            if (left + right) == i:
                print("Number: " + str(i) + " Square: " + str(sqr))
            break

if __name__ == '__main__':
    generate_Kaprekar(10000)

