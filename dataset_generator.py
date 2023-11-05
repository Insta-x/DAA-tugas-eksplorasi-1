from util import list_to_file
from random import randint

def random_numbers(n):
    return [randint(0, n) for _ in range(n)]


def sorted_numbers(n):
    return sorted(random_numbers(n))


def reversed_numbers(n):
    return sorted(random_numbers(n), reverse=True)


def main():
    types = {
        'random' : random_numbers,
        'sorted' : sorted_numbers,
        'reversed' : reversed_numbers,
    }
    sizes = {
        'small' : 1 << 9,
        'medium' : 1 << 13,
        'large' : 1 << 16,
    }
    
    for type in types:
        for size in sizes:
            list_to_file(f'./datasets/{size}_{type}.txt', types[type](sizes[size]))


if __name__ == '__main__':
    main()
    print('Generated datasets')
