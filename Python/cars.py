class Car():
    def __init__(self, model, year, engine_capacity, price, mileage):
        self.model = model
        self.year = year
        self.engine_capacity = engine_capacity
        self.price = price
        self.mileage = mileage
        self.number_of_wheels = 4

    def description_car(self):
        description = f"Модель: {self.model}\nГод выпуска: {self.year}\nОбъем двигателя: {self.engine_capacity}\nЦена: {self.price}\nПробег: {self.mileage}\nКоличество колес: {self.number_of_wheels}\n"
        print(description)

class Truck(Car):
    def __init__(self, model, year, engine_capacity, price, mileage):
        super().__init__(model, year, engine_capacity, price, mileage)
        self.number_of_wheels = 8

car = Car("Octavia",2012,1798,990000,2000)
car.description_car()
truck = Truck("FH", 2012,16080,4649000,1074791)
truck.description_car()