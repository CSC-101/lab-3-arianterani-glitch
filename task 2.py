def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body. Total: 4, 13, 15, 16
    return total

result = tally([4, 9, 2, 1])          # result = 16

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body.
        # 1) new_list: [4], idx: 0   2) new_list: [4, 9], idx: 1   3) new_list: [4, 9, 2], idx: 2   4) new_list: [4, 9, 2, 1], idx: 3
    return new_list                    # How does this loop differ from that above? The first code adds together the values
# of the integers within the list, while this code creates a copy of a list by calling the values within the original list
# and appending them by going through each of the indexes in the for loop until there are no more integers to append.

result = copy([4, 9, 2, 1])

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body.
        # 1) new_list[5]  2) new_list[5, 10]  3) new_list[5, 10, 3]  4) new_list[5, 10, 3, 2]
    return new_list

result = increment_all([4, 9, 2, 1])