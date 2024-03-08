'''
Name: Wyatt Fulton
Lab Time: Thu 2:00 PM
'''
def process_user_contacts(user_input):
    phone_book = {}
    current_contact = []
    user_input = user_input.split()
   
    for i in range(0, len(user_input), 1):
        current_contact = user_input[i].split(',')
        phone_book.update({current_contact[0] : current_contact[1]})
    contact_name = input("Enter the contact name: ")
    print(phone_book.get(contact_name))
    
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
