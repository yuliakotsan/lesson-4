def season(number_of_month):
    name_of_season = 'Out of season'
    if number_of_month in range(1, 13):
        a = {
            12: 'winter', 1: 'winter', 2: 'winter',
            3: 'spring', 4: 'spring', 5: 'spring',
            6: 'summer', 7: 'summer', 8: 'summer',
            9: 'autumn', 10: 'autumn', 11: 'autumn',
        }
        name_of_season = a[number_of_month]
    return name_of_season

print(
    season(
        int(
            input('Input number of month: ')
        )
    )
)
