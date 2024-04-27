"""An old solution that does not work"""
def find_names(file_path):
    """Takes a file and returns a tuple based on it. 
    The first element of the tuple is a set of 3 most popular names.
    The second element is a tuple,
    containing the number of names used only once and the set of those names.
    The third element of the tuple is another tuple, which has the most popular first letter, 
    names starting with that letter and the number of children named with those names"""
    info_dict = dict()
    with open(file_path, 'r', encoding = 'utf-8') as file:
        info = file.readlines()
        info.pop(0)
        for line in info:
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.strip()
            line = line.split(' \t')
            info_dict[line[0]] = int(line[1])
        popular_names = set()
        one_names = set()
        number_name_ocurrences = []
        letter_dict = dict()
        for name, number in info_dict.items():
            if number == 1:
                one_names.add(name)
            number_name_ocurrences.append(number)
        number_name_ocurrences = selection_sort(number_name_ocurrences)[-3:]
        for name, number in info_dict.items():
            for numbers in number_name_ocurrences:
                if number == numbers:
                    popular_names.add(name)
        for i in range(32):
            letter_sum = 0
            for name, number in info_dict.items():
                if name[0] == chr(1040 + i):
                    letter_sum += number
            letter_dict[chr(1040 + i)] = letter_sum
        max_occur = 0
        names_number = 0
        for letter, number in letter_dict.items():
            if number > max_occur:
                max_occur = number
                popular_letter = [letter, max_occur]
        for name, number in info_dict.items():
            if name[0] == popular_letter[0]:
                names_number += 1
        popular_letter_t = (popular_letter[0], names_number, popular_letter[1])
        return (popular_names, (len(one_names), one_names), popular_letter_t)

def selection_sort(lst):
    """
    Sorts a list using the selection method.
    >>> selection_sort([3,5,4])
    [3, 4, 5]
    >>> selection_sort([3,5,4,5])
    [3, 4, 5, 5]
    """
    sorted_list = []
    while len(lst) != 0:
        for index, value in enumerate(lst):
            if value == min(lst):
                sorted_list.append(value)
                lst.pop(index)
    return sorted_list
