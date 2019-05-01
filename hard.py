#
# hard Lesson_01
#

name, surname, age, weight = input('Ваше имя: '), input('Ваша фамилия: '), int(input('Ваш возраст: ')), int(input('Ваш вес: '))

if age <= 30 and weight > 50 and weight < 120:
    print(name + ' ' + surname + ', хорошее состояние')
elif age > 30 and age < 41 and (weight < 50 or weight > 120):
    print(name + ' ' + surname + ', требуется начать вести правильный образ жизни')
elif age > 40 and (weight < 50 or weight > 120):
    print(name + ' ' + surname + ', требуется врачебный осмотр')
else:
    print(name + ' ' + surname + ', если вы все еще живы - вы сверхчеловек.')
