from memory_profiler import memory_usage
from util import file_to_list


def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left_A = A[:mid]
        right_A = A[mid:]

        merge_sort(left_A)
        merge_sort(right_A)

        i = j = k = 0

        while i < len(left_A) and j < len(right_A):
            if left_A[i] < right_A[j]:
                A[k] = left_A[i]
                i += 1
            else:
                A[k] = right_A[j]
                j += 1
            k += 1

        while i < len(left_A):
            A[k] = left_A[i]
            i += 1
            k += 1

        while j < len(right_A):
            A[k] = right_A[j]
            j += 1
            k += 1


def main():
    # A = file_to_list('./datasets/small_random.txt')
    A = [23, 13, 2, 4, 1, -10, 0, 29, 3, 3, 89, 2, 1, 2, 0, 3, 3, 2, 9, 32, 89, 12]
    merge_sort(A)
    assert A == sorted(A)
    print('DONE')


if __name__ == "__main__":
    main()
