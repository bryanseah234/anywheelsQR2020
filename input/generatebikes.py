with open('bikes.txt', 'w') as f:

    for number in range(1,10000):
        if number < 10:
            number = "000" + str(number)
        elif 9 < number < 100:
            number = "00" + str(number)
        elif 99 < number < 1000:
            number = "0" + str(number)
        elif 999 < number < 10000:
            number = str(number)
        bike = "https://sg2.anywheelbike.com?c=630000" + number
        f.write(bike)
        f.write("\n")