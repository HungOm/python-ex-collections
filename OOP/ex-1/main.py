from shirt import Shirt

from test import run_tests



shirt_one = Shirt('red','S','long-sleeve',25)


print(shirt_one.price)
shirt_one.change_price(10)
print(shirt_one.price)

# shirt_one.discount(.12)
print(shirt_one.discount(.12))

print("-----------------------------")
shirt_two = Shirt('orange','L','Short-sleeve',10)


total = shirt_one.price + shirt_two.price
print(total)


total_discount = shirt_one.discount(.14) + shirt_two.discount(.6)
print(total_discount)


print(run_tests(shirt_one, shirt_two, total, total_discount))