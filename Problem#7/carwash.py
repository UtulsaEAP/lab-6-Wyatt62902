'''
Name: Wyatt Fulton
Lab Time: Thur 2:00 PM
'''
def calculate_car_wash_price(service_choice1, service_choice2):
    services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
    base_wash = 10
    total = 0
    serv1_price = 0
    serv2_price = 0
    print('ZyCar Wash\nBase car wash - $10')
    if service_choice1 in services.keys():
        serv1_price = services.get(service_choice1)
        print(service_choice1+' - $'+str(serv1_price))
    if service_choice2 in services.keys():
        serv2_price = services.get(service_choice2)
        print(service_choice2+' - $'+str(serv2_price))
    else:
        arbitrary = 0
    total = 10 + serv1_price + serv2_price
    print('-----')
    print('Total price: $'+str(total))
    
        



    
if __name__ == '__main__':
    # Get user input for service choices
    service_choice1 = input("Enter first service choice: ")
    service_choice2 = input("Enter second service choice: ")

    # Call the function to calculate car wash price
    calculate_car_wash_price(service_choice1, service_choice2)
