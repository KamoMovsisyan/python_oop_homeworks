#1
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def presentation(self):
        return f"Person's name is {self.name}, surname {self.surname} and he is {self.age} years old"

class Student(Person):
    def __init__(self,student_name, student_surname, student_age):
        super().__init__(student_name, student_surname, student_age)
    
    def presentation_for_student(self):

        return super().presentation().replace("Person's", "Student's")

Kamo = Student('Kamo', 'Movsisyan', 17)

print(Kamo.presentation_for_student())

#2
class Country:
    def __init__(self, name : str, continent : str):
        self.name = name
        self.continent = continent

    def presentation(self):
        return f'{self.name}, {self.continent}'

class Brand:
    def __init__(self, brand_name : str, start_date : int):
        self.brand_name = brand_name
        self.start_date = start_date

    def presentation(self):
        return f"the brand name is {self.brand_name}, it's start in {self.start_date}"

class Season:
    def __init__(self, season_name : str, temperature : int):
        self.season_name = season_name
        self.temeperature = temperature
    
    def presentation(self):
        return f"Season - {self.season_name}, Average Tempereature is {self.temeperature}"

class Product(Country, Brand, Season):
    def __init__(self, product_name, type, price, quantity):
        self.product_name = product_name
        self.type = type
        self.price = price
        self.quantity = quantity
    
    def presentation(self):
        return f"The product's name is {self.product_name}, it's type is {self.type}, it's price is {self.price}, its quantity is {self.quantity}"

    def discount(self, percent):
        self.price = self.price - self.price * percent / 100
        return self.price
    
    def increase_quantity(self):
        self.quantity += 1
        return self.quantity

    def decrease_quantity(self):
        self.quantity -= 1
        return self.quantity

my_product = Product('Shirt', 'Cloth', 1000, 1)

my_product.increase_quantity()
my_product.decrease_quantity()
my_product.discount(10)

print(my_product.presentation())

#3
class Hotel:

    name = 'Lerane'
    place = 'Geghard'
    rooms_mid = {'room_1' : 'free', 'room_2' : 'free', 'room_3' : 'free'}
    mid_room_price = 10000
    rooms_lux = {'room_1' : 'free', 'room_2' : 'free', 'room_3' : 'free'}
    lux_room_price = 20000

    def presentation():
        return f'We have mid rooms and lux rooms, price for mid room is {Hotel.mid_room_price}, price for lux room is {Hotel.lux_room_price}'
    
    def book_room(room_type):
        if room_type == 'mid':
            for key, value in Hotel.rooms_mid.items():
                if value == 'free':
                    Hotel.rooms_mid[key] = 'busy'
                    for value2 in Hotel.rooms_mid.values():
                        if value2 == 'busy':
                            break
                        else:
                            continue
                    return 'you booked mid room'
            else:
                return 'all rooms of this type are busy'
        elif room_type == 'lux':
            for key, value in Hotel.rooms_lux.items():
                if value == 'free':
                    Hotel.rooms_lux[key] = 'busy'
                    for value2 in Hotel.rooms_lux.values():
                        if value2 == 'busy':
                            break
                        else:
                            continue
                    return 'you booked lux room'
            else:
                return 'all rooms of this type are busy'
        else:
            return 'Wrong Input !!! '

    def availible_room_check(room_type):
        if room_type == 'mid':
            for value in Hotel.rooms_mid.values():
                if value == 'free':         
                    ask_to_book = input('There is an availible room, do you want to book it (yes / no) : ')
                    if ask_to_book == 'yes':
                        return Hotel.book_room('mid')
                    else:
                        break
            else:
                return 'All rooms are busy'
        elif room_type == 'lux':
            for value in Hotel.rooms_lux.values():
                if value == 'free':         
                    ask_to_book = input('There is an availible room, do you want to book it (yes / no) : ')
                    if ask_to_book == 'yes':
                        return Hotel.book_room('lux')
                    else:
                        break
            else:
                return 'All rooms are busy'

    def discount(room_type, percent):
        if room_type == 'mid':
            Hotel.mid_room_price = Hotel.mid_room_price - Hotel.mid_room_price * percent / 100
            return Hotel.mid_room_price
        elif room_type == 'lux':
            Hotel.lux_room_price = Hotel.lux_room_price - Hotel.lux_room_price * percent / 100
            return Hotel.lux_room_price
        else:
            return 'Wrong input!!!'

class Taxi:
    taxi_name = 'ride_over'
    car_types = 'bmw'
    price_for_tour = 10000
    
    def presentation():
        return f'We have {Taxi.car_types} and price is {Taxi.price_for_tour}'

    def discount(percent : int):
            Taxi.price_for_tour = Taxi.price_for_tour - Taxi.price_for_tour * percent / 100
            return f'now your taxi price is {Taxi.price_for_tour}'

class Tour(Hotel, Taxi):
    tour_name = 'Geghard Tour'

    def __init__(self):

        self.price_mid = self.mid_room_price + self.price_for_tour
        self.price_lux = self.lux_room_price + self.price_for_tour


    def presentation(self):
        return f'Hello we offer {self.tour_name} we have two options {self.price_mid} and {self.price_lux}, \
            which includes transport with {self.taxi_name} company which provides {self.car_types} cars and price for it is {self.price_for_tour} \
            we will stay at hotel {self.name} which offers two types of rooms middle - {self.mid_room_price} and lux - {self.lux_room_price} '
        

example = Tour()

print(example.presentation())