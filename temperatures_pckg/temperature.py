def average_temperatures(filename):

    buffer = []

    with open(filename, "r") as file:
        data_buffer = file.readlines()

    number_of_countries = len(data_buffer[0]) -1
    list_of_countries = get_countries(data_buffer)
    list_of_temperatures = get_temperatures_by_country(data_buffer,len(list_of_countries)+1)

    country1min = list_of_temperatures[-1][list_of_temperatures.index(min(list_of_temperatures[0]))]
    country1max = list_of_temperatures[-1][list_of_temperatures.index(max(list_of_temperatures[0]))]
    country2min = list_of_temperatures[-1][list_of_temperatures.index(min(list_of_temperatures[1]))]
    country2max = list_of_temperatures[-1][list_of_temperatures.index(max(list_of_temperatures[1]))]
    country3min = list_of_temperatures[-1][list_of_temperatures.index(min(list_of_temperatures[2]))]
    country3max = list_of_temperatures[-1][list_of_temperatures.index(max(list_of_temperatures[2]))]



    pass


def get_countries(buffer):
    header = buffer[0].split(" ")
    return header[:-1]

def get_temperatures_by_country(buffer, num_of_ct):

    ret = []

    for i in range(num_of_ct):
        ret.append([])

    for i in range(1,len(buffer)):
        line = buffer[i].split(" ")
        for k in range(len(line)):
            ret[k].append(line[k])

    for i in ret[-1]:
        i.strip()





    return ret




average_temperatures("results.txt")