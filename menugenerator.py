import random

sides = ["mashed potatoes", "spinach", "broccoli", "carrots", "corn salad", "chicken salad", "clam chowder", "french fries"]
main_course = ["grilled chicken", "hamburger", "cheese burger", "pizza", "chicken marsala", "macaroni & cheese", "spaghetti"]
dessert = ["ice cream", "pudding", "cake", "cookies", "brownies", "cupcakes", "chocolate moose"]

random_num1 = random.randint(0,7)
random_num2 = random.randint(0,6)

print (sides[random_num1])
print (main_course [random_num2])
print (dessert [random_num2])
