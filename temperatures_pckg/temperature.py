def average_temperatures(filename):
    buffer = []

    with open(filename, "r") as file:
        data_buffer = file.readlines()

    number_of_countries = len(data_buffer[0]) - 1
    list_of_countries = get_countries(data_buffer)
    list_of_temperatures = get_temperatures_by_country(data_buffer, len(list_of_countries) + 1)
    minmax = min_max_modular(list_of_countries, list_of_temperatures)
    # print_info(list_of_countries,list_of_temperatures)
    print_modular(list_of_countries, minmax)


# separates the countries in a list
def get_countries(buffer):
    header = buffer[0].split(" ")
    return header[:-1]


# sorts the temperatures into a list for each country, any number of countries.
def get_temperatures_by_country(buffer, num_of_ct):
    ret = []

    for i in range(num_of_ct):
        ret.append([])

    for i in range(1, len(buffer)):
        line = buffer[i].split(" ")
        for k in range(len(line)):
            ret[k].append(line[k])

    return ret


# prints the solution for any number of countries
def print_modular(countries, minmax_years):
    for i in range(len(countries)):
        print(countries[i] + " => " + minmax_years[i][0].rstrip() + ", " + minmax_years[i][1].rstrip())


# not included in the final solution
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


# takes any number of countries, calculates max and min years
def min_max_modular(countries, temperatures):
    ret = []

    for i in range(len(countries)):
        ret.append([])

    for i in range(len(countries)):
        ret[i].append(temperatures[-1][temperatures[i].index(min(temperatures[i]))])
        ret[i].append(temperatures[-1][temperatures[i].index(max(temperatures[i]))])

    return ret


average_temperatures("results.txt")
