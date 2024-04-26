for number in [1, 0, -1]:
    try:
        if number < 0:
            raise ValueError(f'no negatives: {number}')
        print(number)
    except ValueError as error:
        print(f'exception: {error}')
