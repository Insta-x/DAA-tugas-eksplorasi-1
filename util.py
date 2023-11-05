def list_to_file(file_path, A):
    with open(file_path, 'w') as f:
        for x in A:
            f.write(f'{x}\n')


def file_to_list(file_path):
    with open(file_path, 'r') as f:
        A = [int(line.strip()) for line in f]
    return A