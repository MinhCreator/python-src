# recipe Un = U(n-1) + d with n >= 2

def sequence(n: int, d: int, num_range: int) -> int:

    """
    Generates a sequence of numbers starting from n and incrementing by d.

    Args:
        n (int): The starting number of the sequence.
        d (int): The increment value.
        num_range (int): The length of the sequence to generate.

    Returns:
        list: The generated sequence of numbers.
    """ 
    sequence = [0] * num_range
    sequence[0] = n
    if n < 2: 
        return "n is invalid"

    else:
        for i in range(1, num_range):

            sequence[i] = sequence[i - 1] + d

            if sequence[i] not in sequence:
                 sequence.append(sequence[i])


    return sequence


print(sequence(2, 3, 5))
