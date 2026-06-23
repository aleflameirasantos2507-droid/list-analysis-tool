numbers = []

while True:
    number = int(input('Enter a number: '))
    numbers.append(number)

    response = input('Would you like to continue? ').strip().upper()

    if response == 'N':
        print(f'Your list contains {len(numbers)} numbers.')

        numbers.sort(reverse=True)
        print(numbers)

        if 5 in numbers:
            print('The value 5 is part of the list!')
        else:
            print('The value 5 is NOT part of the list!')

        break
