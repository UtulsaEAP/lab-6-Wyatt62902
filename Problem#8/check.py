def in_order(nums):
    should_be = []
    for i in range(0, len(nums), 1):
        should_be.append(nums[i])
    print(should_be)
    for i in range(0, len(should_be)-1, 1):
        for j in range(0, len(should_be)-1, 1):
            if j > i:
                if should_be[i] > should_be[j]:
                    temp = should_be[i]
                    should_be[i] = should_be[j]
                    should_be[j] = temp
                    print(should_be)
                else:
                    arbitrary = 0
            else:
                arbitrary = 0
    if nums == should_be:
         test = True
    else:
        test = False

                 
            
    return test
    
if __name__ == '__main__':
    nums = input()
    nums = nums.split(',')
    for i in range(0, len(nums), 1):
        nums[i] = nums[i].strip()
    if in_order(nums):
        print('In order')
    else:
        print('Not in order')

