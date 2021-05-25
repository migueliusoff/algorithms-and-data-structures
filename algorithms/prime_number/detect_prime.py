import math


def is_prime(number: int) -> bool:
    prime = True
    for i in range(2, int(round(math.sqrt(number + 0.5))) + 1):
        if number % i == 0:
            prime = False
            break
    return prime


if __name__ == '__main__':
    print(is_prime(18014398241046527))
