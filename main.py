FILE_NAME = 'recipes.txt'


def file_read(file_name: str):
    cook_book = {}
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            dish = line.strip()
            number_ing = int(file.readline())
            ingridients = []
            for amount_ingridient in range(number_ing):
                ingridients.append(file.readline().strip().split('|'))
                first_recipes_book = []
                for ingridient in ingridients:
                    second_book = {'ingredient_name': ingridient[0], 'quantity': ingridient[1], 'measure': ingridient[2]}
                    first_recipes_book.append(second_book)
                cook_book.update({dish: first_recipes_book})
            file.readline()


        print(cook_book)

file_read(FILE_NAME)
