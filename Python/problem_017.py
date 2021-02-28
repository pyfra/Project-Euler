units_mapping = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

dec_mapping = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

mapped_tenth = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

hundreds_map = {el: str_num + " hundred" for el, str_num in units_mapping.items()}
thousands_map = {el: str_num + " thousand" for el, str_num in units_mapping.items()}

mappings = [thousands_map, hundreds_map, dec_mapping, units_mapping]
mappings = [thousands_map, hundreds_map, dec_mapping, units_mapping]


def map_number_to_word(n):
    if n == 0:
        return 'zero'
    n_str = str(n)
    if len(n_str) > 4: raise NotImplementedError()
    str_number = list()
    for i, digit in enumerate(n_str):
        if int(digit) == 0:
            continue
        if int(digit) == 1 and i + (4 - len(n_str)) == 2:
            str_number.append(mapped_tenth[int(n_str[-2:])])
            break
        str_number.append(mappings[i + (4 - len(n_str))][int(digit)])

    if len(str_number) > 1 and len(n_str) > 2:
        str_number = str_number[:1] + [' and '] + str_number[1:]

    string_number = ''.join(str_number)
    return string_number


def solution():
    n_char = 0
    for i in range(1, 1001):
        n_char += len(map_number_to_word(i).replace(' ', ''))

    print(n_char)


solution()
