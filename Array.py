import collections


# Given an integer array, output all unique pairs that sum up to value k
def pair_sum(arr, k):

    if len(arr) < 2:
        return False

    seen = set()
    output = set()

    for num in arr:
        partner = k-num

        if partner not in seen:
            seen.add(num)

        else:
            output.add((min(num, partner), max(num, partner)))

    return output


# Find the missing element in the second array. Second array is the shuffled first array
def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for i in range(len(arr1)-1):
        if arr1[i] != arr2[i]:
            return arr1[i]

    return arr1[-1]


def finder_hash(arr1, arr2):
    d = collections.defaultdict(int)
    for num in arr2:
        d[num] += 1
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


# Return the largest continuous sum of an array
def LCS(arr):

    if len(arr) == 0:
        return 0

    max_sum = cur_sum = arr[0]
    for num in arr[1:]:
        cur_sum = max(cur_sum+num, num)
        max_sum = max(max_sum, cur_sum)
    return max_sum
