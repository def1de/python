def describe_pet(animal_type, pet_name):
    print(f"\nУ меня есть {animal_type}.")
    print(f"Мой {animal_type} и его зовут {pet_name.title()}.")

type_a = input("Введите вид вашего животного ")
name = input("Введите имя вашего животного ")
describe_pet(type_a, name)

