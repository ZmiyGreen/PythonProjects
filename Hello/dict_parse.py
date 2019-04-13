def dict_parse(keys_list: list, values_list: list) -> dict:
    """
    Есть два списка разной длины. В первом содержатся ключи, а во втором —
    значения. Напишите функцию, которая создает из этих ключей и значений словарь.
    Если какому-то ключу не хватило значения, в словаре должно быть значение None.
    Значения, которым не хватило ключей, нужно игнорировать.
    :param keys_list: список, содержащий ключи
    :param values_list: список, содержащий значения
    :return: словарь, созданный на основе списка ключей и списка значений
    """
    return {value: values_list[key] if key < len(values_list) else None for key, value in enumerate(keys_list)}


def other_dict_parse(keys_list: list, values_list: list) -> dict:
    if len(keys_list) <= len(values_list):
        return {key: value for key, value in zip(keys_list, values_list)}
    else:
        return {**{key: value for key, value in zip(keys_list, values_list)},
                **{i: None for i in keys_list[len(values_list):]}}
        # return {**temp, **{i: None for i in keys_list[len(temp):]}}
        # for i in range(len(temp), len(keys_list)):
        #    temp[keys_list[i]] = None
        # return temp


if __name__ == '__main__':
    dogs = ["Бигль", "Овчарка", "Корг", "Джек расел", "Хаски"]
    rating = [43, 51, 32]
    result = other_dict_parse(dogs, rating)
    print(result)