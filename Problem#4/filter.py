'''
Name: Wyatt Fulton
Lab Time: 2:00 PM
'''
def process_and_print(input_string):
    input_string = input_string.split()
    print(len(input_string))
    remove_list = []

    for i in range(0, len(input_string), 1):
        if int(input_string[i]) > -1:
            remove_list.append(input_string[i])
            print(i)
        else:
            arbitrary = 1
    for i in range(0, len(remove_list), 1):
        input_string.remove(remove_list[i])
    
    input_string.sort()
    input_string.reverse()
    print(*input_string)

    return
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
