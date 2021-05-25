def count_prime_nums(number_from: int, number_to: int) -> int:
    count = 0 if number_from > 1 else 1
    prime_numbers = [True] * (number_to + 1)
    for i in range(2, number_to + 1):
        if prime_numbers[i]:
            if i > number_from:
                count += 1
            for j in range(i * 2, number_to + 1, i):
                prime_numbers[j] = False
    return count


if __name__ == '__main__':
    print(count_prime_nums(10, 100))
