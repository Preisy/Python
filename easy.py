# Задание - 1

# name = 'Василий'
# age = 21
# city = 'Москва'
#
#
# def my_func(name, age, city):
#     return f'{name}, {age} год(a), проживает в городе {city}'
#
#
# print(my_func(name, age, city))

# Задание - 2

# def max_int(*args):
#     max = args[0]
#     for i in args:
#         if i > max:
#             max = i
#     return max
#
#
# print(max_int(2, 4, 5, 56, 264, 4))

# Задание - 3

# Первый способ
# print(max('asdf', 'asdf', 'qwe', 'aewwqre', 'adsf', key=len))

def max_str(*args):

    # Второй способ

    # max_arr = [args[0], len(args[0])]
    # args = list(args)
    # for i in args:
    #     if len(i) > max_arr[1]:
    #         max_arr = [i, len(i)]
    # return max_arr[0]

    # Третий способ
    return max(args, key=len)


print(max_str('asdf', 'asdf', 'qwe', 'aewwqre', 'adsf'))
