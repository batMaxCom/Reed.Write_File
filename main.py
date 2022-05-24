FILE_NAME = 'recipes.txt'
cook_book = {}


def file_read(file_name: str):
    # cook_book = {}
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            dish = line.strip()
            number_ing = int(file.readline())
            ingredients = []
            for amount_ingredient in range(number_ing):
                ingredients.append(file.readline().strip().split('|'))
                first_recipes_book = []
                for ingredient in ingredients:
                    second_book = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]),
                                   'measure': ingredient[2]}
                    first_recipes_book.append(second_book)
                cook_book.update({dish: first_recipes_book})
            file.readline()
        # print(cook_book)


file_read(FILE_NAME)


# print(cook_book)

def get_shop_list_by_dishes(dishes: list, persons: int):
    need_ingredients = {}
    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish]:
                if ing['ingredient_name'] in need_ingredients:
                   need_ingredients[ing['ingredient_name']]['quantity'] += int(ing['quantity']) * persons
                else:
                   need_ingredients[ing['ingredient_name']] = {'quantity': int(ing['quantity']) * persons, 'measure':ing['measure']}
        else:
            print('Такого блюда нет в меню')
    print(need_ingredients)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)

# Проверить, есть ли блюдо в словаре
# Забрать его ингридиенты
# Проверить есть ли ингридиенты в итоговом словаре
# Если ингридиентов нет в словаре - добавить, если есть - обновить
