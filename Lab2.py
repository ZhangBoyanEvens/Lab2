def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")



def get_user_input():
    user_input = input("Enter numbers: ")
    number_strings = user_input.split(",")
    number_list = [float(num) for num in number_strings]
    return number_list



def calc_average_temperature(temperature_list):
    avg = sum(temperature_list) / len(temperature_list)
    return avg

def calc_min_max_temperature(temperature_list):
    min_temp = min(temperature_list)
    max_temp = max(temperature_list)
    return [min_temp, max_temp]



def sort_temperature(temperature_list):
    sorted_list = sorted(temperature_list)
    return sorted_list


def calc_median_temperature(temperature_list):
    sorted_list = sorted(temperature_list)
    length = len(sorted_list)
    middle = length // 2

    if length % 2 == 0:
        median = (sorted_list[middle - 1] + sorted_list[middle]) / 2
    else:
        median = sorted_list[middle]
    return median


def main():
    display_main_menu()
    numbers = get_user_input()

    avg = calc_average_temperature(numbers)
    minmax = calc_min_max_temperature(numbers)
    sorted_list = sort_temperature(numbers)
    median = calc_median_temperature(numbers)

    print("\nResults:")
    print("Average Temperature:", avg)
    print("Min and Max Temperatures:", minmax)
    print("Sorted Temperatures:", sorted_list)
    print("Median Temperature:", median)


main()
