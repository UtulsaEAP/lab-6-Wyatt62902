'''
Name: Wyatt Fulton
Lab Time: 2:00 PM
'''
def check_palindrome(user_input):
 inv_input = user_input[::-1]
 if inv_input == user_input:
    print("palindrome: "+user_input)
 else:
    print("not a palindrome: "+user_input)
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
