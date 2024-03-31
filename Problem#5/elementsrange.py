'''
Name: Wyatt Fulton
Lab Time: Thur 2:00 PM
'''
def filter_and_print_range(input_list, min_val, max_val):
    out_list = []
    for i in range(0, len(input_list), 1):
        if int(input_list[i]) >= int(min_val):
            if int(input_list[i]) <= int(max_val):
                out_list.append(str(input_list[i]))
            else:
                arbitrary = 0    
        else:
            arbitrary = 0
    print(',' .join(out_list)+',',end='')
    return

if __name__ == '__main__':
    int_input = input("Enter a space-separated string of numbers: ")
    integer_list = int_input.split()
    

    range_input = input("Enter the min and max values separated by a space: ")
    range_input = range_input.split()
    min_value = range_input[0]
    max_value = range_input[1]

    filter_and_print_range(integer_list, min_value, max_value)
