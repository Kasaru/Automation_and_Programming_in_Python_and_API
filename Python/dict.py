# список
family_1 = ["Alex", "Olga", "Semen", "Alex"]
print(family_1)
# множество - использование только одиночных значений
family_2 = {"Alex", "Olga", "Semen", "Alex", "alex"}
print(family_2)
# словарь
family_3 = {"Папа":"Alex", "Мама":"Olga", "Сын":"Semen", "Дочь":"Nastya"}
print(family_3["Папа"])
for k, v in family_3.items():
    print(k)