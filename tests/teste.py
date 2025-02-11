def fuzz_sum_number(target):
    result = 0
    for i in range(target):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

print(fuzz_sum_number(10))