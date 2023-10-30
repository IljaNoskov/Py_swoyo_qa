import Booking


def work_with_booking(booking):
    # О вариативности действий
    print('Select the action you want with the reservation')
    print('1 - create a new booking')
    print('2 - get information about an already created reservation')
    print('3 - change booking dates')
    print('4 - delete a reservation')
    print('5 - terminate the program')
    num = input()
    # в зависимости от цифры отправляю разные запросы
    if num == '1':
        print('1 - Create a reservation with standard data')
        print('2 - Create a reservation with your own data')
        num = input()
        if num == '2':
            my_firstname = input('Enter your first name')
            my_lastname = input('Enter your last name')
            my_total_price = input('Enter the price per room')
            my_deposit_paid = input('Enter the availability of the deposit in the format true or false')
            my_chekin = input('select your chekin date in format "YYYY-MM-DD": ')
            my_chekout = input('select your chekout date in format "YYYY-MM-DD": ')
            my_additional_needs = input('Enter your other needs: ')
            booking = Booking.Booking(-1, my_firstname, my_lastname, my_total_price, my_deposit_paid, my_chekin,
                                      my_chekout, my_additional_needs)
        elif num != '1':
            print('Incorrect input')
        print('Reservation creation report')
        print(booking.create())
    elif num == '2':
        print('Your booking report')
        print(booking.get())
    elif num == '3':
        chekin = input('select your chekin date in format "YYYY-MM-DD": ')
        chekout = input('select your chekout date in format "YYYY-MM-DD": ')
        print('Date update eeport')
        print(booking.update_date(chekin, chekout))
    elif num == '4':
        print('Delete report')
        print(booking.delete())
    elif num == '5':
        return 0
    else:
        print('Incorrect input')
    print()


if __name__ == '__main__':
    # Запускаю в вечном цикле работу с бронированием
    my_booking = Booking.Booking()
    while True:
        if work_with_booking(my_booking) == 0:
            break
