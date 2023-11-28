from booking import Booking

print('create new booking')
k = Booking()
print(k.create())
print('\nget info about')
print(k.get())
print('\nupdate date')
print(k.update_date('2022-01-01', '2023-01-01'))
print('\ndelete booking')
print(k.delete())
