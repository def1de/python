from shopping import Shop
from shopping import Discount

store1 = Shop('rozetka', 'hypermarket', 0, '')

store1.describe_shop()
store1.open_shop()

print('\n')

store2 = Shop('Comfy', 'iTech', 0, '')
store2.describe_shop()

print('\n')

store1.number_of_units = int(input('Enter units >>> '))
store1.describe_shop()
store1.open_shop()
store1.set_number_of_units()
store1.incremented = int(input('Enter incremented value of number of units >>> '))
store1.increment_number_of_units()

store_discount = Discount()
store_discount.get_discount_products()
