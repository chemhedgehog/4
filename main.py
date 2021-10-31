def find(nums):

    missed = []

    for i im range(1, len(nums)):
        if i not in nums:
            missed.append(i)

    returned missed 