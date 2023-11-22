
##---------------------------------- Задание 1 --------------------------------------------
cook_book = {}

with open('recipes.txt', encoding='UTF8' ) as file:

    for line in file:
        dish = line.rstrip()    #забираем азвание блюда
        cook_book_ingredient = []
        ingr_list = {}
        ingr_qnt = int(file.readline().rstrip())    #забираем кол-во ингрдиентов

        for i in range(ingr_qnt):   #вложенный цикл по ингридиентам
            ingr_list = {}
            ingredient_name,quantity,measure = file.readline().rstrip().split(' | ')    #расщепляем файл и записываем в словарь
            ingr_list['ingredient_name'] = ingredient_name
            ingr_list['quantity'] = int(quantity)
            ingr_list['measure'] = measure
            cook_book_ingredient.append(ingr_list)


        (file.readline().rstrip())
        cook_book[dish] = cook_book_ingredient  #записываем в словарь

##---------------------------------- Задание 2 --------------------------------------------

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for i in dishes:  ## цикл по блюдам
        if cook_book.get(i) is None:   ## проверка на наличие такого блюда
            continue
        else:
            ingredients_list = cook_book.get(i)
            for x in ingredients_list: ## цикл по ингридиентам
                dict_inside = {}

                if x['ingredient_name'] in shop_list:      ## проверка на наличие уже такого ингридиента и добавление, если есть
                    dict_inside['measure'] = x['measure']
                    dict_inside['quantity'] = shop_list.get(x['ingredient_name']).get('quantity') + x['quantity'] * person_count
                    shop_list[x['ingredient_name']] = dict_inside
                                                            ## просто добавление, если такого ингридиента нет
                else:
                    dict_inside['measure'] = x['measure']
                    dict_inside['quantity'] = x['quantity']*person_count
                    shop_list[x['ingredient_name']] = dict_inside
    print(shop_list)

get_shop_list_by_dishes(['Фахитос','Омлет'],2)  ## собственно тест вызова функции




