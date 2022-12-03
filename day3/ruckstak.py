from collections import Counter
import itertools
import json

with open("day3\source.txt", "r") as f:
    elements = [line.strip() for line in f]


def find_dup_char(string_1, string_2):
    input = string_1 + string_2
    WC = Counter(input)
    for letter, count in WC.items():
        if (count > 1):
            if (letter in string_1 and letter in string_2):
                duplicate = letter
    return duplicate


def find_dup_char_by_three(string_1, string_2, string_3):
    input = string_1 + string_2 + string_3
    WC = Counter(input)
    for letter, count in WC.items():
        if (count > 1):
            if (letter in string_1 and letter in string_2 and letter in string_3):
                duplicate = letter
    return duplicate


def prioritize_char(char):
    with open('day3\prioritize_values.json') as json_file:
        data = json.load(json_file)
    return data.get(char)


total = 0


def create_sub_element_list(element_list, n):
    list_of_sub_n = []
    sub_elements = []
    for i in element_list:
        sub_elements.append(i)
        if ((elements.index(i)+1) % n == 0):
            list_of_sub_n.append(sub_elements)
            sub_elements = []
    return list_of_sub_n


sub_list_of_three = create_sub_element_list(elements, 3)

total = 0
for list in sub_list_of_three:
    str1, str2, str3 = list
    print(list)
    print(str1, str2, str3)
    triplicate_char = find_dup_char_by_three(str1, str2, str3)
    triplicate_value = prioritize_char(triplicate_char)
    total += triplicate_value
    print(triplicate_char, "->", triplicate_value)
print(total)

# for item in itertools.islice(elements, 3):
#     print(item)

# for elem in elements:
# print(elem)
# firstpart, secondpart = elem[:len(elem)//2], elem[len(elem)//2:]
# duplicate_letter = find_dup_char(firstpart, secondpart)
# duplicate_value = prioritize_char(duplicate_letter)
# total += duplicate_value
# print(elem, '\n', firstpart, secondpart)
# print(duplicate_letter, "->", duplicate_value)
# print("***************")
# print(total)
