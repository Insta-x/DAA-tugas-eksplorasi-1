import sys, threading
import time
from util import file_to_list
from memory_profiler import memory_usage
from two_pivot_block_quicksort import two_pivot_block_quicksort
from mergesort import merge_sort


def profile_sort(sort_func, A):
    memory_usages = memory_usage((time_profile_sort, (sort_func, A)), max_iterations=1)
    print(f'{max(memory_usages)} MB')


def time_profile_sort(sort_func, A):
    start_time = time.time()
    sort_func(A)
    end_time = time.time()
    print(f'{(end_time - start_time) * 1000} ms')


def main():
    types = ['random', 'sorted', 'reversed']
    sizes = ['small', 'medium', 'large']
    datasets = {}
    
    for type in types:
        for size in sizes:
            datasets[f'{size}_{type}'] = file_to_list(f'./datasets/{size}_{type}.txt')
    
    for size in sizes:
        for type in types:
            print(f'Two Pivot Block Quicksort sorting {size}_{type}')
            profile_sort(two_pivot_block_quicksort, datasets[f'{size}_{type}'][:])
            print(f'Mergesort sorting {size}_{type}')
            profile_sort(merge_sort, datasets[f'{size}_{type}'][:])


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(2**27)
    thread = threading.Thread(target=main)
    thread.start()
