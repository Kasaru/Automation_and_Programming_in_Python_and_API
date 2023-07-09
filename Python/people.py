class Person():
    '''Создание человека'''
    def __init__(self,name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.weight = 50
    def description_person(self):
        '''Получение описания человека'''
        description = f"Нового человека зовут: {self.name} ему {self.age}, его рост {self.height}, его вес {self.weight}"
        print(description)

    def get_weight(self):
        print(f"Вес {self.name}а {self.weight} кг")
    def update_weight(self,kg):
        self.weight = kg
man = Person("Алекс",20,180)
man.update_weight(110)
man.description_person()
man.get_weight()