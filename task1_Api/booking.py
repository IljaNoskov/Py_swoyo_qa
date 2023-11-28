import requests
import json


# Класс для бронирования - каждый метод соответствующий вопрос
class Booking:
    def __init__(self, booking_id='-1', firstname='Jim', lastname='Brown', total_price=111, deposit_paid='true',
                 chekin='2018-01-01', chekout='2019-01-01', additional_needs='Breakfast'):
        self.booking_id = booking_id
        self.firstname = firstname
        self.lastname = lastname
        self.total_price = total_price
        self.deposit_paid = deposit_paid
        self.chekin = chekin
        self.chekout = chekout
        self.additional_needs = additional_needs

    # Создаю json из данных класса
    def make_json(self):
        new_dict = {"firstname": self.firstname, "lastname": self.lastname,
                    "totalprice": self.total_price, "depositpaid": self.deposit_paid,
                    "bookingdates": {"checkin": self.chekin, "checkout": self.chekout},
                     "additionalneeds": self.additional_needs}
        result = json.dumps(new_dict)
        return result

    # отправляю post запрос чтобы создать бронирование на сайте
    def create(self):
        result = requests.post('https://restful-booker.herokuapp.com/booking',
                               headers={'Content-Type': 'application/json'}, data=self.make_json())
        self.booking_id = result.json()['bookingid']
        if result.status_code != 200:
            return 'error with post'
        return result.content

    # Обновляю даты бронирование через полное изменение (см сайт)
    def update_date(self, new_chekin, new_chekout):
        if self.booking_id == -1:
            result = 'Вы ещё не забронировали номер или уже удалили бронь'
        else:
            self.chekin = new_chekin
            self.chekout = new_chekout
            result = requests.put('https://restful-booker.herokuapp.com/booking/' + str(self.booking_id),
                                  headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                          'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='}, data=self.make_json())
        if result.status_code != 200:
            return 'error with put'
        return result.content

    # Беру информацию с сайта
    def get(self):
        if self.booking_id == -1:
            result = 'Вы ещё не забронировали номер или уже удалили бронь'
        else:
            result = requests.get('https://restful-booker.herokuapp.com/booking/' + str(self.booking_id))
            if result.status_code != 200:
                return 'error with get'
        return result.content

    # Удаляю бронирование с сайта
    def delete(self):
        if self.booking_id == -1:
            result = 'Вы ещё не забронировали номер или уже удалили бронь'
        else:
            result = requests.delete('https://restful-booker.herokuapp.com/booking/' + str(self.booking_id),
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='})
            if result.status_code != 201:
                return 'error with delete'
            elif self.get() != 'error with get':
                return 'error: find booking after delete'
            else:
                self.id = -1
        return result
