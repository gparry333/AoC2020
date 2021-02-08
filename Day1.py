string_array = []
with open(r'C:\Users\Gillian.Parry\PycharmProjects\AoC\DayOneData.txt')as file:
    for line in file:
        string_array.append(line)

    data_array = [int(string_array) for string_array in string_array]
    print(data_array)

    result = 0
    for x in data_array:
        for y in range(1, 200):
            second = data_array[y]
            for z in range(1, 200):
                third = data_array[z]
                result = x + second + third
                if result == 2020:
                    total = x * second * third
                    result_file = open("resultsfile.txt", "w")
                    result_file.write(str(x) + " " + str(second) + " " + str(third) + " " + str(result))
                    result_file.write("Final result is " + str(total))
                    break
