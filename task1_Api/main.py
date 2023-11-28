from booking import Booking


def work_with_booking_list(b_list):
    def work_with_booking(booking):
        # выбор вариативности действий
        print('Select the action you want with the reservation')
        print('1 - create a new booking')
        print('2 - get information about an already created reservation')
        print('3 - change booking dates')
        print('4 - delete a reservation')
        print('5 - terminate the program')
        num = input('your action: ')
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
                booking = Booking(-1, my_firstname, my_lastname, my_total_price, my_deposit_paid, my_chekin,
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
            print('Delete booking')
            print(booking.delete())
        elif num == '5':
            print('stop')
            return 0
        else:
            print('Incorrect input')
        print()

    # Если список не пустой, то предлагаю пользователю выбрать, с каким бронированием он хочет работать
    if len(b_list) > 0:
        for i in range(len(b_list)):
            print(f'booking № {i}: {b_list[i].make_json()}')
            print()
        print(f'chose {len(b_list)} to create new booking')
        n = int(input('Chose your booking number (or -1 to stop:'))
        if n == -1:
            return 0
        elif 0 <= n < len(b_list):
            while True:
                if work_with_booking(b_list[n]) == 0:
                    break
        elif n == len(b_list):
            b = Booking()
            b_list.append(b)
            while True:
                if work_with_booking(b) == 0:
                    break

    else:
        # если список пустой, то создаю новую бронь
        b = Booking()
        b_list.append(b)
        while True:
            if work_with_booking(b) == 0:
                break


if __name__ == '__main__':
    # Запускаю в вечном цикле работу с бронированием
    booking_list = []
    while True:
        print('start work with list')
        if work_with_booking_list(booking_list) == 0:
            break
