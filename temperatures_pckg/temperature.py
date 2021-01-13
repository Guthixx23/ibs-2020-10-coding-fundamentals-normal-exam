def average_temperatures(filename):

    buffer = []

    with open(filename, "r") as file:
        data_buffer = file.readlines()

    number_of_countries = len(data_buffer[0]) -1
    list_of_countries = get_countries(data_buffer)
    list_of_temperatures = get_temperatures_by_country(data_buffer,len(list_of_countries)+1)
    print_info(list_of_countries,list_of_temperatures)


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

    return ret



def print_info(countries, temperatures):
    country1min = temperatures[-1][temperatures[0].index(min(temperatures[0]))]
    country1max = temperatures[-1][temperatures[0].index(max(temperatures[0]))]
    country2min = temperatures[-1][temperatures[1].index(min(temperatures[1]))]
    country2max = temperatures[-1][temperatures[1].index(max(temperatures[1]))]
    country3min = temperatures[-1][temperatures[2].index(min(temperatures[2]))]
    country3max = temperatures[-1][temperatures[2].index(max(temperatures[2]))]

    print(countries[0] + " => " + country1min.rstrip() + ", " + country1max.rstrip())
    print(countries[1] + " => " + country2min.rstrip() + ", " + country2max.rstrip())
    print(countries[2] + " => " + country3min.rstrip() + ", " + country3max.rstrip())






average_temperatures("results.txt")