def is_year_leap(year):
    return True if year % 4 == 0 else False

year = int(input('Введите год '))
result = is_year_leap(year)

print('Год', year ,' : ', result)
