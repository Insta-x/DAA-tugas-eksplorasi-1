import sys
import threading
from memory_profiler import memory_usage
from util import file_to_list


BLOCK_SIZE = 64


def two_pivot_block_quicksort(A):
    stack = [(0, len(A) - 1)]
    
    while len(stack) > 0:
        left, right = stack.pop()
    
        if right - left > 0:
            i, j = block_lomuto_2_pivot(A, left, right)
            
            stack.append((left, i-1))
            if A[i] != A[j]:
                stack.append((i+1, j-1))
            stack.append((j+1, right))


def block_lomuto_2_pivot(A, left, right):
    A[left], A[right] = min(A[left], A[right]), max(A[left], A[right])
    p, q = A[left], A[right]
    block = [0] * BLOCK_SIZE
    i = j = k = left + 1
    num_p = num_q = 0
    
    while k < right:
        t = min(BLOCK_SIZE, right - k)
        for c in range(t):
            block[num_q] = c
            num_q += q >= A[k+c]
        for c in range(num_q):
            A[j+c], A[k+block[c]] = A[k+block[c]], A[j+c]
        k += t
        for c in range(num_q):
            block[num_p] = c
            num_p += p > A[j+c]
        for c in range(num_p):
            A[i], A[j+block[c]] = A[j+block[c]], A[i]
            i += 1
        j += num_q
        num_p = num_q = 0
    
    A[i-1], A[left] = A[left], A[i-1]
    A[j], A[right] = A[right], A[j]
    return (i-1, j)


def main():
    # A = file_to_list('./datasets/large_sorted.txt')
    A = [23, 13, 2, 4, 1, -10, 0, 29, 3, 3, 89, 2, 1, 2, 0, 3, 3, 2, 9, 32, 89, 12]
    two_pivot_block_quicksort(A)
    assert A == sorted(A)
    print('DONE')


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(2**27)
    thread = threading.Thread(target=main)
    thread.start()