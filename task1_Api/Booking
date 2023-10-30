import requests
import json


# Класс для бронирования - каждый метод соответствующий вопрос
class Booking:
    def __init__(self, id='-1', firstname='Jim', lastname='Brown', total_price=111, deposit_paid='true',
                 chekin='2018-01-01', chekout='2019-01-01', additional_needs='Breakfast'):
        self.id = id
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
        self.id = result.json()['bookingid']
        return result.content

    # Обновляю даты бронирование через полное изменение (см сайт)
    def update_date(self, new_chekin, new_chekout):
        if self.id == -1:
            result = 'Вы ещё не забронировали номер или уже удалили бронь'
        else:
            self.chekin = new_chekin
            self.chekout = new_chekout
            result = requests.put('https://restful-booker.herokuapp.com/booking/' + str(self.id),
                                  headers={'Content-Type': 'application/json', 'Accept': 'application/json',
                                          'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='}, data=self.make_json())
        return result.content

    # Беру информацию с сайта
    def get(self):
        if self.id == -1:
            result = 'Вы ещё не забронировали номер или уже удалили бронь'
        else:
            result = requests.get('https://restful-booker.herokuapp.com/booking/' + str(self.id)).content
        return result

    # Удаляю бронирование с сайта
    def delete(self):
        if self.id == -1:
            result = 'Вы ещё не забронировали номер или уже удалили бронь'
        else:
            result = requests.delete('https://restful-booker.herokuapp.com/booking/' + str(self.id),
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='})
            # Не меняю id на -1 чтобы после использования get возвращалось "Not found" (значит запись удалена)
            # self.id = -1
        return result
