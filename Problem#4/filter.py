'''
Name: Wyatt Fulton
Lab Time: 2:00 PM
'''
def process_and_print(input_string):
    input_string = input_string.split()
    remove_list = []
    print_string = ''

    for i in range(0, len(input_string), 1):
        if int(input_string[i]) > -1:
            remove_list.append(input_string[i])
        else:
            arbitrary = 1
    for i in range(0, len(remove_list), 1):
        input_string.remove(remove_list[i])
    
    for i in range(0, len(input_string), 1):
        input_string[i] = int(input_string[i])
    input_string.sort()
    input_string.reverse()

    for i in range(0, len(input_string), 1):
        input_string[i] = str(input_string[i])   



    for i in range(0, len(input_string), 1):
        print_string = print_string + input_string[i] + ' '
    print(print_string, end='')
    return
    
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
