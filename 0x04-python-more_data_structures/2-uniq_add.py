#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_set = set()
    total_sum = 0
    for num in my_list:
        if num not in unique_set:
            total_sum += num
            unique_set.add(num)
    return total_sum

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 2, 3, 4, 4, 5]
    result = uniq_add(my_list)
    print(result)
