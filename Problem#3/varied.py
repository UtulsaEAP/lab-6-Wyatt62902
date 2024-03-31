'''
Name: Wyatt Fulton
Lab Time: Thur 6:00PM
'''
def process_input(input_string):
    input_string = input_string.split()
    for i in range(0, len(input_string), 1):
        input_string[i] = float(input_string[i])
    

    # Get max and average
    max_value = max(input_string)
    average_value = sum(input_string) / len(input_string)
    return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)
    print(f'{max_value:.2f} {average_value:.2f}')

    # print(f'Max Value: {max_value:.2f}')
    # print(f'Average Value: {average_value:.2f}')
    
