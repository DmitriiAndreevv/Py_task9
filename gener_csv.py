import csv
from random import randint


def gen_csv(file_name, rows_count, rand_start, rand_end, nums_count):
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['num_1', 'num_2', 'num_3'])
        for _ in range(rows_count):
            row = [randint(rand_start, rand_end) for _ in range(nums_count)]
            writer.writerow(row)

gen_csv('nums.csv', 80, 0, 1, 100)
