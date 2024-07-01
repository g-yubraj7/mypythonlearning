fruits = []
total_fruits = int(input("How many fruits do you want to add?: "))

for i in range(1, total_fruits+1):
    fruit = input(f"Enter fruit {i}: ")
    fruits.append(fruit)


print("The fruits you added are as below;")
for fruit in fruits:
    print(fruit)
    print("---------------------")