name = 'Название'
price = "Цена"
quantity = "Количество"
unit = "Ед."

product_list = []

name_list = []
price_list = []
quantity_list = []
unit_list = []

n = int(input("Введите количество товаров: "))

for i in range(1, n + 1):
    name_temp = input("Введите наименование товара: ")
    while True:
        price_temp = input("Введите цену товара, руб.: ")
        if not price_temp.isdigit():
            print("Необходимо ввести число")
        else:
            break
    while True:
        quantity_temp = input("Введите количество товара: ")
        if not quantity_temp.isdigit():
            print("Необходимо ввести число")
        else:
            break
    unit_temp = input("Введите единицу измерения: ")
    product_list.append((i, {name: name_temp, price: int(price_temp), quantity: int(quantity_temp), unit: unit_temp}))


for j in product_list:
    print(j)

for k in product_list:
    name_list.append(k[1].get(name))
    price_list.append(k[1].get(price))
    quantity_list.append(k[1].get(quantity))
    unit_list.append(k[1].get(unit))

analytics_dict = {name: list(set(name_list)), price: list(set(price_list)),
                  quantity: list(set(quantity_list)), unit: list(set(unit_list))}

print(f"Аналитика:\n{analytics_dict}")

