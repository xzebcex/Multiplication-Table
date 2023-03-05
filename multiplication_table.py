# Multiplication Table


print('  |  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20')
print('--+------------------------------------------------------------------------------------')

# Display each row of product
for number1 in range(0, 21):
    # print the vertical numbers label
    print(str(number1).rjust(2), end='|')

    # Calculate the product and display it
    for number2 in range(0, 21):
        # Print the product followed by a space
        product = number1 * number2
        print(str(product).rjust(3), end=' ')
    print()
