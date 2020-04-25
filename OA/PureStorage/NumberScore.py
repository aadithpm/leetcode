def get_five_score(number):
    score = 0
    
    # Consecutive 5s
    for idx in range(len(number) - 1):
        if number[idx] == '5' and number[idx + 1] == '5':
            score += 3

    return score

def get_sequence_score(number):
    orig_number = number
    score = 0
    digits = []
    sequence = []

    number = int(number[::-1])
    while number > 0:
        digits.append(number % 10)
        number = number // 10

    # Add zeroes at the tail of number
    while len(digits) < len(orig_number):
        digits.append(0)

    sequence.append(digits[0])
    for idx in range(1, len(digits)):
        if digits[idx] == digits[idx - 1] - 1:
            sequence.append(digits[idx])
        else:
            score += (len(sequence) * len(sequence))
            sequence = [digits[idx]]

    if len(sequence) > 1:
        score += (len(sequence) * len(sequence))
    else:
        score += 1

    return score

def compute_number_score(number):
    score = 0
    digits = [int(i) for i in str(number)]
    
    # Even
    score += len([i for i in digits if i % 2 == 0 or i == 0]) * 4

    # Multiple of 3
    if number % 3 == 0:
        score += 2
    
    # Seven
    score += len([i for i in digits if i == 7])

    # Five
    score += get_five_score(str(number))

    # Sequence
    score += get_sequence_score(str(number))

    return score
